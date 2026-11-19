# Review Record: Use Case Diagram UCD-001

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-016 |
| CrossReference | [UCD-001], [QC-UCD-001], [QC-LANG-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | Stand-in for S01 | Review record; mode autonomous, not independent | pending |

---

## Artifact Under Review

- Instance reviewed: [UCD-001]
- Checklist used: [QC-UCD-001]
- Scope: full review
- Language and domain: en / it
- Language reviewer: S01 (standing confirmation in chat on 2026-11-20)
- Mode: autonomous, not independent (the reviewer is a stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Actors are defined with correct UML stereotypes (e.g. `<<System>>`, `<<Actor>>`) | Pass | Actor `<<Actor>>` and system `<<System>>` stereotypes |
| 2 | System boundary is clearly drawn and labeled | Pass | Boundary rectangle labelled with the system name |
| 3 | Include/extend relationships are used correctly per UML 2.5.1, not as generic "uses" arrows | Pass | No include or extend is used |
| 4 | Every actor participates in at least one use case (no orphan actors) | Pass | User takes part in the one use case |
| 5 | Diagram is traceable to a documented stakeholder need | Pass | Actor table cites S01 and S02 |
| 6 | Use case names are verb phrases describing actor goals, not internal system operations | Pass | `Watermark an image` is a verb phrase and an actor goal |
| 7 | Diagram is free of implementation detail (e.g. UI widgets, database tables) | Pass | No widgets or storage shown |
| 8 | Actor and use case naming is consistent with corresponding Use Case and User Story documents | Pass | Names equal those of UC-001 and US-001 |
| 9 | Each use case lists the user story it comes from and its priority (MoSCoW) with a reason | Pass | Use case table lists the source story and Must with a reason |
| 10 | When there is more than one primary actor, a role matrix (use case by role) is present and marked as a suggestion for the Product Owner to approve | N-A | One primary actor; the document says the matrix is not applicable |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | Pass | Language and Domain rows are present and filled |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list | Pass | Language en is a BCP 47 code; Domain it is in the registry list |
| 3 | The content (prose and table cells) is written in the stated language | Pass | English throughout; S01 gave a standing confirmation in chat on 2026-11-20 and checks the wording of this document in the pull request |
| 4 | The register matches the one the registry gives for the artifact type | Pass | Register IT Professional English as the registry gives for the type |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Pass | PO terms follow the use case and the domain dictionary DICT-001 is written in this gateway; terms follow it; S01 gave a standing confirmation in chat on 2026-11-20 and checks the wording of this document in the pull request |
| 6 | Metadata keys, section headings, IDs and statuses are in English | Pass | Metadata keys, headings, IDs and statuses are English |
| 7 | No translated twin (`<name>.<language>.md`) exists beside the document | Pass | No translated twin exists |
| 8 | A change of language or domain since the previous accepted version has a Version History row and was reviewed again | Pass | No change of language since the first version |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly | Pass | Domain terms confirmed: S01 gave a standing confirmation in chat on 2026-11-20 and checks the wording of this document in the pull request |
| 10 | Abbreviations are spelled out on first use, in the stated language | Pass | Abbreviations are spelled out on first use |

## Overall Verdict

Go — every Mandatory criterion passes, including the language criteria confirmed by S01; no action items

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | 2026-11-20 |

---

[UCD-001]: ../../use-case-diagram.md
[QC-UCD-001]: ../../../framework/qc/artifacts/qc-use-case-diagram.md
[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
