from typing import Literal

from pydantic import BaseModel


Intent = Literal[
    "loan_audit",
    "bookkeeping",
    "financial_literacy",
    "lender_verification",
    "unknown",
]


class AgentTextRequest(BaseModel):
    user_id: str
    language: str = "en"
    message: str


class AgentTextResponse(BaseModel):
    intent: Intent
    language: str
    suggested_skills: list[str]
    response: str

