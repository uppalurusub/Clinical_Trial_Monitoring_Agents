import streamlit as st
import pandas as pd

from utils.formatters import format_percent, format_value, yes_no


def display_response(result):

    if not result:
        st.error("No response received.")
        return

    # ==========================================================
    # Header
    # ==========================================================

    if result.get("success"):

        st.success(result.get("message", "Completed Successfully"))

    else:

        st.error("Request Failed")
        return

    st.divider()

    # ==========================================================
    # Study Information
    # ==========================================================

    st.subheader("Study Information")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Study ID", result.get("study_id", "-"))
    c2.metric("Site ID", result.get("site_id", "-"))
    c3.metric("Site Name", result.get("site_name", "-"))
    c4.metric("Monitoring Status", result.get("monitoring_status", "-"))

    st.divider()

    # ==========================================================
    # Monitoring Metrics
    # ==========================================================

    metrics = result.get("monitoring_metrics", {})

    st.subheader("Monitoring Metrics")

    row1 = st.columns(5)

    row1[0].metric(
        "Enrollment Rate",
        format_percent(metrics.get("enrollment_rate", 0))
    )

    row1[1].metric(
        "Screen Failure",
        format_percent(metrics.get("screen_failure_rate", 0))
    )

    row1[2].metric(
        "Dropout Rate",
        format_percent(metrics.get("dropout_rate", 0))
    )

    row1[3].metric(
        "Protocol Deviation",
        format_percent(metrics.get("protocol_deviation_rate", 0))
    )

    row1[4].metric(
        "Missing Data",
        format_percent(metrics.get("missing_data_rate", 0))
    )

    row2 = st.columns(5)

    row2[0].metric(
        "Query Resolution",
        format_percent(metrics.get("query_resolution_rate", 0))
    )

    row2[1].metric(
        "Compliance",
        format_percent(metrics.get("compliance_score", 0), 0)
    )

    row2[2].metric(
        "Training",
        format_percent(metrics.get("training_completion_rate", 0), 0)
    )

    row2[3].metric(
        "AE Rate",
        format_percent(metrics.get("adverse_event_rate", 0))
    )

    row2[4].metric(
        "SAE Rate",
        format_percent(metrics.get("serious_adverse_event_rate", 0))
    )

    st.divider()

    # ==========================================================
    # Risk Assessment
    # ==========================================================

    risk = result.get("risk_assessment", {})

    st.subheader("Risk Assessment")

    c1, c2, c3 = st.columns(3)

    score = risk.get("risk_score", 0)

    if score >= 80:
        c1.error(f"Risk Score : {score}")

    elif score >= 60:
        c1.warning(f"Risk Score : {score}")

    else:
        c1.success(f"Risk Score : {score}")

    c2.metric("Risk Level", risk.get("risk_level", "-"))
    c3.metric("Site Risk", risk.get("site_risk", "-"))

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Safety Risk",
        risk.get("safety_risk", "-")
    )

    c2.metric(
        "Compliance Risk",
        risk.get("compliance_risk", "-")
    )

    c3.metric(
        "Data Quality Risk",
        risk.get("data_quality_risk", "-")
    )

    c1, c2 = st.columns(2)

    c1.metric(
        "KRI Triggered",
        risk.get("key_risk_indicators_triggered", 0)
    )

    c2.metric(
        "QTL Breaches",
        risk.get("quality_tolerance_limit_breaches", 0)
    )

    st.divider()

    # ==========================================================
    # Compliance Assessment
    # ==========================================================

    compliance = result.get("compliance_assessment", {})

    st.subheader("Compliance Assessment")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Compliance Status",
        compliance.get("compliance_status", "-")
    )

    c2.metric(
        "Protocol Compliance",
        compliance.get("protocol_compliance", "-")
    )

    c3.metric(
        "Audit Readiness",
        compliance.get("audit_readiness_status", "-")
    )

    c1, c2 = st.columns(2)

    c1.metric(
        "Major Findings",
        compliance.get("major_findings", 0)
    )

    c2.metric(
        "Critical Findings",
        compliance.get("critical_findings", 0)
    )

    st.divider()

    # ==========================================================
    # Monitoring Plan
    # ==========================================================

    plan = result.get("monitoring_visit_plan", {})

    st.subheader("Monitoring Visit Plan")

    c1, c2 = st.columns(2)

    c1.info(
        f"Strategy : {plan.get('monitoring_strategy','-')}"
    )

    c2.warning(
        f"Priority : {plan.get('monitoring_priority','-')}"
    )

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Visit Required",
        yes_no(plan.get("next_visit_required"))
    )

    c2.metric(
        "Visit Type",
        plan.get("recommended_visit_type", "-")
    )

    c3.metric(
        "Within Days",
        plan.get("recommended_visit_within_days", "-")
    )

    st.divider()

    # ==========================================================
    # Recommendations
    # ==========================================================

    recs = result.get("recommendations", [])

    if recs:

        st.subheader("Recommendations")

        df = pd.DataFrame(recs)

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

    st.divider()

    # ==========================================================
    # AI Agent Analysis
    # ==========================================================

    agents = result.get("agent_analysis", {})

    st.subheader("AI Agent Analysis")

    with st.expander("Monitoring Agent", expanded=False):

        st.markdown(
            agents.get(
                "monitoring_agent_summary",
                "N/A"
            )
        )

    with st.expander("Risk Agent", expanded=False):

        st.markdown(
            agents.get(
                "risk_agent_summary",
                "N/A"
            )
        )

    with st.expander("Compliance Agent", expanded=False):

        st.markdown(
            agents.get(
                "compliance_agent_summary",
                "N/A"
            )
        )

    st.divider()

    # ==========================================================
    # Footer
    # ==========================================================

    c1, c2 = st.columns(2)

    c1.caption(
        f"Generated By : {result.get('generated_by','-')}"
    )

    c2.caption(
        result.get("message", "")
    )

    with st.expander("Raw JSON Response"):

        st.json(result)