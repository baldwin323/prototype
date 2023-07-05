```python
import requests
from src.authentication import authenticate
from src.data_retrieval import retrieveData
from src.data_parsing import parseData
from src.error_handling import handleError

class InstagramAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://graph.instagram.com"
        self.session = requests.Session()

    def authenticate(self):
        headers = {"Authorization": f"Bearer {self.api_key}"}
        self.session.headers.update(headers)

    def get_user_data(self, user_id):
        try:
            response = self.session.get(f"{self.base_url}/{user_id}")
            response.raise_for_status()
        except requests.exceptions.HTTPError as http_err:
            handleError(http_err)
        except Exception as err:
            handleError(err)
        else:
            user_data = parseData(response.json(), UserSchema)
            return user_data

    def get_user_posts(self, user_id):
        try:
            response = self.session.get(f"{self.base_url}/{user_id}/media")
            response.raise_for_status()
        except requests.exceptions.HTTPError as http_err:
            handleError(http_err)
        except Exception as err:
            handleError(err)
        else:
            posts_data = parseData(response.json(), UserSchema)
            return posts_data

if __name__ == "__main__":
    api_key = authenticate("instagram")
    instagram_api = InstagramAPI(api_key)
    user_data = instagram_api.get_user_data("user_id")
    user_posts = instagram_api.get_user_posts("user_id")
```