def extract_clause(text):
    lines = [l.strip() for l in text.splitlines("\n") if l.strip()]
    return [{"id":i,"text":line} for i, line in enumerate(lines)]