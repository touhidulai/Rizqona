from sentence_transformers import SentenceTransformer

model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

def embed_text(text: str) -> list[float]:
    text_vector = model.encode(text)
    return text_vector.tolist()