import json

from pydantic import BaseModel

from app.agent.prompts import BOOKKEEPING_PARSE_PROMPT
from app.services.gemini_client import GeminiClient


class BookkeepingParseRequest(BaseModel):
    user_id: str
    language: str = "hi"
    text: str


class BookkeepingParseResponse(BaseModel):
    type: str
    amount: float | None
    currency: str = "INR"
    category: str | None
    raw_text: str


def parse_bookkeeping_entry(
    request: BookkeepingParseRequest,
) -> BookkeepingParseResponse:
    prompt = f"""
{BOOKKEEPING_PARSE_PROMPT}

User language: {request.language}
Text: {request.text}
"""

    client = GeminiClient()
    raw_response = client.generate_text(prompt)

    try:
        parsed = json.loads(raw_response)
        return BookkeepingParseResponse(**parsed)
    except Exception:
        return BookkeepingParseResponse(
            type="unknown",
            amount=None,
            currency="INR",
            category=None,
            raw_text=request.text,
        )

