from app.embedding import EmbeddingModel
from app.vector_store import VectorStore


class Retriever:

    def __init__(self):

        self.embedding_model = EmbeddingModel()
        self.vector_store = VectorStore()

    def retrieve(self, question: str, top_k: int = 3):

        print("Generating question embedding...")

        question_embedding = self.embedding_model.generate_embeddings(
            [question]
        )

        print("Searching similar chunks...")

        results = self.vector_store.collection.query(
            query_embeddings=question_embedding.tolist(),
            n_results=top_k
        )

        return results


if __name__ == "__main__":

    print("Testing Retriever...")

    retriever = Retriever()

    question = "What is Machine Learning?"

    results = retriever.retrieve(question)

    documents = results["documents"][0]

    print("\nRetrieved Chunks:\n")

    for i, doc in enumerate(documents, start=1):
        print(f"Rank {i}")
        print(doc)
        print("-" * 50)