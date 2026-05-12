from app.agent.schemas import AgentTextRequest, AgentTextResponse


def classify_intent(message: str) -> tuple[str, list[str]]:
    normalized = message.lower()

    loan_terms = [
        "loan",
        "interest",
        "emi",
        "processing fee",
        "apr",
        "lender",
        "nbfc",
        "karz",
        "vyaj",
        "karj",
    ]

    bookkeeping_terms = [
        "bechi",
        "sold",
        "kharcha",
        "expense",
        "income",
        "aaj",
        "rupaye",
        "kamai",
        "kharch",
    ]

    literacy_terms = [
        "what is",
        "explain",
        "samjhao",
        "meaning",
    ]

    verification_terms = [
        "verify",
        "legit",
        "registered",
        "rbi",
    ]

    if any(term in normalized for term in loan_terms):
        return "loan_audit", ["rate_calculator", "red_flag_scanner", "nbfc_verifier"]

    if any(term in normalized for term in bookkeeping_terms):
        return "bookkeeping", ["bookkeeping"]

    if any(term in normalized for term in verification_terms):
        return "lender_verification", ["nbfc_verifier"]

    if any(term in normalized for term in literacy_terms):
        return "financial_literacy", []

    return "unknown", []


def handle_text_message(request: AgentTextRequest) -> AgentTextResponse:
    intent, skills = classify_intent(request.message)

    if intent == "loan_audit":
        response = (
            "This looks like a loan-audit request. I can check interest rate, "
            "processing fees, lender legitimacy, and red flags."
        )
    elif intent == "bookkeeping":
        response = (
            "This looks like a bookkeeping entry. I can extract amount, category, "
            "and whether it is income or expense."
        )
    elif intent == "lender_verification":
        response = (
            "This looks like a lender-verification request. I can start by checking "
            "the lender details against a registry placeholder."
        )
    elif intent == "financial_literacy":
        response = (
            "This looks like a financial-literacy question. I can explain lending "
            "terms in simple language."
        )
    else:
        response = (
            "I am not sure yet. You can ask me to check a loan, verify a lender, "
            "or record an income or expense."
        )

    return AgentTextResponse(
        intent=intent,
        language=request.language,
        suggested_skills=skills,
        response=response,
    )

