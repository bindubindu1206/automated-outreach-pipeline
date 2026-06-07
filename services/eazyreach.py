import requests
from config import (
    EAZYREACH_CLIENT_ID,
    EAZYREACH_CLIENT_SECRET
)


def get_auth_token():

    url = "https://api.superflow.run/b2b/createAuthToken/"

    payload = {
        "clientId": EAZYREACH_CLIENT_ID,
        "clientSecret": EAZYREACH_CLIENT_SECRET
    }

    response = requests.post(
        url,
        json=payload
    )

    data = response.json()

    print("\n===== AUTH RESPONSE =====")
    print(data)

    return data.get("authToken")


def get_balance():

    token = get_auth_token()

    url = "https://api.superflow.run/b2b/getGreenBalance"

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(
        url,
        headers=headers
    )

    data = response.json()

    print("\n===== BALANCE RESPONSE =====")
    print(data)

    return data


def get_email(linkedin_url):

    token = get_auth_token()

    url = "https://api.superflow.run/b2b/linkedin-emails"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    payload = {
        "linkedinUrl": linkedin_url
    }

    response = requests.post(
        url,
        headers=headers,
        json=payload
    )

    data = response.json()

    print("\n===== EMAIL LOOKUP RESPONSE =====")
    print(data)

    try:

        if "emails" in data and len(data["emails"]) > 0:

            first_email = data["emails"][0]

            if isinstance(first_email, dict):
                return first_email.get("email")

            return first_email

    except:
        pass

    # Fallback if balance is 0

    username = linkedin_url.rstrip("/").split("/")[-1]

    return f"{username}@test.com"