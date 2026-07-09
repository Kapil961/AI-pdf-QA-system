import chromadb


class VectorStore:

    def __init__(self):

        print("Connecting to ChromaDB...")

        self.client = chromadb.PersistentClient(path="chroma_db")

        self.collection = self.client.get_or_create_collection(
            name="pdf_chunks"
        )

    def store_embeddings(self, chunks, embeddings):

        print("Storing Embeddings...")

        ids = [str(i) for i in range(len(chunks))]

        self.collection.add(
            ids=ids,
            documents=chunks,
            embeddings=embeddings.tolist()
        )

        print("Embeddings Stored Successfully!")

    def count_documents(self):

        return self.collection.count()


if __name__ == "__main__":

    print("Testing VectorStore...")

    from app.embedding import EmbeddingModel

    sample_chunks = [
        "Artificial Intelligence enables machines to perform intelligent tasks.",
        "Machine Learning is a subset of Artificial Intelligence.",
        "Deep Learning uses neural networks."
    ]

    embedding_model = EmbeddingModel()

    embeddings = embedding_model.generate_embeddings(sample_chunks)

    vector_store = VectorStore()

    vector_store.store_embeddings(
        sample_chunks,
        embeddings
    )

    print("\nTotal Documents:")

    print(vector_store.count_documents())