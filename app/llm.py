class LLM:

    def generate_answer(self, prompt: str):

        print("Mock LLM Called")

        return (
            "This is a temporary mock response.\n\n"
            "Your RAG pipeline is working correctly.\n"
            "Replace this file with the real API version after obtaining a working API key."
        )


if __name__ == "__main__":

    llm = LLM()

    answer = llm.generate_answer("Hello")

    print(answer)