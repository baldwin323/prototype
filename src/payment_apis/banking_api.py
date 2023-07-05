```python
import requests
from src.error_handling import handleError

api_keys = {
    "banking_api_key": "YOUR_BANKING_API_KEY"
}

def authenticate():
    try:
        response = requests.post(
            "https://bankingapi.com/auth",
            headers={"Authorization": f"Bearer {api_keys['banking_api_key']}"}
        )
        response.raise_for_status()
        return response.json()["access_token"]
    except Exception as e:
        handleError(e)

def retrieveData(access_token, endpoint):
    try:
        response = requests.get(
            f"https://bankingapi.com/{endpoint}",
            headers={"Authorization": f"Bearer {access_token}"}
        )
        response.raise_for_status()
        return response.json()
    except Exception as e:
        handleError(e)

def parseData(data):
    try:
        payment_status = data["status"]
        return payment_status
    except Exception as e:
        handleError(e)

def checkPaymentStatus(transaction_id):
    access_token = authenticate()
    data = retrieveData(access_token, f"transactions/{transaction_id}")
    payment_status = parseData(data)
    return payment_status
```