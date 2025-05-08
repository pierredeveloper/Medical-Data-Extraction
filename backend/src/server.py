from fastapi import FastAPI, Form, UploadFile, File
import uvicorn
from extractor import extract
import uuid
import os

app = FastAPI()

@app.post("/extract_from_doc")
def extract_from_doc(
        file_data: str = Form(...),
        file: UploadFile = File(...),
):
    contents = file.file.read()

    # Generate unique file path
    file_path = "../uploads/" + str(uuid.uuid4()) + "pdf"

    #Save file to disk
    with open(file_path, "wb") as f:
        f.write(contents)

    #Extract data and handle errors
    try:
        data = extract(file_path, file_data)
    except Exception as e:
        data = {
            'error': str(e)
        }

    # Clean up: delete saved file
    if os.path.exists(file_path):
        os.remove(file_path)

    return data

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)





