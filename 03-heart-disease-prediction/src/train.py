from pathlib import Path

import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# -----------------------------
# File Paths
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "data" / "processed" / "processed_heart.csv"
MODEL_PATH = BASE_DIR / "models" / "heart_disease_model.pkl"

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv(DATA_PATH)

# -----------------------------
# Split Features and Target
# -----------------------------
X = df.drop("target", axis=1)
y = df["target"]

# -----------------------------
# Train-Test Split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# -----------------------------
# Train Random Forest Model
# -----------------------------
model = RandomForestClassifier(
    random_state=42
)

model.fit(X_train, y_train)

# -----------------------------
# Save Model
# -----------------------------
joblib.dump(model, MODEL_PATH)

print("===================================")
print("Random Forest Model Trained Successfully")
print(f"Model saved to: {MODEL_PATH}")
print("===================================")