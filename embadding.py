from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

def get_embedding(text):
    embedding = model.encode(text)
    return embedding
def cosine_similarity(vec1, vec2):
    dot_product = np.dot(vec1, vec2)
    norm_vec1 = np.linalg.norm(vec1)
    norm_vec2 = np.linalg.norm(vec2)
    if norm_vec1 == 0 or norm_vec2 == 0:
        return 0.0
    return dot_product / (norm_vec1 * norm_vec2)

dog   = get_embedding("dog")
puppy = get_embedding("puppy")
pizza = get_embedding("pizza")

print("dog vs puppy:", cosine_similarity(dog, puppy))   # HIGH
print("dog vs pizza:", cosine_similarity(dog, pizza))   # LOW