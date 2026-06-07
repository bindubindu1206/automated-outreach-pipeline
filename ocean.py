import requests
from config import OCEAN_API_KEY


def get_similar_companies(domain):

    url = "https://api.ocean.io/v3/search/companies"

    headers = {
        "x-api-token": OCEAN_API_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "size": 5,
        "companiesFilters": {
            "lookalikeDomains": [domain]
        }
    }

    response = requests.post(
        url,
        headers=headers,
        json=payload
    )

    print("\n===== STATUS =====")
    print(response.status_code)

    print("\n===== RESPONSE =====")
    print(response.text)

    data = response.json()

    companies = []

    if "companies" in data:

        for item in data["companies"]:

            company = item.get("company", {})

            companies.append(
                company.get("domain")
            )

    return companies