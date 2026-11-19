# Traceability Matrix: Watermark Image Desktop App

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Deprecated | Jens Tirsvad Nielsen | Stand-in for S01 | Last Reviewed updated for the DCD delta reviews | [05ac937] |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | Stand-in for S01 | Last Reviewed updated for the gateway 4 DCD delta reviews | pending |

---

## Purpose

Tracks backward and forward links between artifact instances so that the cross-artifact traceability of the Business Case is measurable. A row is added or updated whenever an artifact instance is created or reviewed.

## Traceability Table

| Artifact Instance | Type | Language | Domain | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- | --- | --- |
| [BC-001] | BC | en | it | - | [SA-001], [PP-001], [US-001], [UCD-001] | [RC-019] |
| [SA-001] | SA | en | it | [BC-001] | [PP-001], [US-001] | [RC-002] |
| [UCD-001] | UCD | en | it | [BC-001], [US-001], [SA-001] | [UC-001] | [RC-016] |
| [US-001] | US | en | it | [BC-001], [SA-001], [UCD-001] | [UC-001], [MIL-003], [MIL-004], [MIL-005], [MIL-006] | [RC-018] |
| [UC-001] | UC | en | it | [UCD-001], [US-001] | [DM-001], [SSD-001] | [RC-017] |
| [DM-001] | DM | en | it | [UC-001] | [DM-002], [DICT-001], [OC-001] | [RC-020] |
| [DM-002] | DM | en | it | [DM-001] | [DICT-001], [DCD-002] | [RC-021] |
| [DICT-001] | DICT | en | it | [DM-002] | [OC-001], [SD-001], [DCD-001] | [RC-023] |
| [SSD-001] | SSD | en | it | [UC-001] | [OC-001] | [RC-022] |
| [OC-001] | OC | en | it | [SSD-001], [DM-001], [DICT-001] | [SD-001] | [RC-024] |
| [SD-001] | SD | en | it | [OC-001] | [DCD-001] | [RC-025] |
| [DCD-001] | DCD | en | it | [SD-001], [OC-001], [DM-002] | [DCD-002] | [RC-032] |
| [DCD-002] | DCD | en | it | [DCD-001] | - | [RC-031] |
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
| CN-001 | [UC-001], [DM-002], [SD-001], [DCD-002] | - | - | Covered |
| CN-002 | [PP-001] | - | - | Covered |
| CN-003 | - | [ADR-0004] | - | Gap |
| CN-004 | [SD-001], [DCD-002] | [ADR-0002] | - | Covered |
| CN-005 | - | - | - | Gap |
| CN-006 | - | [ADR-0003] | - | Gap |
| CN-007 | - | - | - | Gap |
| CN-008 | - | [ADR-0001] | - | Covered |
| CN-009 | [UC-001], [DM-002], [SD-001], [DCD-002] | - | - | Covered |

## Open Inconsistencies

| # | Views | Inconsistency | Found in (RC-ID) | Status | Resolved in |
| --- | --- | --- | --- | --- | --- |
| - | - | None found | - | Closed | - |

## Coverage Notes

- No Test Plan exists (skipped in ADR-0004), so the quality check column holds `-`.
- `-` in Upstream means foundational; `-` in Downstream means nothing is built on it yet; `-` in Last Reviewed means no review record names the instance.
- A concern is a `Gap` until a view or a decision answers it.

---

[ADR-0001]: ../adr/adr-0001-technology.md
[ADR-0002]: ../adr/adr-0002-architecture.md
[ADR-0003]: ../adr/adr-0003-gui-testing.md
[ADR-0004]: ../adr/adr-0004-conventions.md
[BC-001]: ../business-case.md
[DCD-001]: ../use-cases/uc-001/dcd.md
[DCD-002]: ../dcd.md
[DICT-001]: ../dictionary.md
[DM-001]: ../use-cases/uc-001/dm.md
[DM-002]: ../domain-model.md
[MIL-001]: ../milestones/mil-001-project-setup.md
[MIL-002]: ../milestones/mil-002-design.md
[MIL-003]: ../milestones/mil-003-step-1-upload.md
[MIL-004]: ../milestones/mil-004-step-2-text-watermark.md
[MIL-005]: ../milestones/mil-005-step-3-logo-watermark.md
[MIL-006]: ../milestones/mil-006-step-4-save.md
[OC-001]: ../use-cases/uc-001/oc.md
[PP-001]: ../project-plan.md
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
[RC-016]: reviews/rc-016-use-case-diagram.md
[RC-017]: reviews/rc-017-use-case-uc-001.md
[RC-018]: reviews/rc-018-user-stories.md
[RC-019]: reviews/rc-019-business-case-delta.md
[RC-020]: reviews/rc-020-domain-model-uc-001.md
[RC-021]: reviews/rc-021-domain-model-project.md
[RC-022]: reviews/rc-022-ssd-uc-001.md
[RC-023]: reviews/rc-023-dictionary.md
[RC-024]: reviews/rc-024-oc-uc-001.md
[RC-025]: reviews/rc-025-sd-uc-001.md
[RC-031]: reviews/rc-031-dcd-project-delta-2.md
[RC-032]: reviews/rc-032-dcd-uc-001-delta-2.md
[SA-001]: ../stakeholder-analysis.md
[SD-001]: ../use-cases/uc-001/sd.md
[SSD-001]: ../use-cases/uc-001/ssd.md
[UC-001]: ../use-cases/uc-001/uc.md
[UCD-001]: ../use-case-diagram.md
[US-001]: ../user-stories.md
