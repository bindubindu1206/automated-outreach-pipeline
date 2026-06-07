from dotenv import load_dotenv
import os

load_dotenv()

BREVO_API_KEY = os.getenv("BREVO_API_KEY")
PROSPEO_API_KEY = os.getenv("PROSPEO_API_KEY")
OCEAN_API_KEY = os.getenv("OCEAN_API_KEY")
EAZYREACH_CLIENT_ID = os.getenv("EAZYREACH_CLIENT_ID")
EAZYREACH_CLIENT_SECRET = os.getenv("EAZYREACH_CLIENT_SECRET")