from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from .websocket_manager import ConnectionManager

router = APIRouter()
manager = ConnectionManager()

@router.websocket("/ws/chat/{user_id}")
async def chat_websocket(websocket: WebSocket, user_id: str):
    await manager.connect(user_id, websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(f"[{user_id}] says: {data}")
    except WebSocketDisconnect:
        manager.disconnect(user_id)
