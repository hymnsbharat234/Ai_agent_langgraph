from fastapi import FastAPI
from app.config.settings import settings
from app.api.health import router as health_router
from app.api.auth import router as auth_router
from app.api.user import router as user_router
from app.api.upload import router as upload_router
from app.api.chat import router as chat_router


app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.DEBUG_MODE,
    version="1.0.0",
    description="An AI Researcher Assistant that can help you with your research tasks."
)
app.include_router(health_router)
app.include_router(auth_router)
app.include_router(user_router)
app.include_router(upload_router)
app.include_router(chat_router)
@app.get("/")
async def root():
    return {
        "app":settings.APP_NAME,
        "debug_mode":settings.DEBUG_MODE,
        "message":"Welcome to the AI Researcher Assistant API. Use the /docs endpoint to explore the available endpoints and interact with the API."
    }