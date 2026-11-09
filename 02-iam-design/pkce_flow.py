import os
import secrets
import hashlib
import base64
import webbrowser
import requests

from dotenv import load_dotenv
from urllib.parse import urlencode, urlparse, parse_qs
from http.server import HTTPServer, BaseHTTPRequestHandler

load_dotenv()

DOMAIN = os.getenv("AUTH0_DOMAIN")
CLIENT_ID = os.getenv("WEB_CLIENT_ID")
CLIENT_SECRET = os.getenv("WEB_CLIENT_SECRET")
AUDIENCE = os.getenv("AUTH0_AUDIENCE")
CALLBACK_URL = os.getenv("CALLBACK_URL")

# Generate PKCE verifier and challenge
verifier = secrets.token_urlsafe(64)

challenge = base64.urlsafe_b64encode(
    hashlib.sha256(verifier.encode()).digest()
).decode().rstrip("=")

state = secrets.token_urlsafe(32)


class CallbackHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        query = parse_qs(urlparse(self.path).query)

        if query.get("state", [None])[0] != state:
            self.send_error(400, "Invalid state")
            return

        CallbackHandler.code = query.get("code", [None])[0]

        self.send_response(200)
        self.end_headers()
        self.wfile.write(
            b"Authentication completed. You can close this window."
        )

    def log_message(self, format, *args):
        pass


def run_pkce():

    if not all([DOMAIN, CLIENT_ID, CLIENT_SECRET,
                AUDIENCE, CALLBACK_URL]):
        print("Missing Auth0 configuration in .env")
        return

    auth_url = f"https://{DOMAIN}/authorize"

    params = {
        "client_id": CLIENT_ID,
        "response_type": "code",
        "redirect_uri": CALLBACK_URL,
        "scope": "openid profile email read:ai-data",
        "audience": AUDIENCE,
        "state": state,
        "code_challenge": challenge,
        "code_challenge_method": "S256"
    }

    url = auth_url + "?" + urlencode(params)

    print("Opening Auth0 login...")
    webbrowser.open(url)

    print("Waiting for login...")
    server = HTTPServer(("0.0.0.0", 3000), CallbackHandler)
    server.timeout = 180
    server.handle_request()
    server.server_close()

    code = getattr(CallbackHandler, "code", None)

    if not code:
        print("Login timed out or authorization failed.")
        return

    token_url = f"https://{DOMAIN}/oauth/token"

    payload = {
        "grant_type": "authorization_code",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "code": code,
        "redirect_uri": CALLBACK_URL,
        "code_verifier": verifier
    }

    response = requests.post(token_url, json=payload)

    if response.status_code == 200:
        tokens = response.json()
        print("PKCE authentication successful!")
        print("Token type:", tokens.get("token_type"))
        print("Expires in:", tokens.get("expires_in"))
        print("Access token received successfully.")
    else:
        print("Token exchange failed:", response.status_code)
        print(response.text)


if __name__ == "__main__":
    run_pkce()

