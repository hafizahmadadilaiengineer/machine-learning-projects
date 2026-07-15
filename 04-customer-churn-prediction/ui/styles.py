"""
Custom CSS styles for the Customer Churn Prediction dashboard.

Blue-and-white professional theme with clean typography and spacing.
"""

CUSTOM_CSS = """
/* ---------- Global ---------- */
.stApp {
    background-color: #ffffff;
}

/* ---------- Typography ---------- */
h1, h2, h3, h4, h5, h6 {
    color: #1a3a5c !important;
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}

p, label, .stMarkdown, .stTextInput label, .stSelectbox label,
.stNumberInput label {
    color: #2c3e50 !important;
}

/* ---------- Hero ---------- */
.hero-container {
    background: linear-gradient(135deg, #1a3a5c 0%, #2c6fbb 100%);
    padding: 3rem 2rem;
    border-radius: 18px;
    margin-bottom: 2.5rem;
    text-align: center;
    box-shadow: 0 8px 32px rgba(26, 58, 92, 0.18);
}

.hero-container h1 {
    color: #ffffff !important;
    font-size: 2.6rem;
    font-weight: 700;
    margin-bottom: 0.5rem;
}

.hero-container p {
    color: rgba(255, 255, 255, 0.85) !important;
    font-size: 1.15rem;
    max-width: 640px;
    margin: 0 auto;
    line-height: 1.6;
}

.hero-badge {
    display: inline-block;
    background: rgba(255, 255, 255, 0.15);
    color: #ffffff !important;
    padding: 0.3rem 1.2rem;
    border-radius: 20px;
    font-size: 0.8rem;
    font-weight: 600;
    letter-spacing: 0.5px;
    text-transform: uppercase;
    margin-bottom: 1rem;
}

/* ---------- Section headers ---------- */
.section-header {
    border-left: 4px solid #2c6fbb;
    padding-left: 1rem;
    margin-bottom: 1.25rem;
    margin-top: 0.5rem;
}

.section-header h3 {
    margin-bottom: 0.25rem;
    font-weight: 600;
}

/* ---------- Cards ---------- */
.card {
    background: #ffffff;
    border: 1px solid #e8edf2;
    border-radius: 12px;
    padding: 1.5rem;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
    transition: box-shadow 0.2s ease;
    height: 100%;
}

.card:hover {
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
}

/* ---------- Input fields ---------- */
.stTextInput input, .stSelectbox select, .stNumberInput input {
    border: 1px solid #d1d9e0 !important;
    border-radius: 8px !important;
    padding: 0.5rem 0.75rem !important;
    font-size: 0.95rem !important;
}

.stTextInput input:focus, .stSelectbox select:focus, .stNumberInput input:focus {
    border-color: #2c6fbb !important;
    box-shadow: 0 0 0 2px rgba(44, 111, 187, 0.15) !important;
}

/* ---------- Selectbox ---------- */
.stSelectbox div[data-baseweb="select"] > div {
    border: 1px solid #d1d9e0 !important;
    border-radius: 8px !important;
}

/* ---------- Prediction button ---------- */
.predict-btn-wrapper {
    display: flex;
    justify-content: center;
    margin: 2rem 0;
}

.predict-btn-wrapper .stButton {
    display: flex;
    justify-content: center;
    width: 100%;
}

.predict-btn-wrapper button {
    background: linear-gradient(135deg, #2c6fbb 0%, #1a3a5c 100%) !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 14px !important;
    padding: 1rem 5.5rem !important;
    font-size: 1.35rem !important;
    font-weight: 700 !important;
    letter-spacing: 0.6px;
    box-shadow: 0 6px 24px rgba(44, 111, 187, 0.35);
    transition: box-shadow 0.25s ease, transform 0.25s ease;
    cursor: pointer;
}

.predict-btn-wrapper button:hover {
    box-shadow: 0 10px 34px rgba(44, 111, 187, 0.5) !important;
    transform: translateY(-3px);
}

.predict-btn-wrapper button:active {
    transform: translateY(-1px);
    box-shadow: 0 6px 20px rgba(44, 111, 187, 0.4) !important;
}

/* ---------- Result card ---------- */
.result-card {
    border: 1px solid #e8edf2;
    border-radius: 14px;
    padding: 2rem;
    text-align: center;
    background: #f8fafc;
    margin-bottom: 2rem;
}

.result-card h4 {
    color: #6b7c8b !important;
    font-weight: 500;
    margin-bottom: 0;
}

.result-card .result-value {
    font-size: 2.8rem;
    font-weight: 700;
    margin: 0.5rem 0;
}

.result-value.churn {
    color: #d63031;
}

.result-value.no-churn {
    color: #27ae60;
}

.result-card .result-detail {
    color: #6b7c8b !important;
    font-size: 0.95rem;
}

/* Confidence bar */
.confidence-bar-wrapper {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    max-width: 400px;
    margin: 1rem auto;
}

.confidence-label {
    font-size: 0.85rem;
    font-weight: 600;
    color: #4a5b6b;
    white-space: nowrap;
    min-width: 2.8rem;
}

.confidence-bar-track {
    flex: 1;
    height: 12px;
    background: #e8edf2;
    border-radius: 6px;
    overflow: hidden;
}

.confidence-bar-fill {
    height: 100%;
    border-radius: 6px;
    transition: width 0.4s ease;
}

.confidence-bar-fill.churn {
    background: linear-gradient(90deg, #e74c3c, #d63031);
}

.confidence-bar-fill.no-churn {
    background: linear-gradient(90deg, #2ecc71, #27ae60);
}

/* Recommendation box */
.recommendation-box {
    background: #ffffff;
    border: 1px solid #e8edf2;
    border-radius: 10px;
    padding: 0.9rem 1.2rem;
    margin-top: 1.2rem;
    text-align: left;
    color: #2c3e50 !important;
    font-size: 0.9rem;
    line-height: 1.6;
}

.recommendation-box strong {
    color: #1a3a5c;
}

/* ---------- About section ---------- */
.about-section {
    background: #f8fafc;
    border-radius: 14px;
    padding: 2rem;
    margin-top: 2rem;
    border: 1px solid #e8edf2;
}

.about-section h3 {
    margin-top: 0;
}

.about-section p {
    color: #4a5b6b !important;
    line-height: 1.7;
}

/* ---------- Footer ---------- */
.footer {
    text-align: center;
    padding: 2rem 0 1rem;
    color: #9aa8b5 !important;
    font-size: 0.85rem;
    border-top: 1px solid #e8edf2;
    margin-top: 2rem;
}

.footer-main {
    margin-bottom: 1.25rem;
}

/* Developer card */
.dev-card {
    display: inline-flex;
    align-items: center;
    gap: 1rem;
    background: #f8fafc;
    border: 1px solid #e8edf2;
    border-radius: 12px;
    padding: 0.9rem 1.6rem;
    text-align: left;
}

.dev-avatar {
    font-size: 2rem;
}

.dev-info {
    line-height: 1.5;
}

.dev-name {
    font-weight: 700;
    color: #1a3a5c !important;
    font-size: 0.95rem;
}

.dev-role {
    font-size: 0.8rem;
    color: #6b7c8b !important;
}

.dev-links {
    margin-top: 0.2rem;
    font-size: 0.8rem;
}

.dev-links a {
    color: #2c6fbb;
    text-decoration: none;
    font-weight: 600;
}

.dev-links a:hover {
    text-decoration: underline;
}

/* ---------- Sidebar ---------- */
.css-1d391kg, .css-12oz5g7 {
    background-color: #f8fafc;
}

/* Sidebar info table */
.info-card {
    margin: 0.5rem 0;
}

.info-table {
    width: 100%;
    border-collapse: collapse;
}

.info-table tr {
    border-bottom: 1px solid #e8edf2;
}

.info-table tr:last-child {
    border-bottom: none;
}

.info-table td {
    padding: 0.4rem 0;
    font-size: 0.85rem;
}

.info-key {
    color: #6b7c8b;
    font-weight: 500;
    width: 40%;
}

.info-val {
    color: #1a3a5c;
    font-weight: 600;
    text-align: right;
}

.info-val a {
    color: #2c6fbb;
    text-decoration: none;
}

.info-val a:hover {
    text-decoration: underline;
}

/* ---------- Spacing helpers ---------- */
.mt-2 { margin-top: 2rem; }
.mb-1 { margin-bottom: 1rem; }
.mb-2 { margin-bottom: 2rem; }

/* ---------- Stat cards ---------- */
.stat-card {
    background: #ffffff;
    border: 1px solid #e8edf2;
    border-radius: 10px;
    padding: 0.8rem 1rem;
    text-align: center;
    box-shadow: 0 1px 4px rgba(0, 0, 0, 0.04);
    margin-bottom: 1rem;
}
.stat-icon {
    font-size: 1.2rem;
    opacity: .4;
}
.stat-label {
    font-size: 0.7rem;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: #6b7c8b;
}
.stat-value {
    font-size: 1.4rem;
    font-weight: 700;
    color: #1a3a5c;
}

/* ---------- Progress bar ---------- */
[data-testid="stSidebar"] section[data-testid="stSidebarContent"] div[data-testid="stProgress"] > div {
    background-color: #e8edf2;
}
[data-testid="stSidebar"] section[data-testid="stSidebarContent"] div[data-testid="stProgress"] > div > div {
    background-color: #2c6fbb;
}

/* ---------- Divider ---------- */
.custom-divider {
    border: none;
    height: 1px;
    background: linear-gradient(to right, transparent, #e8edf2, transparent);
    margin: 0.5rem 0 1.5rem;
}
"""


def load_styles() -> None:
    import streamlit as st
    st.markdown(f"<style>{CUSTOM_CSS}</style>", unsafe_allow_html=True)
