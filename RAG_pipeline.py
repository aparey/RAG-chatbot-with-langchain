from pdf_loader import PDFLoader
from prompt_engineering import construct_prompt
import openai

class RAGPipeline:
    def __init__(self):
        self.documents = PDFLoader().load_documents()
        self.vector_index = self.build_vector_index(self.documents)

    def build_vector_index(self, documents):
        from langchain.vectorstores import FAISS
        from langchain.embeddings.openai import OpenAIEmbeddings

        embeddings = OpenAIEmbeddings()
        return FAISS.from_texts(documents, embeddings)

    def answer_query(self, query):
        docs = self.vector_index.similarity_search(query, k=5)
        context = "\n".join([doc.page_content for doc in docs])
        prompt = construct_prompt(query, context)
        
        response = openai.Completion.create(
            model="gpt-4",
            prompt=prompt,
            temperature=0.7,
            max_tokens=300
        )
        return response.choices[0].text.strip()
