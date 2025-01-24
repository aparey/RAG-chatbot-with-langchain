import os
from PyPDF2 import PdfReader

class PDFLoader:
    def __init__(self, directory="documents"):
        self.directory = directory

    def load_documents(self):
        documents = []
        for filename in os.listdir(self.directory):
            if filename.endswith(".pdf"):
                path = os.path.join(self.directory, filename)
                documents.append(self._extract_text_from_pdf(path))
        return documents

    def _extract_text_from_pdf(self, file_path):
        reader = PdfReader(file_path)
        text = []
        for page in reader.pages:
            text.append(page.extract_text())
        return "\n".join(text)
