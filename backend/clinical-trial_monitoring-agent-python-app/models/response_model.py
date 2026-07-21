from pydantic import BaseModel, Field
from typing import List, Optional


class MonitoringRecommendation(BaseModel):
    category: str
    priority: str
    recommendation: str


class MonitoringMetrics(BaseModel):
    enrollment_rate: float
    screen_failure_rate: float
    dropout_rate: float

    protocol_deviation_rate: float
    missing_data_rate: float

    query_resolution_rate: float

    compliance_score: float
    training_completion_rate: float

    adverse_event_rate: float
    serious_adverse_event_rate: float


class RiskAssessment(BaseModel):
    risk_score: float
    risk_level: str

    site_risk: str
    safety_risk: str
    compliance_risk: str
    data_quality_risk: str

    key_risk_indicators_triggered: int
    quality_tolerance_limit_breaches: int


class ComplianceAssessment(BaseModel):
    compliance_status: str

    protocol_compliance: str
    informed_consent_compliance: str
    training_compliance: str

    audit_readiness_status: str

    major_findings: int
    critical_findings: int


class MonitoringVisitPlan(BaseModel):
    monitoring_strategy: str

    next_visit_required: bool

    recommended_visit_type: str

    recommended_visit_within_days: int

    monitoring_priority: str


class AgentAnalysis(BaseModel):
    monitoring_agent_summary: str

    risk_agent_summary: str

    compliance_agent_summary: str


class MonitoringResponse(BaseModel):
    success: bool

    study_id: str
    site_id: str
    site_name: str

    monitoring_status: str

    monitoring_metrics: MonitoringMetrics

    risk_assessment: RiskAssessment

    compliance_assessment: ComplianceAssessment

    monitoring_visit_plan: MonitoringVisitPlan

    agent_analysis: AgentAnalysis

    recommendations: List[MonitoringRecommendation]

    generated_by: str = "Clinical Trial Monitoring Agent"

    message: str