from google import genai

client = genai.Client()
result = client.models.embed_content(
	model = "gemini-embedding-2",
	contents="Refund requests are allowed within 7 days."
)
# print(interaction.output_text)

vector = result.embeddings

print(vector)
