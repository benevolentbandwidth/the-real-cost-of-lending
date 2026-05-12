# Cloud Run Deployment Notes

## Required settings

- GCP project: `<gcp-project-id>`
- Region: `<cloud-run-region>`
- Service account: `<runtime-service-account>`
- Min instances: `0`
- Max instances: `3`
- Build type: Dockerfile
- Dockerfile path: `Dockerfile`

Project IDs, service accounts, organization names, and other infrastructure-specific values should be kept in private deployment notes or environment-specific runbooks.

## First-time setup

1. Go to Cloud Run.
2. Click Create service.
3. Select Continuously deploy from a repository.
4. Click Set up with Cloud Build.
5. Select the correct GitHub organization or account.
6. Select this repository.
7. Select branch `main`.
8. Use Dockerfile build.
9. Select the target Cloud Run region.
10. Select the runtime service account.
11. Set min instances to `0`.
12. Set max instances to `3`.
13. Choose the authentication setting appropriate for the deployment environment.
14. Deploy.

## Troubleshooting

If the repo or branch does not appear, confirm that the repo has at least one commit on `main`.

If the Cloud Build link is greyed out, ask for Cloud Build Connection Admin access.

If service account selection fails, ask for `iam.serviceAccounts.actAs` / service account user access.

If Gemini fails, verify the Cloud Run service account has Vertex AI access.
