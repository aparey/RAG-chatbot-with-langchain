import os
from rag_pipeline import RAGPipeline
from flask import Flask, request, jsonify

app = Flask(__name__)
rag_pipeline = RAGPipeline()

@app.route('/query', methods=['POST'])
def query():
    data = request.json
    user_query = data.get("query", "")
    if not user_query:
        return jsonify({"error": "Query not provided"}), 400
    
    response = rag_pipeline.answer_query(user_query)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True, port=int(os.getenv("PORT", 5000)))
