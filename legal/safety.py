blocked_for_safety = [
    "should i sue",
    "can i file a case",
    "legal action against"
]

def is_safe(query):
    q = query.lower()
    return not any(phrase in q for phrase in blocked_for_safety)

def safety_warning_message():
    return ("Your query may involve legal actions. Please consult a qualified attorney for advice.")