import chromadb
from embadding import MyEmbedding
def build_vectorstore(chunks):
    client = chromadb.Client()
    collection = client.get_or_create_collection("docs", embedding_function=MyEmbedding())

    collection.add(
        documents=[c.page_content for c in chunks],
        ids=[f"chunk_{i}" for i in range(len(chunks))]
    )
    return collection