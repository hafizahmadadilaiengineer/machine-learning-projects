"""
API client for the Smart Loan Approval & Risk Assessment frontend.

Sends loan application data to the FastAPI ``/predict`` endpoint and
returns a uniform success/failure dictionary regardless of the error type.
"""

import requests

from .config import PREDICT_ENDPOINT, REQUEST_TIMEOUT


def predict_loan(data: dict) -> dict:
    """POST a loan application payload to the prediction API.

    Args:
        data: Dictionary of applicant features accepted by the backend
              ``LoanApplication`` schema.

    Returns:
        On success::

            {"success": True, "prediction": "Approved", "probability": 0.98}

        On failure::

            {"success": False, "message": "Human-readable error description"}
    """
    try:
        response = requests.post(
            PREDICT_ENDPOINT,
            json=data,
            timeout=REQUEST_TIMEOUT,
        )

        # Convert 4xx / 5xx into an HTTPError so it is handled below.
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
        status = exc.response.status_code if exc.response is not None else "N/A"
        return {
            "success": False,
            "message": f"Server returned HTTP {status}: {exc}",
        }

    except ValueError:
        return {
            "success": False,
            "message": "Invalid JSON received from the API.",
        }

    except requests.RequestException as exc:
        return {
            "success": False,
            "message": f"An unexpected error occurred: {exc}",
        }
