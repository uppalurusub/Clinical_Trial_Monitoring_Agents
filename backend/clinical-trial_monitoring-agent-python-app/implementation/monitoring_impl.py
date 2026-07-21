from utils.logger import logger

from agents.monitoring_agents import MonitoringAgents

from models.request_model import MonitoringRequest

from models.response_model import (
    MonitoringResponse,
    MonitoringMetrics,
    RiskAssessment,
    ComplianceAssessment,
    MonitoringVisitPlan,
    AgentAnalysis,
    MonitoringRecommendation
)


class MonitoringImplementation:

    def __init__(self):

        logger.info(
            "Initializing MonitoringImplementation..."
        )

        self.agent_factory = MonitoringAgents()

        logger.success(
            "MonitoringImplementation initialized successfully."
        )

    async def analyze(
        self,
        request: MonitoringRequest
    ) -> MonitoringResponse:

        try:

            logger.info(
                f"Starting monitoring analysis "
                f"for Site={request.site_id}"
            )

            # --------------------------------------------------
            # Metrics Calculation
            # --------------------------------------------------

            enrollment_rate = (
                (request.enrolled_subjects /
                 request.screened_subjects) * 100
                if request.screened_subjects > 0
                else 0
            )

            screen_failure_rate = (
                100 - enrollment_rate
            )

            dropout_rate = (
                (request.dropout_subjects /
                 request.enrolled_subjects) * 100
                if request.enrolled_subjects > 0
                else 0
            )

            protocol_deviation_rate = (
                (request.protocol_deviations /
                 request.enrolled_subjects) * 100
                if request.enrolled_subjects > 0
                else 0
            )

            missing_data_rate = (
                (request.missing_data_points /
                 request.enrolled_subjects) * 100
                if request.enrolled_subjects > 0
                else 0
            )

            query_resolution_rate = (
                (
                    (request.open_queries -
                     request.overdue_queries)
                    / request.open_queries
                ) * 100
                if request.open_queries > 0
                else 100
            )

            ae_rate = (
                (request.adverse_events /
                 request.enrolled_subjects) * 100
                if request.enrolled_subjects > 0
                else 0
            )

            sae_rate = (
                (request.serious_adverse_events /
                 request.enrolled_subjects) * 100
                if request.enrolled_subjects > 0
                else 0
            )

            logger.info(
                "Monitoring metrics calculated successfully."
            )

            # --------------------------------------------------
            # Risk Score Calculation
            # --------------------------------------------------

            risk_score = self.calculate_risk_score(
                request
            )

            risk_level = self.determine_risk_level(
                risk_score
            )

            logger.info(
                f"Risk Score={risk_score}, "
                f"Risk Level={risk_level}"
            )

            # --------------------------------------------------
            # Create Agents
            # --------------------------------------------------

            monitoring_agent = (
                self.agent_factory.monitoring_agent()
            )

            risk_agent = (
                self.agent_factory.risk_agent()
            )

            compliance_agent = (
                self.agent_factory.compliance_agent()
            )

            # --------------------------------------------------
            # Monitoring Agent
            # --------------------------------------------------

            monitoring_prompt = f"""
            Study ID: {request.study_id}
            Site Name: {request.site_name}

            Enrollment Rate: {enrollment_rate:.2f}
            Dropout Rate: {dropout_rate:.2f}

            Protocol Deviations:
            {request.protocol_deviations}

            Missing Data:
            {request.missing_data_points}

            Findings:
            {request.monitoring_findings}

            Provide monitoring assessment.
            """

            monitoring_result = await monitoring_agent.run(
                task=monitoring_prompt
            )

            monitoring_summary = (
                monitoring_result.messages[-1].content
            )

            logger.info(
                "Monitoring Agent completed."
            )

            # --------------------------------------------------
            # Risk Agent
            # --------------------------------------------------

            risk_prompt = f"""
            Risk-Based Monitoring Assessment

            Risk Indicator Score:
            {request.risk_indicator_score}

            KRI Triggered:
            {request.key_risk_indicators_triggered}

            QTL Breaches:
            {request.quality_tolerance_limit_breaches}

            Protocol Deviations:
            {request.protocol_deviations}

            Missing Data:
            {request.missing_data_points}

            Serious Adverse Events:
            {request.serious_adverse_events}

            Determine site risk.
            """

            risk_result = await risk_agent.run(
                task=risk_prompt
            )

            risk_summary = (
                risk_result.messages[-1].content
            )

            logger.info(
                "Risk Agent completed."
            )

            # --------------------------------------------------
            # Compliance Agent
            # --------------------------------------------------

            compliance_prompt = f"""
            Compliance Review

            Compliance Score:
            {request.compliance_score}

            Training Completion:
            {request.training_completion_rate}

            Informed Consent Compliance:
            {request.informed_consent_compliance}

            Critical Findings:
            {request.critical_findings}

            Major Findings:
            {request.major_findings}

            Determine compliance status.
            """

            compliance_result = (
                await compliance_agent.run(
                    task=compliance_prompt
                )
            )

            compliance_summary = (
                compliance_result.messages[-1].content
            )

            logger.info(
                "Compliance Agent completed."
            )

            # --------------------------------------------------
            # Build Response Objects
            # --------------------------------------------------

            metrics = MonitoringMetrics(
                enrollment_rate=round(
                    enrollment_rate, 2
                ),
                screen_failure_rate=round(
                    screen_failure_rate, 2
                ),
                dropout_rate=round(
                    dropout_rate, 2
                ),
                protocol_deviation_rate=round(
                    protocol_deviation_rate, 2
                ),
                missing_data_rate=round(
                    missing_data_rate, 2
                ),
                query_resolution_rate=round(
                    query_resolution_rate, 2
                ),
                compliance_score=request.compliance_score,
                training_completion_rate=request.training_completion_rate,
                adverse_event_rate=round(
                    ae_rate, 2
                ),
                serious_adverse_event_rate=round(
                    sae_rate, 2
                )
            )

            risk_assessment = RiskAssessment(
                risk_score=round(
                    risk_score, 2
                ),
                risk_level=risk_level,
                site_risk=risk_level,
                safety_risk=self.get_safety_risk(
                    request
                ),
                compliance_risk=self.get_compliance_risk(
                    request
                ),
                data_quality_risk=self.get_data_quality_risk(
                    request
                ),
                key_risk_indicators_triggered=request.key_risk_indicators_triggered,
                quality_tolerance_limit_breaches=request.quality_tolerance_limit_breaches
            )

            compliance_assessment = (
                ComplianceAssessment(
                    compliance_status=self.get_compliance_status(
                        request
                    ),
                    protocol_compliance=self.get_protocol_compliance(
                        request
                    ),
                    informed_consent_compliance="Compliant",
                    training_compliance="Compliant",
                    audit_readiness_status=self.get_audit_readiness(
                        request
                    ),
                    major_findings=request.major_findings,
                    critical_findings=request.critical_findings
                )
            )

            visit_plan = MonitoringVisitPlan(
                monitoring_strategy="Risk-Based Monitoring",
                next_visit_required=True,
                recommended_visit_type=(
                    "On-Site Monitoring"
                    if risk_level == "High"
                    else "Remote Monitoring"
                ),
                recommended_visit_within_days=(
                    7
                    if risk_level == "High"
                    else 30
                ),
                monitoring_priority=risk_level
            )

            recommendations = self.generate_recommendations(
                request,
                risk_level
            )

            agent_analysis = AgentAnalysis(
                monitoring_agent_summary=monitoring_summary,
                risk_agent_summary=risk_summary,
                compliance_agent_summary=compliance_summary
            )

            logger.success(
                f"Monitoring analysis completed "
                f"for Site={request.site_id}"
            )

            return MonitoringResponse(
                success=True,
                study_id=request.study_id,
                site_id=request.site_id,
                site_name=request.site_name,
                monitoring_status="Completed",
                monitoring_metrics=metrics,
                risk_assessment=risk_assessment,
                compliance_assessment=compliance_assessment,
                monitoring_visit_plan=visit_plan,
                agent_analysis=agent_analysis,
                recommendations=recommendations,
                message="Clinical Trial Monitoring Analysis Completed Successfully."
            )

        except Exception as ex:

            logger.exception(
                f"Monitoring Analysis Failed: {str(ex)}"
            )

            raise

    # =====================================================
    # Helper Methods
    # =====================================================

    def calculate_risk_score(
        self,
        request: MonitoringRequest
    ) -> float:

        score = (
            request.protocol_deviations * 3 +
            request.major_protocol_deviations * 5 +
            request.critical_findings * 10 +
            request.serious_adverse_events * 8 +
            request.overdue_queries * 2 +
            request.quality_tolerance_limit_breaches * 10 +
            request.key_risk_indicators_triggered * 5
        )

        return min(score, 100)

    def determine_risk_level(
        self,
        score: float
    ) -> str:

        if score >= 75:
            return "High"

        if score >= 40:
            return "Medium"

        return "Low"

    def get_safety_risk(
        self,
        request: MonitoringRequest
    ) -> str:

        if request.serious_adverse_events >= 5:
            return "High"

        if request.serious_adverse_events >= 2:
            return "Medium"

        return "Low"

    def get_compliance_risk(
        self,
        request: MonitoringRequest
    ) -> str:

        if request.compliance_score < 80:
            return "High"

        if request.compliance_score < 90:
            return "Medium"

        return "Low"

    def get_data_quality_risk(
        self,
        request: MonitoringRequest
    ) -> str:

        if request.missing_data_points > 20:
            return "High"

        if request.missing_data_points > 10:
            return "Medium"

        return "Low"

    def get_compliance_status(
        self,
        request: MonitoringRequest
    ) -> str:

        if request.compliance_score >= 90:
            return "Compliant"

        if request.compliance_score >= 75:
            return "Partially Compliant"

        return "Non-Compliant"

    def get_protocol_compliance(
        self,
        request: MonitoringRequest
    ) -> str:

        if request.protocol_deviations <= 2:
            return "Good"

        if request.protocol_deviations <= 5:
            return "Moderate"

        return "Poor"

    def get_audit_readiness(
        self,
        request: MonitoringRequest
    ) -> str:

        if (
            request.critical_findings == 0
            and request.compliance_score >= 90
        ):
            return "Ready"

        return "Not Ready"

    def generate_recommendations(
        self,
        request: MonitoringRequest,
        risk_level: str
    ):

        recommendations = []

        if risk_level == "High":
            recommendations.append(
                MonitoringRecommendation(
                    category="Risk",
                    priority="High",
                    recommendation="Schedule immediate on-site monitoring visit."
                )
            )

        if request.protocol_deviations > 5:
            recommendations.append(
                MonitoringRecommendation(
                    category="Compliance",
                    priority="High",
                    recommendation="Conduct protocol retraining for site staff."
                )
            )

        if request.missing_data_points > 10:
            recommendations.append(
                MonitoringRecommendation(
                    category="Data Quality",
                    priority="Medium",
                    recommendation="Perform targeted SDV and resolve missing data."
                )
            )

        if request.critical_findings > 0:
            recommendations.append(
                MonitoringRecommendation(
                    category="CAPA",
                    priority="High",
                    recommendation="Initiate CAPA immediately."
                )
            )

        return recommendations