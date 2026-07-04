from pathlib import Path
import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# Paths
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "models" / "house_price_model.pkl"

# Load model
model = joblib.load(MODEL_PATH)

# -----------------------------
# App Title
# -----------------------------
st.set_page_config(page_title="House Price Prediction", page_icon="🏠")

st.title("🏠 House Price Prediction")
st.write("Enter house details below to predict the price.")

# -----------------------------
# User Inputs
# -----------------------------
area = st.number_input("Area", min_value=500, max_value=20000, value=7420)

bedrooms = st.slider("Bedrooms", 1, 10, 4)
bathrooms = st.slider("Bathrooms", 1, 10, 2)
stories = st.slider("Stories", 1, 5, 3)

mainroad = st.selectbox("Main Road", ["Yes", "No"])
guestroom = st.selectbox("Guest Room", ["Yes", "No"])
basement = st.selectbox("Basement", ["Yes", "No"])
hotwater = st.selectbox("Hot Water Heating", ["Yes", "No"])
airconditioning = st.selectbox("Air Conditioning", ["Yes", "No"])
parking = st.slider("Parking", 0, 5, 2)
prefarea = st.selectbox("Preferred Area", ["Yes", "No"])

furnishing = st.selectbox(
    "Furnishing Status",
    [
        "Furnished",
        "Semi-Furnished",
        "Unfurnished"
    ]
)

# -----------------------------
# Encoding
# -----------------------------
yes_no = {"Yes": 1, "No": 0}

furnishing_map = {
    "Furnished": 0,
    "Semi-Furnished": 1,
    "Unfurnished": 2
}

input_df = pd.DataFrame({
    "area": [area],
    "bedrooms": [bedrooms],
    "bathrooms": [bathrooms],
    "stories": [stories],
    "mainroad": [yes_no[mainroad]],
    "guestroom": [yes_no[guestroom]],
    "basement": [yes_no[basement]],
    "hotwaterheating": [yes_no[hotwater]],
    "airconditioning": [yes_no[airconditioning]],
    "parking": [parking],
    "prefarea": [yes_no[prefarea]],
    "furnishingstatus": [furnishing_map[furnishing]]
})

# -----------------------------
# Prediction
# -----------------------------
if st.button("Predict Price"):

    prediction = model.predict(input_df)

    st.success(f"Estimated House Price: {prediction[0]:,.2f}")