import subprocess
import requests
import time


def is_ollama_server_running():
    """
    Check if the Ollama server is running.
    :return: True if the server is running, False otherwise.
    """
    try:
        response = requests.get("http://localhost:11434/api/models", timeout=2)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False


def start_ollama_server():
    """
    Start the Ollama server if it is not already running.
    :return: None
    """
    try:
        # Start the server as a subprocess
        subprocess.Popen(["ollama", "serve"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("Starting Ollama server...")
        time.sleep(5)  # Wait for the server to initialize
    except Exception as e:
        raise RuntimeError(f"Failed to start Ollama server: {e}")


def load_model(model_name):
    """
    Load a model using Ollama. Starts the server if necessary and ensures the model is available.
    :param model_name: Name of the model to load.
    :return: A confirmation message that the model is ready.
    """
    # Check if the server is running, and start it if necessary
    if not is_ollama_server_running():
        start_ollama_server()

    # Ensure the model is available in Ollama
    try:
        # Pull the model using Ollama CLI
        subprocess.run(["ollama", "pull", model_name], check=True)
        print(f"Model '{model_name}' is ready to use.")
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Failed to load model '{model_name}': {e}")

    return f"Model '{model_name}' loaded successfully and ready to use with Ollama."