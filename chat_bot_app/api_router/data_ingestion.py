from fastapi import APIRouter,UploadFile,File
from chat_bot_app.data_loader.load_documents import extract_text_from_bytes

router = APIRouter()

@router.get("/data_ingest")
def start():
    return {"message":"all okay"}

from fastapi import UploadFile, File

@router.post("/upload")
async def upload(file: UploadFile = File(...)):

    if file.content_type != "application/pdf":
        return {"error": "Only PDF files allowed"}

    file_bytes = await file.read() 

    extracted_text = extract_text_from_bytes(file_bytes)

    return {
        "filename": file.filename,
        "content": extracted_text
    }
