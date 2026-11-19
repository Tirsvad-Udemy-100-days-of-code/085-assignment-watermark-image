# Traceability Matrix: Watermark Image Desktop App

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-19 | Accepted | Jens Tirsvad Nielsen | Stand-in for S01 | Initial version | pending |

---

## Purpose

Tracks backward and forward links between artifact instances so that the cross-artifact traceability of the Business Case is measurable. A row is added or updated whenever an artifact instance is created or reviewed.

## Traceability Table

| Artifact Instance | Type | Language | Domain | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- | --- | --- |
| [BC-001] | BC | en | it | - | [SA-001], [PP-001], [US-001] | [RC-001] |
| [SA-001] | SA | en | it | [BC-001] | [PP-001], [US-001] | [RC-002] |
| [US-001] | US | en | it | [BC-001], [SA-001] | [MIL-003], [MIL-004], [MIL-005], [MIL-006] | - |
| [PP-001] | PP | en | it | [BC-001], [SA-001] | [MIL-001], [MIL-002], [MIL-003], [MIL-004], [MIL-005], [MIL-006] | [RC-003] |
| [MIL-001] | MIL | en | it | [PP-001], [BC-001] | [MIL-002] | [RC-004] |
| [MIL-002] | MIL | en | it | [MIL-001] | [MIL-003] | [RC-005] |
| [MIL-003] | MIL | en | it | [MIL-002], [US-001] | [MIL-004] | [RC-006] |
| [MIL-004] | MIL | en | it | [MIL-003], [US-001] | [MIL-005] | [RC-007] |
| [MIL-005] | MIL | en | it | [MIL-004], [US-001] | [MIL-006] | [RC-008] |
| [MIL-006] | MIL | en | it | [MIL-005], [US-001] | - | [RC-009] |
| [ADR-0001] | ADR | - | - | [BC-001], [SA-001] | - | [RC-010] |
| [ADR-0002] | ADR | - | - | [BC-001], [SA-001] | - | [RC-011] |
| [ADR-0003] | ADR | - | - | [BC-001] | - | [RC-012] |
| [ADR-0004] | ADR | - | - | [BC-001], [PP-001] | - | [RC-013] |

## Concern Coverage

| Concern (CN-ID) | Views that answer it | Decisions (ADR) | Quality check (TP) | Status |
| --- | --- | --- | --- | --- |
| CN-001 | - | - | - | Gap |
| CN-002 | [PP-001] | - | - | Covered |
| CN-003 | - | [ADR-0004] | - | Gap |
| CN-004 | - | [ADR-0002] | - | Gap |
| CN-005 | - | - | - | Gap |
| CN-006 | - | [ADR-0003] | - | Gap |
| CN-007 | - | - | - | Gap |
| CN-008 | - | [ADR-0001] | - | Covered |
| CN-009 | - | - | - | Gap |

## Open Inconsistencies

| # | Views | Inconsistency | Found in (RC-ID) | Status | Resolved in |
| --- | --- | --- | --- | --- | --- |
| - | - | None found | - | Closed | - |

## Coverage Notes

- No Test Plan exists (skipped in ADR-0004), so the quality check column holds `-`.
- `-` in Upstream means foundational; `-` in Downstream means nothing is built on it yet; `-` in Last Reviewed means no review record names the instance.
- A concern is a `Gap` until a design view answers it; the design artifacts arrive in gateway 2.

---

[ADR-0001]: ../adr/adr-0001-technology.md
[ADR-0002]: ../adr/adr-0002-architecture.md
[ADR-0003]: ../adr/adr-0003-gui-testing.md
[ADR-0004]: ../adr/adr-0004-conventions.md
[BC-001]: ../business-case.md
[MIL-001]: ../milestones/mil-001-project-setup.md
[MIL-002]: ../milestones/mil-002-design.md
[MIL-003]: ../milestones/mil-003-step-1-upload.md
[MIL-004]: ../milestones/mil-004-step-2-text-watermark.md
[MIL-005]: ../milestones/mil-005-step-3-logo-watermark.md
[MIL-006]: ../milestones/mil-006-step-4-save.md
[PP-001]: ../project-plan.md
[RC-001]: reviews/rc-001-business-case.md
[RC-002]: reviews/rc-002-stakeholder-analysis.md
[RC-003]: reviews/rc-003-project-plan.md
[RC-004]: reviews/rc-004-mil-001-project-setup.md
[RC-005]: reviews/rc-005-mil-002-design.md
[RC-006]: reviews/rc-006-mil-003-step-1-upload.md
[RC-007]: reviews/rc-007-mil-004-step-2-text-watermark.md
[RC-008]: reviews/rc-008-mil-005-step-3-logo-watermark.md
[RC-009]: reviews/rc-009-mil-006-step-4-save.md
[RC-010]: reviews/rc-010-adr-0001-technology.md
[RC-011]: reviews/rc-011-adr-0002-architecture.md
[RC-012]: reviews/rc-012-adr-0003-gui-testing.md
[RC-013]: reviews/rc-013-adr-0004-conventions.md
[SA-001]: ../stakeholder-analysis.md
[US-001]: ../user-stories.md
