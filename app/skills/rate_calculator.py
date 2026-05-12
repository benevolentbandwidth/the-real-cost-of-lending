from pydantic import BaseModel, Field


class RateCalculationRequest(BaseModel):
    principal: float = Field(gt=0)
    annual_interest_rate_percent: float = Field(ge=0)
    tenure_months: int = Field(gt=0)
    processing_fee_percent: float = Field(default=0, ge=0)


class RateCalculationResponse(BaseModel):
    principal: float
    annual_interest_rate_percent: float
    tenure_months: int
    processing_fee: float
    estimated_total_interest: float
    estimated_all_in_cost: float
    risk_flag: str
    disclaimer: str


def calculate_rate(request: RateCalculationRequest) -> RateCalculationResponse:
    processing_fee = request.principal * (request.processing_fee_percent / 100)

    estimated_total_interest = (
        request.principal
        * (request.annual_interest_rate_percent / 100)
        * (request.tenure_months / 12)
    )

    estimated_all_in_cost = (
        request.principal
        + estimated_total_interest
        + processing_fee
    )

    if request.annual_interest_rate_percent >= 26 or request.processing_fee_percent > 2:
        risk_flag = "high"
    elif request.annual_interest_rate_percent >= 18:
        risk_flag = "medium"
    else:
        risk_flag = "low"

    return RateCalculationResponse(
        principal=request.principal,
        annual_interest_rate_percent=request.annual_interest_rate_percent,
        tenure_months=request.tenure_months,
        processing_fee=round(processing_fee, 2),
        estimated_total_interest=round(estimated_total_interest, 2),
        estimated_all_in_cost=round(estimated_all_in_cost, 2),
        risk_flag=risk_flag,
        disclaimer="Starter estimate only. Production APR logic pending.",
    )

