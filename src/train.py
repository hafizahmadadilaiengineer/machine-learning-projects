from pathlib import Path
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Project root
BASE_DIR = Path(__file__).resolve().parent.parent

# Paths
DATA_PATH = BASE_DIR / "data" / "processed" / "processed_housing.csv"
MODEL_PATH = BASE_DIR / "models" / "house_price_model.pkl"

# Load data
df = pd.read_csv(DATA_PATH)

# Features and target
X = df.drop("price", axis=1)
y = df["price"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, MODEL_PATH)

print("✅ Model trained successfully!")
print("Model saved to:", MODEL_PATH)