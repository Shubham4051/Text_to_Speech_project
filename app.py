from fastapi import FastAPI, Request
from typing import Optional
import pyttsx3
from pyttsx3 import init

app = FastAPI()

engine = init()

def convert_text_to_speech(text):
    engine.say(text)
    engine.runAndWait()

@app.post("/convert-text-to-speech")
async def convert_text_to_speech_endpoint(request: Request):
    data = await request.json()
    text = data["text": "Text converted to speech successfully"]

    convert_text_to_speech(text)

    return {"message": "Text converted to speech successfully"}