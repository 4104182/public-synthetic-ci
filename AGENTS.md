# Public CI agents — synthetic tests ONLY

This is a PUBLIC repository. Treat every file and Actions log as globally readable.

**Owner objective:** GitHub-hosted tests must run only in PUBLIC repos, isolated from all private project sources. All application source, internal test APKs and migration evidence must stay in the matching verified PRIVATE GitHub repository. Servers are temporary build/test workers, never canonical source stores.

The CI here may test only independently created synthetic data and intentionally publishable contracts. Before pushing any content, verify that it has no secret, private app code, signing keys, tokens, mnemonics, proprietary APK, device identifiers, exact private server paths, personal records or customer/payment data. Never clone, pull or check out any private repo in this public workflow; never provide private tokens to Actions. Do not change any private repo visibility.

For actual engineering work, locate the corresponding private repository and read its private AGENTS.md to obtain current account/RDC instructions, owners, source versions and migration status. Do not publish those private instructions here. Keep all production features/mainnet, native wallet, signing and real-money operations disabled until independent verified owner-controlled audits.

**Test labels:** PUBLIC_SYNTHETIC_PASS means only this repository's fake fixtures passed. It is never AEGIS_BUILD_PASS, LIVE_VPN_PASS, ANDROID_CRYPTO_PASS or PRODUCTION_READY.
