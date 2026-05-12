from app.skills.rate_calculator import RateCalculationRequest, calculate_rate


def test_rate_calculator_high_processing_fee():
    request = RateCalculationRequest(
        principal=50000,
        annual_interest_rate_percent=24,
        tenure_months=12,
        processing_fee_percent=3,
    )

    response = calculate_rate(request)

    assert response.processing_fee == 1500
    assert response.risk_flag == "high"

