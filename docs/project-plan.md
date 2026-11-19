# Project Plan: Watermark Image Desktop App

## Metadata
| Key | Value |
| --- | --- |
| ID | PP-001 |
| CrossReference | [BC-001], [SA-001], [MIL-001], [MIL-002], [MIL-003], [MIL-004], [MIL-005], [MIL-006], [US-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-19 | Accepted | Jens Tirsvad Nielsen | Stand-in for S01 | Initial version<br>Accepted on Go in RC-003 | pending |

---

## Purpose

This plan schedules the six gateways of the Watermark Image Desktop App inside the one-week window of [BC-001], from 2026-11-19 to 2026-11-26. Each gateway is one milestone document, one branch and one pull request, so the build steps stay traceable.

## Planning Assumptions

- Week 1 starts 2026-11-19; the plan ends by 2026-11-26. No deadline was given, so the window is the author's proposal for S01 to confirm (source: [BC-001] Constraints).
- Phase length: one day per gateway, with one day of reserve before the end date. S01 is the only person who works on the project (source: [SA-001]).
- Each gateway has its own branch (`mil-NNN-<slug>`) and pull request; a reviewer merges. In autonomous mode the pull request is merged after its checks are green, as `AGENTS.md` sets out.
- The local quality gate, including the opengrep scan, runs before every push (source: [BC-001] Constraints).
- The plan-first gate holds: no file under `src/` or `tests/` is written before the gateway's milestone is `Accepted` with a Go review.
- The repository name follows the existing `origin` remote and not the underscore spelling in the first prompt.
- S01 accepted this plan in chat on 2026-11-19: the one-week window, the reading of "greater than 3.13" as 3.13 or newer, Pillow as the single runtime dependency, the repository name, and a local PlantUML server at `http://localhost:8080` (a container); a GitHub mirror is outside the scope. S01 also confirmed the English and IT-domain wording of the baseline documents.

## Gateway Schedule

| Gateway | Document | Window | Decision date | Owner | Stories | Main deliverable | Milestone |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Project setup | [MIL-001] | 2026-11-19 to 2026-11-20 | 2026-11-20 | S01 | US-001.06, US-001.07 | Repository tooling, README, wiki skeleton, Docker harness, ADRs | |
| Design | [MIL-002] | 2026-11-20 to 2026-11-21 | 2026-11-21 | S01 | US-001.01 to US-001.05 | Accepted design artifacts of UC-001 | |
| Step 1, upload | [MIL-003] | 2026-11-21 to 2026-11-22 | 2026-11-22 | S01 | US-001.01 | Window and `upload_image`, step 1 documentation | |
| Step 2, text watermark | [MIL-004] | 2026-11-22 to 2026-11-23 | 2026-11-23 | S01 | US-001.02, US-001.03 | Text watermark with placement and opacity, step 2 documentation | |
| Step 3, logo watermark | [MIL-005] | 2026-11-23 to 2026-11-24 | 2026-11-24 | S01 | US-001.04 | Logo watermark, step 3 documentation | |
| Step 4, save | [MIL-006] | 2026-11-24 to 2026-11-25 | 2026-11-25 | S01 | US-001.05 | `save_image`, completed documentation, verified success criteria | |

```plantuml
@startgantt
Project starts 2026-11-19
[Project setup] starts 2026-11-19 and ends 2026-11-20
[Design] starts 2026-11-20 and ends 2026-11-21
[Step 1 upload] starts 2026-11-21 and ends 2026-11-22
[Step 2 text watermark] starts 2026-11-22 and ends 2026-11-23
[Step 3 logo watermark] starts 2026-11-23 and ends 2026-11-24
[Step 4 save] starts 2026-11-24 and ends 2026-11-25
[Setup Go/No-Go] happens 2026-11-20
[Design Go/No-Go] happens 2026-11-21
[Step 1 Go/No-Go] happens 2026-11-22
[Step 2 Go/No-Go] happens 2026-11-23
[Step 3 Go/No-Go] happens 2026-11-24
[Step 4 Go/No-Go] happens 2026-11-25
[Reserve] starts 2026-11-25 and ends 2026-11-26
@endgantt
```

## Scope Coverage

| Business Case scope item | Gateway |
| --- | --- |
| Window and image upload (step 1) | [MIL-003] |
| Text watermark with position and opacity (step 2) | [MIL-004] |
| Logo watermark (step 3) | [MIL-005] |
| Save (step 4) | [MIL-006] |
| `pyproject.toml`, `.gitignore`, `.editorconfig`, `Doxyfile`, `constants.py`, `tests/` | [MIL-001] |
| README with `.venv` and pip instructions, run and test instructions | [MIL-001], completed in [MIL-006] |
| README screenshots and wiki pages per step in three languages | [MIL-003] to [MIL-006]; skeleton in [MIL-001] |
| Screenshots produced in a Docker container | [MIL-001] harness, [MIL-003] to [MIL-006] captures |
| Repository description and topics | [MIL-001] |
| Framework project documents (use case and design, dictionary, traceability, reviews, decisions) | [MIL-001] decisions, [MIL-002] design |

## Dependencies

```
MIL-001 → MIL-002 → MIL-003 → MIL-004 → MIL-005 → MIL-006
```

A No-Go at a gateway stops the later gateways. The gateway is reworked and decided again; the end date 2026-11-26 moves only if the reserve day is used up, and only S01 decides to move it, recording the new date in a new Version History row of this plan and of [BC-001].

## Plan Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| The Docker harness takes longer than a day to work (virtual display, fonts) | Gateway 1 and every screenshot task slip | Build the harness first in gateway 1; if it fails, stop and report instead of using the host desktop; the reserve day absorbs one slip |
| Reviews of the many design artifacts take longer than planned | Gateway 2 slips | One use case only; design artifacts that nothing needs are skipped with a recorded reason |
| Danish and Bahasa Malaysia pages need a native-reader check | Wiki reviews stay conditional | Keep the sentences short and the terms fixed; the language criteria stay pending until S01 confirms (Business Case risk on wiki quality) |
| The git host token lacks a scope (issues, repository, wiki) | Sync, push or wiki publication fails | Check each scope in gateway 1 and stop if one is missing; no workaround |
| Two pull requests need the same file (README, wiki sidebar) | Merge conflicts | One pull request at a time, in gateway order |

## Open Issues

- Wiki publication needs the wiki enabled for the repository and the publish workflow of the git host; both are checked in gateway 1.
- The language criteria of the Danish and Bahasa Malaysia wiki pages need a person who reads those languages; the stand-in reviews leave them pending until S01 has checked them.

---

[BC-001]: ./business-case.md
[SA-001]: ./stakeholder-analysis.md
[US-001]: ./user-stories.md
[MIL-001]: ./milestones/mil-001-project-setup.md
[MIL-002]: ./milestones/mil-002-design.md
[MIL-003]: ./milestones/mil-003-step-1-upload.md
[MIL-004]: ./milestones/mil-004-step-2-text-watermark.md
[MIL-005]: ./milestones/mil-005-step-3-logo-watermark.md
[MIL-006]: ./milestones/mil-006-step-4-save.md
