```python
import requests
import json
from src.authentication import authenticate

class TwitterAPI:
    def __init__(self, api_keys):
        self.api_keys = api_keys
        self.base_url = "https://api.twitter.com/1.1/"
        self.auth_token = None

    def authenticate(self):
        self.auth_token = authenticate(self.api_keys)

    def get_user_data(self, username):
        headers = {"Authorization": f"Bearer {self.auth_token}"}
        response = requests.get(f"{self.base_url}users/show.json?screen_name={username}", headers=headers)
        if response.status_code == 200:
            user_data = json.loads(response.text)
            return user_data
        else:
            raise Exception(f"Failed to retrieve user data: {response.text}")

    def get_follower_count(self, username):
        user_data = self.get_user_data(username)
        return user_data.get('followers_count', 0)

    def get_engagement_metrics(self, username):
        user_data = self.get_user_data(username)
        return {
            'favourites_count': user_data.get('favourites_count', 0),
            'statuses_count': user_data.get('statuses_count', 0)
        }

    def get_content_uploads(self, username):
        headers = {"Authorization": f"Bearer {self.auth_token}"}
        response = requests.get(f"{self.base_url}statuses/user_timeline.json?screen_name={username}", headers=headers)
        if response.status_code == 200:
            tweets = json.loads(response.text)
            return [tweet['text'] for tweet in tweets]
        else:
            raise Exception(f"Failed to retrieve tweets: {response.text}")
```