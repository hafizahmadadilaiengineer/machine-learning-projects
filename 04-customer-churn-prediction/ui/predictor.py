"""
Model loading, feature extraction, and prediction logic.

Decoupled from the UI — call `run_prediction()` from app.py after the user
clicks "Run Prediction".
"""

from pathlib import Path

import joblib
import pandas as pd

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
_BASE_DIR = Path(__file__).resolve().parent.parent

_MODEL_PATH = _BASE_DIR / "models" / "customer_churn_model.pkl"

# ---------------------------------------------------------------------------
# Model loader (lazy singleton)
# ---------------------------------------------------------------------------
_model = None


def _load_model():
    global _model
    if _model is None:
        _model = joblib.load(_MODEL_PATH)
    return _model


# ---------------------------------------------------------------------------
# Label encoding maps (derived from the training notebook's preprocessing)
# ---------------------------------------------------------------------------

_ENCODINGS: dict[str, dict[str, int]] = {
    "Gender": {"Female": 0, "Male": 1},
    "Under 30": {"No": 0, "Yes": 1},
    "Senior Citizen": {"No": 0, "Yes": 1},
    "Married": {"No": 0, "Yes": 1},
    "Dependents": {"No": 0, "Yes": 1},
    "Country": {"United States": 0},
    "State": {"California": 0},
    "Quarter": {"Q3": 0},
    "Referred a Friend": {"No": 0, "Yes": 1},
    "Offer": {
        "No Offer": 0,
        "Offer A": 1,
        "Offer B": 2,
        "Offer C": 3,
        "Offer D": 4,
        "Offer E": 5,
    },
    "Phone Service": {"No": 0, "Yes": 1},
    "Multiple Lines": {"No": 0, "Yes": 1},
    "Internet Service": {"No": 0, "Yes": 1},
    "Internet Type": {
        "Cable": 0,
        "DSL": 1,
        "Fiber Optic": 2,
        "No Internet": 3,
    },
    "Online Security": {"No": 0, "Yes": 1},
    "Online Backup": {"No": 0, "Yes": 1},
    "Device Protection Plan": {"No": 0, "Yes": 1},
    "Premium Tech Support": {"No": 0, "Yes": 1},
    "Streaming TV": {"No": 0, "Yes": 1},
    "Streaming Movies": {"No": 0, "Yes": 1},
    "Streaming Music": {"No": 0, "Yes": 1},
    "Unlimited Data": {"No": 0, "Yes": 1},
    "Contract": {"Month-to-Month": 0, "One Year": 1, "Two Year": 2},
    "Paperless Billing": {"No": 0, "Yes": 1},
    "Payment Method": {
        "Bank Withdrawal": 0,
        "Credit Card": 1,
        "Mailed Check": 2,
    },
}

# ---------------------------------------------------------------------------
# Defaults for columns the UI does *not* expose
# ---------------------------------------------------------------------------
# The model expects 43 features.  The UI exposes most of them, but a few
# (City, Lat/Lng, Satisfaction Score, etc.) are not surfaced in the form.
# We set them to the most common / median value from the training set.
_DEFAULT_FEATURES: dict[str, int | float] = {
    "Age": 46,
    "Number of Dependents": 0,
    "Country": 0,
    "State": 0,
    "City": 554,
    "Zip Code": 93518,
    "Latitude": 36.205465,
    "Longitude": -119.595293,
    "Population": 17554,
    "Quarter": 0,
    "Referred a Friend": 0,
    "Number of Referrals": 0,
    "Avg Monthly Long Distance Charges": 22.89,
    "Avg Monthly GB Download": 17,
    "Streaming Music": 0,
    "Unlimited Data": 0,
    "Total Refunds": 0.0,
    "Total Extra Data Charges": 0,
    "Total Long Distance Charges": 401.44,
    "Total Revenue": 2108.64,
    "Satisfaction Score": 3,
}

# ---------------------------------------------------------------------------
# UI session-state key → processed column name mapping
# ---------------------------------------------------------------------------
_KEY_TO_COLUMN: dict[str, str] = {
    "gender": "Gender",
    "senior_citizen": "Senior Citizen",
    "partner": "Married",
    "dependents": "Dependents",
    "tenure": "Tenure in Months",
    "phone_service": "Phone Service",
    "multiple_lines": "Multiple Lines",
    "online_security": "Online Security",
    "online_backup": "Online Backup",
    "device_protection": "Device Protection Plan",
    "tech_support": "Premium Tech Support",
    "streaming_tv": "Streaming TV",
    "streaming_movies": "Streaming Movies",
    "paperless_billing": "Paperless Billing",
    "monthly_charges": "Monthly Charge",
    "total_charges": "Total Charges",
}

