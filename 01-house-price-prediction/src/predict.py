from pathlib import Path
import pandas as pd
import joblib

# Project root
BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "house_price_model.pkl"

# Load trained model
model = joblib.load(MODEL_PATH)

# Sample input
sample_house = pd.DataFrame({
    "area": [7420],
    "bedrooms": [4],
    "bathrooms": [2],
    "stories": [3],
    "mainroad": [1],
    "guestroom": [0],
    "basement": [0],
    "hotwaterheating": [0],
    "airconditioning": [1],
    "parking": [2],
    "prefarea": [1],
    "furnishingstatus": [2]
})

prediction = model.predict(sample_house)

print("=" * 50)
print("🏠 House Price Prediction")
print("=" * 50)
print(f"Predicted Price: {prediction[0]:,.2f}")