
import os
from datetime import datetime, timezone
from typing import Any

from langsmith import get_current_run_tree, traceable

from utils.logger import get_logger

logger = get_logger()

PROJECT_NAME = os.getenv(
    "LANGSMITH_PROJECT",
    os.getenv(
        "langsmith_project",
        "clinical-trial-monitoring-agents",
    ),
)


@traceable(
    name="clinical_trial_monitoring",
    run_type="llm",
    project_name=PROJECT_NAME,
    #metadata={"ls_provider": "openrouter"},
)
def _create_usage_run(
    workflow: str,
    usage_metadata: dict[str, int | float],
    model_name: str,
    error: str | None = None,
) -> dict[str, Any]:
    run_tree = get_current_run_tree()

    if run_tree is None:
        raise RuntimeError("LangSmith trace context is unavailable.")

    run_tree.metadata.update({
        "ls_provider": "openrouter",
        "ls_model_name": model_name,
        "cost_source": "configured_rate_estimate",
        "usage_available": True,
    })

    # Use LangSmith's documented usage reporting mechanism.
    run_tree.set(usage_metadata=usage_metadata)

    return {
        "status": "failed" if error else "completed",
        "workflow": "clinical_trial_monitoring",
        "usage_metadata": usage_metadata,
        "error": error,
    }


def log_monitoring_usage(
    usage: dict[str, Any],
    model_name: str,
    input_rate_per_1m: float,
    output_rate_per_1m: float,
    start_time: datetime,
    end_time: datetime | None = None,
    error: str | None = None,
) -> str:
    end_time = end_time or datetime.now(timezone.utc)

    input_tokens = int(usage.get("input_tokens", 0) or 0)
    output_tokens = int(usage.get("output_tokens", 0) or 0)

    if not usage.get("usage_found", False):
        raise ValueError("Actual token usage is unavailable.")

    if input_tokens < 0 or output_tokens < 0:
        raise ValueError("Token counts cannot be negative.")

    try:
        input_rate = float(input_rate_per_1m)
        output_rate = float(output_rate_per_1m)
    except (TypeError, ValueError) as exc:
        raise ValueError(
            "Pricing rates must be numeric."
        ) from exc

    if input_rate < 0 or output_rate < 0:
        raise ValueError("Pricing rates cannot be negative.")

    input_cost = input_tokens * input_rate / 1_000_000
    output_cost = output_tokens * output_rate / 1_000_000

    usage_metadata = {
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "total_tokens": input_tokens + output_tokens,
        "input_cost": input_cost,
        "output_cost": output_cost,
        "total_cost": input_cost + output_cost,
    }

    logger.info(
        "Recording usage: model={}, input_tokens={}, "
        "output_tokens={}, total_cost={}",
        model_name,
        input_tokens,
        output_tokens,
        usage_metadata["total_cost"],
    )

    result = _create_usage_run(
        workflow="clinical_trial_monitoring",
        usage_metadata=usage_metadata,
        model_name=model_name,
        error=error,
    )

    logger.success(
        "Usage run submitted: status={}, usage={}",
        result["status"],
        usage_metadata,
    )

    return result["status"]