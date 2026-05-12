from fastapi import APIRouter, HTTPException

from app.core.config import settings
from app.services.gemini_client import GeminiClient

router = APIRouter(prefix="/api/v1/gemini", tags=["gemini"])


@router.get("/ping")
def gemini_ping():
    try:
        client = GeminiClient()
        response = client.generate_text(
            "Say exactly: SmartLend Gemini connection is working."
        )
        return {
            "status": "ok",
            "project": settings.gcp_project_id,
            "location": settings.google_cloud_location,
            "model": settings.gemini_model,
            "response": response,
        }
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Gemini ping failed: {str(exc)}",
        ) from exc

