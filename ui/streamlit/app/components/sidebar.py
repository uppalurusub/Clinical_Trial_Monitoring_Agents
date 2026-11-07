import streamlit as st

from api.revenue_cycle_api import health_check


def render_sidebar():
    st.sidebar.title("🏥 Revenue Cycle Management")
    page = st.sidebar.radio("Navigation", ["Process Claim"])

    st.sidebar.divider()
    status = health_check()
    if str(status.get("status", "")).lower() in {"ok", "healthy", "available"}:
        st.sidebar.success("API Connected")
    else:
        st.sidebar.warning("API Unavailable")

    return page
