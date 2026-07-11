from pathlib import Path

import joblib
import pandas as pd

# -----------------------------
# File Paths
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "heart_disease_model.pkl"

# -----------------------------
# Load Model
# -----------------------------
model = joblib.load(MODEL_PATH)

# -----------------------------
# Sample Patient Data
# -----------------------------
patient = pd.DataFrame({
    "age": [52],
    "sex": [1],
    "cp": [0],
    "trestbps": [125],
    "chol": [212],
    "fbs": [0],
    "restecg": [1],
    "thalach": [168],
    "exang": [0],
    "oldpeak": [1.0],
    "slope": [2],
    "ca": [2],
    "thal": [3]
})

# -----------------------------
# Predict
# -----------------------------
prediction = model.predict(patient)[0]

# -----------------------------
# Display Result
# -----------------------------
print("=" * 40)

if prediction == 1:
    print("Prediction: Heart Disease Detected")
else:
    print("Prediction: No Heart Disease")

print("=" * 40)