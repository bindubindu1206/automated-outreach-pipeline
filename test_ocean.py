from services.ocean import get_similar_companies

companies = get_similar_companies(
    "openai.com"
)

print(companies)