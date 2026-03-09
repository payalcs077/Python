import os
import requests
from flask import Flask, redirect, request,render_template
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")

# Step 1: Redirect to Google
@app.route("/")
def login():
    google_auth_url = (
        "https://accounts.google.com/o/oauth2/v2/auth"
        "?response_type=code"
        f"&client_id={CLIENT_ID}"
        f"&redirect_uri={REDIRECT_URI}"
        "&scope=openid%20email%20profile"
    )
    return redirect(google_auth_url)

# Step 2: Google redirects here
@app.route("/callback")
def callback():
    code = request.args.get("code")

    token_url = "https://oauth2.googleapis.com/token"

    data = {
        "code": code,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "redirect_uri": REDIRECT_URI,
        "grant_type": "authorization_code",
    }

    token_response = requests.post(token_url, data=data)
    token_json = token_response.json()

    access_token = token_json.get("access_token")

    user_info = requests.get(
        "https://www.googleapis.com/oauth2/v1/userinfo",
        params={"access_token": access_token},
    ).json()

    return render_template("profile.html", user=user_info)

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(debug=True, port=8000)