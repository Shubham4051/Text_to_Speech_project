from fastapi import FastAPI, Request
from _Speech_Engine import _Speech_Engine

app = FastAPI()

@app.get("/")
def read_root():
    return{"message":"Welcome to text to speech world"}

@app.post("/text_to_speech")
def api_text_to_speech(text: str):
    try :
        text_to_Speech = _Speech_Engine()
        text_to_Speech.start(text)
        del(text_to_Speech)
        return{"Success"}
    except Exception as e:
        print(e)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)