import os

from pydantic import BaseModel


class Settings(BaseModel):
    service_name: str = "smartlend-lending-lens"
    gcp_project_id: str = (
        os.getenv("GCP_PROJECT_ID")
        or os.getenv("GOOGLE_CLOUD_PROJECT")
        or "b2-lending-lens"
    )
    google_cloud_location: str = os.getenv("GOOGLE_CLOUD_LOCATION", "us-east1")
    gemini_model: str = os.getenv("GEMINI_MODEL", "gemini-1.5-flash")
    storage_bucket: str = os.getenv("B2_STORAGE_BUCKET", "b2-foundation")
    storage_prefix: str = os.getenv("B2_STORAGE_PREFIX", "lending-lens/")


settings = Settings()

