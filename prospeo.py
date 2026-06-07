import requests
from config import PROSPEO_API_KEY


def find_contacts(company):

    print("\n******** PROSPEO FILE LOADED ********")
    print(f"Company: {company}")

    url = "https://api.prospeo.io/search-person"

    headers = {
        "X-KEY": PROSPEO_API_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "page": 1,
        "filters": {
            "company_domain": company
        }
    }

    response = requests.post(
        url,
        headers=headers,
        json=payload
    )

    print("\n===== PROSPEO STATUS CODE =====")
    print(response.status_code)

    print("\n===== PROSPEO RAW RESPONSE =====")
    print(response.text)

    try:
        data = response.json()
    except Exception as e:
        print("JSON Error:", e)
        return []

    print("\n===== PROSPEO JSON RESPONSE =====")
    print(data)

    contacts = []

    results = data.get("results", [])

    for item in results[:10]:

        person = item.get("person", {})

        email = (
            person.get("email")
            or person.get("work_email")
            or person.get("email_address")
            or ""
        )

        contacts.append({
            "name": person.get("full_name", ""),
            "title": person.get("current_job_title", ""),
            "linkedin": person.get("linkedin_url", ""),
            "email": email
        })

    print(f"\n===== CONTACTS FOUND FOR {company} =====")
    print(contacts)

    return contacts