from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()

inbox_store = {}

class MessageInput(BaseModel):
    username: str
    message: str

@router.post("/send")
async def send_reply(data: MessageInput):
    if not data.username or not data.message:
        raise HTTPException(status_code=400, detail="Username and message required.")
    inbox_store.setdefault(data.username, []).append({
        "text": data.message,
        "timestamp": datetime.utcnow().isoformat()
    })
    return {"success": True}

@router.get("/inbox/{username}")
def get_inbox(username: str):
    messages = inbox_store.get(username, [])
    return {"messages": messages}

