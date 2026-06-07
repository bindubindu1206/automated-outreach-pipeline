import streamlit as st
import time

from services.ocean import get_similar_companies
from services.prospeo import find_contacts
from utils.lead_scoring import calculate_score

st.set_page_config(
    page_title="Automated Outreach Pipeline",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 Automated Outreach Pipeline")

domain = st.text_input(
    "Enter Company Domain",
    placeholder="openai.com"
)

if st.button("Search"):

    if not domain:
        st.warning("Please enter a company domain")
        st.stop()

    with st.spinner("Searching companies and contacts..."):

        companies = get_similar_companies(domain)

        st.subheader("Ocean Results")
        st.write(companies)

        contacts_list = []

        # Only test first company to avoid rate limits
        companies = companies[:1]

        for company in companies:

            st.write(f"Searching contacts for: {company}")

            try:

                contacts = find_contacts(company)

                time.sleep(3)

                st.write("Prospeo Response:")
                st.write(contacts)

                for contact in contacts:

                    score = calculate_score(
                        contact.get("title", "")
                    )

                    contacts_list.append({
                        "Name": contact.get("name", ""),
                        "Title": contact.get("title", ""),
                        "LinkedIn": contact.get("linkedin", ""),
                        "Score": score
                    })

            except Exception as e:
                st.error(f"Error for {company}: {e}")

        st.success(f"{len(contacts_list)} contacts found")

        if contacts_list:

            st.dataframe(
                contacts_list,
                use_container_width=True
            )

        else:
            st.error("No contacts found")