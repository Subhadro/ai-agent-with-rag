from ollama import chat

response = chat(
	model = "gemma3:1b",
	messages = [
		{
			"role" : "user",
			"content" :"Explain ml in one sentence"
		}
	]
)
print(response.message.content)