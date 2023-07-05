```python
import requests
from src.authentication import authenticate
from src.social_media_apis.onlyfans_api import OnlyFansAPI
from src.social_media_apis.twitter_api import TwitterAPI
from src.social_media_apis.instagram_api import InstagramAPI

def retrieveData(api_keys):
    user_data = {}

    # Authenticate with the APIs
    onlyfans_auth = authenticate(api_keys['onlyfans'])
    twitter_auth = authenticate(api_keys['twitter'])
    instagram_auth = authenticate(api_keys['instagram'])

    # Create API objects
    onlyfans_api = OnlyFansAPI(onlyfans_auth)
    twitter_api = TwitterAPI(twitter_auth)
    instagram_api = InstagramAPI(instagram_auth)

    # Retrieve user data from OnlyFans
    onlyfans_data = onlyfans_api.get_user_data()
    user_data['onlyfans'] = onlyfans_data

    # Retrieve user data from Twitter
    twitter_data = twitter_api.get_user_data()
    user_data['twitter'] = twitter_data

    # Retrieve user data from Instagram
    instagram_data = instagram_api.get_user_data()
    user_data['instagram'] = instagram_data

    return user_data
```