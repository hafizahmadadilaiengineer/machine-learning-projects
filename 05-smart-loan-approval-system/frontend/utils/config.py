"""
Configuration constants for the Smart Loan Approval frontend client.

Centralises all API connection settings so they can be updated in a single
location without touching the rest of the codebase.
"""

# ---------------------------------------------------------------------------
# API connection
# ---------------------------------------------------------------------------

API_BASE_URL: str = "http://127.0.0.1:8000"

PREDICT_ENDPOINT: str = f"{API_BASE_URL}/predict"

REQUEST_TIMEOUT: int = 10  # seconds