# ---------------------------------------------------------------------------
# Columns the model expects, in the exact order as training
# ---------------------------------------------------------------------------
_FEATURE_COLUMNS: list[str] = [
    "Gender",
    "Age",
    "Under 30",
    "Senior Citizen",
    "Married",
    "Dependents",
    "Number of Dependents",
    "Country",
    "State",
    "City",
    "Zip Code",
    "Latitude",
    "Longitude",
    "Population",
    "Quarter",
    "Referred a Friend",
    "Number of Referrals",
    "Tenure in Months",
    "Offer",
    "Phone Service",
    "Avg Monthly Long Distance Charges",
    "Multiple Lines",
    "Internet Service",
    "Internet Type",
    "Avg Monthly GB Download",
    "Online Security",
    "Online Backup",
    "Device Protection Plan",
    "Premium Tech Support",
    "Streaming TV",
    "Streaming Movies",
    "Streaming Music",
    "Unlimited Data",
    "Contract",
    "Paperless Billing",
    "Payment Method",
    "Monthly Charge",
    "Total Charges",
    "Total Refunds",
    "Total Extra Data Charges",
    "Total Long Distance Charges",
    "Total Revenue",
    "Satisfaction Score",
]


# ---------------------------------------------------------------------------
# Feature extraction
# ---------------------------------------------------------------------------

def _build_feature_row(session_state: dict) -> pd.DataFrame:
    """
    Convert Streamlit's session_state into a single-row DataFrame with exactly
    the 43 columns the model expects, all properly label-encoded.
    """
    row: dict[str, int | float] = {}

    # --- 1. Capture fields exposed by the UI (label-encode them) -----------
    for ui_key, col_name in _KEY_TO_COLUMN.items():
        raw_val = session_state.get(ui_key, "")

        if col_name in _ENCODINGS:
            enc_map = _ENCODINGS[col_name]
            row[col_name] = enc_map.get(str(raw_val), 0)
        else:
            # Numeric columns (tenure, monthly_charges, total_charges)
            try:
                row[col_name] = float(raw_val) if raw_val not in ("", None) else 0.0
            except (ValueError, TypeError):
                row[col_name] = 0.0

    # --- 1b. Handle Internet Service — the UI combines Internet Service
    #         type and Internet Type.  Map accordingly.
    _internet_raw = str(session_state.get("internet_service", ""))
    _internet_encodings = {"": 0, "No": 0, "DSL": 1, "Fiber optic": 1}
    row["Internet Service"] = _internet_encodings.get(_internet_raw, 0)

    # --- 1c. Handle Contract — normalise casing
    _contract_raw = str(session_state.get("contract", ""))
    _contract_map = {
        "": 0,
        "month-to-month": 0,
        "Month-to-Month": 0,
        "one year": 1,
        "One Year": 1,
        "two year": 2,
        "Two Year": 2,
    }
    row["Contract"] = _contract_map.get(_contract_raw, 0)

    # --- 1d. Handle Payment Method — normalise to raw dataset values
    _pmt_raw = str(session_state.get("payment_method", ""))
    _pmt_map = {
        "": 0,
        "Bank Withdrawal": 0,
        "Credit Card": 1,
        "Mailed Check": 2,
    }
    row["Payment Method"] = _pmt_map.get(_pmt_raw, 0)

    # --- 2. Set Under 30 default -----------------------------------------
    # The UI does not expose Age or Under 30.  Default to 0.
    row["Under 30"] = 0

    # --- 3. Set Offer default based on UI ---------------------------------
    # The UI doesn't expose Offer.  Default to No Offer.
    row["Offer"] = 0

    # --- 4. Derive Internet Type from the combined UI ---------------------
    # UI merged Internet Service and Internet Type into one dropdown with
    # options ["", "DSL", "Fiber optic", "No"].
    _internet_raw = str(session_state.get("internet_service", ""))
    _internet_type_map: dict[str, int] = {
        "": 3,
        "No": 3,
        "DSL": 1,
        "Fiber optic": 2,
    }
    row["Internet Type"] = _internet_type_map.get(_internet_raw, 3)

    # --- 5. No phone service implies no multiple lines --------------------
    phone_svc = row.get("Phone Service", 0)
    if phone_svc == 0:
        row["Multiple Lines"] = 0

    # --- 6. Apply defaults for remaining columns ---------------------------
    for col, default in _DEFAULT_FEATURES.items():
        row[col] = default

    # --- 4. Build DataFrame in the exact column order ----------------------
    df = pd.DataFrame([row], columns=_FEATURE_COLUMNS)

    return df


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def run_prediction(session_state: dict) -> tuple[int, float]:
    """
    Return (predicted_label, churn_probability).

    - predicted_label : int (0 = No Churn, 1 = Churn)
    - churn_probability : float in [0.0, 1.0] (probability of class 1)
    """
    model = _load_model()

    X = _build_feature_row(session_state)

    pred: int = int(model.predict(X)[0])
    proba: float = float(model.predict_proba(X)[0][1])

    return pred, proba
