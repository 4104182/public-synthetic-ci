# Public synthetic CI laboratory

This repository is **PUBLIC by design** and is used **only for GitHub-hosted synthetic tests**. All tests and fixtures are independently authored, generic and safe for publication.

## Boundary

- **Allowed:** artificial sample inputs, open algorithms, non-sensitive protocol contracts, publicly distributable example programs, and public CI output that reveals no private details.
- **Prohibited:** private repository source or patches, actual owner server paths/IP addresses/user lists, confidential build artifacts or debug APKs, signing material, private keys, wallet seeds, credentials, proprietary test data, customer/payment data, internal trace/log files, secret-dependent integrations, and links that expose access tokens.
- Do **not** grant this workflow access to any private project repository or app secrets, and do **not** add a checkout step for private sources. Do not attempt to make any existing private repository public.
- Do not call synthetic test success a production app pass. Original Android/native tests and artifact storage are performed separately in owner-controlled isolated build/test environments; sanitized summary metrics may be copied here once disclosure has been reviewed.
- All source migrations, preserved version history, and debug/test APK assets live in **PRIVATE GitHub**. Production signing keys must remain entirely outside GitHub and outside general-purpose build servers.
- Agents working on a related PRIVATE project must follow that project's private `AGENTS.md` and source migration ledger; PUBLIC GitHub Actions never read private code.

## CI

`.github/workflows/synthetic-ci.yml` runs a small Python standard-library test suite using public fabricated fixtures, with restricted GitHub token permissions and no secrets. It does **not** build an actual wallet or prove cryptographic security.

**Status:** a public workflow run is not a private project build or integration release authorization.
