import pyttsx3
import uuid

class speech_engine():
    def __init__(self):
        self.engine.setProperty("rate", 150)
        self.engine = pyttsx3.init()
# text = input()
text_ = input()
def Text_to_Speech(self, text_):
    self.engine.say(text_)
    file_name = (str(uuid.uuid4())) + ".mp3"
    self.engine.save_to_file(text_, file_name)
    self.engine.runAndWait()