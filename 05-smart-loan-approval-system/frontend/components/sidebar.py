"""
Sidebar component: premium banking application form with validation.

Sections:
    1. Applicant Information
    2. Financial Information
    3. Asset Information
    4. Credit Profile
    5. Validation & Tips
    6. Application Summary (live)
    7. Risk Preview (live)
"""

import streamlit as st


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _risk_preview(cibil: int, income: int, loan: int) -> tuple[str, str, str]:
    """Return (label, emoji, css-class) for the live risk preview."""
    if cibil >= 750 and income >= 8_000_000:
        return "Strong Candidate", "&#128994;", "rp-strong"
    if cibil >= 600 or income >= 4_000_000:
        return "Moderate Candidate", "&#128992;", "rp-moderate"
    return "High Risk Candidate", "&#128308;", "rp-high"


def _fmt(val: int) -> str:
    """Format an integer with comma separators."""
    return f"{val:,}"


def _validate(income: int, loan: int, loan_term: int, cibil: int,
              assets: int) -> list[str]:
    """Return a list of validation error messages."""
    errors = []
    if income <= 0:
        errors.append("&#9888;&#65039; Annual income must be greater than zero.")
    if loan <= 0:
        errors.append("&#9888;&#65039; Loan amount must be greater than zero.")
    if loan_term <= 0:
        errors.append("&#9888;&#65039; Loan term must be greater than zero.")
    if cibil < 300 or cibil > 900:
        errors.append("&#9888;&#65039; CIBIL Score must be between 300 and 900.")
    if assets < 0:
        errors.append("&#9888;&#65039; Total assets cannot be negative.")
    return errors


def _completion_pct(income: int, loan: int, loan_term: int,
                    cibil: int, assets: int) -> int:
    """Return 0-100 completion percentage."""
    checks = [
        income > 0,
        loan > 0,
        loan_term > 0,
        300 <= cibil <= 900,
        assets > 0,
    ]
    return int((sum(checks) / len(checks)) * 100)


def _eligibility_label(cibil: int, income: int, assets: int) -> tuple[str, str]:
    """Return (text, colour) for estimated eligibility."""
    if cibil >= 750 and income >= 8_000_000 and assets >= 10_000_000:
        return "Strong Candidate", "#28A745"
    if cibil >= 600 or income >= 4_000_000:
        return "Moderate Candidate", "#FFC107"
    return "High Risk Candidate", "#DC3545"


def _tips(income: int, loan: int, cibil: int, assets: int) -> list[str]:
    """Generate helpful tips based on current values."""
    tips = []
    if cibil < 750:
        tips.append("Improve your CIBIL Score (target 750+).")
    if loan > income * 5:
        tips.append("Reduce requested loan amount relative to income.")
    if assets < loan:
        tips.append("Increase available assets to strengthen collateral.")
    if income < 5_000_000:
        tips.append("A higher annual income improves approval odds.")
    if not tips:
        tips.append("Your application looks strong! Ready for analysis.")
    return tips


# ---------------------------------------------------------------------------
# Main renderer
# ---------------------------------------------------------------------------

