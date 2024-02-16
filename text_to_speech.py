# Created with Sample 2 as a reference.  
# using a tool that will work offline pyttsx3

import pyttsx3

engine = pyttsx3.init()
engine.setProperty("rate",150)

engine.say("this is the line to be converted")
engine.runAndWait()
engine.stop()