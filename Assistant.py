import openai

class Assistant:

    def __init__(self, key):
        openai.api_key = key
        self.history = [{"role": "system", "content": "You are a personal assistant. Use only English. Provide helpful responses."}]


    #def activate(self):

