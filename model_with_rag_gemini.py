import numpy as np
from google import genai

client = genai.Client()

# 1. Knowledge Base / Local Data Chunks
documents = [
    "Refund requests are allowed within 7 days of purchase with full money back guarantee.",
    "Shipping takes 3 to 5 business days for domestic orders.",
    "For technical issues, you can contact our support team at support@example.com.",
]

# 2. Function to compute Cosine Similarity
def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

# 3. Generate Embeddings for all document chunks
doc_embeddings = []
for doc in documents:
    response = client.models.embed_content(
        model="gemini-embedding-2",  # or "gemini-embedding-2"
        contents=doc,
    )
    doc_embeddings.append(response.embeddings[0].values)

# 4. User Question
user_query = "Can I call if any problem occurs? Is there any mode to connect with your team ? "

# 5. Embed the User Query
query_response = client.models.embed_content(
    model="gemini-embedding-2",
    contents=user_query,
)
query_vector = query_response.embeddings[0].values

# 6. Retrieve the most relevant context using Similarity Search
similarities = [cosine_similarity(query_vector, doc_vec) for doc_vec in doc_embeddings]
best_match_idx = int(np.argmax(similarities))
retrieved_context = documents[best_match_idx]

print(f"Retrieved Context: {retrieved_context}")
print(f"Similarity Score: {similarities[best_match_idx]:.4f}\n")

# 7. Pass context + question to Gemini model
prompt = f"""
You are an AI assistant. Answer the user question STRICTLY based on the provided context below.
If the answer is not mentioned in the context, say "Context provided does not have this information."

Context:
{retrieved_context}

Question:
{user_query}
"""

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=prompt,
)

print("AI Response:")
print(response.text)