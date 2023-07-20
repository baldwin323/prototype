```python
import api_integration
from backend import User, Client, Sales

class SalesManager:
    def __init__(self, ai_clone, user_credentials):
        self.ai_clone = ai_clone
        self.user_credentials = user_credentials

    def sell_content(self, content, client):
        if self.ai_clone.authenticate(self.user_credentials):
            sale = Sales(content=content, client=client)
            api_integration.sell_content(sale)
            self.ai_clone.communicate(f"Content {content.id} sold to {client.name}")
            return True
        else:
            return False

    def sell_art(self, art, client):
        if self.ai_clone.authenticate(self.user_credentials):
            sale = Sales(art=art, client=client)
            api_integration.sell_art(sale)
            self.ai_clone.communicate(f"Art {art.id} sold to {client.name}")
            return True
        else:
            return False

    def close_sale(self, sale):
        if self.ai_clone.authenticate(self.user_credentials):
            api_integration.close_sale(sale)
            self.ai_clone.communicate(f"Sale {sale.id} closed")
            return True
        else:
            return False
```