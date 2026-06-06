from services.ocean import get_similar_companies
from services.prospeo import find_contacts
from services.eazyreach import get_email
from services.brevo import send_email

domain = input("Enter company domain: ")

companies = get_similar_companies(domain)

contacts_list = []

for company in companies:

    contacts = find_contacts(company)

    for contact in contacts:

        email = get_email(contact["linkedin"])

        contact["email"] = email

        contacts_list.append(contact)

print("\n===== SUMMARY =====")

for contact in contacts_list:
    print(contact)

choice = input("\nSend emails? (y/n): ")

if choice.lower() == "y":

    for contact in contacts_list:
        send_email(
            contact["email"],
            contact["name"]
        )

print("\nPipeline completed successfully.")