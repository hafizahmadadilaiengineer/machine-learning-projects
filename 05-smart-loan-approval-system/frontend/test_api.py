from utils.api_client import predict_loan

sample = {
    "no_of_dependents": 2,
    "education": 0,
    "self_employed": 0,
    "income_annum": 9600000,
    "loan_amount": 29900000,
    "loan_term": 12,
    "cibil_score": 778,
    "residential_assets_value": 2400000,
    "commercial_assets_value": 17600000,
    "luxury_assets_value": 22700000,
    "bank_asset_value": 8000000
}

print(predict_loan(sample))