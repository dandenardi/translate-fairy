from fastapi import FastAPI, Form
from fastapi.responses import FileResponse, HTMLResponse
from processor import process_video
import uuid
import os

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def index():
    return """
    <form action="/process" method="post">
        <input name="url" type="text" placeholder="Cole o link do vídeo aqui" style="width: 300px"/>
        <button type="sumbit">Processar</button>
    </form>
"""

@app.post("/process")
def handle_process(url: str = Form(...)):
    job_id = str((uuid.uuid4()))
    output_zip=process_video(url, job_id)
    return FileResponse(output_zip, filename=f"{job_id}.zip")