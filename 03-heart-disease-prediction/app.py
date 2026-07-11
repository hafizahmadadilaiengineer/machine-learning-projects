# Imports 
import joblib
import pandas as pd
import streamlit as st

from pathlib import Path

# Page Configuration
st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤️",
    layout="wide"
)

#Title
st.title("❤️ Heart Disease Prediction System")

st.markdown(
    """
Predict whether a patient is likely to have heart disease
using a Machine Learning model.
"""
)

#Load Model
BASE_DIR = Path(__file__).resolve().parent

MODEL_PATH = BASE_DIR / "models" / "heart_disease_model.pkl"

model = joblib.load(MODEL_PATH)

#Side bar
st.sidebar.header("❤️ Patient Information")

# Dictionaries
sex_options = {
    "Male": 1,
    "Female": 0
}

cp_options = {
    "Typical Angina": 0,
    "Atypical Angina": 1,
    "Non-anginal Pain": 2,
    "Asymptomatic": 3
}

fbs_options = {
    "False (<120 mg/dl)": 0,
    "True (>120 mg/dl)": 1
}

restecg_options = {
    "Normal": 0,
    "ST-T Wave Abnormality": 1,
    "Left Ventricular Hypertrophy": 2
}

exang_options = {
    "No": 0,
    "Yes": 1
}

slope_options = {
    "Upsloping": 0,
    "Flat": 1,
    "Downsloping": 2
}

thal_options = {
    "Normal": 1,
    "Fixed Defect": 2,
    "Reversible Defect": 3
}

#sidebar Inputs
age = st.sidebar.slider(
    "Age",
    20,
    100,
    50
)

sex = st.sidebar.selectbox(
    "Sex",
    list(sex_options.keys())
)

cp = st.sidebar.selectbox(
    "Chest Pain Type",
    list(cp_options.keys())
)

trestbps = st.sidebar.number_input(
    "Resting Blood Pressure",
    80,
    220,
    120
)

chol = st.sidebar.number_input(
    "Cholesterol",
    100,
    600,
    200
)

fbs = st.sidebar.selectbox(
    "Fasting Blood Sugar",
    list(fbs_options.keys())
)

restecg = st.sidebar.selectbox(
    "Resting ECG",
    list(restecg_options.keys())
)

thalach = st.sidebar.number_input(
    "Maximum Heart Rate",
    60,
    220,
    150
)

exang = st.sidebar.selectbox(
    "Exercise Induced Angina",
    list(exang_options.keys())
)

oldpeak = st.sidebar.number_input(
    "Old Peak",
    0.0,
    10.0,
    1.0,
    step=0.1
)

slope = st.sidebar.selectbox(
    "Slope",
    list(slope_options.keys())
)

ca = st.sidebar.selectbox(
    "Number of Major Vessels",
    [0, 1, 2, 3, 4]
)

thal = st.sidebar.selectbox(
    "Thalassemia",
    list(thal_options.keys())
)

# Create Input Data
input_data = pd.DataFrame({
    "age": [age],
    "sex": [sex_options[sex]],
    "cp": [cp_options[cp]],
    "trestbps": [trestbps],
    "chol": [chol],
    "fbs": [fbs_options[fbs]],
    "restecg": [restecg_options[restecg]],
    "thalach": [thalach],
    "exang": [exang_options[exang]],
    "oldpeak": [oldpeak],
    "slope": [slope_options[slope]],
    "ca": [ca],
    "thal": [thal_options[thal]]
})

# Show Patient Information
st.subheader("📋 Patient Information")

col1, col2 = st.columns(2)

with col1:
    st.write(f"**Age:** {age}")
    st.write(f"**Sex:** {sex}")
    st.write(f"**Chest Pain Type:** {cp}")
    st.write(f"**Resting Blood Pressure:** {trestbps}")
    st.write(f"**Cholesterol:** {chol}")
    st.write(f"**Fasting Blood Sugar:** {fbs}")
    st.write(f"**Resting ECG:** {restecg}")

with col2:
    st.write(f"**Maximum Heart Rate:** {thalach}")
    st.write(f"**Exercise Induced Angina:** {exang}")
    st.write(f"**Old Peak:** {oldpeak}")
    st.write(f"**Slope:** {slope}")
    st.write(f"**Major Vessels (CA):** {ca}")
    st.write(f"**Thalassemia:** {thal}")

# Prediction Button
if st.button(
    "🔍 Predict Heart Disease",
    use_container_width=True
):
    prediction = model.predict(input_data)[0]

    # Prediction Result
    if prediction == 1:

        st.error("""
### ❤️ Heart Disease Detected

The model predicts that the patient is at risk of heart disease.

Please consult a qualified healthcare professional for further evaluation.
""")

    else:

        st.success("""
### 💚 No Heart Disease Detected

The model predicts a low likelihood of heart disease.

This prediction should not replace professional medical advice.
""")

# Probability
probability = model.predict_proba(input_data)[0]

st.subheader("Prediction Confidence")

st.write(f"❤️ Heart Disease: {probability[1] * 100:.2f}%")
st.progress(float(probability[1]))

st.write(f"💚 No Heart Disease: {probability[0] * 100:.2f}%")
st.progress(float(probability[0]))

st.markdown("---")

st.header("📖 About the Project")

st.write("""
This application predicts whether a patient is likely to have heart disease
using a Random Forest Classifier trained on the UCI Heart Disease dataset.

The model analyzes multiple clinical features and predicts the likelihood
of heart disease.
""")

st.header("📊 Dataset Information")

st.write("""
- Dataset: UCI Heart Disease Dataset
- Machine Learning Algorithm: Random Forest Classifier
- Problem Type: Binary Classification
""")

st.header("👨‍💻 Developer")

st.write("""
**Hafiz Ahmad Adil**

- MS Computer Science
- AI Engineer
- IT Instructor
- Founder of Learn with Adil
""")
st.markdown("---")

st.caption(
    "© 2026 Hafiz Ahmad Adil | Built with Python, Scikit-learn and Streamlit"
)