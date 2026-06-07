def calculate_score(title):

    score = 0

    title = title.lower()

    if "founder" in title:
        score += 30

    if "ceo" in title:
        score += 30

    if "owner" in title:
        score += 25

    if "director" in title:
        score += 20

    if "manager" in title:
        score += 15

    return score