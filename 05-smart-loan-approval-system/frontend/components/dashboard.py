"""
Dashboard components: hero banner, summary cards, result display, and about.

These are pure-render functions that receive data and produce HTML/markdown.
No business logic or API calls live here.
"""

import streamlit as st

from styles import inject_styles

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _risk_level(probability: float, prediction: str) -> tuple[str, str]:
    """Derive a human-readable risk level from the model output.

    Returns:
        Tuple of (label, CSS class name).
    """
    if prediction == "Approved":
        if probability >= 0.85:
            return "Low Risk", "risk-low"
        return "Medium Risk", "risk-medium"

    if probability >= 0.85:
        return "High Risk", "risk-high"
    return "Medium Risk", "risk-medium"


def _progress_color(probability: float, prediction: str) -> str:
    """Return a CSS class for the progress bar colour."""
    if prediction == "Approved":
        return "fill-green" if probability >= 0.70 else "fill-yellow"
    return "fill-red" if probability >= 0.70 else "fill-yellow"


def _recommendation(prediction: str, risk_label: str) -> str:
    """Return a recommendation paragraph."""
    if prediction == "Approved":
        return (
            "Applicant demonstrates excellent repayment capability "
            "and financial stability."
        )
    return (
        "Applicant currently does not satisfy loan approval requirements. "
        "Improve credit profile or reduce loan amount before reapplying."
    )


def _decision_insights(data: dict, prediction: str) -> list[tuple[str, str]]:
    """Generate 3-5 rule-based insights from the submitted form data.

    Each insight is a ``(icon, text)`` tuple.
    """
    insights: list[tuple[str, str]] = []
    cibil = data.get("cibil_score", 0)
    income = data.get("income_annum", 0)
    loan = data.get("loan_amount", 0)
    total_assets = (
        data.get("residential_assets_value", 0)
        + data.get("commercial_assets_value", 0)
        + data.get("luxury_assets_value", 0)
        + data.get("bank_asset_value", 0)
    )

    # Credit score insight
    if cibil >= 750:
        insights.append(("&#10003;", "Excellent Credit Score"))
    elif cibil >= 600:
        insights.append(("&#10003;", "Good Credit Score"))
    else:
        insights.append(("&#9888;", "Low Credit Score"))

    # Income insight
    if income >= 8_000_000:
        insights.append(("&#10003;", "High Annual Income"))
    elif income >= 4_000_000:
        insights.append(("&#10003;", "Moderate Annual Income"))
    else:
        insights.append(("&#9888;", "Low Annual Income"))

    # Loan vs income ratio
    if income > 0 and loan / income <= 3:
        insights.append(("&#10003;", "Healthy Loan-to-Income Ratio"))
    else:
        insights.append(("&#9888;", "Loan Amount Exceeds Safe Threshold"))

    # Asset portfolio
    if total_assets >= 30_000_000:
        insights.append(("&#10003;", "Strong Asset Portfolio"))
    elif total_assets >= 15_000_000:
        insights.append(("&#10003;", "Moderate Asset Portfolio"))
    else:
        insights.append(("&#9888;", "Weak Asset Position"))

    # Self employed risk
    if data.get("self_employed", 0) == 1:
        insights.append(("&#9888;", "Self-Employed (Higher Risk Category)"))
    else:
        insights.append(("&#10003;", "Salaried Employment (Stable Income)"))

    return insights


# ---------------------------------------------------------------------------
# Public renderers
# ---------------------------------------------------------------------------


