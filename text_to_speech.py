# Creating this project with Scratch
# A tool or program to convert the Text to Speech 

# First importing a library to work with it

from gtts import gTTS
import gtts # gtts - Interface of google translate api


from playsound import playsound

# Make request to google to get Synthesis
tts = gtts.gTTs("Hello World !") 

# Saving audio to a file
tts.save("hello.mp3")