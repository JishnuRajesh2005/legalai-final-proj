def resolve_followup(history, query):
    if not history:
        return query
    # FIXED: added tuple for multiple values
    if query.lower().startswith(("what about", "and", "does it", "what if")):
        return history[-1]["user"] + " " + query
    
    return query
