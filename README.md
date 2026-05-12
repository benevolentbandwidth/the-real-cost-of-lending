# SmartLend / Real Cost of Lending Lens

Cloud Run starter backend for the Benevolent Bandwidth Real Cost of Lending Lens / SmartLend project.

## Project

- GCP project: `b2-lending-lens`
- Region: `us-east1`
- Runtime service account: `ll-app-service@b2-lending-lens.iam.gserviceaccount.com`
- Storage bucket: `b2-foundation`
- Storage prefix: `lending-lens/`

## Purpose

This repo starts the SmartLend backend as a minimal FastAPI service that can be deployed to Cloud Run and expanded into the PRD architecture.

## MVP architecture

- Agent orchestrator
- Loan Term Extractor skill
- NBFC Verifier skill
- Rate Calculator skill
- Red Flag Scanner skill
- Bookkeeping Assistant skill
- WhatsApp webhook placeholder
- Gemini integration through Vertex AI

## Local setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8080
```

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8080
```

## Local Google authentication

```bash
gcloud auth application-default login
```

Cloud Run does not need local credentials. It authenticates through the selected runtime service account.

## Test endpoints

```text
GET  /
GET  /health
GET  /api/v1/gemini/ping
POST /api/v1/agent/text
POST /api/v1/skills/rate-calculate
POST /api/v1/skills/bookkeeping-parse
POST /api/v1/whatsapp/webhook
```

## Cloud Run settings

Use:

```text
Region: us-east1
Service account: ll-app-service@b2-lending-lens.iam.gserviceaccount.com
Min instances: 0
Max instances: 3
Authentication: Allow unauthenticated invocations for initial public testing
```

## PRD

Place the approved PRD at:

```text
docs/prd/smartlend_prd_v4.pdf
```

Do not commit private internal notes or unapproved source PDFs.

## Security notes

- Do not commit secrets.
- Do not commit service account JSON files.
- Do not hardcode API keys.
- Use Secret Manager for future third-party API keys.
- Use Cloud Run service identity for Google Cloud APIs.

