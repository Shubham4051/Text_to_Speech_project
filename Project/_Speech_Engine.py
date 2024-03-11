import pyttsx3
import uuid

class _Speech_Engine:
    engine = None
    rate = None
    def __init__(self):
        self.engine=pyttsx3.init()

    def start(self,text_):
        self.engine.say(text_)
        file_name = (str(uuid.uuid4())) + ".mp3"
        self.engine.save_to_file(text_ , file_name)
        self.engine.runAndWait()