import os

API_BASE_URL = os.getenv(
    "API_BASE_URL",
    "http://127.0.0.1:8000"
)

PREDICT_ENDPOINT = f"{API_BASE_URL}/predict"

REQUEST_TIMEOUT = 10