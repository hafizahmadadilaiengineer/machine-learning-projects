"""
Model loader and prediction engine for the Smart Loan Approval System.

Handles loading the trained RandomForestClassifier from disk, converting
validated request data into a DataFrame, and returning predictions with
associated probabilities.
"""

import os
from pathlib import Path
from typing import Dict, Any

import joblib
import pandas as pd

from schemas import LoanApplication

# Resolve the model path relative to the project root (one level above backend/)


MODEL_PATH: Path = Path(
    os.getenv(
        "MODEL_PATH",
        str(Path(__file__).resolve().parent.parent / "models" / "loan_approval_model.pkl")
    )
)

# Human-readable label map matching the training encoding
LABEL_MAP: Dict[int, str] = {0: "Approved", 1: "Rejected"}

# Model columns in the exact order expected by the trained classifier
FEATURE_COLUMNS: list[str] = [
    "no_of_dependents",
    "education",
    "self_employed",
    "income_annum",
    "loan_amount",
    "loan_term",
    "cibil_score",
    "residential_assets_value",
    "commercial_assets_value",
    "luxury_assets_value",
    "bank_asset_value",
]


def _load_model() -> Any:
    """Load the serialized model from disk.

    Raises:
        FileNotFoundError: If the model file does not exist at the expected path.

    Returns:
        The trained scikit-learn estimator.
    """
    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            f"Model file not found at: {MODEL_PATH}"
        )
    return joblib.load(MODEL_PATH)


# Load once at module import time to avoid repeated I/O on every request
model = _load_model()


def predict(application: LoanApplication) -> Dict[str, Any]:
    """Run inference on a single loan application.

    Args:
        application: Validated Pydantic model containing applicant features.

    Returns:
        Dictionary with keys ``prediction`` (str) and ``probability`` (float).
    """
    input_df = pd.DataFrame(
        [application.model_dump()],
        columns=FEATURE_COLUMNS,
    )

    prediction = int(model.predict(input_df)[0])
    probability = float(model.predict_proba(input_df)[0][prediction])

    return {
        "prediction": LABEL_MAP[prediction],
        "probability": round(probability, 4),
    }
