from typing import Union
from fastapi import FastAPI, File, UploadFile
from test import *
import json
import whisper
from whisper.utils import get_writer
from recognition import *

model = whisper.load_model(r"C:\Users\nigama\.cache\whisper\base.pt")
data = dict()

app = FastAPI()


@app.post("/api/audiofile/")
async def upload(file: UploadFile = File(...)):
    """
    Upload a file
    :param file:
    :return:
    """
    try:
        print("Attempting to generate transcripts ...")
        result = transcribe(str(file.filename))
        '''audio = model.load_audio("audio_20230413_083417.wav")
        print("--------------------------------------------")

        result = model.transcribe(audio)
        print(result)
        data['text'] = result["text"]
        data['lang'] = result["language"]
        print("Successfully generated transcripts")'''

    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()

    return json.dumps(result)


# run command : uvicorn main:app --reload

@app.post("/audioname")
def sendFile(filename: str):
    try:
        print("--------------------------------------------")
        print("Attempting to generate transcripts ...")
        audio = whisper.load_audio(filename)
        result = model.transcribe(audio)
        print(result)
        data['text'] = result["text"]
        data['lang'] = result["language"]
        print("Succesfully generated transcripts")
        return "Pass"
    except Exception:
        return {"message": "There was an error uploading the file"}
