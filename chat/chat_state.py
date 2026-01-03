class ChatState:
    def __init__(self):
            self.history = []
            self.documents = []

    def add_turn(self, user, assistant):
          self.history.append({"user": user, "assistant": assistant})
    
    def get_history(self):
          return self.history
    
    def add_document(self, document):
          self.documents.append(document)
    
    def get_documents(self):
          return self.documents