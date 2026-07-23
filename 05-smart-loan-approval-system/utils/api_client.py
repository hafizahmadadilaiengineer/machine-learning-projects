"""
API client for the Smart Loan Approval & Risk Assessment System.

Provides a typed wrapper around the FastAPI ``/predict`` endpoint using
the ``requests`` library with robust error handling for network, timeout,
and HTTP-level failures.
"""

import requests

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

API_URL: str = "http://127.0.0.1:8000/predict"
REQUEST_TIMEOUT: int = 10  # seconds


# ---------------------------------------------------------------------------
# Public interface
# ---------------------------------------------------------------------------


def predict_loan(data: dict) -> dict:
    """Send a loan application to the prediction API and return the result.

    Args:
        data: Dictionary containing the 11 loan application features expected
              by the ``LoanApplication`` Pydantic schema.

    Returns:
        On success::

            {
                "success": True,
                "prediction": "Approved" | "Rejected",
                "probability": 0.9836
            }

        On failure::

            {
                "success": False,
                "message": "<human-readable error description>"
            }
    """
    try:
        response = requests.post(
            API_URL,
            json=data,
            timeout=REQUEST_TIMEOUT,
        )

        # Raise an HTTPError for 4xx / 5xx status codes so we can handle
        # them in one place below.
        response.raise_for_status()

        payload = response.json()

        return {
            "success": True,
            "prediction": payload["prediction"],
            "probability": payload["probability"],
        }

    except requests.ConnectionError:
        return {
            "success": False,
            "message": "Unable to connect to the prediction API. Please verify the server is running.",
        }

    except requests.Timeout:
        return {
            "success": False,
            "message": "Request timed out. The server took too long to respond.",
        }

    except requests.HTTPError as exc:
        status_code = exc.response.status_code if exc.response is not None else "N/A"
        return {
            "success": False,
            "message": f"Server returned HTTP {status_code}: {exc}",
        }

    except (KeyError, ValueError) as exc:
        return {
            "success": False,
            "message": f"Invalid response format from the API: {exc}",
        }

    except requests.RequestException as exc:
        return {
            "success": False,
            "message": f"An unexpected request error occurred: {exc}",
        }
