from fastapi import APIRouter

router = APIRouter()

@router.get("data_ingest")
def start():
    return {"message":"all okay"}