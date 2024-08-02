import os

from api import OPENAPI
from Assistant import Assistant


def terminate(query):
    termination_keywords = ["exit","shut down", "stop listening", "bye", "thats all", "goodbye", "shutdown"] # Add more if necessary
    return any(keyword in query for keyword in termination_keywords)

def main():
    #Initialize gpt
    assistant = Assistant(OPENAPI)
    while True:
        query = assistant.listen().lower()
        if query:
            if terminate(query):
                assistant.speak("Have a nice day!")
                assistant.speak("Shutting down...")
                break
            assistant.process_query(query)

            #Automatically store memory on system for next startup, clear if requested
            #Branch cases below
                #Turn voice off/on
                #File/Applications
                #Math
                #Time/Timer/Stopwatch/Alarm
                #Calendar?
                #Generic text generation
                #API Calls
                    #Weather
                    #Music
                    #News?



    #Initialize system
    #Take in user input through voice
    #Process to text
    #Check query to determine if system process or search
    #Feed text to model
    #Receive response, output as speech and text
    


if __name__ == "__main__":
    main()