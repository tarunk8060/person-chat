docs = [
    "Reset password by clicking forgot password.",
    "401 error means invalid API token.",
    "Billing refunds take 5-7 days."
]


def load_documents():
    pass


def retrieve(query):
    query = query.lower()
    matches = []

    for doc in docs:
        for word in query.split():
            if word in doc.lower():
                matches.append(doc)
                break

    if not matches:
        matches = docs[:2]

    return [matches[:2]]
