def construct_prompt(query, context):
    return f"""
You are an expert chatbot. Answer the user's query based on the provided context.

Context:
{context}

Query:
{query}

Answer:
"""
