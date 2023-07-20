```python
import api_integration
from ai_clone import ai_clone
from sms_connector import send_sms

class ChatRoom:
    def __init__(self, user_credentials, client_list):
        self.user_credentials = user_credentials
        self.client_list = client_list
        self.ai_clone = ai_clone(self.user_credentials)

    def integrate_social_media(self):
        for credential in self.user_credentials['social']:
            api_integration.integrateAPI(credential)

    def send_message(self, client, message):
        if client['preferred_contact'] == 'sms':
            send_sms(client['phone_number'], message)
        else:
            self.ai_clone.communicate(message)

    def receive_message(self, message):
        self.ai_clone.communicate(message)

    def update_client_list(self, new_client):
        self.client_list.append(new_client)

    def get_client_list(self):
        return self.client_list
```