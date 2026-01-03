def classify_document(text):
    t=text.lower()
    if "agreement" in t():
        return "Contract"
    elif "policy" in t():
        return "Policy"
    return "Unknown"