from utils.logger import logger

from implementation.monitoring_impl import (
    MonitoringImplementation
)

from models.request_model import (
    MonitoringRequest
)

from models.response_model import (
    MonitoringResponse
)

import mlflow
from datetime import datetime
import time

mlflow.set_tracking_uri(
    "http://localhost:5000"
)

mlflow.set_experiment(
    "Clinical_Trial_Monitoring_Agent_Interface"
)


class MonitoringService:

    def __init__(self):

        logger.info(
            "Initializing MonitoringService..."
        )

        self.monitoring_impl = (
            MonitoringImplementation()
        )

        logger.success(
            "MonitoringService initialized successfully."
        )

    async def analyze_monitoring(
        self,
        request: MonitoringRequest
    ) -> MonitoringResponse:
        """
        Clinical Trial Monitoring Analysis

        Parameters
        ----------
        request : MonitoringRequest

        Returns
        -------
        MonitoringResponse
        """

        try:

            start_time = datetime.now()
            start_ts = time.time()

            logger.info(
                f"Received monitoring request "
                f"for Study={request.study_id}, "
                f"Site={request.site_id}"
            )

            # ----------------------------------------
            # Business Validations
            # ----------------------------------------

            self._validate_request(
                request
            )

            logger.info(
                "Request validation completed."
            )

            # ----------------------------------------
            # Execute Monitoring Analysis
            # ----------------------------------------

            
            with mlflow.start_run(
                run_name=
                f"Clinical_Trial_Monitoring_Agent_Analyze_Monitoring_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            ):
                # Log to MLflow
                mlflow.log_param(
                    "start_time",
                    start_time.strftime("%Y-%m-%d %H:%M:%S")
                )
                mlflow.log_param(
                    "input_text",
                    request
                )
                response = await (
                    self.monitoring_impl.analyze(
                        request
                    )
                )

                mlflow.log_param(
                    "response",
                    response
                )

                mlflow.set_tag(
                    "source",
                    "FastAPI"
                )

                mlflow.set_tag(
                    "endpoint",
                    "monitoring/analyze"
                )



                end_time = datetime.now()
                end_ts = time.time()

                execution_time = end_ts - start_ts

                mlflow.log_param(
                    "end_time",
                    end_time.strftime("%Y-%m-%d %H:%M:%S")
                )

                mlflow.log_metric(
                    "execution_time_seconds",
                    round(execution_time, 4)
                )


            logger.success(
                f"Monitoring analysis completed "
                f"for Site={request.site_id}"
            )

            return response

        except ValueError as ex:

            logger.error(
                f"Validation Error: {str(ex)}"
            )

            raise

        except Exception as ex:

            logger.exception(
                f"Monitoring Service Failed: {str(ex)}"
            )

            raise

    async def health_check(self) -> dict:
        """
        Health Check API
        """

        try:

            logger.info(
                "Monitoring Service Health Check Started."
            )

            return {
                "status": "healthy",
                "service": "Clinical Trial Monitoring Service"
            }

        except Exception as ex:

            logger.exception(
                f"Health Check Failed: {str(ex)}"
            )

            return {
                "status": "unhealthy",
                "error": str(ex)
            }

    def _validate_request(
        self,
        request: MonitoringRequest
    ) -> None:
        """
        Business Validation Rules
        """

        logger.info(
            "Validating monitoring request..."
        )

        # ----------------------------------------
        # Enrollment Validation
        # ----------------------------------------

        if request.screened_subjects < 0:
            raise ValueError(
                "Screened subjects cannot be negative."
            )

        if request.enrolled_subjects < 0:
            raise ValueError(
                "Enrolled subjects cannot be negative."
            )

        if (
            request.enrolled_subjects >
            request.screened_subjects
        ):
            raise ValueError(
                "Enrolled subjects cannot exceed screened subjects."
            )

        # ----------------------------------------
        # Compliance Validation
        # ----------------------------------------

        if (
            request.compliance_score < 0 or
            request.compliance_score > 100
        ):
            raise ValueError(
                "Compliance score must be between 0 and 100."
            )

        # ----------------------------------------
        # Training Validation
        # ----------------------------------------

        if (
            request.training_completion_rate < 0 or
            request.training_completion_rate > 100
        ):
            raise ValueError(
                "Training completion rate must be between 0 and 100."
            )

        # ----------------------------------------
        # Risk Indicator Validation
        # ----------------------------------------

        if (
            request.risk_indicator_score < 0 or
            request.risk_indicator_score > 100
        ):
            raise ValueError(
                "Risk indicator score must be between 0 and 100."
            )

        # ----------------------------------------
        # Monitoring Findings Validation
        # ----------------------------------------

        total_findings = (
            request.critical_findings +
            request.major_findings +
            request.minor_findings
        )

        if (
            request.monitoring_findings > 0 and
            total_findings >
            request.monitoring_findings
        ):
            raise ValueError(
                "Total findings exceed monitoring findings."
            )

        logger.success(
            "Monitoring request validation passed."
        )