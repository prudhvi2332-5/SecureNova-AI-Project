import os
import secrets
import hashlib
import base64
import jwt
import json

from flask import Flask, redirect, request, session, url_for
from authlib.integrations.flask_client import OAuth
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")

app.config["SESSION_COOKIE_SECURE"] = True
app.config["SESSION_COOKIE_HTTPONLY"] = True
app.config["SESSION_COOKIE_SAMESITE"] = "Lax"

oauth = OAuth(app)

auth0 = oauth.register(
    "auth0",
    client_id=os.getenv("AUTH0_CLIENT_ID"),
    client_secret=os.getenv("AUTH0_CLIENT_SECRET"),
    client_kwargs={
        "scope": "openid profile email",
        "code_challenge_method": "S256",
    },
    server_metadata_url=(
        f"https://{os.getenv('AUTH0_DOMAIN')}/.well-known/openid-configuration"
    ),
)
#Register the second Auth0 application
auth0_client2 = oauth.register(
    "auth0_client2",
    client_id=os.getenv("AUTH0_CLIENT2_ID"),
    client_secret=os.getenv("AUTH0_CLIENT2_SECRET"),
    server_metadata_url=(
        f"https://{os.getenv('AUTH0_DOMAIN')}/.well-known/openid-configuration"
    ),
    client_kwargs={
        "scope": "openid profile email",
        "code_challenge_method": "S256",
    },
)

@app.route("/")
def home():
    if "user" in session:
        return f"""
        <h1>SecureNova AI</h1>
        <h2>Welcome {session['user'].get('name', 'User')}</h2>
        <a href='/logout'>Logout</a>
        """
    return "<h1>SecureNova AI</h1><a href='/login'>Login with Auth0</a>"

@app.route("/login")
def login():
    verifier = secrets.token_urlsafe(64)
    challenge = base64.urlsafe_b64encode(
        hashlib.sha256(verifier.encode()).digest()
    ).decode("utf-8").rstrip("=")

    session["code_verifier"] = verifier

    return auth0.authorize_redirect(
        redirect_uri=os.getenv("AUTH0_CALLBACK_URL"),
        code_challenge=challenge,
        code_challenge_method="S256",
        audience=os.getenv("AUTH0_AUDIENCE"),
        scope="openid profile email read:ai-data write:admin offline_access"
    )

@app.route("/callback")
def callback():
    

    token = auth0.authorize_access_token()
    print("ACCESS TOKEN EXISTS:",bool(token.get("access_token")))
    print("ID TOKEN EXISTS:",bool(token.get("id_token")))
    print("REFRESH TOKEN EXISTS:",bool(token.get("refresh_token")))

    print("ACCESS TOKEN:",token.get("access_token"))
       

    session["user"] = token.get("userinfo", {})
    return redirect("/")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(
        f"https://{os.getenv('AUTH0_DOMAIN')}/v2/logout?"
        f"client_id={os.getenv('AUTH0_CLIENT_ID')}"
        f"&returnTo={os.getenv('AUTH0_CALLBACK_URL').replace('/callback',"")}"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
# Second application home page
@app.route("/client2")
def client2_home():
    if "client2_user" in session:
        return """
        <h1>SecureNova-AI-Client2</h1>
        <h2>Authenticated Successfully!</h2>
        <p>Authentication completed using Auth0 Client2.</p>
        """

    return """
    <h1>SecureNova-AI-Client2</h1>
    <a href="/client2/login">Login using Auth0</a>
    """


# Client2 login
@app.route("/client2/login")
def client2_login():
    callback_url = os.getenv("AUTH0_CLIENT2_CALLBACK_URL")

    if not callback_url:
        return "Client2 callback URL is missing", 500

    return auth0_client2.authorize_redirect(callback_url)


# Client2 callback
@app.route("/client2/callback")
def client2_callback():
    token = auth0_client2.authorize_access_token()
    userinfo = token.get("userinfo")

    if not userinfo:
        return "User information was not returned by Auth0", 500

    session["client2_user"] = {
        "sub": userinfo.get("sub"),
        "email": userinfo.get("email"),
    }

    return redirect("/client2")
