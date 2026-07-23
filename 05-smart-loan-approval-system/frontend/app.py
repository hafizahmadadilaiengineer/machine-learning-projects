"""
Smart Loan Approval & Risk Assessment System -- Streamlit Frontend.

This is the entry point for the Streamlit application.  It orchestrates
layout, style injection, form rendering, API calls, and result display.
"""

import sys
import time
from pathlib import Path

import streamlit as st

# ---------------------------------------------------------------------------
# Ensure the ``frontend`` directory is on sys.path so that absolute imports
# such as ``from components import ...`` and ``from styles import ...`` work
# regardless of where ``streamlit run`` is executed from.
# ---------------------------------------------------------------------------

_FRONTER_DIR = Path(__file__).resolve().parent
if str(_FRONTER_DIR) not in sys.path:
    sys.path.insert(0, str(_FRONTER_DIR))

from styles import inject_styles                          # noqa: E402
from components import (                                 # noqa: E402
    render_hero,
    render_summary_cards,
    render_result_card,
    render_about,
    render_footer,
    render_sidebar,
)
from components.dashboard import render_api_status       # noqa: E402
from utils.api_client import predict_loan                # noqa: E402
from utils.config import API_BASE_URL                    # noqa: E402

import requests  # noqa: E402


# ---------------------------------------------------------------------------
# Page configuration
# ---------------------------------------------------------------------------

st.set_page_config(
    page_title="Smart Loan Approval",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded",
)

inject_styles()


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _check_api_connection() -> bool:
    """Ping the FastAPI root to verify the backend is reachable."""
    try:
        resp = requests.get(f"{API_BASE_URL}/health", timeout=5)
        return resp.status_code == 200
    except requests.RequestException:
        return False


# ---------------------------------------------------------------------------
# Loading workflow
# ---------------------------------------------------------------------------

_LOADING_STEPS: list[tuple[str, int]] = [
    ("&#10003; Validating Applicant Information",  20),
    ("&#10003; Verifying Financial Details",        40),
    ("&#10003; Running Random Forest Model",        65),
    ("&#10003; Calculating Confidence Score",        85),
    ("&#10003; Preparing Final Decision",           100),
]


def _run_analysis(form_data: dict) -> dict:
    """Display a multi-step loading animation, then call the prediction API.

    Args:
        form_data: Applicant features dictionary.

    Returns:
        Prediction result dictionary from ``predict_loan()``.
    """
    status = st.empty()
    progress = st.progress(0)

    status.markdown(
        '<p style="font-size:1.05rem;font-weight:600;color:#0F1B2D;">'
        "&#127974; Processing Loan Application...</p>",
        unsafe_allow_html=True,
    )

    for step_text, pct in _LOADING_STEPS:
        time.sleep(0.45)
        progress.progress(pct)
        status.markdown(
            f'<p style="font-size:0.95rem;color:#6C757D;">{step_text}</p>',
            unsafe_allow_html=True,
        )

    time.sleep(0.3)
    result = predict_loan(form_data)

    progress.empty()
    status.empty()

    return result


# ---------------------------------------------------------------------------
# Layout
# ---------------------------------------------------------------------------

# -- Sidebar (form) ---------------------------------------------------------
form_data, form_valid = render_sidebar()

# -- Main area --------------------------------------------------------------
render_hero()

connected = _check_api_connection()

# Summary row with API status
col_metrics, col_status = st.columns([5, 1])
with col_metrics:
    render_summary_cards()
with col_status:
    st.markdown("<br><br>", unsafe_allow_html=True)
    render_api_status(connected)

st.markdown("---")

# -- Analyze button ---------------------------------------------------------
st.markdown(
    '<div class="section-header">Run Analysis</div>',
    unsafe_allow_html=True,
)

analyze_clicked = st.button(
    "Analyze Loan Application",
    type="primary",
    use_container_width=True,
    disabled=not form_valid,
)

if not form_valid:
    st.warning(
        "Please complete all required fields before running the analysis."
    )

# -- Prediction -------------------------------------------------------------
if analyze_clicked:
    if not connected:
        st.error(
            "Cannot reach the prediction API. "
            "Please ensure the FastAPI backend is running on "
            f"`{API_BASE_URL}`."
        )
    else:
        result = _run_analysis(form_data)
        render_result_card(result, form_data=form_data)

st.markdown("---")

# -- About ------------------------------------------------------------------
render_about()

# -- Footer -----------------------------------------------------------------
render_footer()
