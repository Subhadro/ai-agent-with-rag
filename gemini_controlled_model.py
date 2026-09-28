from google import genai

client = genai.Client()
interaction = client.interactions.create(
	model = "gemini-3.6-flash",
	input = "Explain machine learning ",
	generation_config={
		"temperature" : 1.0,
		"max_output_tokens" : 600,
	}

)
print(interaction.output_text)
