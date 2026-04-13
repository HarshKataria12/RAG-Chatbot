import chromadb

client     = chromadb.Client()
collection = client.create_collection("my_docs")

collection.add(
    documents=[c.page_content for c in chunks],  # real chunks
    ids=[f"chunk_{i}" for i in range(len(chunks))]  # auto IDs
)

results = collection.query(
    query_texts=["what do you sell?"],
    n_results=1
)

print(results["documents"])