def render_hero() -> None:
    """Render the top hero banner with gradient background, title, and feature badges."""
    st.markdown(
        """
        <div class="hero-banner">
            <span class="hero-icon">&#127974;</span>
            <h1>Smart Loan Approval &amp; Risk Assessment</h1>
            <p class="hero-subtitle">
                Enterprise-grade Machine Learning system for intelligent loan approval.
            </p>
            <div class="hero-features">
                <span class="hero-feature-badge">
                    <span class="badge-icon">&#10003;</span> Instant Loan Prediction
                </span>
                <span class="hero-feature-badge">
                    <span class="badge-icon">&#10003;</span> 98.36% Model Accuracy
                </span>
                <span class="hero-feature-badge">
                    <span class="badge-icon">&#10003;</span> FastAPI REST API
                </span>
                <span class="hero-feature-badge">
                    <span class="badge-icon">&#10003;</span> AI Risk Assessment
                </span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_api_status(connected: bool) -> None:
    """Display a small pill indicating backend connectivity."""
    if connected:
        html = '<span class="status-pill status-connected">Connected</span>'
    else:
        html = '<span class="status-pill status-disconnected">Disconnected</span>'
    st.sidebar.markdown(html, unsafe_allow_html=True)


def render_summary_cards() -> None:
    """Render a row of four KPI summary cards."""
    col1, col2, col3, col4 = st.columns(4)

    cards = [
        ("kpi-teal",   "&#129504;", "Random Forest", "Machine Learning Model"),
        ("kpi-gold",   "&#127919;", "98.36%",         "Model Accuracy"),
        ("kpi-navy",   "&#128202;", "11",             "Input Features"),
        ("kpi-danger", "&#9889;",   "FastAPI",        "REST API Backend"),
    ]

    for col, (accent, icon, value, subtitle) in zip(
        [col1, col2, col3, col4], cards
    ):
        with col:
            st.markdown(
                '<div class="kpi-card {}">'
                '<span class="kpi-icon">{}</span>'
                '<div class="kpi-value">{}</div>'
                '<div class="kpi-subtitle">{}</div>'
                '</div>'.format(accent, icon, value, subtitle),
                unsafe_allow_html=True,
            )


def render_result_card(result: dict, form_data: dict | None = None) -> None:
    """Render the AI Decision Report card.

    Args:
        result: Prediction result dictionary from ``predict_loan()``.
        form_data: Original applicant form data for generating insights.
    """
    if not result.get("success"):
        st.error(f"Prediction failed: {result.get('message', 'Unknown error')}")
        return

    prediction = result["prediction"]
    probability = result["probability"]
    confidence_pct = round(probability * 100, 2)

    badge_class = "approved" if prediction == "Approved" else "rejected"
    risk_label, risk_css = _risk_level(probability, prediction)
    recommendation = _recommendation(prediction, risk_label)
    fill_class = _progress_color(probability, prediction)

    # Decision icon
    if prediction == "Approved":
        decision_icon = "&#128994;"
        decision_text = "LOAN APPROVED"
    else:
        decision_icon = "&#10060;"
        decision_text = "LOAN REJECTED"

    # Build insights HTML
    insights_html = ""
    if form_data:
        insights = _decision_insights(form_data, prediction)
        for icon, text in insights:
            insights_html += (
                '<div class="insight-item">'
                '<span class="insight-icon">{}</span>{}'
                '</div>'
            ).format(icon, text)

    st.markdown(
        (
            '<div class="decision-report">'

            # Header
            '<div class="report-header">'
            '<span>&#127974;</span> AI Decision Report'
            '</div>'

            # Decision badge
            '<div style="text-align:center;">'
            '<div class="decision-badge {}">'
            '<span class="badge-icon">{}</span> {}'
            '</div>'
            '</div>'

            # Confidence
            '<div class="confidence-section" style="text-align:center; margin-top:1.2rem;">'
            '<div class="confidence-label">Confidence Score</div>'
            '<div class="confidence-value">{}%</div>'
            '<div class="progress-track">'
            '<div class="progress-fill {}" style="width:{}%;"></div>'
            '</div>'
            '</div>'

            # Risk + Recommendation row
            '<div style="display:flex; gap:1rem; margin-top:1.2rem; flex-wrap:wrap;">'

            # Risk pill
            '<div style="flex:0 0 auto;">'
            '<div class="risk-pill {}">&#9888; {}</div>'
            '</div>'

            # Recommendation
            '<div style="flex:1; min-width:280px;">'
            '<div class="recommendation-box">'
            '<div class="rec-title">&#128204; Recommendation</div>'
            '<p class="rec-text">{}</p>'
            '</div>'
            '</div>'

            '</div>'

            # Decision Summary
            '<div class="insights-section">'
            '<div class="insights-title">&#128269; Decision Summary</div>'
            '{}'
            '</div>'

            # Footer
            '<div class="report-footer">'
            '<div class="report-footer-item">'
            '<div class="rf-label">Model Used</div>'
            '<div class="rf-value">Random Forest Classifier</div>'
            '</div>'
            '<div class="report-footer-item">'
            '<div class="rf-label">Accuracy</div>'
            '<div class="rf-value">98.36%</div>'
            '</div>'
            '</div>'

            '</div>'
        ).format(
            badge_class,
            decision_icon,
            decision_text,
            confidence_pct,
            fill_class,
            confidence_pct,
            risk_css,
            risk_label,
            recommendation,
            insights_html,
        ),
        unsafe_allow_html=True,
    )


def render_about() -> None:
    """Render the About section with project description."""
    st.markdown(
        '<div class="section-header">About This Project</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <div class="about-card">
            <p>
                The <strong>Smart Loan Approval &amp; Risk Assessment System</strong>
                is an end-to-end machine learning project that predicts whether a
                loan application should be approved or rejected. It combines a
                <strong>Random Forest Classifier</strong> (98.36% accuracy) trained
                on 4,269 historical records with a <strong>FastAPI</strong> backend
                and a <strong>Streamlit</strong> frontend. The system analyses 11
                applicant features -- including income, credit score, assets, and
                employment status -- to deliver instant, data-driven lending
                decisions.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
