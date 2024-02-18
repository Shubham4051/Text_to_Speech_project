# Created with Sample 2 as a reference.  
# using a tool that will work offline pyttsx3
import uuid
import pyttsx3

engine = pyttsx3.init()
engine.setProperty("rate",150)

def text_to_speech_function(text: str):
    # text = input("Enter your Text \n")
    engine.say(text)
    file_name = (str(uuid.uuid4())) + ".mp3"
    engine.save_to_file(text , file_name)
    engine.runAndWait()
    engine.stop()
    return

text_to_speech_function("lets go to work")

