from fastapi import FastAPI
from chat_bot_app.api_router import data_ingestion

app = FastAPI()

@app.get("/")
def get_start():
    return {"message":"okk"}

app.include_router(router=data_ingestion.router,tags=["data_ingestion"])