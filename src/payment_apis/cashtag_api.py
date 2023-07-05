```python
import requests
from src.error_handling import handleError

api_keys = {
    "cashtag": "YOUR_CASHTAG_API_KEY"
}

def authenticate():
    try:
        response = requests.get(
            "https://api.cashtag.com/authenticate",
            headers={"Authorization": f"Bearer {api_keys['cashtag']}"}
        )
        response.raise_for_status()
        return response.json()["token"]
    except Exception as e:
        handleError(e)

def retrievePaymentStatus(cashtag):
    try:
        token = authenticate()
        response = requests.get(
            f"https://api.cashtag.com/payments/{cashtag}",
            headers={"Authorization": f"Bearer {token}"}
        )
        response.raise_for_status()
        return response.json()["status"]
    except Exception as e:
        handleError(e)

def verifyPayment(cashtag):
    payment_status = retrievePaymentStatus(cashtag)
    if payment_status == "completed":
        return True
    else:
        return False
```