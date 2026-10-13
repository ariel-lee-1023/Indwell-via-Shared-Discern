# Current validation — original-English source audit

The English runtime passes the existing-skill fold-in checks in [foldin-validation.json](foldin-validation.json), including all-English SKILL.md/references, the response-language rule, links, routing, budgets, MIT license, and discovery link. The unmodified generic validator's report is retained in generic-validation.json; its one directory-shape objection concerns the intentionally retained examples/. No other error is waived.

The earlier local-draft reports are preserved under local-draft-2026-10-13/. They describe the Chinese draft, not this runtime. The original reading and coverage records remain historical. New direct-English passage checks, source hashes, and item-level dispositions are recorded in the [source audit](original-english-audit.md). See [English revision](english-release.md) for scope and publication authorization.

HTML/SVG files are unchanged by this source audit. The earlier page-checks.json records 15 actual calculation, invalid-input, preset, and keyboard assertions, with screenshots inspected at wide and narrow widths. That evidence does not establish learning efficacy.

Independent model behavior (baseline/core/core+references), host import, learning efficacy, and Mermaid rendering remain unrun. No passing model scores or retrieval traces have been invented.

Reproduce structural checks with: `python3 fidelity-ledger/validate-foldin.py <Books-to-Skill-Refs-root> <skill-root>`. The adapter also saves the unmodified generic validator result.

Source-audit coverage and runtime correspondence pass in [original-english-audit-validation.json](original-english-audit-validation.json). Reproduce with `python3 fidelity-ledger/validate-source-audit.py <skill-root>`. This checks inventory integrity, not source interpretation truth. The core scan has no findings; the reference scan retains nine LOW legacy external links and no HIGH findings. The staged published-layout check has only the same inherited examples-directory exception.
