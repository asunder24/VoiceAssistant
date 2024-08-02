import openai
import speech_recognition as sr 

class Assistant:

    def __init__(self, key):
        #self.client = OpenAI(api_key=key)
        #openai.api_key = key
        self.voice = False
        self.history = [{"role": "system", "content": "You are a personal assistant. Use only English. Provide helpful responses. Be as concise as possible."}]


    #def activate(self):

    def listen(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as user_input:
            self.speak("Listening for a query...")
            audio = recognizer.listen(user_input)
        try:
            #  return recognizer.recognize_sphinx(audio) -- nonfunctional for now, issues with sphinx installation
            return recognizer.recognize_google(audio) # Add a specific API key functionality later, the default could be inconsistent
        except sr.UnknownValueError:
            self.speak("Sorry, I couldn't quite understand that. Please try again.")
            return ""
        except sr.RequestError:
            self.speak("Error! Please try again later.")
            return ""

    def process_query(self, query){
        #feed query into gpt model
        #provide list of tool functions so model can call if necessary
        #use error checking the ensure no hallucination
        return None
    }
    
    def toggle_voice(self):
        self.voice = not self.voice
        if self.voice == True:
            self.speak("Activating text to speech...")
            return None
        self.speak("Deactivating text to speech...")

    def speak(self, response):
        if self.voice == False:
            print(response)
            return None
        #else text to speech with model response
    

