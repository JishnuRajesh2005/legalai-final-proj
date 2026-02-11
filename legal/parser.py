def extract_clause(text):
    lines = [l.strip() for l in text.splitlines() if l.strip()]  # FIXED: removed "\\n"
    return [{"id": i, "text": line} for i, line in enumerate(lines)]
