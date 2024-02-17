# Created with Sample 2 as a reference.  
# using a tool that will work offline pyttsx3

import pyttsx3

engine = pyttsx3.init()
engine.setProperty("rate",150)

def text_to_speech_function():
    text = input("Enter your Text \n")
    engine.say(text)
    engine.save_to_file(text , "real_audio.mp3")
    engine.runAndWait()
    engine.stop()

text_to_speech_function()