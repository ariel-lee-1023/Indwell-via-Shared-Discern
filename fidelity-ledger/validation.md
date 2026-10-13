# Current validation — English revision

The English runtime passes the existing-skill fold-in checks in [foldin-validation.json](foldin-validation.json), including all-English SKILL.md/references, the response-language rule, links, routing, budgets, MIT license, and discovery link. The unmodified generic validator's report is retained in generic-validation.json; its one directory-shape objection concerns the intentionally retained examples/. No other error is waived.

The earlier local-draft reports are preserved under local-draft-2026-10-13/. They describe the Chinese draft, not this runtime. Source reading and coverage records remain historical evidence rather than new reads. See [English revision](english-release.md) for scope and publication authorization.

HTML/SVG files are unchanged by this revision. The earlier page-checks.json records 15 actual calculation, invalid-input, preset, and keyboard assertions, with screenshots inspected at wide and narrow widths. That evidence does not establish learning efficacy.

Independent model behavior (baseline/core/core+references), host import, learning efficacy, and Mermaid rendering remain unrun. No passing model scores or retrieval traces have been invented.

Reproduce structural checks with: `python3 fidelity-ledger/validate-foldin.py <Books-to-Skill-Refs-root> <skill-root>`. The adapter also saves the unmodified generic validator result.
