from pypdf import PdfReader


class PDFHandler:
    def extract_text(self, pdf_path: str) -> str:
        print("Reading PDF...")

        reader = PdfReader(pdf_path)
        text = ""

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        print("PDF text extraction completed.")
        return text