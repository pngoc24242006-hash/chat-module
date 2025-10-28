import json
from fastapi import APIRouter, WebSocket, WebSocketDisconnect, status
from .websocket_manager import ConnectionManager

router = APIRouter()
manager = ConnectionManager()

@router.websocket("/signaling/{username}")
async def websocket_endpoint(websocket: WebSocket, username: str):
    origin = websocket.headers.get("origin")
    print(f"🔗 WebSocket request from: {origin}")

    # Accept tất cả origin trong dev
    await manager.connect(username, websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(json.dumps({username: data}))
    except WebSocketDisconnect:
        manager.disconnect(username)
