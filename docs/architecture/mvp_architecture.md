# SmartLend MVP Architecture

## Overview

SmartLend is a voice-first, WhatsApp-first, agentic AI lending-transparency platform for women micro-entrepreneurs.

The MVP backend is organized around an agent orchestrator and modular skills.

## Primary user

Mann Deshi small business woman:

- Kirana shop owner
- Tailor
- Livestock manager
- SHG participant or group leader
- Comfortable with WhatsApp voice notes
- Prefers Marathi, Hindi, or Hinglish

## Primary channel

WhatsApp Business API.

The first repo version only includes a webhook placeholder. Real BSP integration is pending.

## Agent flow

```text
User message
-> WhatsApp webhook / API input
-> Agent orchestrator
-> Intent classification
-> Skill dispatch
-> Advisory response
-> Future voice/text response
```

## MVP skills

1. Loan Term Extractor
2. NBFC Verifier
3. Rate Calculator
4. Red Flag Scanner
5. Bookkeeping Assistant

## Deferred components

- Full WhatsApp BSP integration
- IVR integration
- Gemini Vision OCR
- Firestore persistence
- Cloud Storage document lifecycle
- DhanKanya RAG
- Vector Search
- Full APR engine
- Grievance filing assistant

