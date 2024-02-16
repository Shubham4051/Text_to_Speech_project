from fastapi import FastAPI, Request
from typing import Optional
import pyttsx3
from pyttsx3 import init
import text_to_speech

app = FastAPI()

@app.get("/")
def read_root():
    return{"message": "Welcome to the text-to-speech API"}

@app.get("/text_to_speech")
def text_to_speech(text: str):
    speech = text_to_speech(text)
    return{"speech": speech}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,port=8000)

# app = FastAPI()

# engine = init()

# def convert_text_to_speech(text):
#     engine.say(text)
#     engine.runAndWait()

# @app.post("/convert-text-to-speech")
# async def convert_text_to_speech_endpoint(request: Request):
#     data = await request.json()
#     text = data["text": "Text converted to speech successfully"]

#     convert_text_to_speech(text)

#     return {"message": "Text converted to speech successfully"}