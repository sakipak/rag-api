import requests

def ask_question(question):
    # Call to ngrok-exposed local Ollama
    url = "https://your-ngrok-id.ngrok.io/ollama"
    payload = {
        "model": "mistral",
        "prompt": f"Answer this question: {question}"
    }
    response = requests.post(url, json=payload)
    return response.json().get("response", "No answer returned.")
