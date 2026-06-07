from services.ocean import get_similar_companies
from services.prospeo import find_contacts
from services.eazyreach import get_email
from services.brevo import send_email

from utils.lead_scoring import calculate_score
from utils.export import export_contacts


domain = input("Enter company domain: ")

print("\nSearching...\n")

companies = get_similar_companies(domain)

contacts_list = []
seen_emails = set()

for company in companies:

    contacts = find_contacts(company)

    for contact in contacts:

        email = get_email(contact["linkedin"])

        if not email:
            continue

        if email in seen_emails:
            continue

        seen_emails.add(email)

        contact["email"] = email

        score = calculate_score(
            contact["title"]
        )

        contact["score"] = score

        contacts_list.append(contact)

print("\n===== SUMMARY =====")
print(f"Companies Found: {len(companies)}")
print(f"Contacts Found: {len(contacts_list)}")

for contact in contacts_list:

    print("\n------------------")
    print(f"Name : {contact['name']}")
    print(f"Title: {contact['title']}")
    print(f"Email: {contact['email']}")
    print(f"Score: {contact['score']}")

export_contacts(
    contacts_list
)

choice = input("\nSend emails? (y/n): ")

if choice.lower() == "y":

    for contact in contacts_list:

        send_email(
            contact["email"],
            contact["name"]
        )

print("\nPipeline completed successfully.")