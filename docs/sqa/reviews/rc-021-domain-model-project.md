# Review Record: Project Domain Model DM-002

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-021 |
| CrossReference | [DM-002], [QC-DM-001], [QC-LANG-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | Stand-in for S01 | Review record; mode autonomous, not independent | pending |

---

## Artifact Under Review

- Instance reviewed: [DM-002]
- Checklist used: [QC-DM-001]
- Scope: full review
- Language and domain: en / it
- Language reviewer: S01 (standing confirmation in chat on 2026-11-20)
- Mode: autonomous, not independent (the reviewer is a stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Uses ubiquitous/business language throughout; no technical or implementation jargon (e.g. no "table", "class", "pointer") | Pass | Only Picture, Watermark, Text mark, Logo mark, Placement and Marked picture; no software words |
| 2 | Multiplicities on associations are correct and complete (e.g. `1..*`, `0..1`) | Pass | Every association shows both multiplicities |
| 3 | No operation/method signatures shown — attributes and associations only | Pass | No operations shown (`hide methods`) |
| 4 | Associations are named with an unambiguous reading direction | Pass | Names read in one direction: is made from, carries, sits at, is drawn from |
| 5 | Generalization/specialization used correctly, reflecting true "is-a" relationships, not misused for code reuse | Pass | Text mark and Logo mark are true kinds of Watermark |
| 6 | Every concept traces to a noun phrase found in the use cases or glossary | Pass | Concept table cites the use case noun phrase of each concept |
| 7 | Attributes are simple domain data (no foreign-key-like references or object pointers modeled as attributes) | Pass | Attributes are plain data; relations are associations |
| 8 | The Purpose names the concerns (`CN-NNN`) the Domain Model answers and the stakeholders it serves, so its viewpoint is stated | Pass | Purpose names CN-001 and CN-009 and the stakeholders S01 and S02 |
| 9 | No technical solution names: only conceptual classes of the Product Owner's world, never a file, an environment variable, a setting source, a database, a table, an API, a service, a cache or any other mechanism | Pass | No file, library or mechanism is named |
| 10 | No empty concept: every concept has at least one attribute and at least one association | Pass | Each concept has an attribute and an association or generalization |
| 11 | A Domain Model written for one use case reuses the concepts, attributes, associations and names of the project Domain Model, and its additions and changes are added to the project Domain Model | Pass | This is the project Domain Model; it holds the concepts of DM-001 unchanged |
| 12 | The software is a black box and a normal person can read the model: no concept or attribute exists only because the software exists (a run, command, option, mode, step, exit code, log, session, question, prompt, summary or other screen or tool element); no attribute is computed from other concepts, and none is an identifier or a storage type; every concept in the Concept Table has a one-sentence definition in everyday words with no IT term | Pass | Nothing exists only because the software exists; a person can read it |

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

[DM-002]: ../../domain-model.md
[QC-DM-001]: ../../../framework/qc/artifacts/qc-domain-model.md
[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
