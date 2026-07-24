import os

API_BASE_URL = os.getenv(
    "API_BASE_URL",
    "https://loan-approval-api-lr4z.onrender.com"
)

PREDICT_ENDPOINT = f"{API_BASE_URL}/predict"
REQUEST_TIMEOUT = 15