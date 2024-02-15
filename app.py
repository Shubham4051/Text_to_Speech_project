from fastapi import FastAPI
from typing import Optional
from text_to_speech import text_to_speech_function  # Import your text-to-speech function

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Text-to-Speech API"}

@app.get("/text_to_speech/")
def text_to_speech(text: str):
    speech = text_to_speech_function(text)
    return {"speech": speech}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
