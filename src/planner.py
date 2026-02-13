def create_plan(user_input):
    text = user_input.lower()

    if "korelasyon" in text:
        return "correlation"
    elif "özet" in text:
        return "summary"
    elif "nasıl geliştiririm" in text:
        return "improvement"
    else:
        return "general"
