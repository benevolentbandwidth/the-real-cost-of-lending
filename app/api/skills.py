from fastapi import APIRouter

from app.skills.bookkeeping import (
    BookkeepingParseRequest,
    BookkeepingParseResponse,
    parse_bookkeeping_entry,
)
from app.skills.rate_calculator import (
    RateCalculationRequest,
    RateCalculationResponse,
    calculate_rate,
)

router = APIRouter(prefix="/api/v1/skills", tags=["skills"])


@router.post("/rate-calculate", response_model=RateCalculationResponse)
def rate_calculate(request: RateCalculationRequest):
    return calculate_rate(request)


@router.post("/bookkeeping-parse", response_model=BookkeepingParseResponse)
def bookkeeping_parse(request: BookkeepingParseRequest):
    return parse_bookkeeping_entry(request)

