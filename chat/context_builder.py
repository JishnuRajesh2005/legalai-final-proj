from legal.parser import extract_clause
from legal.classifier import classify_document

def build_context(chat_state, current_input):
    docs = []

    for doc in chat_state.get_documents():
        docs.append({
            "type": classify_document(doc["content"]),
            "clauses": extract_clause(doc["content"])[:15]
        })
    
    # FIXED: return moved outside the loop
    return {
        "history": chat_state.get_history()[-5:],
        "documents": docs,
        "current_input": current_input
    }
