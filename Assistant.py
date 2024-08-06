import openai
import speech_recognition as sr 
import pyttsx3
import os
import time
import json
import requests
import signal
from scandir import scandir
import ctypes
from api import WEATHER

class Assistant:

    def __init__(self, key):
        #self.client = OpenAI(api_key=key)
        #openai.api_key = key
        self.weather_api = WEATHER
        self.voice = True
        self.time = None
        self.engine = pyttsx3.init() 
        self.engine.setProperty('voice', 0)
        print(self.find_files('C:\\',['requirements.txt']))
        #self.get_current_weather("San Francisco")
        self.history = [{"role": "system", "content": "You are a personal assistant. Use only English. Provide helpful responses. Be as concise as possible."}]
        self.tools = [
            {
                "type": "function",
                "function": {
                    "name":  "get_current_weather",
                    "description": "Get the current weather in a given location",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "location": {
                                "type": "string",
                                "description": "The city, e.g. San Francisco, or the Latitude and Longitude (Decimal degree) e.g: 48.8567,2.3508, or the US zipcode e.g.: 10001"
                            }
                        },
                        "required": ["location"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name":  "toggle_voice",
                    "description": "Toggle text-to-speech off or on"
                }
            }
        ]

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

    def process_query(self, query):
        #feed query into gpt model
        #provide list of tool functions so model can call if necessary
        #use error checking the ensure no hallucination
        return None

    def get_current_weather(self, location=None):
        if location == None:
            return None
        base_url = "http://api.weatherapi.com/v1/current.json"
        parameters={"key": self.weather_api, "q": location}
        response = requests.get(base_url, params=parameters)
        if response.status_code == 200:
            return response.json()
        
        return None

    def get_weather_prediction(self):
        #predict location and time
        return None

    def get_time(self):
        #get time at any location, default to current one
        return None
        

    
    
    def toggle_voice(self):
        self.voice = not self.voice
        if self.voice == True:
            self.speak("Activating text to speech...")
            return None
        self.speak("Deactivating text to speech...")

    def speak(self, response):
        print(response)
        if self.voice == True:
            self.engine.say(response)
            self.engine.runAndWait()
        return None

    def clear_mem(self):
        #Clear stored memory, including all written files
        return None
    

    def wolfram(self):
        #Make an API call to wolfram alpha for a query
        #Can do math or other scientific questions
        return None

    def store_mem(self):
        return None
    
    

    def is_sym_link(self, path):
        # http://stackoverflow.com/a/35915819
        FILE_ATTRIBUTE_REPARSE_POINT = 0x0400
        return os.path.isdir(path) and (ctypes.windll.kernel32.GetFileAttributesW(path) & FILE_ATTRIBUTE_REPARSE_POINT)

    def find_files(self, base, filenames):
        hits = []
        def find_in_dir_subdir(direc):
            content = scandir(direc)
            try:
                for entry in content:
                    if entry.name in filenames:
                        hits.append(os.path.join(direc, entry.name))

                    elif entry.is_dir() and not self.is_sym_link(os.path.join(direc, entry.name)):
                        try:
                            find_in_dir_subdir(os.path.join(direc, entry.name))
                        except UnicodeDecodeError:
                            print("Could not resolve " + os.path.join(direc, entry.name))
                            continue
            except OSError as e:
                pass
        if not os.path.exists(base):
            return
        else:
            find_in_dir_subdir(base)
        return hits




    #host of file processing functions needed still
    #host of weather calls needed still
    #news still questionable??

    def calendar(self):
        #Make a separate Calendar object to store info?
        #Put all operations in that class
        #Worry about GUI later
        return None

    def timeout_handler(signal, frame):
        raise Exception('Time is up!')

    def start_timer(self, time_limit):
        signal.signal(signal.SIGALRM, timeout_handler)
        signal.alarm(time_limit)
        #Rework this and use threading to make it run in the background and interrupt main thread when over
        return None

    def music(self):
        #spotify API calls
        return None

    


    
    

