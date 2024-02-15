# making this for ofline modle usinf pyttsx3, main fratures
# It works fully offline
# You can choose among different voices that are installed on your system
# Controlling the speed of speech
# Tweaking volume
# Saving the speech audio into a file.

import pyttsx3

# initialize Text-to-speech engine

times = int(input('Enter a number '))
engine = pyttsx3.init()
engine.setProperty("rate", 100)
while times > 0:
    times -= 1
# convert this text to speech
    text = input()
    engine.say(text)


# play the speech
    engine.runAndWait()

# get details of speaking rate
# rate = engine.getProperty("rate")
# print(rate)

# saving speech audio into a file
# engine.save_to_file(text, "python.mp3")
# engine.runAndWait()

#to get voice properties
# voices = engine.getProperty("voices")
# print(voices)