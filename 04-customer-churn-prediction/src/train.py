# Import Libraries
from pathlib import Path

import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)

# Project Paths
BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "data" / "processed" / "processed_telco.csv"

MODEL_PATH = BASE_DIR / "models" / "customer_churn_model.pkl"

# Load Dataset
df = pd.read_csv(DATA_PATH)

print("Dataset Loaded Successfully!")

# Features & Target
X = df.drop("Churn Label", axis=1)

y = df["Churn Label"]

# Train & Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# Initialize Model
model = GradientBoostingClassifier(
    random_state=42
)

# Train Model
model.fit(X_train, y_train)

# Prediction
predictions = model.predict(X_test)

# Evaluation
accuracy = accuracy_score(y_test, predictions)

precision = precision_score(y_test, predictions)

recall = recall_score(y_test, predictions)

f1 = f1_score(y_test, predictions)

# Print Results
print("=" * 50)

print("Customer Churn Prediction")

print("=" * 50)

print(f"Accuracy  : {accuracy:.4f}")

print(f"Precision : {precision:.4f}")

print(f"Recall    : {recall:.4f}")

print(f"F1-Score  : {f1:.4f}")

# Save Model
joblib.dump(model, MODEL_PATH)

print("\n✅ Model Saved Successfully!")

print(f"Model Location:\n{MODEL_PATH}")