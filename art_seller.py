```python
import os
from api_integration import integrateAPI
from backend import User, Client, Sales

class ArtSeller:
    def __init__(self, user_credentials, ai_clone, client_list):
        self.user_credentials = user_credentials
        self.ai_clone = ai_clone
        self.client_list = client_list

    def sellArt(self, art_id, client_id):
        client = self._getClient(client_id)
        if not client:
            return "Client not found."

        art = self._getArt(art_id)
        if not art:
            return "Art not found."

        sale = Sales(art_id, client_id)
        sale.save()

        self._notifyClient(client, art)
        return "Art sold successfully."

    def _getClient(self, client_id):
        for client in self.client_list:
            if client.id == client_id:
                return client
        return None

    def _getArt(self, art_id):
        # This is a placeholder. In a real application, you would integrate with an art database here.
        return {"id": art_id, "name": "Art Name", "price": 100}

    def _notifyClient(self, client, art):
        message = f"Dear {client.name},\n\nYou have successfully purchased {art['name']} for ${art['price']}.\n\nThank you for your purchase."
        self.ai_clone.communicate(client, message)

if __name__ == "__main__":
    user_credentials = os.getenv("USER_CREDENTIALS")
    ai_clone = os.getenv("AI_CLONE")
    client_list = os.getenv("CLIENT_LIST")

    art_seller = ArtSeller(user_credentials, ai_clone, client_list)
    art_seller.sellArt(1, 1)
```