def render_sidebar() -> tuple[dict, bool]:
    """Render the sidebar form and return (form_data, is_valid)."""
    with st.sidebar:

        # ---- Loan Application header ------------------------------------
        st.markdown(
            '<div style="text-align:center; margin-bottom:0.6rem;">'
            '<span style="font-size:1.6rem;">&#127974;</span><br>'
            '<span style="font-size:1.05rem; font-weight:700; color:#0F1B2D;">'
            'Loan Application</span>'
            '</div>',
            unsafe_allow_html=True,
        )

        # ---- Section 1: Applicant Information ---------------------------
        st.markdown(
            '<div class="sidebar-card">'
            '<div class="sidebar-card-title">'
            '<span>&#128100;</span> Applicant Information'
            '</div>',
            unsafe_allow_html=True,
        )

        no_of_dependents = st.number_input(
            "Dependents",
            min_value=0,
            max_value=15,
            value=2,
        )

        education = st.selectbox(
            "Education Level",
            options=["Graduate", "Not Graduate"],
            index=0,
        )

        self_employed = st.selectbox(
            "Employment Type",
            options=["Salaried", "Self-Employed"],
            index=0,
        )

        st.markdown('</div>', unsafe_allow_html=True)

        # ---- Section 2: Financial Information ---------------------------
        st.markdown(
            '<div class="sidebar-card">'
            '<div class="sidebar-card-title">'
            '<span>&#128176;</span> Financial Information'
            '</div>',
            unsafe_allow_html=True,
        )

        income_annum = st.number_input(
            "Annual Income (PKR)",
            min_value=0,
            value=9_600_000,
            step=100_000,
            format="%d",
        )
        st.markdown(
            '<div class="sidebar-helper">Total annual income before taxes</div>',
            unsafe_allow_html=True,
        )

        loan_amount = st.number_input(
            "Requested Loan Amount (PKR)",
            min_value=0,
            value=29_900_000,
            step=100_000,
            format="%d",
        )
        st.markdown(
            '<div class="sidebar-helper">Total loan amount you wish to borrow</div>',
            unsafe_allow_html=True,
        )

        loan_term = st.number_input(
            "Loan Term (Years)",
            min_value=1,
            max_value=30,
            value=12,
        )

        st.markdown('</div>', unsafe_allow_html=True)

        # ---- Section 3: Asset Information -------------------------------
        st.markdown(
            '<div class="sidebar-card">'
            '<div class="sidebar-card-title">'
            '<span>&#127968;</span> Asset Information'
            '</div>',
            unsafe_allow_html=True,
        )

        residential_assets_value = st.number_input(
            "Residential Assets (PKR)",
            min_value=0,
            value=2_400_000,
            step=100_000,
            format="%d",
        )

        commercial_assets_value = st.number_input(
            "Commercial Assets (PKR)",
            min_value=0,
            value=17_600_000,
            step=100_000,
            format="%d",
        )

        luxury_assets_value = st.number_input(
            "Luxury Assets (PKR)",
            min_value=0,
            value=22_700_000,
            step=100_000,
            format="%d",
        )

        bank_asset_value = st.number_input(
            "Bank Assets (PKR)",
            min_value=0,
            value=8_000_000,
            step=100_000,
            format="%d",
        )

        st.markdown('</div>', unsafe_allow_html=True)

        # ---- Section 4: Credit Profile ----------------------------------
        st.markdown(
            '<div class="sidebar-card">'
            '<div class="sidebar-card-title">'
            '<span>&#128200;</span> Credit Profile'
            '</div>',
            unsafe_allow_html=True,
        )

        cibil_score = st.slider(
            "CIBIL Score",
            min_value=300,
            max_value=900,
            value=778,
        )
        st.markdown(
            '<div class="sidebar-helper">'
            '300 = Poor &nbsp;|&nbsp; 600 = Good &nbsp;|&nbsp; 750+ = Excellent'
            '</div>',
            unsafe_allow_html=True,
        )

        st.markdown('</div>', unsafe_allow_html=True)

        # ---- Derived values ---------------------------------------------
        total_assets = (
            residential_assets_value
            + commercial_assets_value
            + luxury_assets_value
            + bank_asset_value
        )

        # ---- Section 5: Validation & Tips ------------------------------
        errors = _validate(income_annum, loan_amount, loan_term,
                           cibil_score, total_assets)
        is_valid = len(errors) == 0
        pct = _completion_pct(income_annum, loan_amount, loan_term,
                              cibil_score, total_assets)

        # Completion indicator
        fill_cls = "fill-full" if pct == 100 else ("fill-mid" if pct >= 60 else "fill-low")
        pct_color = "#28A745" if pct == 100 else ("#FFC107" if pct >= 60 else "#DC3545")

        st.markdown(
            '<div class="sidebar-card">'
            '<div class="sidebar-card-title">'
            '<span>&#128202;</span> Application Completion'
            '</div>'
            '<div class="completion-bar-track">'
            '<div class="completion-bar-fill {fill}" style="width:{pct}%;"></div>'
            '</div>'
            '<div class="completion-text" style="color:{clr};">{pct}% Complete</div>'
            '</div>'.format(fill=fill_cls, pct=pct, clr=pct_color),
            unsafe_allow_html=True,
        )

        # Validation messages
        for err in errors:
            st.markdown(
                '<div class="validation-msg">{}</div>'.format(err),
                unsafe_allow_html=True,
            )

        # Success banner
        if is_valid:
            st.markdown(
                '<div class="success-banner">'
                '&#10003; Application Complete &mdash; Ready for AI Analysis'
                '</div>',
                unsafe_allow_html=True,
            )

        # Estimated eligibility
        elig_text, elig_clr = _eligibility_label(cibil_score, income_annum,
                                                  total_assets)
        st.markdown(
            '<div class="sidebar-card">'
            '<div class="sidebar-card-title">'
            '<span>&#127919;</span> Estimated Eligibility'
            '</div>'
            '<div style="font-size:0.88rem;font-weight:700;color:{clr};">'
            '{text}</div>'
            '</div>'.format(clr=elig_clr, text=elig_text),
            unsafe_allow_html=True,
        )

        # Helpful tips
        tips = _tips(income_annum, loan_amount, cibil_score, total_assets)
        tip_html = "".join(
            '<div class="tip-item">&#8226; {}</div>'.format(t) for t in tips
        )
        st.markdown(
            '<div class="tips-box">'
            '<div class="tips-title">&#128161; Helpful Tips</div>'
            '{}'
            '</div>'.format(tip_html),
            unsafe_allow_html=True,
        )

        # ---- Section 6: Live Application Summary -----------------------
        emp_label = "Salaried" if self_employed == "Salaried" else "Self-Employed"

        st.markdown(
            '<div class="sidebar-summary">'
            '<div class="ss-title">&#128202; Application Summary</div>'
            '<div class="ss-row"><span class="ss-label">Income</span>'
            '<span class="ss-value">PKR {:,}</span></div>'
            '<div class="ss-row"><span class="ss-label">Loan Amount</span>'
            '<span class="ss-value">PKR {:,}</span></div>'
            '<div class="ss-row"><span class="ss-label">Credit Score</span>'
            '<span class="ss-value">{}</span></div>'
            '<div class="ss-row"><span class="ss-label">Dependents</span>'
            '<span class="ss-value">{}</span></div>'
            '<div class="ss-row"><span class="ss-label">Education</span>'
            '<span class="ss-value">{}</span></div>'
            '<div class="ss-row"><span class="ss-label">Employment</span>'
            '<span class="ss-value">{}</span></div>'
            '<div class="ss-row"><span class="ss-label">Total Assets</span>'
            '<span class="ss-value">PKR {:,}</span></div>'
            '</div>'.format(
                income_annum,
                loan_amount,
                cibil_score,
                no_of_dependents,
                education,
                emp_label,
                total_assets,
            ),
            unsafe_allow_html=True,
        )

        # ---- Section 7: Risk Preview ------------------------------------
        risk_label, risk_icon, risk_css = _risk_preview(
            cibil_score, income_annum, loan_amount
        )
        st.markdown(
            '<div class="risk-preview {}">{} {}</div>'.format(
                risk_css, risk_icon, risk_label
            ),
            unsafe_allow_html=True,
        )

    # -- Encode categoricals to match training preprocessing -------------
    education_encoded = 0 if education == "Graduate" else 1
    self_employed_encoded = 0 if self_employed == "Salaried" else 1

    form_data = {
        "no_of_dependents": no_of_dependents,
        "education": education_encoded,
        "self_employed": self_employed_encoded,
        "income_annum": income_annum,
        "loan_amount": loan_amount,
        "loan_term": loan_term,
        "cibil_score": cibil_score,
        "residential_assets_value": residential_assets_value,
        "commercial_assets_value": commercial_assets_value,
        "luxury_assets_value": luxury_assets_value,
        "bank_asset_value": bank_asset_value,
    }

    return form_data, is_valid
