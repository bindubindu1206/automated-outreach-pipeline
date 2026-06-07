# Automated Outreach Pipeline

## Overview

Automated Outreach Pipeline is a lead generation and outreach automation project built with Python.

The system discovers similar companies, finds decision-makers, scores leads, exports results, and sends outreach emails automatically.

## Features

* Company discovery using Ocean.io
* Contact discovery using Prospeo
* Lead scoring based on job titles
* CSV export of qualified leads
* Automated email outreach using Brevo
* Streamlit dashboard for easy interaction

## Tech Stack

* Python
* Streamlit
* Ocean.io API
* Prospeo API
* Brevo API

## Project Flow

Company Domain
→ Ocean.io
→ Similar Companies
→ Prospeo
→ Contacts
→ Lead Scoring
→ CSV Export
→ Email Outreach

## Installation

```bash
pip install -r requirements.txt
```

## Run CLI Version

```bash
python main.py
```

## Run Streamlit Dashboard

```bash
streamlit run app.py
```

## Notes

Prospeo free accounts have daily rate limits. Contact retrieval may be temporarily unavailable when API limits are exceeded.

## Author

Bindu Shree

