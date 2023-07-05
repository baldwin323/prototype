```python
import requests
from src.authentication import authenticate
from src.data_retrieval import retrieveData
from src.data_parsing import parseData
from src.error_handling import handleError

class OnlyFansAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://onlyfans.com/api/v1/"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}"
        }

    def get_user_data(self, username):
        try:
            # Authenticate with the API
            authenticate(self.api_key)

            # Make a GET request to the OnlyFans API
            response = requests.get(f"{self.base_url}users/{username}", headers=self.headers)

            # Retrieve and parse the data
            user_data = retrieveData(response)
            parsed_data = parseData(user_data, UserSchema)

            return parsed_data

        except Exception as e:
            # Handle any errors that occur
            handleError(e)

    def get_user_posts(self, username):
        try:
            # Authenticate with the API
            authenticate(self.api_key)

            # Make a GET request to the OnlyFans API
            response = requests.get(f"{self.base_url}users/{username}/posts", headers=self.headers)

            # Retrieve and parse the data
            user_posts = retrieveData(response)
            parsed_posts = parseData(user_posts, UserSchema)

            return parsed_posts

        except Exception as e:
            # Handle any errors that occur
            handleError(e)
```