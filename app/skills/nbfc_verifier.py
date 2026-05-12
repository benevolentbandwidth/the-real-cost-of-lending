from pydantic import BaseModel


class NBFCVerificationRequest(BaseModel):
    lender_name: str
    registration_number: str | None = None


class NBFCVerificationResponse(BaseModel):
    lender_name: str
    registration_number: str | None
    status: str
    notes: str


def verify_nbfc(request: NBFCVerificationRequest) -> NBFCVerificationResponse:
    return NBFCVerificationResponse(
        lender_name=request.lender_name,
        registration_number=request.registration_number,
        status="unknown",
        notes="Starter placeholder. RBI NBFC registry integration pending.",
    )

