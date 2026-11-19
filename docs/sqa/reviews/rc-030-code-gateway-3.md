# Review Record: Source code of gateway 3

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-030 |
| CrossReference | [MIL-003], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | Stand-in for S01 | Review record; mode autonomous, not independent | [05ac937] |

---

## Artifact Under Review

- Instance reviewed: source code under src/watermark_image/ and tests/ for gateway 3 (milestone [MIL-003])
- Checklist used: [QC-PY-001]
- Scope: full review of the code written in gateway 3
- Language and domain: n/a
- Language reviewer: none
- Mode: autonomous, not independent (the reviewer is a stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | Checked by reading the code and by scripts/check.sh |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Checked by reading the code and by scripts/check.sh |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | ruff check and format pass in scripts/check.sh |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | Checked by reading the code and by scripts/check.sh |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | ImageReadError is raised from the cause; no bare except |
| 6 | No mutable default arguments and no shadowed builtins | Pass | Checked by reading the code and by scripts/check.sh |
| 7 | Files, locks and connections are managed with context managers | Pass | PillowImage.open is used in a with block |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Checked by reading the code and by scripts/check.sh |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | No print and no logging needed |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | Pass | Names and signatures follow docs/dcd.md; deviations (scale_to_fit, window, refresh, composition import) are written into both DCDs in this pull request |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | 42 tests plus one graphical test in Docker; real files in tmp_path; no network |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | mypy strict passes without Any |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | Pillow is declared; nothing unused |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | Checked by reading the code and by scripts/check.sh |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | import-linter: 2 contracts kept; domain and application import no PIL or Tkinter |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | Checked by reading the code and by scripts/check.sh |
| 17 | Source is laid out in the layers and folders of the clean architecture folder structure (`domain`, `application`, `infrastructure`, `presentation` packages under `src/`, and `unit`, `integration` and `e2e` under `tests/`), in `snake_case`, and imports between the layers point inward | Pass | domain, application, infrastructure, presentation under src/watermark_image |
| 18 | File and folder names are English, contain no space and no character outside letters, digits, `-`, `_` and `.`, and follow the casing of the language for files | Pass | snake_case English file names |

## Overall Verdict

Go — every Mandatory criterion passes; no action items

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | 2026-11-20 |

---

[MIL-003]: ../../milestones/mil-003-step-1-upload.md
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
[05ac937]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/085-assignment-watermark-image/commit/05ac937057e51bc75db7351de9a9f6d67c274724
