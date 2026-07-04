#Import Libraries
from pathlib import Path
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    r2_score,
    mean_absolute_error,
    mean_squared_error
)
# Project Paths
BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "data" / "processed" / "processed_student.csv"

MODEL_PATH = BASE_DIR / "models" / "student_performance_model.pkl"

# Load Dataset
df = pd.read_csv(DATA_PATH)

print("Dataset Loaded Successfully!")

df.head()

# Features & Targets
X = df.drop("math score", axis=1)

y = df["math score"]

# Train & Test Split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# Train Model
model = LinearRegression()

model.fit(X_train, y_train)

# Prediction
predictions = model.predict(X_test)

# Evaluation
r2 = r2_score(y_test, predictions)

mae = mean_absolute_error(y_test, predictions)

mse = mean_squared_error(y_test, predictions)

rmse = mse ** 0.5

# Print Results
print("=" * 50)

print("Student Performance Prediction")

print("=" * 50)

print(f"R² Score : {r2:.4f}")

print(f"MAE      : {mae:.4f}")

print(f"MSE      : {mse:.4f}")

print(f"RMSE     : {rmse:.4f}")

# Save Model
joblib.dump(model, MODEL_PATH)

print("\n✅ Model Saved Successfully!")

print(f"Model Location:\n{MODEL_PATH}")

