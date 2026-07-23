"""
Pydantic schemas for request validation and response serialization.

Defines the input schema for loan application data and the output schema
for prediction results used across the FastAPI backend.
"""

from pydantic import BaseModel, Field


class LoanApplication(BaseModel):
    """Schema for incoming loan application prediction requests."""

    no_of_dependents: int = Field(
        ..., ge=0, description="Number of dependents", examples=[2]
    )
    education: int = Field(
        ...,
        ge=0,
        le=1,
        description="Education level: 0 = Graduate, 1 = Not Graduate",
        examples=[0],
    )
    self_employed: int = Field(
        ...,
        ge=0,
        le=1,
        description="Self-employment status: 0 = No, 1 = Yes",
        examples=[0],
    )
    income_annum: float = Field(
        ..., gt=0, description="Annual income", examples=[9600000]
    )
    loan_amount: float = Field(
        ..., gt=0, description="Requested loan amount", examples=[29900000]
    )
    loan_term: int = Field(
        ..., gt=0, description="Loan repayment term in years", examples=[12]
    )
    cibil_score: int = Field(
        ...,
        ge=300,
        le=900,
        description="CIBIL credit score (300-900)",
        examples=[778],
    )
    residential_assets_value: float = Field(
        ..., ge=0, description="Total value of residential assets", examples=[2400000]
    )
    commercial_assets_value: float = Field(
        ..., ge=0, description="Total value of commercial assets", examples=[17600000]
    )
    luxury_assets_value: float = Field(
        ..., ge=0, description="Total value of luxury assets", examples=[22700000]
    )
    bank_asset_value: float = Field(
        ..., ge=0, description="Total value of bank assets", examples=[8000000]
    )


class PredictionResponse(BaseModel):
    """Schema for the prediction result returned to the client."""

    prediction: str = Field(
        ..., description="Loan decision: Approved or Rejected"
    )
    probability: float = Field(
        ..., ge=0, le=1, description="Model confidence for the prediction"
    )
