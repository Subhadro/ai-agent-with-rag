from google import genai

client = genai.Client()
interaction = client.interactions.create(
	model = "gemini-3.6-flash",
	input = "Explain machine learning in one simple sentence"

)
print(interaction.output_text)
