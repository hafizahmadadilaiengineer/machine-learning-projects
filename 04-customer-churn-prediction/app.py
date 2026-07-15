"""
Main entry point for the Customer Churn Prediction System.

Run with: streamlit run app.py
"""

import streamlit as st

from ui.config import PAGE_CONFIG
from ui.styles import load_styles
from ui.predictor import run_prediction
from ui.components import (
    render_hero,
    render_sidebar_info,
    render_customer_information,
    render_services_section,
    render_billing_section,
    render_summary_stats,
    render_predict_button,
    render_result_card,
    render_about_section,
    render_footer,
)

st.set_page_config(**PAGE_CONFIG)

load_styles()

# ---------------------------------------------------------------------------
# Session state defaults
# ---------------------------------------------------------------------------
_DEFAULTS = {
    "prediction_triggered": False,
    "prediction": None,
    "probability": None,
    "processing": False,
}
for key, val in _DEFAULTS.items():
    if key not in st.session_state:
        st.session_state[key] = val


def _run_prediction() -> None:
    st.session_state.processing = True


render_sidebar_info()

render_hero()

render_customer_information()

render_services_section()

render_billing_section()

render_predict_button(on_click=_run_prediction)

if st.session_state.processing:
    with st.spinner("Analyzing customer information..."):
        pred, proba = run_prediction(st.session_state)
        st.session_state.prediction = pred
        st.session_state.probability = proba
        st.session_state.prediction_triggered = True
        st.session_state.processing = False
    st.rerun()

render_result_card()

render_about_section()

render_footer()
