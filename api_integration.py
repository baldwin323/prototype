import requests
import json
from user_credentials import user_credentials

def integrateAPI(api_url, headers=None, params=None):
    response = requests.get(api_url, headers=headers, params=params)
    return response.json()

def socialMediaAPIIntegration():
    for platform, credentials in user_credentials['social_media'].items():
        api_url = f"https://api.{platform}.com"
        headers = {"Authorization": f"Bearer {credentials['access_token']}"}
        response = integrateAPI(api_url, headers)
        print(f"Connected to {platform} API successfully.")

def financialAPIIntegration():
    for institution, credentials in user_credentials['financial_institutions'].items():
        api_url = f"https://api.{institution}.com"
        headers = {"Authorization": f"Bearer {credentials['access_token']}"}
        response = integrateAPI(api_url, headers)
        print(f"Connected to {institution} API successfully.")

if __name__ == "__main__":
    socialMediaAPIIntegration()
    financialAPIIntegration()