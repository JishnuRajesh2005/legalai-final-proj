def load_text(file):
    return{
        "type": "text",
        "content": file.read().decode("utf-8")
    }