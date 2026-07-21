import requests

API_BASE_URL = "http://localhost:8000/api/v1/monitoring"


def analyze_monitoring(payload: dict, timeout: int = 300) -> dict:
    response = requests.post(
        f"{API_BASE_URL}/analyze",
        json=payload,
        timeout=timeout,
    )
    response.raise_for_status()
    return response.json()
