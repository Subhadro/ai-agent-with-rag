from google import genai

client = genai.Client()
stream = client.interactions.create(
	model = "gemini-3.6-flash",
	input = "Explain machine learning in one simple sentence and add 4 examples in each of one line",
	stream = True

)
for event in stream:
	if event.event_type == 'step.delta':
		if event.delta.type == "text":
			print(event.delta.text, end="", flush=True)
