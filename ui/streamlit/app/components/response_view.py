import streamlit as st

from utils.formatters import (
    format_currency,
    format_score,
    format_seconds,
    value_or_na,
    yes_no,
)


def render_response(response):
    st.subheader("Response")

    if not response.get("success"):
        st.error("Claim Processing Failed")
        st.json(response)
        return

    st.success("✅ Claim Processed Successfully")

    st.subheader("Claim Summary")
    cols = st.columns(4)
    cols[0].metric("Claim ID", value_or_na(response.get("claim_id")))
    cols[1].metric("Patient ID", value_or_na(response.get("patient_id")))
    cols[2].metric("Workflow Status", value_or_na(response.get("workflow_status")))
    cols[3].metric("Risk Level", value_or_na(response.get("overall_risk_level")))
    st.divider()

    claim = response.get("claim_analysis", {})
    st.subheader("📄 Claim Analysis")
    cols = st.columns(3)
    cols[0].metric("Claim Status", value_or_na(claim.get("claim_status")))
    cols[1].metric("Submission Ready", yes_no(claim.get("submission_ready")))
    cols[2].metric("Confidence Score", format_score(claim.get("confidence_score")))
    with st.expander("Claim Summary"):
        st.write(claim.get("summary", ""))
    st.divider()

    billing = response.get("billing_analysis", {})
    st.subheader("💰 Billing Analysis")
    cols = st.columns(3)
    cols[0].metric("Claim Amount", format_currency(billing.get("total_claim_amount")))
    cols[1].metric(
        "Estimated Reimbursement",
        format_currency(billing.get("estimated_reimbursement")),
    )
    cols[2].metric(
        "Revenue Leakage", value_or_na(billing.get("revenue_leakage_risk"))
    )
    with st.expander("Billing Summary"):
        st.write(billing.get("summary", ""))
    st.divider()

    validation = response.get("validation_analysis", {})
    st.subheader("✔ Validation")
    cols = st.columns(2)
    cols[0].metric(
        "Validation Status", value_or_na(validation.get("validation_status"))
    )
    cols[1].metric(
        "Compliance", value_or_na(validation.get("compliance_status"))
    )

    missing_fields = validation.get("missing_fields", [])
    if missing_fields:
        st.warning("Missing Fields")
        st.write(missing_fields)
    else:
        st.success("No Missing Fields")

    issues = validation.get("issues", [])
    if issues:
        st.error("Validation Issues")
        st.write(issues)
    else:
        st.success("No Validation Issues")
    st.divider()

    st.subheader("💡 Recommendations")
    recommendations = response.get("recommendations", [])
    if recommendations:
        for recommendation in recommendations:
            st.info(f"• {recommendation}")
    else:
        st.write("No Recommendations")
    st.divider()

    st.subheader("⚙ Processing Information")
    cols = st.columns(2)
    cols[0].metric(
        "Processing Time", format_seconds(response.get("processing_time_seconds"))
    )
    cols[1].metric("Workflow", value_or_na(response.get("workflow_status")))
    st.divider()

    metadata = response.get("metadata", {})
    st.subheader("🏥 Metadata")
    cols = st.columns(2)
    cols[0].metric(
        "Insurance Provider", value_or_na(metadata.get("insurance_provider"))
    )
    cols[1].metric("Service Date", value_or_na(metadata.get("service_date")))
    st.divider()

    outputs = response.get("agent_outputs", {})
    st.subheader("🤖 Agent Outputs")
    tabs = st.tabs(["Claims Agent", "Billing Agent", "Validation Agent"])

    output_keys = [
        ("Claims Agent Summary", "claims_agent_output"),
        ("Billing Agent Summary", "billing_agent_output"),
        ("Validation Agent Summary", "validation_agent_output"),
    ]

    for tab, (label, key) in zip(tabs, output_keys):
        with tab:
            agent_output = outputs.get(key, "")

            if agent_output:
                st.markdown(f"### {label}")
                st.markdown(agent_output)
            else:
                st.info("No agent summary available.")

    with st.expander("View Complete JSON Response"):
        st.json(response)
