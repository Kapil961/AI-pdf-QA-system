class PromptBuilder:

    def build_prompt(self, question: str, retrieved_chunks):

        print("Building Prompt...")

        context = "\n\n".join(retrieved_chunks)

        prompt = f"""
You are a helpful AI assistant.

Answer the user's question ONLY using the provided context.

If the answer is not available in the context, reply:
"I could not find the answer in the uploaded document."

--------------------
Context:
{context}
--------------------

Question:
{question}

Answer:
"""

        return prompt


if __name__ == "__main__":

    sample_chunks = [
        "Machine Learning is a subset of Artificial Intelligence.",
        "Deep Learning uses neural networks.",
        "Artificial Intelligence enables machines to perform intelligent tasks."
    ]

    question = "What is Machine Learning?"

    prompt_builder = PromptBuilder()

    prompt = prompt_builder.build_prompt(
        question,
        sample_chunks
    )

    print("\nGenerated Prompt:\n")

    print(prompt)