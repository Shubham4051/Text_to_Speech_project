import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
print("Male Voice : {0}".format(voices[0].id))
print("Feale Voice : {0}".format(voices[1].id))
for voice in voices:
    print(voice, voice.id)
    engine.setProperty('voice', voice.id)
    engine.say("Hello World!, Welcoe to the world of AI")
    engine.runAndWait()
    engine.stop()   