```python
import requests
from src.payment_apis.banking_api import BankingAPI
from src.payment_apis.cashtag_api import CashTagAPI

class PaymentVerification:
    def __init__(self, api_keys):
        self.banking_api = BankingAPI(api_keys['banking'])
        self.cashtag_api = CashTagAPI(api_keys['cashtag'])

    def verify_payment(self, payment_id, payment_type):
        if payment_type == 'banking':
            response = self.banking_api.get_payment_status(payment_id)
        elif payment_type == 'cashtag':
            response = self.cashtag_api.get_payment_status(payment_id)
        else:
            raise ValueError("Invalid payment type")

        if response.status_code != 200:
            raise Exception("Error in payment verification")

        payment_status = self.parse_payment_status(response.json())
        return payment_status

    def parse_payment_status(self, payment_data):
        payment_status = payment_data['status']
        return payment_status
```