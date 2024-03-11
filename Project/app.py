from fastapi import FastAPI, Request
from speech_engine import Text_to_Speech

app = FastAPI()

@app.get("/")
def read_root():
    return{"message":"Welcome to text to speech world"}

@app.post("/text_to_speech")
def api_text_to_speech(text: str):
    
    
    
    # try :
    #     speech = Text_to_Speech()
    #     speech.start(text)
    #     del(speech)
    #     return{"Success"}
    # except Exception as e:
    #     print(e)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)