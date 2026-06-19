def should_escalate(query):
    critical_words = ["lawsuit", "legal", "complaint", "court"]

    query = query.lower()

    for word in critical_words:
        if word in query:
            return True

    return False
