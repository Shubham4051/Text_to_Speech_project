from fastapi import FastAPI, Request
from speech_engine import Text_to_Speech

app = FastAPI()

@app.get("/")
def read_root():
    return{"message":"Welcome to text to speech world"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)