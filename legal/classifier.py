def classify_document(text):
    t = text.lower()
    if "agreement" in t:  # FIXED: removed ()
        return "Contract"
    elif "policy" in t:  # FIXED: removed ()
        return "Policy"
    return "Unknown"
