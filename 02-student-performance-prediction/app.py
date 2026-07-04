from pathlib import Path

import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Student Performance Prediction",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -----------------------------
# Custom Styling
# -----------------------------
st.markdown(
    """
    <style>
        .main .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        .score-card {
            background: linear-gradient(135deg, #6a5cf7 0%, #8f7ff8 100%);
            padding: 2rem;
            border-radius: 16px;
            text-align: center;
            color: white;
            margin-top: 1rem;
        }
        .score-card h1 {
            font-size: 3.2rem;
            margin: 0.2rem 0;
            color: white;
        }
        .score-card p {
            font-size: 1rem;
            opacity: 0.9;
            margin: 0;
        }
        .stButton>button {
            width: 100%;
            border-radius: 10px;
            height: 3em;
            font-weight: 600;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# Load Models (cached so this only runs once)
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent


@st.cache_resource(show_spinner="Loading model...")
def load_artifacts():
    model_path = BASE_DIR / "models" / "student_performance_model.pkl"
    encoder_path = BASE_DIR / "models" / "encoder.pkl"
    scaler_path = BASE_DIR / "models" / "scaler.pkl"

    missing = [p.name for p in (model_path, encoder_path, scaler_path) if not p.exists()]
    if missing:
        raise FileNotFoundError(
            f"Missing model file(s): {', '.join(missing)}. "
            f"Make sure the 'models' folder is next to app.py."
        )

    return (
        joblib.load(model_path),
        joblib.load(encoder_path),
        joblib.load(scaler_path),
    )


try:
    model, encoder, scaler = load_artifacts()
except Exception as e:
    st.error(f"⚠️ Could not load model artifacts: {e}")
    st.stop()

# -----------------------------
# Header
# -----------------------------
st.title("🎓 Student Performance Prediction")
st.caption("Predict a student's **Math Score** from demographics and academic history.")

st.divider()

# -----------------------------
# Sidebar — Inputs
# -----------------------------
with st.sidebar:
    st.header("📋 Student Profile")

    st.subheader("Demographics")
    gender = st.selectbox("Gender", ["female", "male"])
    race = st.selectbox(
        "Race / Ethnicity",
        ["group A", "group B", "group C", "group D", "group E"],
    )
    parent = st.selectbox(
        "Parental Level of Education",
        [
            "some high school",
            "high school",
            "some college",
            "associate's degree",
            "bachelor's degree",
            "master's degree",
        ],
    )
    lunch = st.selectbox("Lunch Type", ["standard", "free/reduced"])
    prep = st.selectbox("Test Preparation Course", ["none", "completed"])

    st.subheader("Academic Scores")
    reading = st.slider("Reading Score", 0, 100, 70)
    writing = st.slider("Writing Score", 0, 100, 70)

    st.divider()
    predict_clicked = st.button("🔮 Predict Math Score", type="primary")

# -----------------------------
# Main Area
# -----------------------------
left, right = st.columns([1, 1], gap="large")

with left:
    st.subheader("📋 Student Summary")
    summary_df = pd.DataFrame(
        {
            "Field": [
                "Gender",
                "Race / Ethnicity",
                "Parental Education",
                "Lunch",
                "Test Prep",
                "Reading Score",
                "Writing Score",
            ],
            "Value": [gender, race, parent, lunch, prep, reading, writing],
        }
    )
    st.dataframe(summary_df, hide_index=True, use_container_width=True)

    m1, m2 = st.columns(2)
    m1.metric("📖 Reading", f"{reading}/100")
    m2.metric("✍️ Writing", f"{writing}/100")

with right:
    st.subheader("🎯 Prediction Result")

    if predict_clicked:
        student = pd.DataFrame(
            {
                "gender": [gender],
                "race/ethnicity": [race],
                "parental level of education": [parent],
                "lunch": [lunch],
                "test preparation course": [prep],
                "reading score": [reading],
                "writing score": [writing],
            }
        )

        categorical_columns = [
            "gender",
            "race/ethnicity",
            "parental level of education",
            "lunch",
            "test preparation course",
        ]
        numerical_columns = ["reading score", "writing score"]

        try:
            with st.spinner("Running prediction..."):
                encoded = encoder.transform(student[categorical_columns])
                encoded_df = pd.DataFrame(
                    encoded,
                    columns=encoder.get_feature_names_out(categorical_columns),
                )

                scaled = scaler.transform(student[numerical_columns])
                scaled_df = pd.DataFrame(scaled, columns=numerical_columns)

                processed = pd.concat([scaled_df, encoded_df], axis=1)
                prediction = float(model.predict(processed)[0])
                prediction = max(0.0, min(100.0, prediction))

            # Result card
            st.markdown(
                f"""
                <div class="score-card">
                    <p>PREDICTED MATH SCORE</p>
                    <h1>{prediction:.1f}</h1>
                    <p>out of 100</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

            st.progress(int(prediction))

            if prediction >= 85:
                st.success("🌟 Excellent performance predicted!")
            elif prediction >= 70:
                st.info("👍 Good performance predicted.")
            elif prediction >= 50:
                st.warning("📚 Average performance — extra practice may help.")
            else:
                st.error("⚠️ Below average — additional support recommended.")

        except Exception as e:
            st.error(f"Something went wrong during prediction: {e}")
    else:
        st.info("Fill in the student profile in the sidebar and click **Predict Math Score**.")

st.divider()
with st.expander("ℹ️ About this app"):
    st.write(
        """
        This app uses a trained machine learning model to estimate a student's
        Math score based on demographic factors and their Reading/Writing scores.
        Adjust the inputs in the sidebar and click **Predict Math Score** to see
        the result.
        """
    )
st.divider()

st.markdown(
    """
### 👨‍💻 Developed by Hafiz Ahmad Adil

**Aspiring AI Engineer | Machine Learning Enthusiast**

📌 **Project:** Student Performance Prediction

🛠 **Tech Stack:** Python • Scikit-Learn • Pandas • Streamlit

🔗 GitHub: https://github.com/hafizahmadadilaiengineer

💼 LinkedIn: https://www.linkedin.com/in/hafizahmadadildurrani

⭐ Thank you for trying this application!
"""
)
