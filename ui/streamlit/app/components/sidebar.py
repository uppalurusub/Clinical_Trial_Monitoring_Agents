import streamlit as st


def render_sidebar() -> str:
    st.sidebar.title("Clinical Trial Monitoring")
    return st.sidebar.radio(
        "Navigation",
        ["Monitoring Analysis"],
    )
