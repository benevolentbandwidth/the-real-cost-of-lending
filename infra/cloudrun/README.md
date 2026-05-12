# Cloud Run Deployment Notes

## Required settings

- GCP project: `b2-lending-lens`
- Region: `us-east1`
- Service account: `ll-app-service@b2-lending-lens.iam.gserviceaccount.com`
- Min instances: `0`
- Max instances: `3`
- Build type: Dockerfile
- Dockerfile path: `Dockerfile`

## First-time setup

1. Go to Cloud Run.
2. Click Create service.
3. Select Continuously deploy from a repository.
4. Click Set up with Cloud Build.
5. Switch GitHub authorization to the `benevolentbandwidth` organization.
6. Select `the-real-cost-of-lending`.
7. Select branch `main`.
8. Use Dockerfile build.
9. Select region `us-east1`.
10. Select service account `ll-app-service@b2-lending-lens.iam.gserviceaccount.com`.
11. Set min instances to `0`.
12. Set max instances to `3`.
13. Allow unauthenticated invocations for initial public app testing.
14. Deploy.

## Troubleshooting

If the repo or branch does not appear, confirm that the repo has at least one commit on `main`.

If the Cloud Build link is greyed out, ask for Cloud Build Connection Admin access.

If service account selection fails, ask for `iam.serviceAccounts.actAs` / service account user access.

If Gemini fails, verify the Cloud Run service account has Vertex AI access.

