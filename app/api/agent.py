from fastapi import APIRouter

from app.agent.orchestrator import handle_text_message
from app.agent.schemas import AgentTextRequest, AgentTextResponse

router = APIRouter(prefix="/api/v1/agent", tags=["agent"])


@router.post("/text", response_model=AgentTextResponse)
def agent_text(request: AgentTextRequest):
    return handle_text_message(request)

