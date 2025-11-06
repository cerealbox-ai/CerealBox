from fastapi import FastAPI
from backend.routes.reply import router as reply_router

app = FastAPI()

app.include_router(reply_router, prefix="/reply")
