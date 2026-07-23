"""
Centralised CSS for the Smart Loan Approval frontend.

Injecting raw CSS via ``st.markdown`` lets us style Streamlit widgets that
are otherwise locked to default theming.  Every class name defined here is
referenced from the component modules.
"""

# ---------------------------------------------------------------------------
# Global stylesheet
# ---------------------------------------------------------------------------

GLOBAL_CSS: str = """
<style>
/* ------------------------------------------------------------------
   Root & base
   ------------------------------------------------------------------*/
:root {
    --navy:       #0F1B2D;
    --navy-light: #1A3A5C;
    --teal:       #00BFA6;
    --gold:       #D4A843;
    --bg:         #F4F6F9;
    --card:       #FFFFFF;
    --text:       #1A1A2E;
    --muted:      #6C757D;
    --success:    #28A745;
    --danger:     #DC3545;
    --warning:    #FFC107;
    --radius:     12px;
    --shadow:     0 4px 24px rgba(0,0,0,0.06);
}

html, body, [class*="css"] {
    font-family: 'Inter', 'Segoe UI', sans-serif;
    background: var(--bg);
}

/* ------------------------------------------------------------------
   Hero banner
   ------------------------------------------------------------------*/
@keyframes heroFadeIn {
    from { opacity: 0; transform: translateY(18px); }
    to   { opacity: 1; transform: translateY(0); }
}
.hero-banner {
    background: linear-gradient(135deg, var(--navy) 0%, var(--navy-light) 100%);
    border-radius: var(--radius);
    padding: 3.2rem 2rem 2.8rem;
    margin-bottom: 2rem;
    color: #FFFFFF;
    text-align: center;
    box-shadow: var(--shadow);
    animation: heroFadeIn 0.7s ease-out both;
}
.hero-banner .hero-icon {
    font-size: 2.6rem;
    display: block;
    margin-bottom: 0.6rem;
}
.hero-banner h1 {
    font-size: 2.7rem;
    font-weight: 800;
    margin-bottom: 0.4rem;
    letter-spacing: -0.8px;
    line-height: 1.15;
}
.hero-banner .hero-subtitle {
    font-size: 1.08rem;
    opacity: 0.82;
    margin: 0 auto 1.6rem;
    max-width: 620px;
    line-height: 1.55;
}
/* Feature badges row */
.hero-features {
    display: flex;
    justify-content: center;
    gap: 0.8rem;
    flex-wrap: wrap;
}
.hero-feature-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    background: rgba(255, 255, 255, 0.12);
    border: 1px solid rgba(255, 255, 255, 0.2);
    border-radius: 50px;
    padding: 0.45rem 1.1rem;
    font-size: 0.82rem;
    font-weight: 600;
    color: #FFFFFF;
    backdrop-filter: blur(4px);
    transition: all 0.25s ease;
}
.hero-feature-badge:hover {
    background: rgba(255, 255, 255, 0.22);
    border-color: rgba(255, 255, 255, 0.4);
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.15);
}
.hero-feature-badge .badge-icon {
    font-size: 0.95rem;
}

/* ------------------------------------------------------------------
   Section headers
   ------------------------------------------------------------------*/
.section-header {
    font-size: 1.15rem;
    font-weight: 600;
    color: var(--navy);
    border-left: 4px solid var(--teal);
    padding-left: 0.75rem;
    margin: 1.8rem 0 1rem 0;
}

/* ------------------------------------------------------------------
   KPI / summary cards
   ------------------------------------------------------------------*/
.kpi-card {
    background: var(--card);
    border-radius: var(--radius);
    padding: 1.6rem 1rem 1.4rem;
    text-align: center;
    box-shadow: var(--shadow);
    border-top: 4px solid var(--teal);
    transition: all 0.25s ease;
    height: 100%;
}
.kpi-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.1);
}
.kpi-card .kpi-icon {
    font-size: 2rem;
    display: block;
    margin-bottom: 0.6rem;
}
.kpi-card .kpi-value {
    font-size: 1.55rem;
    font-weight: 700;
    color: var(--navy);
    margin-bottom: 0.25rem;
    line-height: 1.2;
}
.kpi-card .kpi-subtitle {
    font-size: 0.78rem;
    color: var(--muted);
    letter-spacing: 0.3px;
}
/* Per-card accent colours on the top border */
.kpi-card.kpi-teal   { border-top-color: var(--teal); }
.kpi-card.kpi-gold   { border-top-color: var(--gold); }
.kpi-card.kpi-navy   { border-top-color: var(--navy-light); }
.kpi-card.kpi-danger { border-top-color: var(--danger); }

/* ------------------------------------------------------------------
   Result card  --  AI Decision Report
   ------------------------------------------------------------------*/
@keyframes progressFill {
    from { width: 0; }
}
.decision-report {
    background: var(--card);
    border-radius: var(--radius);
    padding: 2.2rem 2rem 1.8rem;
    box-shadow: var(--shadow);
    margin-top: 1rem;
    border-left: 5px solid var(--teal);
}
.decision-report .report-header {
    font-size: 1.15rem;
    font-weight: 700;
    color: var(--navy);
    margin-bottom: 1.2rem;
    padding-bottom: 0.8rem;
    border-bottom: 1px solid #E9ECEF;
}
.decision-report .report-header span {
    font-size: 1.2rem;
}
/* Decision badge */
.decision-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.6rem 2rem;
    border-radius: 50px;
    font-size: 1.25rem;
    font-weight: 700;
    color: #fff;
    letter-spacing: 0.3px;
}
.decision-badge.approved {
    background: linear-gradient(135deg, #28A745, #20C997);
}
.decision-badge.rejected {
    background: linear-gradient(135deg, #DC3545, #E83E8C);
}
.decision-badge .badge-icon {
    font-size: 1.15rem;
}
/* Confidence section */
.confidence-section {
    margin: 1.4rem 0;
}
.confidence-value {
    font-size: 2.6rem;
    font-weight: 800;
    color: var(--navy);
    line-height: 1.1;
}
.confidence-label {
    font-size: 0.8rem;
    color: var(--muted);
    text-transform: uppercase;
    letter-spacing: 0.8px;
    margin-bottom: 0.6rem;
}
/* Animated progress bar */
.progress-track {
    width: 100%;
    height: 10px;
    background: #E9ECEF;
    border-radius: 50px;
    overflow: hidden;
    margin-top: 0.5rem;
}
.progress-fill {
    height: 100%;
    border-radius: 50px;
    animation: progressFill 1s ease-out forwards;
}
.progress-fill.fill-green  { background: linear-gradient(90deg, #28A745, #20C997); }
.progress-fill.fill-yellow { background: linear-gradient(90deg, #FFC107, #FD7E14); }
.progress-fill.fill-red    { background: linear-gradient(90deg, #DC3545, #E83E8C); }
/* Risk pill */
.risk-pill {
    display: inline-flex;
    align-items: center;
    gap: 0.35rem;
    padding: 0.35rem 1.1rem;
    border-radius: 50px;
    font-size: 0.82rem;
    font-weight: 600;
    margin-top: 0.3rem;
}
.risk-pill.risk-low    { background: #D4EDDA; color: #155724; }
.risk-pill.risk-medium { background: #FFF3CD; color: #856404; }
.risk-pill.risk-high   { background: #F8D7DA; color: #721C24; }
/* Recommendation */
.recommendation-box {
    background: #F8F9FA;
    border-radius: 10px;
    padding: 1rem 1.2rem;
    margin-top: 1rem;
    border-left: 3px solid var(--gold);
}
.recommendation-box .rec-title {
    font-size: 0.82rem;
    font-weight: 700;
    color: var(--navy);
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 0.3rem;
}
.recommendation-box .rec-text {
    font-size: 0.9rem;
    color: #495057;
    line-height: 1.55;
    margin: 0;
}
/* Decision summary insights */
.insights-section {
    margin-top: 1.2rem;
}
.insights-title {
    font-size: 0.85rem;
    font-weight: 700;
    color: var(--navy);
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 0.6rem;
}
.insight-item {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.45rem 0;
    font-size: 0.88rem;
    color: #495057;
    border-bottom: 1px solid #F1F3F5;
}
.insight-item:last-child {
    border-bottom: none;
}
.insight-item .insight-icon {
    font-size: 0.95rem;
    flex-shrink: 0;
}
/* Bottom model info */
.report-footer {
    display: flex;
    justify-content: center;
    gap: 2.5rem;
    margin-top: 1.4rem;
    padding-top: 1rem;
    border-top: 1px solid #E9ECEF;
}
.report-footer-item {
    text-align: center;
}
.report-footer-item .rf-label {
    font-size: 0.72rem;
    color: var(--muted);
    text-transform: uppercase;
    letter-spacing: 0.5px;
}
.report-footer-item .rf-value {
    font-size: 0.95rem;
    font-weight: 700;
    color: var(--navy);
}

/* ------------------------------------------------------------------
   API status pill
   ------------------------------------------------------------------*/
.status-pill {
    display: inline-block;
    padding: 0.25rem 0.85rem;
    border-radius: 50px;
    font-size: 0.78rem;
    font-weight: 600;
}
.status-connected    { background: #D4EDDA; color: #155724; }
.status-disconnected { background: #F8D7DA; color: #721C24; }

/* ------------------------------------------------------------------
   Footer
   ------------------------------------------------------------------*/
.footer {
    text-align: center;
    padding: 2.5rem 2rem 1.5rem;
    color: var(--muted);
    font-size: 0.85rem;
    border-top: 2px solid #E2E8F0;
    margin-top: 3rem;
    background: linear-gradient(180deg, var(--bg) 0%, #EDF1F7 100%);
    border-radius: var(--radius) var(--radius) 0 0;
}
.footer-developer {
    font-size: 0.95rem;
    font-weight: 600;
    color: var(--navy);
    margin-bottom: 0.15rem;
}
.footer-role {
    font-size: 0.82rem;
    color: var(--muted);
    margin-bottom: 1rem;
}
.footer-links {
    display: flex;
    justify-content: center;
    gap: 1rem;
    margin-bottom: 1.3rem;
}
.footer-link {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    padding: 0.45rem 1.1rem;
    border-radius: 50px;
    font-size: 0.82rem;
    font-weight: 600;
    text-decoration: none !important;
    transition: all 0.25s ease;
    border: 1.5px solid #E2E8F0;
    color: var(--navy);
    background: #FFFFFF;
}
.footer-link:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(0,0,0,0.08);
}
.footer-link.github:hover {
    border-color: #24292E;
    color: #24292E;
    background: #F6F8FA;
}
.footer-link.linkedin:hover {
    border-color: #0A66C2;
    color: #0A66C2;
    background: #E8F4FD;
}
.footer-link svg {
    width: 16px;
    height: 16px;
    flex-shrink: 0;
}
.footer-tech {
    display: flex;
    justify-content: center;
    gap: 1.2rem;
    flex-wrap: wrap;
    margin-top: 0.5rem;
    margin-bottom: 0.8rem;
}
.footer-tech-item {
    font-size: 0.8rem;
    color: var(--muted);
    display: inline-flex;
    align-items: center;
    gap: 0.3rem;
}
.footer-version {
    font-size: 0.75rem;
    opacity: 0.55;
    margin-top: 0.8rem;
    letter-spacing: 0.3px;
}

/* ------------------------------------------------------------------
   About section
   ------------------------------------------------------------------*/
.about-card {
    background: var(--card);
    border-radius: var(--radius);
    padding: 1.5rem 2rem;
    box-shadow: var(--shadow);
    border-left: 4px solid var(--gold);
}
.about-card p {
    color: var(--muted);
    line-height: 1.65;
    margin: 0;
}

/* ------------------------------------------------------------------
   Sidebar -- banking form cards
   ------------------------------------------------------------------*/
.sidebar-card {
    background: #F8F9FB;
    border: 1px solid #E2E8F0;
    border-radius: 10px;
    padding: 1rem 0.8rem 0.8rem;
    margin-bottom: 1rem;
}
.sidebar-card-title {
    font-size: 0.88rem;
    font-weight: 700;
    color: var(--navy);
    margin-bottom: 0.7rem;
    padding-bottom: 0.4rem;
    border-bottom: 1px solid #E2E8F0;
}
.sidebar-card-title span {
    font-size: 0.95rem;
    margin-right: 0.3rem;
}
/* Application summary */
.sidebar-summary {
    background: linear-gradient(135deg, var(--navy) 0%, var(--navy-light) 100%);
    border-radius: 10px;
    padding: 1rem 0.9rem;
    color: #FFFFFF;
    margin-bottom: 1rem;
}
.sidebar-summary .ss-title {
    font-size: 0.82rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    opacity: 0.8;
    margin-bottom: 0.6rem;
}
.sidebar-summary .ss-row {
    display: flex;
    justify-content: space-between;
    padding: 0.3rem 0;
    font-size: 0.8rem;
    border-bottom: 1px solid rgba(255,255,255,0.1);
}
.sidebar-summary .ss-row:last-child {
    border-bottom: none;
}
.sidebar-summary .ss-label {
    opacity: 0.75;
}
.sidebar-summary .ss-value {
    font-weight: 600;
}
/* Risk preview */
.risk-preview {
    border-radius: 10px;
    padding: 0.75rem 0.9rem;
    text-align: center;
    margin-bottom: 1rem;
    font-weight: 700;
    font-size: 0.88rem;
}
.risk-preview.rp-strong {
    background: #D4EDDA;
    color: #155724;
    border: 1px solid #C3E6CB;
}
.risk-preview.rp-moderate {
    background: #FFF3CD;
    color: #856404;
    border: 1px solid #FFEEBA;
}
.risk-preview.rp-high {
    background: #F8D7DA;
    color: #721C24;
    border: 1px solid #F5C6CB;
}
/* Helper text under inputs */
.sidebar-helper {
    font-size: 0.72rem;
    color: var(--muted);
    margin-top: -0.4rem;
    margin-bottom: 0.5rem;
    padding-left: 2px;
}

/* ------------------------------------------------------------------
   Sidebar -- validation & UX
   ------------------------------------------------------------------*/
.validation-msg {
    font-size: 0.78rem;
    color: #DC3545;
    padding: 0.35rem 0.6rem;
    background: #FFF5F5;
    border-radius: 6px;
    border-left: 3px solid #DC3545;
    margin: 0.3rem 0 0.5rem;
}
.completion-bar-track {
    width: 100%;
    height: 8px;
    background: #E9ECEF;
    border-radius: 50px;
    overflow: hidden;
    margin: 0.4rem 0;
}
.completion-bar-fill {
    height: 100%;
    border-radius: 50px;
    transition: width 0.4s ease;
}
.completion-bar-fill.fill-full { background: linear-gradient(90deg, #28A745, #20C997); }
.completion-bar-fill.fill-mid  { background: linear-gradient(90deg, #FFC107, #FD7E14); }
.completion-bar-fill.fill-low  { background: linear-gradient(90deg, #DC3545, #E83E8C); }
.completion-text {
    font-size: 0.78rem;
    font-weight: 600;
    margin-top: 0.15rem;
}
.success-banner {
    background: #D4EDDA;
    color: #155724;
    border: 1px solid #C3E6CB;
    border-radius: 8px;
    padding: 0.6rem 0.8rem;
    font-size: 0.82rem;
    font-weight: 600;
    text-align: center;
    margin: 0.5rem 0;
}
.tips-box {
    background: #FFF8E1;
    border: 1px solid #FFECB3;
    border-radius: 8px;
    padding: 0.6rem 0.8rem;
    margin: 0.5rem 0;
}
.tips-box .tips-title {
    font-size: 0.78rem;
    font-weight: 700;
    color: #856404;
    margin-bottom: 0.3rem;
}
.tips-box .tip-item {
    font-size: 0.75rem;
    color: #856404;
    padding: 0.15rem 0;
}

/* ------------------------------------------------------------------
   Progress bar override
   ------------------------------------------------------------------*/
div[data-testid="stProgressBar"] > div > div {
    background: linear-gradient(90deg, var(--teal), var(--navy-light));
}
</style>
"""


def inject_styles() -> None:
    """Inject the global stylesheet into the Streamlit page."""
    import streamlit as st
    st.markdown(GLOBAL_CSS, unsafe_allow_html=True)
