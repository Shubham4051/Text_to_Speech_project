# Creating this project with Scratch
# A tool or program to convert the Text to Speech 

# First importing a library to work with it

from gtts import gTTS
import gtts # gtts - Interface of google translate api

# importing io
from io import BytesIO

from playsound import playsound

print(gtts.lang.tts_langs())

# Make request to google to get Synthesis
#tts = gtts.gTTS("Bhaiya Ji, Kam ho Gya Acche se kam bhi kr rha hai ", lang='hi')

#1 Saving audio to a file
#1 tts.save("hello.mp3")

#2 play the sound
#2 playsound("hello.mp3")

#9 all available languages along with their IETF tag
#9 print(gtts.lang.tts_langs())

mp3_fp = BytesIO()
tts = gTTS('"Hello', lang='hi')
tts.write_to_fp(mp3_fp)