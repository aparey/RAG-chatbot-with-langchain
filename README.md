# RAG-chatbot-with-langchain
# Document-Based Chatbot with Retrieval-Augmented Generation (RAG)

This repository contains the implementation of a Document-Based Chatbot that uses a Retrieval-Augmented Generation (RAG) system to interact with multiple PDF documents. The system is developed using the LangChain framework and integrates state-of-the-art Large Language Models (LLMs) such as OpenAI's GPT and Mistral AI. By leveraging prompt engineering and the RAG architecture, the chatbot enables efficient and accurate retrieval of relevant information from documents and generates coherent responses.

## Features
- **Multi-PDF Support**: Seamlessly handle queries across multiple PDF documents.
- **RAG Architecture**: Combines retrieval and generation to enhance response accuracy and relevance.
- **LangChain Framework**: Efficient implementation of retrieval and query pipelines.
- **Prompt Engineering**: Customized prompts to guide LLM responses.
- **LLM Integration**: Flexible support for OpenAI and Mistral AI models.

---

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Code Overview](#code-overview)
4. [Example](#example)
5. [License](#license)

---

## Installation

### Prerequisites
Ensure the following are installed on your machine:
- Python 3.8+
- pip (Python package manager)
- Node.js (optional, for certain PDF processing libraries)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/document-based-chatbot.git
   cd document-based-chatbot
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables. Create a `.env` file in the root directory with the following:
   ```env
   OPENAI_API_KEY=your_openai_api_key
   MISTRAL_API_KEY=your_mistral_api_key
   ```

---

## Usage

### Running the Chatbot
1. Place your PDF documents in the `documents/` folder.
2. Start the system:
   ```bash
   python main.py
   ```
3. Open the chatbot interface (default: `http://localhost:5000`) to interact with the system.

### Querying
- Enter a question, and the chatbot will retrieve the most relevant content from the documents and provide a detailed response.
- Example question: "What are the main findings in the quarterly report?"

---

## Code Overview

### File Structure
```
.
├── main.py                # Entry point for the chatbot
├── rag_pipeline.py        # Core RAG pipeline implementation
├── pdf_loader.py          # PDF parsing and text extraction
├── prompt_engineering.py  # Custom prompts for LLMs
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables
├── documents/             # Folder to store PDF files
└── static/                # Frontend assets (optional)
```

### Main Components
1. **PDF Loader**:
   - Extracts text from PDFs using PyPDF2 or pdfplumber.
   - Stores the text in a vector database (e.g., FAISS or Pinecone).

2. **RAG Pipeline**:
   - Retrieves relevant document chunks based on user queries.
   - Sends the retrieved context to the LLM for generation.

3. **Prompt Engineering**:
   - Ensures the LLM understands the task with context-specific prompts.

4. **Frontend**:
   - Optional web-based UI for interacting with the chatbot.

---

## Example

### Input
"Summarize the key points from the 2023 sustainability report."

### Output
"The 2023 sustainability report highlights the following key points: 1. A 30% reduction in carbon emissions compared to the previous year. 2. Investments in renewable energy projects increased by $10M. 3. New recycling initiatives launched in three major facilities."

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---
