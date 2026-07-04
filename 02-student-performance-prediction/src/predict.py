# Import Libraries
from pathlib import Path
import joblib
import pandas as pd

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "student_performance_model.pkl"

ENCODER_PATH = BASE_DIR / "models" / "encoder.pkl"

SCALER_PATH = BASE_DIR / "models" / "scaler.pkl"

# Load Everything
model = joblib.load(MODEL_PATH)

encoder = joblib.load(ENCODER_PATH)

scaler = joblib.load(SCALER_PATH)

print("✅ All files loaded successfully!")

# Create Sample Student
student = pd.DataFrame({

    "gender": ["female"],

    "race/ethnicity": ["group C"],

    "parental level of education": ["bachelor's degree"],

    "lunch": ["standard"],

    "test preparation course": ["completed"],

    "reading score": [80],

    "writing score": [85]

})

# Separate Columns
categorical_columns = [

    "gender",

    "race/ethnicity",

    "parental level of education",

    "lunch",

    "test preparation course"

]

numerical_columns = [

    "reading score",

    "writing score"

]

# Encode Categories
encoded = encoder.transform(

    student[categorical_columns]

)

encoded_df = pd.DataFrame(

    encoded,

    columns=encoder.get_feature_names_out(categorical_columns)

)

# Scale Numbers
scaled = scaler.transform(

    student[numerical_columns]

)

scaled_df = pd.DataFrame(

    scaled,

    columns=numerical_columns

)

# Combine
student_processed = pd.concat(

    [

        scaled_df,

        encoded_df

    ],

    axis=1

)

# Prediction
prediction = model.predict(student_processed)

# Display Result
print("=" * 50)

print("🎓 Student Performance Prediction")

print("=" * 50)

print(f"Predicted Math Score: {prediction[0]:.2f}")