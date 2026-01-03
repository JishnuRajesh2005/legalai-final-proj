def build_prompt(context):
    return f"""  You are a legal information assistant. Do NOT provide any legal advice.
    Conversation:
    {context['history']}
    
    Documents:
    {context['documents']}

    User question:
    {context['current_input']}

"""