from fastapi import APIRouter,UploadFile,File

router = APIRouter()

@router.get("/data_ingest")
def start():
    return {"message":"all okay"}

@router.post("/upload_data")
def upload(data:UploadFile = File(...)):
    return data