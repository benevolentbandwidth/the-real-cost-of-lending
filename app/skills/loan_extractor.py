from pydantic import BaseModel


class LoanExtractionRequest(BaseModel):
    document_uri: str | None = None
    raw_text: str | None = None


class LoanExtractionResponse(BaseModel):
    lender_name: str | None = None
    principal: float | None = None
    interest_rate_percent: float | None = None
    tenure_months: int | None = None
    processing_fee_percent: float | None = None
    notes: str


def extract_loan_terms(request: LoanExtractionRequest) -> LoanExtractionResponse:
    return LoanExtractionResponse(
        notes="Starter placeholder. Gemini Vision OCR extraction pending.",
    )

