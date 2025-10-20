from fastapi import FastAPI
from core import settings
from api.v1.routes import strings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="A RESTful API for analyzing and storing string properties (in-memory)."
)

app.include_router(strings.router)

@app.get("/")
def root():
    return {
        "app_name": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "uptime_since": settings.START_TIME.isoformat()
    }
