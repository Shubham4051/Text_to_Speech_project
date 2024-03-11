from fastapi import FastAPI, Request
# import pyttsx3
from speech_engine import Text_to_Speech

app = FastAPI()

@app.get("/")
def read_root():
    return{"message":"Welcome to text to speech world"}

# @app.post("/text_to_speech")
# def api_text_to_speech(text: str)