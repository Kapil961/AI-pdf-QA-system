import gradio as gr
import requests

BASE_URL = "http://127.0.0.1:8000"


def upload_pdf(pdf_file):
    if pdf_file is None:
        return "Please upload a PDF file."

    try:
        with open(pdf_file.name, "rb") as file:
            files = {
                "file": (pdf_file.name, file, "application/pdf")
            }

            response = requests.post(
                f"{BASE_URL}/upload-pdf",
                files=files,
                timeout=120
            )

        if response.status_code == 200:
            data = response.json()
            return (
                f"PDF uploaded successfully!\n\n"
                f"Filename: {data['filename']}\n"
                f"Chunks Created: {data['total_chunks']}\n"
                f"Message: {data['message']}"
            )

        return f"Error: {response.text}"

    except requests.exceptions.ConnectionError:
        return "Backend is not running. Please start FastAPI first."

    except Exception as error:
        return f"Unexpected error: {str(error)}"


def ask_question(question):
    if not question.strip():
        return "Please enter a question.", ""

    try:
        payload = {
            "question": question
        }

        response = requests.post(
            f"{BASE_URL}/ask",
            json=payload,
            timeout=120
        )

        if response.status_code == 200:
            data = response.json()

            answer = data["answer"]
            context = "\n\n---\n\n".join(data["context"])

            return answer, context

        return f"Error: {response.text}", ""

    except requests.exceptions.ConnectionError:
        return "Backend is not running. Please start FastAPI first.", ""

    except Exception as error:
        return f"Unexpected error: {str(error)}", ""


with gr.Blocks(title="AI PDF Q&A System") as demo:
    gr.Markdown("# AI PDF Q&A System")
    gr.Markdown("Upload a PDF, then ask questions from the document.")

    with gr.Tab("Upload PDF"):
        pdf_file = gr.File(
            label="Upload PDF",
            file_types=[".pdf"]
        )

        upload_button = gr.Button("Process PDF")

        upload_status = gr.Textbox(
            label="Upload Status",
            lines=6
        )

        upload_button.click(
            fn=upload_pdf,
            inputs=pdf_file,
            outputs=upload_status
        )

    with gr.Tab("Ask Question"):
        question = gr.Textbox(
            label="Enter your question",
            placeholder="Example: What is Machine Learning?"
        )

        ask_button = gr.Button("Ask")

        answer = gr.Textbox(
            label="Answer",
            lines=8
        )

        context = gr.Textbox(
            label="Retrieved Context",
            lines=10
        )

        ask_button.click(
            fn=ask_question,
            inputs=question,
            outputs=[answer, context]
        )


if __name__ == "__main__":
    demo.launch(
        server_name="127.0.0.1",
        server_port=7860,
        share=False
    )