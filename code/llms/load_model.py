"""
	load lm
"""

import subprocess

import requests


def load_ollama_model(model_name, system_prompt=None):
    """
    Load and interact with an Ollama model given its name and an optional system prompt.
    :param model_name: Name of the model to load (string).
    :param system_prompt: Optional system prompt to set the model's behavior or context.
    :return: Function to query the model.
    """
    base_url = "http://localhost:11434/api"

    # Ensure the Ollama server is running
    try:
        response = requests.get(f"{base_url}/tags", timeout=5)
        if response.status_code != 200:
            raise RuntimeError("Ollama server is not running.")
    except requests.exceptions.RequestException:
        # Attempt to start the server
        try:
            subprocess.Popen(["ollama", "serve"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print("Starting Ollama server...")
        except Exception as e:
            raise RuntimeError(f"Failed to start Ollama server: {e}")

    # Pull the model if not already available
    try:
        response = requests.get(f"{base_url}/tags", timeout=5)
        available_models = [model["name"] for model in response.json()["models"]]
        if model_name not in available_models:
            print(f"Model '{model_name}' not found locally. Downloading...")
            subprocess.run(["ollama", "pull", model_name], check=True)
            print(f"Model '{model_name}' downloaded successfully.")
    except Exception as e:
        raise RuntimeError(f"Failed to ensure model availability: {e}")

    # Return a function to query the model
    def query_model(prompt):
        payload = {
            "model": model_name,
            "prompt": prompt,
            "stream": False,
            "options": {
                "num_predict": 50
            }
        }
        # Add the system prompt if provided
        if system_prompt:
            payload["system"] = system_prompt

        try:
            response = requests.post(f"{base_url}/generate", json=payload)
            response.raise_for_status()
            return response.json().get("response", "")
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Error querying model '{model_name}': {e}")

    return query_model
