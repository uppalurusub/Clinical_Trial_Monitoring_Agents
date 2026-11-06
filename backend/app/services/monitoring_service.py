from datetime import datetime
import time

import mlflow

from app.config.settings import (
    settings,
    usage_capture,
    INPUT_PRICE_PER_1M,
    OUTPUT_PRICE_PER_1M,
)
from app.implementation.monitoring_impl import MonitoringImplementation
from app.models.request_model import MonitoringRequest
from app.models.response_model import MonitoringResponse

logger = settings.get_logger()

mlflow.set_tracking_uri("http://localhost:5000")
mlflow.set_experiment("Clinical_Trial_Monitoring_Agent_Interface")


class MonitoringService:

    def __init__(self):
        logger.info("Initializing MonitoringService...")
        self.monitoring_impl = MonitoringImplementation()
        logger.success("MonitoringService initialized successfully.")

    async def analyze_monitoring(
        self,
        request: MonitoringRequest
    ) -> MonitoringResponse:
        """Execute clinical trial monitoring and record LLM usage/cost."""

        try:
            start_time = datetime.now()
            start_ts = time.perf_counter()

            logger.info(
                f"Received monitoring request for "
                f"Study={request.study_id}, Site={request.site_id}"
            )

            self._validate_request(request)
            logger.info("Request validation completed.")

            run_name = (
                "Clinical_Trial_Monitoring_Agent_Analyze_Monitoring_"
                f"{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            )

            with mlflow.start_run(run_name=run_name):
                # Do not log raw clinical request/response payloads to MLflow.
                # They may contain confidential or personal trial information.
                mlflow.log_param("start_time", start_time.isoformat())
                mlflow.set_tag("source", "FastAPI")
                mlflow.set_tag("endpoint", "monitoring/analyze")
                mlflow.set_tag("llm_provider", "OpenRouter")

                with usage_capture() as usage:
                    response = await self.monitoring_impl.analyze(request)

                execution_time = time.perf_counter() - start_ts
                usage_values = usage.as_dict()

                # Log configuration and actual usage separately.
                mlflow.log_param("llm_model", usage_values["model"])
                mlflow.log_param(
                    "input_price_per_1m_usd", INPUT_PRICE_PER_1M
                )
                mlflow.log_param(
                    "output_price_per_1m_usd", OUTPUT_PRICE_PER_1M
                )
                mlflow.log_param("input", request)
                mlflow.log_param("output", response)
                mlflow.log_param("execution_time", execution_time)

                metric_names = (
                    "input_tokens",
                    "output_tokens",
                    "total_tokens",
                    "input_cost_usd",
                    "output_cost_usd",
                    "total_cost_usd",
                    "llm_call_count",
                    "usage_reported_call_count",
                )
                for metric_name in metric_names:
                    mlflow.log_metric(
                        metric_name,
                        float(usage_values[metric_name])
                    )

                mlflow.log_metric(
                    "execution_time_seconds",
                    round(execution_time, 4)
                )

                mlflow.set_tag("llm_usage_source", usage_values["source"])
                mlflow.log_param("end_time", datetime.now().isoformat())

                logger.info(
                    "LLM usage captured: "
                    f"model={usage_values['model']}, "
                    f"input_tokens={usage_values['input_tokens']}, "
                    f"output_tokens={usage_values['output_tokens']}, "
                    f"total_tokens={usage_values['total_tokens']}, "
                    f"input_cost_usd={usage_values['input_cost_usd']:.15f}, "
                    f"output_cost_usd={usage_values['output_cost_usd']:.15f}, "
                    f"total_cost_usd={usage_values['total_cost_usd']:.15f}, "
                    f"llm_call_count={usage_values['llm_call_count']}, "
                    f"usage_reported_call_count="
                    f"{usage_values['usage_reported_call_count']}"
                )

                if usage_values["usage_reported_call_count"] == 0:
                    logger.warning(
                        "No token usage was reported by the AutoGen model "
                        "client. Check that MonitoringImplementation uses "
                        "settings.get_model_client() and that the provider "
                        "returns usage metadata."
                    )

            logger.success(
                f"Monitoring analysis completed for Site={request.site_id}"
            )
            return response

        except ValueError as ex:
            logger.error(f"Validation Error: {str(ex)}")
            raise

        except Exception as ex:
            logger.exception(f"Monitoring Service Failed: {str(ex)}")
            raise

    async def health_check(self) -> dict:
        try:
            logger.info("Monitoring Service Health Check Started.")
            return {
                "status": "healthy",
                "service": "Clinical Trial Monitoring Service",
            }
        except Exception as ex:
            logger.exception(f"Health Check Failed: {str(ex)}")
            return {"status": "unhealthy", "error": str(ex)}

    def _validate_request(self, request: MonitoringRequest) -> None:
        logger.info("Validating monitoring request...")

        if request.screened_subjects < 0:
            raise ValueError("Screened subjects cannot be negative.")

        if request.enrolled_subjects < 0:
            raise ValueError("Enrolled subjects cannot be negative.")

        if request.enrolled_subjects > request.screened_subjects:
            raise ValueError(
                "Enrolled subjects cannot exceed screened subjects."
            )

        if not 0 <= request.compliance_score <= 100:
            raise ValueError(
                "Compliance score must be between 0 and 100."
            )

        if not 0 <= request.training_completion_rate <= 100:
            raise ValueError(
                "Training completion rate must be between 0 and 100."
            )

        if not 0 <= request.risk_indicator_score <= 100:
            raise ValueError(
                "Risk indicator score must be between 0 and 100."
            )

        total_findings = (
            request.critical_findings
            + request.major_findings
            + request.minor_findings
        )

        if (
            request.monitoring_findings > 0
            and total_findings > request.monitoring_findings
        ):
            raise ValueError(
                "Total findings exceed monitoring findings."
            )

        logger.success("Monitoring request validation passed.")
