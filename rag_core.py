import requests

def ask_question(question):
    url = "https://your-ngrok-id.ngrok.io/ollama"  # make sure this is correct
    payload = {
        "model": "mistral",
        "prompt": f"Answer this question: {question}"
    }

    try:
        response = requests.post(url, json=payload, timeout=10)

        # check for HTTP error
        response.raise_for_status()

        # try parsing as JSON
        data = response.json()
        return data.get("response", "No 'response' key in result.")

    except requests.exceptions.RequestException as e:
        return f"Request error: {str(e)}"
    except ValueError as e:
        return f"Invalid JSON response: {response.text}"
