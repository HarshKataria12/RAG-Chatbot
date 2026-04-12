import chromadb

client     = chromadb.Client()
collection = client.create_collection("my_docs")

collection.add(
    documents=[
        "Our refund policy is 30 days, no questions asked.",
        "We sell laptops, phones, and tablets.",
        "Customer support is available 24/7 via chat.",
    ],
    ids=["chunk1", "chunk2", "chunk3"]
)

results = collection.query(
    query_texts=["what do you sell?"],
    n_results=1
)

print(results["documents"])