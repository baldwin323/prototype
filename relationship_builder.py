```python
import json
from client import Client

class RelationshipBuilder:
    def __init__(self, client_list):
        self.client_list = client_list

    def build_relationship(self, client_id, relationship_level):
        for client in self.client_list:
            if client.id == client_id:
                client.relationship_level = relationship_level
                self.update_client(client)
                return True
        return False

    def update_client(self, client):
        for i, c in enumerate(self.client_list):
            if c.id == client.id:
                self.client_list[i] = client
                self.save_clients()
                return True
        return False

    def save_clients(self):
        with open('client_list.json', 'w') as f:
            json.dump([client.to_dict() for client in self.client_list], f)

    def load_clients(self):
        try:
            with open('client_list.json', 'r') as f:
                self.client_list = [Client.from_dict(c) for c in json.load(f)]
        except FileNotFoundError:
            self.client_list = []

if __name__ == "__main__":
    rb = RelationshipBuilder([])
    rb.load_clients()
    rb.build_relationship('client1', 'high')
```