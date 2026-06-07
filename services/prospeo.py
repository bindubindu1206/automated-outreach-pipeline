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
            "company_domain": company,
            "person_seniority": {
                "include": [
                    "Founder/Owner",
                    "C-Level",
                    "VP",
                    "Director"
                ]
            }
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

    for item in results[:5]:

        person = item.get("person", {})

        contacts.append({
            "name": person.get("full_name", ""),
            "title": person.get("current_job_title", ""),
            "linkedin": person.get("linkedin_url", "")
        })

    print(f"\n===== CONTACTS FOUND FOR {company} =====")
    print(contacts)

    return contacts