import requests
from llm_ollama.prompt_builder import build_prompt 

class OllamaClient:
    def __init__(self, model = "llama3"):
        self.url = "http://localhost:11434/api/generate"
        self.model = model 

        def generate(self, context):
            payload = {
                "model": self.model,
                "prompt": build_prompt(context),
                "stream": False
            }

            req = requests.post(self.url, json=payload, timeout = 120)
            req.raise_for_status()
            return req.json().get("response", "")