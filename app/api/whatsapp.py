from fastapi import APIRouter
from pydantic import BaseModel, Field

router = APIRouter(prefix="/api/v1/whatsapp", tags=["whatsapp"])


class WhatsAppWebhookRequest(BaseModel):
    sender: str | None = Field(default=None, alias="from")
    message_type: str | None = None
    text: str | None = None


@router.post("/webhook")
def whatsapp_webhook(request: WhatsAppWebhookRequest):
    return {
        "status": "received",
        "message": "WhatsApp webhook placeholder. BSP integration pending.",
    }

