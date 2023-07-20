```python
import api_integration
from backend import User, Sales
from sms_connector import send_sms

def sellContent(user_credentials, client_list):
    for client in client_list:
        content = api_integration.fetch_content(user_credentials)
        if content:
            sales = Sales(user_credentials, client, content)
            success = sales.make_sale()
            if success:
                message = f"Successfully sold content to {client.name}"
                print(message)
                send_sms(user_credentials, message)
            else:
                print(f"Failed to sell content to {client.name}")
        else:
            print("No content available for sale")

if __name__ == "__main__":
    user_credentials = User.get_credentials()
    client_list = User.get_clients()
    sellContent(user_credentials, client_list)
```