from sentence_transformers import SentenceTransformer
import numpy as np


class EmbeddingModel:

    def __init__(self):

        print("Loading Embedding Model...")

        self.model = SentenceTransformer(
            "sentence-transformers/all-MiniLM-L6-v2"
        )

    def generate_embeddings(self, texts):

        print("Generating Embeddings...")

        embeddings = self.model.encode(
            texts,
            convert_to_numpy=True,
            normalize_embeddings=True
        )

        print(f"Embedding Shape: {embeddings.shape}")

        return embeddings
if __name__ == "__main__":

    texts = [
        "Artificial Intelligence",
        "Machine Learning",
        "Deep Learning"
    ]

    embedding = EmbeddingModel()

    vectors = embedding.generate_embeddings(texts)

    print(vectors[0][:10])
