from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

# Import routers (đảm bảo đúng đường dẫn tới router modules)
from .chat_routes import router as chat_router
from .signaling_routes import router as signaling_router

app = FastAPI(title="Chat & VideoCall Service", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Đăng ký các router
app.include_router(chat_router, prefix="/api/chat", tags=["Chat"])
app.include_router(signaling_router, prefix="/ws", tags=["Signaling"])

# Mount static (nếu bạn build FE hoặc có file HTML test)
app.mount(
    "/",
    StaticFiles(directory="app/static", html=True),
    name="static",
)
