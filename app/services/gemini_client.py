from typing import Optional

import vertexai
from vertexai.generative_models import GenerativeModel

from app.core.config import settings


class GeminiClient:
    def __init__(
        self,
        project_id: Optional[str] = None,
        location: Optional[str] = None,
        model_name: Optional[str] = None,
    ):
        self.project_id = project_id or settings.gcp_project_id
        self.location = location or settings.google_cloud_location
        self.model_name = model_name or settings.gemini_model

    def generate_text(self, prompt: str) -> str:
        vertexai.init(
            project=self.project_id,
            location=self.location,
        )

        model = GenerativeModel(self.model_name)
        response = model.generate_content(prompt)

        return response.text or ""

