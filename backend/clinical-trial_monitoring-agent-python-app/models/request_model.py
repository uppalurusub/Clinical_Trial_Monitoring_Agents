from pydantic import BaseModel, Field
from typing import Optional


class MonitoringRequest(BaseModel):
    # Study Information
    study_id: str = Field(
        ...,
        description="Clinical study identifier"
    )

    study_name: Optional[str] = Field(
        None,
        description="Clinical study name"
    )

    # Site Information
    site_id: str = Field(
        ...,
        description="Clinical site identifier"
    )

    site_name: str = Field(
        ...,
        description="Clinical site name"
    )

    investigator_name: Optional[str] = Field(
        None,
        description="Principal Investigator"
    )

    country: Optional[str] = None

    # Enrollment Metrics
    screened_subjects: int = Field(
        ...,
        ge=0,
        description="Total screened subjects"
    )

    enrolled_subjects: int = Field(
        ...,
        ge=0,
        description="Total enrolled subjects"
    )

    randomized_subjects: int = Field(
        0,
        ge=0,
        description="Total randomized subjects"
    )

    dropout_subjects: int = Field(
        0,
        ge=0,
        description="Total dropout subjects"
    )

    # Monitoring Metrics
    protocol_deviations: int = Field(
        0,
        ge=0,
        description="Protocol deviations reported"
    )

    major_protocol_deviations: int = Field(
        0,
        ge=0,
        description="Major protocol deviations"
    )

    minor_protocol_deviations: int = Field(
        0,
        ge=0,
        description="Minor protocol deviations"
    )

    missing_data_points: int = Field(
        0,
        ge=0,
        description="Missing CRF/EDC data points"
    )

    open_queries: int = Field(
        0,
        ge=0,
        description="Open data management queries"
    )

    overdue_queries: int = Field(
        0,
        ge=0,
        description="Overdue data queries"
    )

    # Safety Metrics
    adverse_events: int = Field(
        0,
        ge=0,
        description="Adverse Events"
    )

    serious_adverse_events: int = Field(
        0,
        ge=0,
        description="Serious Adverse Events"
    )

    suspected_unexpected_serious_adverse_reactions: int = Field(
        0,
        ge=0,
        description="SUSAR count"
    )

    # Compliance Metrics
    compliance_score: float = Field(
        ...,
        ge=0,
        le=100,
        description="Site compliance score"
    )

    training_completion_rate: float = Field(
        100,
        ge=0,
        le=100,
        description="Training completion percentage"
    )

    informed_consent_compliance: float = Field(
        100,
        ge=0,
        le=100,
        description="ICF compliance percentage"
    )

    source_data_verification_rate: float = Field(
        100,
        ge=0,
        le=100,
        description="SDV completion percentage"
    )

    # Monitoring Visit Information
    last_monitoring_visit_date: Optional[str] = Field(
        None,
        description="Last monitoring visit date"
    )

    days_since_last_visit: int = Field(
        0,
        ge=0,
        description="Days since last monitoring visit"
    )

    monitoring_findings: int = Field(
        0,
        ge=0,
        description="Open monitoring findings"
    )

    critical_findings: int = Field(
        0,
        ge=0,
        description="Critical monitoring findings"
    )

    major_findings: int = Field(
        0,
        ge=0,
        description="Major monitoring findings"
    )

    minor_findings: int = Field(
        0,
        ge=0,
        description="Minor monitoring findings"
    )

    # Risk-Based Monitoring Inputs
    risk_indicator_score: float = Field(
        0,
        ge=0,
        le=100,
        description="RBM Risk Indicator Score"
    )

    quality_tolerance_limit_breaches: int = Field(
        0,
        ge=0,
        description="QTL breaches"
    )

    key_risk_indicators_triggered: int = Field(
        0,
        ge=0,
        description="Number of KRIs triggered"
    )

    # CTMS Integration Fields
    ctms_study_status: Optional[str] = Field(
        "Active",
        description="Study status from CTMS"
    )

    ctms_site_status: Optional[str] = Field(
        "Active",
        description="Site status from CTMS"
    )

    monitoring_frequency_days: int = Field(
        30,
        ge=1,
        description="Planned monitoring frequency"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "study_id": "STUDY-001",
                "study_name": "Phase III Diabetes Study",
                "site_id": "SITE-101",
                "site_name": "Apollo Research Center",
                "investigator_name": "Dr. John Smith",
                "country": "India",
                "screened_subjects": 220,
                "enrolled_subjects": 180,
                "randomized_subjects": 170,
                "dropout_subjects": 10,
                "protocol_deviations": 8,
                "major_protocol_deviations": 3,
                "minor_protocol_deviations": 5,
                "missing_data_points": 15,
                "open_queries": 25,
                "overdue_queries": 8,
                "adverse_events": 12,
                "serious_adverse_events": 2,
                "suspected_unexpected_serious_adverse_reactions": 1,
                "compliance_score": 85,
                "training_completion_rate": 92,
                "informed_consent_compliance": 95,
                "source_data_verification_rate": 88,
                "last_monitoring_visit_date": "2026-05-15",
                "days_since_last_visit": 39,
                "monitoring_findings": 12,
                "critical_findings": 1,
                "major_findings": 3,
                "minor_findings": 8,
                "risk_indicator_score": 78,
                "quality_tolerance_limit_breaches": 2,
                "key_risk_indicators_triggered": 4,
                "ctms_study_status": "Active",
                "ctms_site_status": "Active",
                "monitoring_frequency_days": 30
            }
        }