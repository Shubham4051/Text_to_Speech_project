# import uuid
# import pyttsx3
# from typing import Optional
# import pyttsx3
# from pyttsx3 import init
# import text_to_speech
# from text_to_speech import text_to_speech_function

from fastapi import FastAPI, Request
from _TTS import _TTS

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the text-to-speech API"}


@app.post("/text_to_speech")
def api_text_to_speech(text: str):
    # text_to_speech_function(text)
    try:
        tts = _TTS()
        tts.start(text)
        del(tts)
        return {"success"}
    except Exception as e:
        print(e)


    return {"abcgddc"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)


# app = FastAPI() ok

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