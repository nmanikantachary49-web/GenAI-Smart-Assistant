from flask import Flask, render_template, request
import os
import requests
from langchain_ollama.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

app = Flask(__name__)

# LLM (Ollama Local)
# Allow overriding the Ollama model via the OLLAMA_MODEL environment variable
# e.g. set OLLAMA_MODEL=gemma:2b
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", None)
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
OLLAMA_NUM_PREDICT = int(os.getenv("OLLAMA_NUM_PREDICT", "120"))
OLLAMA_NUM_CTX = int(os.getenv("OLLAMA_NUM_CTX", "1024"))
OLLAMA_KEEP_ALIVE = os.getenv("OLLAMA_KEEP_ALIVE", "10m")
PREFERRED_MODELS = ("tinyllama:latest", "tinyllama", "gemma:2b")

chain = None


def get_available_models():
    """Fetch list of available models from Ollama."""
    try:
        response = requests.get(f"{OLLAMA_BASE_URL}/api/tags", timeout=5)
        response.raise_for_status()
        data = response.json()
        models = [m.get("name") for m in data.get("models", [])]
        return models
    except Exception:
        return []


def get_model_name():
    """Determine which model to use."""
    if OLLAMA_MODEL:
        return OLLAMA_MODEL
    
    available = get_available_models()
    for preferred_model in PREFERRED_MODELS:
        if preferred_model in available:
            return preferred_model

    if available:
        return available[0]
    
    raise RuntimeError(
        "No Ollama models are installed. "
        "Please install a model first by running: ollama pull llama2 (or another model like gemma:2b, mistral, etc.)"
    )


def get_chain():
    global chain

    if chain is not None:
        return chain

    try:
        model_name = get_model_name()
        llm = ChatOllama(
            model=model_name,
            base_url=OLLAMA_BASE_URL,
            keep_alive=OLLAMA_KEEP_ALIVE,
            num_ctx=OLLAMA_NUM_CTX,
            num_predict=OLLAMA_NUM_PREDICT,
            temperature=0.3,
        )
        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "You are a helpful assistant. Answer clearly and briefly unless the user asks for details.",
                ),
                ("user", "Question: {question}"),
            ]
        )
        output_parser = StrOutputParser()
        chain = prompt | llm | output_parser
        return chain
    except Exception as exc:
        raise RuntimeError(
            "Unable to initialize the Ollama model. "
            "Make sure Ollama is running and a model is installed. "
            f"Details: {exc}"
        ) from exc

@app.route("/", methods=["GET", "POST"])
def home():
    response = ""
    if request.method == "POST":
        user_input = request.form.get("question", "")
        try:
            response = get_chain().invoke({"question": user_input})
        except Exception as error:
            response = (
                "Error communicating with Ollama. "
                "Make sure Ollama is running and the model is available. "
                f"Details: {error}"
            )
    return render_template("new.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)
