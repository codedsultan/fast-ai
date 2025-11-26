from fastapi import FastAPI
from config.settings import settings
from src.content.router import router as content_router

app = FastAPI(title=settings.APP_NAME)

@app.get("/")
def health():
    return {"status": "ok"}

app.include_router(content_router, prefix="/content")
