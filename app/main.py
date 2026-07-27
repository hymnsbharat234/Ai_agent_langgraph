from fastapi import FastAPI
from app.config.settings import settings
from app.api.health import router as health_router
from app.api.auth import router as auth_router

app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.DEBUG_MODE,
    version="1.0.0",
    description="An AI Researcher Assistant that can help you with your research tasks."
)
app.include_router(health_router)
app.include_router(auth_router)
@app.get("/")
async def root():
    return {
        "app":settings.APP_NAME,
        "debug_mode":settings.DEBUG_MODE,
        "message":"Welcome to the AI Researcher Assistant API. Use the /docs endpoint to explore the available endpoints and interact with the API."
    }