"""
FastAPI application for the Smart Loan Approval & Risk Assessment System.

Exposes a REST API with a root health-check endpoint and a POST /predict
endpoint that accepts loan application data and returns an approval decision
along with the model's confidence score.
"""

from fastapi import FastAPI, HTTPException

from schemas import LoanApplication, PredictionResponse
from predictor import predict, model

# ---------------------------------------------------------------------------
# App configuration
# ---------------------------------------------------------------------------

app = FastAPI(
    title="Smart Loan Approval & Risk Assessment System",
    description=(
        "A machine learning-powered REST API that predicts whether a loan "
        "application should be approved or rejected based on applicant "
        "financial and demographic features."
    ),
    version="1.0.0",
)


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------


@app.get("/")
def root() -> dict:
    """Health-check endpoint returning basic API information."""
    return {
        "application": "Smart Loan Approval & Risk Assessment System",
        "status": "active",
        "version": app.version,
    }


@app.get("/health")
def health() -> dict:
    """Return service health status and model availability."""
    return {
        "status": "healthy",
        "model_loaded": model is not None,
        "version": app.version,
    }


@app.post("/predict", response_model=PredictionResponse)
def predict_loan(application: LoanApplication) -> PredictionResponse:
    """Predict loan approval for a given application.

    Accepts applicant features, runs them through the trained RandomForest
    model, and returns the predicted decision (Approved / Rejected) with the
    associated confidence probability.
    """
    try:
        result = predict(application)
        return PredictionResponse(**result)
    except FileNotFoundError as exc:
        raise HTTPException(
            status_code=503,
            detail=f"Model not available: {exc}",
        )
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {exc}",
        )


# ---------------------------------------------------------------------------
# Entry point for local development
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)
