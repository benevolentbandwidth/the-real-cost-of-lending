from fastapi import FastAPI

from app.api.agent import router as agent_router
from app.api.gemini import router as gemini_router
from app.api.health import router as health_router
from app.api.skills import router as skills_router
from app.api.whatsapp import router as whatsapp_router
from app.core.config import settings

app = FastAPI(
    title="SmartLend / Real Cost of Lending Lens API",
    version="0.1.0",
    description="Cloud Run starter service for the SmartLend lending-transparency platform.",
)

app.include_router(health_router)
app.include_router(gemini_router)
app.include_router(agent_router)
app.include_router(skills_router)
app.include_router(whatsapp_router)


@app.get("/")
def root():
    return {
        "service": settings.service_name,
        "status": "running",
        "message": "SmartLend Cloud Run starter service is live.",
        "docs": "/docs",
    }

