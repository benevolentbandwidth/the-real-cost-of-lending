from pydantic import BaseModel


class RedFlagScanRequest(BaseModel):
    text: str


class RedFlag(BaseModel):
    severity: str
    issue: str
    explanation: str


class RedFlagScanResponse(BaseModel):
    flags: list[RedFlag]


def scan_red_flags(request: RedFlagScanRequest) -> RedFlagScanResponse:
    flags: list[RedFlag] = []

    normalized = request.text.lower()

    if "upfront fee" in normalized or "pay before disbursement" in normalized:
        flags.append(
            RedFlag(
                severity="high",
                issue="Upfront payment before disbursement",
                explanation="Requiring payment before loan disbursement is a common fraud indicator.",
            )
        )

    if "contacts" in normalized or "sms" in normalized:
        flags.append(
            RedFlag(
                severity="medium",
                issue="Excessive phone permissions",
                explanation="Loan apps requesting contacts or SMS access may create privacy and recovery-risk concerns.",
            )
        )

    return RedFlagScanResponse(flags=flags)

