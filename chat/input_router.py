from chat.context_builder import build_context
from chat.followup_resolver import resolve_followup
from llm.ollama_client import OllamaClient
from legal.safety import is_safe, safety_response