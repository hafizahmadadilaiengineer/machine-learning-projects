"""
Reusable UI components for the Customer Churn Prediction dashboard.

Each function renders a distinct section of the page.
"""

from collections.abc import Callable

import streamlit as st


# ---------------------------------------------------------------------------
# Helper: section header
# ---------------------------------------------------------------------------

def _section_header(title: str, subtitle: str | None = None) -> None:  # noqa: UP007
    st.markdown(
        f"""
        <div class="section-header">
            <h3>{title}</h3>
            {"<p style='color: #6b7c8b; font-size: 0.9rem;'>" + subtitle + "</p>" if subtitle else ""}
        </div>
        """,
        unsafe_allow_html=True,
    )


# ---------------------------------------------------------------------------
# Hero
# ---------------------------------------------------------------------------

def render_hero() -> None:
    st.markdown(
        """
        <div class="hero-container">
            <div class="hero-badge">Machine Learning</div>
            <h1>Customer Churn Prediction</h1>
            <p>
                Identify customers at risk of leaving by analysing their account,
                service, and billing data. Enter the details below and run a
                prediction to get started.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ---------------------------------------------------------------------------
# Sidebar
# ---------------------------------------------------------------------------

def render_sidebar_info() -> None:
    with st.sidebar:
        st.markdown("## About This System")

        st.markdown(
            """
            <div class="info-card">
                <table class="info-table">
                    <tr><td class="info-key">Algorithm</td><td class="info-val">Gradient Boosting Classifier</td></tr>
                    <tr><td class="info-key">Dataset</td><td class="info-val"><a href="https://www.kaggle.com/blastchar/telco-customer-churn" target="_blank">Telco Customer Churn</a></td></tr>
                    <tr><td class="info-key">Total Rows</td><td class="info-val">7,043</td></tr>
                    <tr><td class="info-key">Features</td><td class="info-val">43</td></tr>
                    <tr><td class="info-key">Target</td><td class="info-val">Churn (Yes / No)</td></tr>
                    <tr><td class="info-key">Accuracy</td><td class="info-val">~80%</td></tr>
                    <tr><td class="info-key">AUC-ROC</td><td class="info-val">~0.85</td></tr>
                </table>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("---")
        st.markdown("**Progress**  —  fields completed")
        _render_progress_bar()

        st.markdown("---")
        st.markdown(
            "Built with [Streamlit](https://streamlit.io) &nbsp;·&nbsp; "
            "Model: Gradient Boosting"
        )


def _render_progress_bar() -> None:
    """
    Count how many key fields have been filled and show a progress bar.
    This gives the user a visual cue before they hit *Run Prediction*.
    """
    tracked_keys = [
        "gender", "senior_citizen", "partner", "dependents", "tenure",
        "phone_service", "internet_service", "contract",
        "payment_method", "monthly_charges", "total_charges",
    ]
    filled = sum(
        1 for k in tracked_keys
        if st.session_state.get(k) not in (None, "", 0, 0.0)
    )
    total = len(tracked_keys)
    pct = filled / total
    st.progress(pct, text=f"{filled} / {total}")


# ---------------------------------------------------------------------------
# Customer Information
# ---------------------------------------------------------------------------

def render_customer_information() -> None:
    _section_header("Customer Information", "Demographics and account details")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.selectbox(
            "Gender",
            options=["", "Male", "Female"],
            key="gender",
        )

    with col2:
        st.selectbox(
            "Senior Citizen",
            options=["", "Yes", "No"],
            key="senior_citizen",
        )

    with col3:
        st.selectbox(
            "Partner",
            options=["", "Yes", "No"],
            key="partner",
        )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.selectbox(
            "Dependents",
            options=["", "Yes", "No"],
            key="dependents",
        )

    with col2:
        st.number_input(
            "Tenure (months)",
            min_value=0,
            max_value=100,
            value=0,
            step=1,
            key="tenure",
        )


# ---------------------------------------------------------------------------
# Services
# ---------------------------------------------------------------------------

def render_services_section() -> None:
    _section_header("Services", "Subscribed products and features")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.selectbox(
            "Phone Service",
            options=["", "Yes", "No"],
            key="phone_service",
        )

        st.selectbox(
            "Multiple Lines",
            options=["", "Yes", "No", "No phone service"],
            key="multiple_lines",
        )

    with col2:
        st.selectbox(
            "Internet Service",
            options=["", "DSL", "Fiber optic", "No"],
            key="internet_service",
        )

        st.selectbox(
            "Online Security",
            options=["", "Yes", "No", "No internet service"],
            key="online_security",
        )

    with col3:
        st.selectbox(
            "Online Backup",
            options=["", "Yes", "No", "No internet service"],
            key="online_backup",
        )

        st.selectbox(
            "Device Protection",
            options=["", "Yes", "No", "No internet service"],
            key="device_protection",
        )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.selectbox(
            "Tech Support",
            options=["", "Yes", "No", "No internet service"],
            key="tech_support",
        )

    with col2:
        st.selectbox(
            "Streaming TV",
            options=["", "Yes", "No", "No internet service"],
            key="streaming_tv",
        )

    with col3:
        st.selectbox(
            "Streaming Movies",
            options=["", "Yes", "No", "No internet service"],
            key="streaming_movies",
        )


# ---------------------------------------------------------------------------
# Billing
# ---------------------------------------------------------------------------

def render_billing_section() -> None:
    _section_header("Billing", "Payment and contract information")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.selectbox(
            "Contract",
            options=["", "Month-to-Month", "One Year", "Two Year"],
            key="contract",
        )

        st.selectbox(
            "Paperless Billing",
            options=["", "Yes", "No"],
            key="paperless_billing",
        )

    with col2:
        st.selectbox(
            "Payment Method",
            options=[
                "",
                "Bank Withdrawal",
                "Credit Card",
                "Mailed Check",
            ],
            key="payment_method",
        )

        st.number_input(
            "Monthly Charges ($)",
            min_value=0.0,
            max_value=200.0,
            value=0.0,
            step=0.1,
            format="%.2f",
            key="monthly_charges",
        )

    with col3:
        st.number_input(
            "Total Charges ($)",
            min_value=0.0,
            max_value=10000.0,
            value=0.0,
            step=1.0,
            format="%.2f",
            key="total_charges",
        )


# ---------------------------------------------------------------------------
# Summary stats row — purely decorative snapshot of current input state
# ---------------------------------------------------------------------------

def render_summary_stats() -> None:
    cols = st.columns(4)

    tenure = st.session_state.get("tenure", 0)
    monthly = st.session_state.get("monthly_charges", 0.0)
    contract = st.session_state.get("contract", "")
    internet = st.session_state.get("internet_service", "")

    metrics = [
        ("Tenure", f"{tenure}m", "\U0001f4c5"),
        ("Monthly", f"${monthly:,.2f}", "\U0001f4b0"),
        ("Contract", contract if contract else "—", "\U0001f4c4"),
        ("Internet", internet if internet else "—", "\U0001f310"),
    ]

    for col, (label, value, icon) in zip(cols, metrics):
        with col:
            st.markdown(
                f"""
                <div class="stat-card">
                    <div class="stat-icon">{icon}</div>
                    <div class="stat-label">{label}</div>
                    <div class="stat-value">{value}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )


# ---------------------------------------------------------------------------
# Predict button
# ---------------------------------------------------------------------------

def render_predict_button(on_click: Callable | None = None) -> None:
    st.markdown("---")
    render_summary_stats()
    st.markdown('<div class="predict-btn-wrapper">', unsafe_allow_html=True)
    st.button(
        "\U0001f52e Predict Customer Churn",
        type="primary",
        key="predict_btn",
        on_click=on_click,
    )
    st.markdown("</div>", unsafe_allow_html=True)


# ---------------------------------------------------------------------------
# Result card
# ---------------------------------------------------------------------------

def render_result_card() -> None:
    _section_header("Prediction Result")

    triggered = st.session_state.get("prediction_triggered", False)
    pred = st.session_state.get("prediction")
    prob = st.session_state.get("probability")

    if triggered and pred is not None:
        is_churn = pred == 1 or str(pred).lower() == "yes"
        label = "\U0001f534 Likely to Churn" if is_churn else "\U0001f7e2 Likely to Stay"
        value_class = "churn" if is_churn else "no-churn"
        conf_pct = prob if is_churn else 1.0 - prob
        confidence = conf_pct * 100

        if is_churn:
            recommendation = (
                "Consider offering a retention discount, reviewing contract terms, "
                "or reaching out with a loyalty incentive."
            )
        else:
            recommendation = (
                "The customer appears satisfied. Maintain good service and "
                "consider upsell opportunities."
            )

        st.markdown(
            f"""
            <div class="result-card">
                <h4>Prediction Result</h4>
                <div class="result-value {value_class}">{label}</div>
                <p class="result-detail">
                    Churn probability: <strong>{prob * 100:.1f}%</strong>
                </p>
                <div class="confidence-bar-wrapper">
                    <div class="confidence-label">Confidence</div>
                    <div class="confidence-bar-track">
                        <div class="confidence-bar-fill {value_class}"
                             style="width: {confidence:.0f}%;"></div>
                    </div>
                    <div class="confidence-label">{confidence:.1f}%</div>
                </div>
                <div class="recommendation-box">
                    <strong>Recommendation:</strong> {recommendation}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            """
            <div class="result-card">
                <h4>No prediction yet</h4>
                <p class="result-detail">
                    Fill in the fields above and click
                    <strong>\U0001f52e Predict Customer Churn</strong>
                    to see the result.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )


# ---------------------------------------------------------------------------
# About section
# ---------------------------------------------------------------------------

def render_about_section() -> None:
    with st.container():
        st.markdown(
            """
            <div class="about-section">
                <h3>About This Project</h3>
                <p>
                    Customer churn — when a customer stops using a company's
                    product or service — is a critical metric for subscription-based
                    businesses. This system applies a <strong>Gradient Boosting
                    classifier</strong> to the publicly available
                    <a href="https://www.kaggle.com/blastchar/telco-customer-churn"
                       target="_blank">Telco Customer Churn dataset</a>
                    to estimate the likelihood that a given customer will churn.
                </p>
                <p>
                    The model was trained on 7 043 records with 21 features
                    covering demographics, account details, service subscriptions,
                    and billing information. Feature engineering includes one-hot
                    encoding of categorical variables and standard scaling of
                    numerical columns.
                </p>
                <p><strong>Disclaimer:</strong> Predictions are for
                demonstration purposes only and should not be used for
                production decision-making without appropriate validation.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )


# ---------------------------------------------------------------------------
# Footer
# ---------------------------------------------------------------------------

def render_footer() -> None:
    st.markdown(
        """
        <div class="footer">
            <div class="footer-main">
                Customer Churn Prediction System &nbsp;·&nbsp; Built with Streamlit
                &nbsp;·&nbsp; Gradient Boosting
            </div>
            <div class="dev-card">
                <div class="dev-avatar">\U0001f468\u200d\U0001f4bb</div>
                <div class="dev-info">
                    <div class="dev-name">Hafiz Ahmad Adil</div>
                    <div class="dev-role">AI Engineer</div>
                    <div class="dev-links">
                        <a href="https://github.com/hafizahmadadilaiengineer" target="_blank">GitHub</a>
                        &nbsp;·&nbsp;
                        <a href="https://www.linkedin.com/in/hafizahmadadildurrani" target="_blank">LinkedIn</a>
                    </div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
