import streamlit as st

from api.monitoring_api import analyze_monitoring
from components.request_form import render_request_form
from components.response_view import display_response
from components.sidebar import render_sidebar

st.set_page_config(
    page_title="Clinical Trial Monitoring",
    page_icon="🩺",
    layout="wide",
)

page = render_sidebar()

if page == "Monitoring Analysis":
    st.title("Clinical Trial Monitoring Analysis")
    st.divider()

    payload = render_request_form()

    with st.expander("Request JSON"):
        st.json(payload)

    if st.button("Analyze Monitoring", use_container_width=True):
        with st.spinner("Running Monitoring Agents..."):
            try:
                result = analyze_monitoring(payload)
                st.success("Analysis Completed")
                display_response(result)
            except Exception as exc:
                st.error(str(exc))
