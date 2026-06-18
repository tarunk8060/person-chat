import chromadb

client = chromadb.Client()
collection = client.create_collection("support_docs")

def load_documents():
    docs = [
        "Reset password by clicking forgot password.",
        "401 error means invalid API token.",
        "Billing refunds take 5-7 days."
    ]

    for i, doc in enumerate(docs):
        collection.add(
            documents=[doc],
            ids=[str(i)]
        )

def retrieve(query):
    result = collection.query(
        query_texts=[query],
        n_results=2
    )
    return result["documents"]