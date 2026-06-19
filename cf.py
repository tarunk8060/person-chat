def classify_persona(message):
    msg = message.lower()

    technical_words = ["api", "token", "error", "bug", "server", "database"]
    frustrated_words = ["angry", "worst", "hate", "urgent", "immediately", "!"]
    business_words = ["revenue", "timeline", "business", "impact", "client", "payment"]

    if any(word in msg for word in technical_words):
        return "Technical Expert"

    elif any(word in msg for word in frustrated_words):
        return "Frustrated User"

    elif any(word in msg for word in business_words):
        return "Business Executive"

    return "General User"
