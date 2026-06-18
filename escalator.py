def should_escalate(message):
    sensitive_words = ["refund", "billing", "lawsuit", "legal"]

    for word in sensitive_words:
        if word in message.lower():
            return True

    return False