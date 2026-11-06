import streamlit as st


def render_request_form() -> dict:
    st.subheader("Study Information")
    col1, col2 = st.columns(2)

    with col1:
        study_id = st.text_input("Study ID", "STUDY-001")
        study_name = st.text_input("Study Name", "Phase III Diabetes Study")
        country = st.text_input("Country", "India")

    with col2:
        ctms_study_status = st.selectbox(
            "Study Status", ["Active", "Completed", "Paused", "Closed"]
        )
        investigator_name = st.text_input("Principal Investigator", "Dr. John Smith")

    st.divider()
    st.subheader("Site Information")
    col1, col2 = st.columns(2)

    with col1:
        site_id = st.text_input("Site ID", "SITE-101")
        site_name = st.text_input("Site Name", "Apollo Research Center")

    with col2:
        ctms_site_status = st.selectbox(
            "Site Status", ["Active", "Closed", "Suspended"]
        )
        last_monitoring_visit_date = st.date_input("Last Monitoring Visit")

    st.divider()
    st.subheader("Subject Metrics")
    c1, c2, c3, c4 = st.columns(4)
    screened_subjects = c1.number_input("Screened", value=220)
    enrolled_subjects = c2.number_input("Enrolled", value=180)
    randomized_subjects = c3.number_input("Randomized", value=170)
    dropout_subjects = c4.number_input("Dropouts", value=10)

    st.divider()
    st.subheader("Monitoring Metrics")
    col1, col2, col3 = st.columns(3)
    monitoring_findings = col1.number_input("Monitoring Findings", value=12)
    major_findings = col2.number_input("Major Findings", value=3)
    minor_findings = col3.number_input("Minor Findings", value=8)

    col1, col2, col3 = st.columns(3)
    critical_findings = col1.number_input("Critical Findings", value=1)
    monitoring_frequency_days = col2.number_input("Monitoring Frequency", value=30)
    days_since_last_visit = col3.number_input("Days Since Last Visit", value=39)

    st.divider()
    st.subheader("Compliance")
    c1, c2, c3 = st.columns(3)
    compliance_score = c1.slider("Compliance Score", 0, 100, 85)
    informed_consent_compliance = c2.slider("Informed Consent %", 0, 100, 95)
    training_completion_rate = c3.slider("Training %", 0, 100, 92)
    source_data_verification_rate = st.slider("SDV %", 0, 100, 88)

    st.divider()
    st.subheader("Risk Indicators")
    c1, c2, c3 = st.columns(3)
    adverse_events = c1.number_input("Adverse Events", value=12)
    serious_adverse_events = c2.number_input("Serious AE", value=2)
    suspected_unexpected_serious_adverse_reactions = c3.number_input("SUSAR", value=1)

    c1, c2, c3 = st.columns(3)
    protocol_deviations = c1.number_input("Protocol Deviations", value=8)
    major_protocol_deviations = c2.number_input("Major Protocol Deviations", value=3)
    minor_protocol_deviations = c3.number_input("Minor Protocol Deviations", value=5)

    c1, c2, c3 = st.columns(3)
    open_queries = c1.number_input("Open Queries", value=25)
    overdue_queries = c2.number_input("Overdue Queries", value=8)
    missing_data_points = c3.number_input("Missing Data", value=15)

    c1, c2 = st.columns(2)
    key_risk_indicators_triggered = c1.number_input("KRI Triggered", value=4)
    quality_tolerance_limit_breaches = c2.number_input("QTL Breaches", value=2)
    risk_indicator_score = st.slider("Risk Score", 0, 100, 78)

    return {
        "study_id": study_id,
        "study_name": study_name,
        "country": country,
        "ctms_study_status": ctms_study_status,
        "investigator_name": investigator_name,
        "site_id": site_id,
        "site_name": site_name,
        "ctms_site_status": ctms_site_status,
        "last_monitoring_visit_date": str(last_monitoring_visit_date),
        "screened_subjects": screened_subjects,
        "enrolled_subjects": enrolled_subjects,
        "randomized_subjects": randomized_subjects,
        "dropout_subjects": dropout_subjects,
        "monitoring_findings": monitoring_findings,
        "major_findings": major_findings,
        "minor_findings": minor_findings,
        "critical_findings": critical_findings,
        "monitoring_frequency_days": monitoring_frequency_days,
        "days_since_last_visit": days_since_last_visit,
        "compliance_score": compliance_score,
        "informed_consent_compliance": informed_consent_compliance,
        "training_completion_rate": training_completion_rate,
        "source_data_verification_rate": source_data_verification_rate,
        "adverse_events": adverse_events,
        "serious_adverse_events": serious_adverse_events,
        "suspected_unexpected_serious_adverse_reactions": suspected_unexpected_serious_adverse_reactions,
        "protocol_deviations": protocol_deviations,
        "major_protocol_deviations": major_protocol_deviations,
        "minor_protocol_deviations": minor_protocol_deviations,
        "open_queries": open_queries,
        "overdue_queries": overdue_queries,
        "missing_data_points": missing_data_points,
        "key_risk_indicators_triggered": key_risk_indicators_triggered,
        "quality_tolerance_limit_breaches": quality_tolerance_limit_breaches,
        "risk_indicator_score": risk_indicator_score,
    }
