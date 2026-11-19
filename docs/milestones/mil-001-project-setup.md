# Gateway 1: Project setup

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001], [US-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-19 | Accepted | Jens Tirsvad Nielsen | Stand-in for S01 | Initial version<br>Accepted on Go in RC-004 | [44b1b5e] |

---

## Purpose

Decide whether the repository, the tooling and the documentation skeleton are ready for design and coding: a reproducible Python 3.13 environment, the quality gates, the Docker harness for graphical tests, the README and the wiki skeleton, and the recorded technology decisions.

## Deliverable

A repository on the git host with a description and topics, containing `pyproject.toml`, `.gitignore`, `.editorconfig`, `Doxyfile`, the package skeleton with `constants.py`, a passing smoke test, a local quality gate script that runs opengrep, a Docker harness that captures a screenshot of an empty window, a `README.md` from the framework template, the wiki skeleton in English, Danish and Bahasa Malaysia, and four architecture decision records.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | The repository has a description and at least five topics | The git host API returns both | Either is empty |
| 2 | A fresh `.venv` on Python 3.13 installs the project with `python -m pip install -e ".[dev]"` and the smoke test passes | `pytest` exits 0 | Install or test fails |
| 3 | Doxygen builds the documentation | `doxygen Doxyfile` reports 0 warnings | Any warning |
| 4 | The README and the editor configuration follow the framework | `check-readme.sh` and `check-editorconfig.sh` exit 0 | Either exits non-zero |
| 5 | The local quality gate passes | `scripts/check.sh` exits 0, including the opengrep scan with 0 WARNING or ERROR findings | Any finding or failure |
| 6 | The Docker harness works | The container run exits 0 and writes a screenshot file of an empty window to `docs/screenshots/` | No screenshot or a host desktop was used |
| 7 | The wiki skeleton exists in three languages | `Home`, `Setup` and `_Sidebar` exist, with `-da` and `-ms` variants of the pages | A page of a language is missing |
| 8 | The pull request is open with its closing issue lines and no failing check | Pull request body lists one `Closes #N` per line | A check fails |

## Dependencies

| Depends on | Reason |
| --- | --- |
| None | First gateway; follows the accepted Business Case, Stakeholder Analysis, Project Plan and this milestone |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O2, O3, O5, O6, O7 | [BC-001] |
| Success criteria 3, 7, 8 | [BC-001] |
| US-001.06 (run from the README), US-001.07 (wiki in my language) | [US-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-20 — inside the Business Case window that ends 2026-11-26.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Set repository description and topics | Set a one-sentence description and at least five topics (for example python, tkinter, pillow, watermark, udemy, 100-days-of-code) on the git host through its API, using the repository token from the personal `.env` file without printing or copying it. This gives repository visitors (S03) a clear first impression and meets objective O7. | No | BC-001 O7 |
| 2 | Create pyproject.toml | Declare the project with `requires-python = ">=3.13"`, the `src` layout, Pillow as the only runtime dependency, and an optional `dev` group with pytest, pytest-cov, ruff, mypy and import-linter, plus their configuration. One file configures the whole project, as the Product Owner asked. | No | BC-001 O3, O5 |
| 3 | Add Python .gitignore | Add a Python `.gitignore` that also ignores `.venv`, `.env`, coverage output, Doxygen output and the prompt log folder when the repository is public. This keeps secrets and generated files out of the repository. | No | BC-001 O3 |
| 4 | Add .editorconfig and its check | Create the root `.editorconfig` from the framework baseline and make `check-editorconfig.sh` pass, so every editor formats files the same way. | No | AGENTS.md rule 10 |
| 5 | Create package skeleton and constants.py | Create `src/watermark_image/` with `__init__.py` and `constants.py` (application name, supported image extensions, default font size, default opacity, default margin), and `tests/unit/` with a first test of the constants. All constants live in one module, as the Product Owner asked. | No | BC-001 O2, O3 |
| 6 | Add Doxyfile and Doxygen comment style | Add a `Doxyfile` for Python that reads `src/` and writes to `build/doxygen/`, and define the Doxygen comment style used in source (documentation comments with `@brief`, `@param`, `@return`). A build with no warnings proves the style works. | No | BC-001 O2 |
| 7 | Write README.md from the framework template | Fill the framework README template: overview, requirements, setup with creating a local `.venv` and `python -m pip install --upgrade pip`, run, tests, license and the document appendix. Step screenshots are added by the step gateways. | No | BC-001 O3, O4 |
| 8 | Add local quality gate script with opengrep | Add `scripts/check.sh` that runs pytest, ruff, mypy, import-linter and the opengrep scan (`~/.opengrep/cli/latest/opengrep.exe`), and fails on any finding. It is run before every push, as the Product Owner asked. | No | BC-001 O6 |
| 9 | Add Docker harness for GUI tests and screenshots | Add a Dockerfile and a run script that start the application under a virtual display (Xvfb) in a Linux container, run the graphical tests, and write screenshots to `docs/screenshots/`. This is the GUI test environment required by the framework: the host desktop is never used. | No | framework/process/gui-testing.md |
| 10 | Add wiki skeleton in three languages | Create `docs/wiki/` with `Home`, `Setup` and `_Sidebar`, in English and with `-da` (Danish) and `-ms` (Bahasa Malaysia) variants. Explain what the setup step taught. Check that the wiki is enabled for the repository. | No | BC-001 O4; US-001.07 |
| 11 | Install git hooks | Run the framework's hook installer so commits on `main` are refused and the plan gate is enforced for `src/` and `tests/`, which keeps the one-branch-per-step discipline. | No | BC-001 O6 |
| 12 | Record the technology and process decisions as ADRs | Write four architecture decision records: Tkinter with Pillow and Python 3.13 or newer; layered architecture with MVVM and the assignment's function names; GUI tests and screenshots in Docker; and the artifact types that are skipped, with the reason, together with the Doxygen and wiki conventions. | No | BC-001 Assumptions |
| 13 | Run quality gates and open the pull request for Gateway 1 | Run the local quality gate, record the code review as a review record, commit, resolve pending commit links, push the branch and open the pull request that closes the issues of this gateway. | No | BC-001 O6 |

---

[BC-001]: ../business-case.md
[US-001]: ../user-stories.md
[44b1b5e]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/085-assignment-watermark-image/commit/44b1b5e31086612d7f3fdfb7e709507066247e4a
