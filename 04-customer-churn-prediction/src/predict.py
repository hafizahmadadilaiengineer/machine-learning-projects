# Import Libraries
from pathlib import Path

import pandas as pd
import joblib

# Project Paths
BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "data" / "processed" / "processed_telco.csv"

MODEL_PATH = BASE_DIR / "models" / "customer_churn_model.pkl"

# Load Dataset
df = pd.read_csv(DATA_PATH)

print("Dataset Loaded Successfully!")

# Load Model
model = joblib.load(MODEL_PATH)

print("Model Loaded Successfully!")

# Select Sample Record
sample = df.drop("Churn Label", axis=1).iloc[[0]]

# Actual Value
actual = df["Churn Label"].iloc[0]

# Prediction
prediction = model.predict(sample)[0]

# Prediction Probability
probability = model.predict_proba(sample)[0]

# Display Results
# Convert Labels
actual_label = "Churn" if actual == 1 else "No Churn"

predicted_label = "Churn" if prediction == 1 else "No Churn"

# Display Results
print("=" * 50)

print("Customer Churn Prediction")

print("=" * 50)

print(f"Actual Value     : {actual_label}")

print(f"Predicted Value  : {predicted_label}")

print(f"\nPrediction Confidence")

print(f"No Churn : {probability[0]:.2%}")

print(f"Churn    : {probability[1]:.2%}")