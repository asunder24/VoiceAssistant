import openai
import speech_recognition as sr

class Assistant:

    def __init__(self, key):
        #self.client = OpenAI(api_key=key)
        #openai.api_key = key
        self.history = [{"role": "system", "content": "You are a personal assistant. Use only English. Provide helpful responses. Be as concise as possible."}]


    #def activate(self):

    def listen(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as user_input:
            print("Listening for a query...")
            audio = recognizer.listen(user_input)
        try:
            #  return recognizer.recognize_sphinx(audio) -- nonfunctional for now, issues with sphinx installation
            return recognizer.recognize_google(audio) # Add a specific API key functionality later, the default could be inconsistent
        except sr.UnknownValueError:
            print("Sorry, I couldn't quite understand that. Please try again.")
            return ""
        except sr.RequestError:
            print("Error! Please try again later.")
            return ""


