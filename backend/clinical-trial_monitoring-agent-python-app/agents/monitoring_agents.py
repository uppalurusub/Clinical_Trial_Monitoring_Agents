from utils.logger import logger

from autogen_agentchat.agents import AssistantAgent


from config.llm_config import get_model_client,model


class MonitoringAgents:
    """
    Clinical Trial Monitoring Agents

    Agents:
    1. Monitoring Agent
    2. Risk Agent
    3. Compliance Agent
    """

    def __init__(self):
        try:
            logger.info(
                "Initializing Clinical Trial Monitoring Agents..."
            )

            self.model_client = get_model_client()

            logger.success(
                f"Model Client Initialized Successfully: {model}"
            )

        except Exception as ex:
            logger.exception(
                f"Failed to initialize model client: {str(ex)}"
            )
            raise

    def monitoring_agent(self) -> AssistantAgent:
        """
        Monitoring Agent

        Responsibilities:
        - Site Monitoring
        - Enrollment Review
        - Protocol Deviations
        - Data Quality Assessment
        """

        try:
            logger.info(
                "Creating Monitoring Agent..."
            )

            agent = AssistantAgent(
                name="MonitoringAgent",
                model_client=self.model_client,
                system_message="""
You are a Clinical Trial Monitoring Expert.

Your responsibilities include:

1. Site Performance Review
2. Enrollment Monitoring
3. Subject Retention Analysis
4. Protocol Deviation Review
5. Missing Data Assessment
6. Monitoring Findings Evaluation
7. Site Monitoring Recommendations

Provide:
- Monitoring Summary
- Site Performance Assessment
- Monitoring Recommendations
- Monitoring Priority
"""
            )

            logger.success(
                "Monitoring Agent Created Successfully"
            )

            return agent

        except Exception as ex:
            logger.exception(
                f"Error creating Monitoring Agent: {str(ex)}"
            )
            raise

    def risk_agent(self) -> AssistantAgent:
        """
        Risk-Based Monitoring Agent

        Responsibilities:
        - Risk Scoring
        - KRI Analysis
        - QTL Assessment
        - Site Risk Classification
        """

        try:
            logger.info(
                "Creating Risk Agent..."
            )

            agent = AssistantAgent(
                name="RiskAgent",
                model_client=self.model_client,
                system_message="""
You are a Clinical Trial Risk-Based Monitoring Specialist.

Evaluate:

1. Protocol Deviations
2. Major Findings
3. Critical Findings
4. Missing Data
5. Open Queries
6. Overdue Queries
7. Serious Adverse Events
8. Key Risk Indicators (KRI)
9. Quality Tolerance Limits (QTL)

Classify Risk:

- Low Risk
- Medium Risk
- High Risk
- Critical Risk

Provide:

- Overall Risk Score
- Risk Level
- Root Cause Analysis
- Risk Mitigation Recommendations
"""
            )

            logger.success(
                "Risk Agent Created Successfully"
            )

            return agent

        except Exception as ex:
            logger.exception(
                f"Error creating Risk Agent: {str(ex)}"
            )
            raise

    def compliance_agent(self) -> AssistantAgent:
        """
        Compliance Agent

        Responsibilities:
        - GCP Compliance
        - Audit Readiness
        - CAPA Assessment
        - Regulatory Compliance
        """

        try:
            logger.info(
                "Creating Compliance Agent..."
            )

            agent = AssistantAgent(
                name="ComplianceAgent",
                model_client=self.model_client,
                system_message="""
You are a Clinical Trial Compliance and GCP Expert.

Assess:

1. ICH-GCP Compliance
2. Protocol Compliance
3. Informed Consent Compliance
4. Training Compliance
5. Audit Readiness
6. CAPA Requirements
7. Regulatory Inspection Readiness

Determine:

- Compliance Status
- Audit Readiness Status
- CAPA Requirements
- Compliance Recommendations

Classification:

- Compliant
- Partially Compliant
- Non-Compliant
"""
            )

            logger.success(
                "Compliance Agent Created Successfully"
            )

            return agent

        except Exception as ex:
            logger.exception(
                f"Error creating Compliance Agent: {str(ex)}"
            )
            raise

    def get_all_agents(self):
        """
        Return all monitoring agents
        """

        try:
            logger.info(
                "Initializing all Clinical Trial Monitoring Agents..."
            )

            agents = {
                "monitoring_agent": self.monitoring_agent(),
                "risk_agent": self.risk_agent(),
                "compliance_agent": self.compliance_agent()
            }

            logger.success(
                "All Monitoring Agents Initialized Successfully"
            )

            return agents

        except Exception as ex:
            logger.exception(
                f"Failed to initialize agents: {str(ex)}"
            )
            raise