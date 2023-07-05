```python
import requests
from requests_oauthlib import OAuth1

# Shared dependencies
api_keys = {
    "onlyfans": {"api_key": "YOUR_ONLYFANS_API_KEY", "api_secret": "YOUR_ONLYFANS_API_SECRET"},
    "twitter": {"api_key": "YOUR_TWITTER_API_KEY", "api_secret": "YOUR_TWITTER_API_SECRET"},
    "instagram": {"api_key": "YOUR_INSTAGRAM_API_KEY", "api_secret": "YOUR_INSTAGRAM_API_SECRET"},
    "openai": {"api_key": "YOUR_OPENAI_API_KEY"}
}

def authenticate(api_name):
    """
    Function to authenticate with the given API.
    """
    api_key = api_keys[api_name]["api_key"]
    api_secret = api_keys[api_name]["api_secret"]

    if api_name in ["onlyfans", "twitter", "instagram"]:
        # OAuth1 Authentication
        auth = OAuth1(api_key, api_secret)
    elif api_name == "openai":
        # Bearer Token Authentication
        auth = {"Authorization": f"Bearer {api_key}"}
    else:
        raise ValueError(f"Unsupported API: {api_name}")

    return auth

def test_authentication():
    """
    Function to test the authentication with all APIs.
    """
    for api_name in api_keys.keys():
        auth = authenticate(api_name)
        print(f"Successfully authenticated with {api_name} API using {auth}")

if __name__ == "__main__":
    test_authentication()
```