import requests

API_URL = "http://127.0.0.1:8000/revenue-cycle"
TIMEOUT_SECONDS = 120


def health_check():
    try:
        response = requests.get(f"{API_URL}/health", timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as exc:
        return {"status": "Unavailable", "error": str(exc)}


def get_info():
    try:
        response = requests.get(f"{API_URL}/info", timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as exc:
        return {"error": str(exc)}


def process_claim(payload):
    try:
        response = requests.post(
            f"{API_URL}/process-claim",
            json=payload,
            timeout=TIMEOUT_SECONDS,
        )
        if response.status_code == 200:
            return response.json()
        return {"error": response.text, "status_code": response.status_code}
    except requests.RequestException as exc:
        return {"error": str(exc)}
