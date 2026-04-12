from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
# Load the PDF document
loader = PyPDFLoader("001-2025-0805_DLBCSTCSML01_Course_Book.pdf")
pages = loader.load_and_split()
# Initialize the text splitter
print(f"Total pages: {len(pages)}")
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
# Split the pages into chunks
chunks = text_splitter.split_documents(pages)

print(f"Total chunks: {len(chunks)}")
print(f"\nFirst chunk:\n{chunks[0].page_content}")
print(f"\nSecond chunk:\n{chunks[1].page_content}")
    