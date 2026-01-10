from chat.context_builder import build_context
from chat.followup_resolver import resolve_followup
from llm_ollama.ollama_client import OllamaClient
from legal.safety import is_safe, safety_warning_message

def route_input(user_input, chat_state):
    resolved =  resolve_followup(chat_state.get_history(), user_input)

    if not is_safe(resolved):
        return safety_warning_message()
    
    context = build_context(chat_state, resolved)
    response = OllamaClient().generate(context)
    
    chat_state.add_turn(resolved, response)
    return response