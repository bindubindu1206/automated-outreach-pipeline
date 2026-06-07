#  Automated Outreach Pipeline

## Overview

Automated Outreach Pipeline is a Python-based lead generation and outreach automation system.

The project automates the process of:

* Discovering similar companies
* Finding relevant contacts
* Scoring leads
* Exporting results
* Sending outreach emails automatically

The application includes both a Command Line Interface (CLI) and a Streamlit web dashboard.

---

## Features

### Company Discovery

Uses Ocean.io API to discover companies similar to a target company.

### Contact Discovery

Uses Prospeo API to identify relevant contacts within discovered companies.

### Lead Scoring

Scores leads based on job titles and decision-making authority.

### CSV Export

Exports qualified contacts into a CSV file for future use.

### Automated Email Outreach

Uses Brevo API to send personalized outreach emails.

### Streamlit Dashboard

Provides a simple user interface for running the pipeline.

---

## Tech Stack

* Python
* Streamlit
* Ocean.io API
* Prospeo API
* Brevo API
* CSV Export
* Git & GitHub

---

## Project Workflow

Company Domain
↓
Ocean.io
↓
Similar Companies
↓
Prospeo
↓
Relevant Contacts
↓
Lead Scoring
↓
CSV Export
↓
Brevo Email Outreach

---

## Project Structure

```text
automated-outreach-pipeline/
│
├── app.py
├── main.py
├── config.py
├── requirements.txt
├── README.md
│
├── services/
│   ├── ocean.py
│   ├── prospeo.py
│   └── brevo.py
│
├── utils/
│   ├── export.py
│   └── lead_scoring.py
│
└── .env
```

## Installation

Clone the repository:

```bash
git clone https://github.com/bindubindu1206/automated-outreach-pipeline.git
cd automated-outreach-pipeline
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env
OCEAN_API_KEY=YOUR_OCEAN_API_KEY
PROSPEO_API_KEY=YOUR_PROSPEO_API_KEY
BREVO_API_KEY=YOUR_BREVO_API_KEY
```

---

## Run CLI Version

```bash
python main.py
```

---

## Run Streamlit Dashboard

```bash
streamlit run app.py
```

---

## Example Output

* Similar companies discovered using Ocean.io
* Contacts retrieved using Prospeo
* Lead scores assigned
* Results exported to CSV
* Emails sent through Brevo

---

## Known Limitation

This project relies on the Prospeo API for contact discovery.

Prospeo free-tier accounts are subject to daily and monthly API limits.

When the quota is exceeded, the API returns:

```text
429 Rate limit exceeded
```

In such cases, contact retrieval may temporarily return no results until the API quota resets.

This limitation is related to the external API service and not to the application logic.

---

## Future Improvements

* Email open tracking
* AI-generated personalized outreach emails
* Dashboard analytics
* Contact enrichment
* Multi-channel outreach automation

---

## Author

Bindu Shree

GitHub:
https://github.com/bindubindu1206

---

## License

This project is developed for educational and internship assessment purposes.

