import requests
from config import BREVO_API_KEY

def send_email(email, name):

    url = "https://api.brevo.com/v3/smtp/email"

    headers = {
        "accept": "application/json",
        "api-key": BREVO_API_KEY,
        "content-type": "application/json"
    }

    payload = {
        "sender": {
            "name": "BinduTech Solutions",
            "email": "1mp24cs400@gmail.com"
        },
        "to": [
            {
                "email": email,
                "name": name
            }
        ],
        "subject": "Automated Outreach Pipeline Test",
        "htmlContent": f"""
        <html>
        <body>
            <h2>Hello {name}</h2>

            <p>This is a test email sent from my Automated Outreach Pipeline project.</p>

            <p>
            This project automatically:
            </p>

            <ul>
                <li>Finds similar companies</li>
                <li>Finds decision makers</li>
                <li>Finds email addresses</li>
                <li>Sends outreach emails</li>
            </ul>

            <p>
            Regards,<br>
            Bindushree S
            </p>

        </body>
        </html>
        """
    }

    try:
        response = requests.post(
            url,
            json=payload,
            headers=headers
        )

        print("\n===== BREVO RESPONSE =====")
        print("Status Code:", response.status_code)
        print("Response:", response.text)

    except Exception as e:
        print("Error:", e)