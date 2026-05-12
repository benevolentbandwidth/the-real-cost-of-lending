BOOKKEEPING_PARSE_PROMPT = """
You are parsing a bookkeeping entry for a woman micro-entrepreneur in India.

Return only valid JSON with these fields:
- type: "income", "expense", or "unknown"
- amount: numeric amount if present, otherwise null
- currency: "INR"
- category: short English category if inferable, otherwise null
- raw_text: original text
"""

