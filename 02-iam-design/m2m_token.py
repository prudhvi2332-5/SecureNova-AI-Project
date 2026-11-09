import os
import requests
from dotenv import load_dotenv

load_dotenv()

AUTH0_DOMAIN = os.getenv("AUTH0_DOMAIN")
CLIENT_ID = os.getenv("M2M_CLIENT_ID")
CLIENT_SECRET = os.getenv("M2M_CLIENT_SECRET")
AUDIENCE = os.getenv("AUTH0_AUDIENCE")

def get_access_token():

    url = f"https://{AUTH0_DOMAIN}/oauth/token"

    payload = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "audience": AUDIENCE,
        "grant_type": "client_credentials"
    }

    response = requests.post(url, json=payload)

    if response.status_code == 200:
        token_data = response.json()
        print("Access token generated successfully!")
        print("Token type:", token_data.get("token_type"))
        print("Expires in:", token_data.get("expires_in"), "seconds")
        return token_data["access_token"]

    print("Token generation failed!")
    print("Status:", response.status_code)
    print("Response:", response.text)
    return None


if __name__ == "__main__":
    get_access_token()

