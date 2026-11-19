# Business Case: Watermark Image Desktop App

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | [SA-001], [UCD-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-19 | Deprecated | Jens Tirsvad Nielsen | Stand-in for S01 | Initial version<br>Accepted on Go in RC-001 | [44b1b5e] |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | Stand-in for S01 | CrossReference adds UCD-001 (metadata only)<br>Accepted on Go in RC-019 | pending |

---

## Executive Summary

This project builds the Day 85 assignment of the Udemy course "100 Days of Code: The Complete Python Pro Bootcamp": a desktop program in which a user uploads an image, adds a watermark (text or logo) and saves the result. The product is a small, readable Python 3.13 application with a graphical user interface, a pytest suite, Doxygen-documented source, and a repository that other course participants and visitors can read, run and learn from. Each build step is shown with a screenshot in the README and explained in a wiki in English, Danish and Bahasa Malaysia. The work is scoped to one week, needs one runtime dependency (Pillow), and costs only the Product Owner's time. The recommendation is to proceed.

## Methodological and Standards Foundation

- Methodology: Larman, *Applying UML and Patterns* (use cases, domain model, system sequence diagram, operation contracts, sequence diagram, design class diagram), as set out in the framework's artifact catalog.
- Quality standard: ISO/IEC 25010:2023 characteristics tag every quality criterion used in reviews.
- Architecture: Clean Architecture layers (`domain`, `application`, `adapters`, `infrastructure`, `presentation`) with the Model-View-ViewModel (MVVM) pattern for the user interface, as the framework's `clean-architecture` skill defines.
- Process: plan-first gate; one branch and one pull request per milestone; every artifact reviewed against its checklist and recorded as an `RC-*` review record.

## Problem Statement

The course assignment says only "a desktop program where you can upload images and add a watermark". Participants who solve it publish code that is hard to run on another machine: no stated Python version, no virtual environment instructions, no tests, no screenshots, and names that differ from the assignment. A participant comparing solutions cannot see which step produced which behaviour, and a visitor cannot tell within a minute whether the repository is worth reading.

## Business Opportunity

A single, well-documented reference solution lets the Product Owner (S01) show a complete, reproducible piece of work, lets course participants (S02) compare their own solution with a runnable one, and lets visitors (S03) judge the repository quickly from its description, topics, README and screenshots. The three-language wiki also serves as a worked example of documenting a learning project in more than one language.

## Objectives

| ID | Objective |
| --- | --- |
| O1 | Deliver a desktop application that uploads an image, adds a text or logo watermark with a chosen position and opacity, and saves the watermarked image without changing the original file. |
| O2 | Provide the assignment's function names (`upload_image`, `add_watermark`, `save_image`) in readable code with Doxygen comments and a `Doxyfile`. |
| O3 | Make the project reproducible: Python 3.13 or newer, a local `.venv`, `pyproject.toml`, pytest tests, constants kept in `constants.py`. |
| O4 | Show every build step with a screenshot in the `README.md` and in the wiki, and explain in the wiki, in English, Danish and Bahasa Malaysia, what each step taught. |
| O5 | Keep runtime dependencies to those the assignment needs (one: Pillow). |
| O6 | Pass the local quality gates (tests, linter, type checker, opengrep scan) before every push, and track the steps as branches and pull requests. |
| O7 | Publish a clear repository description and topics on the git host. |

## Scope

### In Scope

- A Tkinter desktop application with the steps: window and image upload, text watermark with position and opacity, logo watermark, save.
- Pillow as the only runtime dependency; development tools (pytest, ruff, mypy, import-linter, coverage) as optional development dependencies.
- `pyproject.toml`, Python `.gitignore`, `.editorconfig`, `Doxyfile`, `constants.py`, `tests/`.
- `README.md` from the framework template, with `.venv` and `python -m pip install --upgrade pip` instructions, run and test instructions, and one screenshot per build step.
- A wiki in `docs/wiki/` in English, Danish and Bahasa Malaysia: one page per build step with the screenshot and the learning gained.
- Screenshots produced in a Docker container (virtual display), never on the host desktop.
- Repository description and topics on the git host.
- Project documents of the framework: Business Case, Stakeholder Analysis, user stories, Project Plan, milestones, one use case with its design artifacts, domain dictionary, traceability matrix, review records and architecture decision records.

### Out of Scope

- Batch watermarking of many images, undo history, watermark templates, and drag-and-drop placement.
- A command-line interface, a web interface, and installers or packaged executables.
- A GitHub mirror and any release or package publication.
- Support for Python versions older than 3.13.
- Image formats beyond those Pillow reads and writes by default (JPEG, PNG, BMP, GIF, WebP are tested; others are not promised).

## Expected Benefits

### Tangible Benefits

- A runnable repository: from a fresh clone to the running application in six commands or fewer.
- A test suite and quality gates that anyone can run locally.
- Eighteen wiki pages (six pages in each of three languages) and a screenshot for each build step.

### Intangible Benefits

- A reference solution that course participants can compare with their own.
- Practice in the framework's plan, design, review and pull request workflow on a small project.
- A documented example of keeping a learning project readable for visitors.

## Strategic Alignment

The project supports the Product Owner's goal of completing the 100 Days of Code course with work that is reproducible and reviewable, and of keeping every project of the course under the same framework, folder structure (`src/`, `tests/`, `docs/`) and review discipline.

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| 1 | The application performs upload, watermark and save | All three functions work for JPEG and PNG, verified by tests | `pytest` exits 0 and the GUI test in the container exits 0 |
| 2 | Unit test coverage of the domain and application layers | At least 85 % line coverage | `pytest --cov` report |
| 3 | Number of runtime dependencies | Exactly 1 (Pillow) | `[project] dependencies` in `pyproject.toml` |
| 4 | Time from fresh clone to running application | At most 6 commands, verified in a clean container | The command list in the README, run once per release |
| 5 | Screenshots | At least one per build step (four), in the README and in every wiki language | Count of image links in `README.md` and `docs/wiki/` |
| 6 | Wiki pages | 18 (Home, Setup and four step pages in each of en, da, ms) | File count in `docs/wiki/` |
| 7 | Static analysis | 0 findings of severity WARNING or ERROR in the opengrep scan before each push | Scan output recorded in each pull request |
| 8 | Repository metadata | A description and at least five topics set | Repository settings on the git host |
| 9 | Step tracking | One merged pull request per milestone (six) | Pull request list of the repository |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| A graphical interface cannot be tested on the host desktop without taking the user's mouse and keyboard | Untested interface code | GUI tests and screenshots run in a Docker container with a virtual display, as `framework/process/gui-testing.md` requires; view-model logic is tested without a window |
| Screenshots from a Linux container look different from the Windows host | Visitors expect a different look | The README states that screenshots come from a Linux container |
| Danish and Bahasa Malaysia text contains errors | Misleading wiki pages | Short sentences, a glossary of fixed terms per language, and a native-reader check by the Product Owner recorded as a pending condition on the review |
| The git host's wiki is disabled or the token lacks scope | Wiki not published | Check the repository settings and token scope in milestone 1; report instead of working around |
| Scope grows beyond the assignment | Plan slips | The Out of Scope list; a change needs a new Version History row and a review |
| The opengrep rules cannot be fetched or are noisy | Gate cannot run or blocks | Use a rule set stored in the repository if the registry is unreachable; record every suppression with its reason |
| Pillow has no wheel for the chosen Python version | Installation fails | Test the install in a clean container on the declared Python version before each pull request |

## Assumptions

- The Product Owner is S01; S01 also develops and reviews. In autonomous mode the reviewer role is held by a stand-in, and each review record says so.
- S02 and S03 are not consulted; their concerns are inferred from the Product Owner's description.
- "Python greater than 3.13" is read as "3.13 or newer" (`requires-python = ">=3.13"`); Python 3.13.14 is installed on the development machine.
- S03's wish for no runtime dependencies is read as "no dependency that the assignment does not need". Tkinter reads only PNG and GIF and cannot composite with transparency, so Pillow is needed for JPEG support and for the watermark itself.
- The git host repository already exists and its `main` branch holds the initial commit.
- Docker is available on the development machine for GUI tests and screenshots.
- The git host repository name follows the existing `origin` remote (`Tirsvad-Udemy-100-days-of-code/085-assignment-watermark-image`), not the underscore spelling in the first prompt.

## Constraints

- Time window: 2026-11-19 to 2026-11-26. No deadline was given; the window is set by the author and is for the Product Owner to confirm or change.
- Python 3.13 or newer, a local `.venv`, pytest, constants in `constants.py`, configuration in `pyproject.toml`.
- Folder structure `src/`, `tests/`, `docs/`.
- Product Owner language English, domain IT; the wiki also exists in Danish and Bahasa Malaysia.
- Tokens come from the personal `.env` file, which is never imported into, tested by or committed to the project.
- No artifact names the tooling that produced it (Product Owner instruction).
- Source files carry Doxygen comments; a `Doxyfile` is part of the project.
- opengrep (`~\.opengrep\cli\latest\opengrep.exe`) is run locally before every push.
- Branches and pull requests track the steps; a reviewer merges.

## Cost–Benefit Assessment

The assessment is qualitative: the project has no revenue, no purchases and no licences, so a money figure would be invented. The cost is measured in effort.

| Costs | Benefits |
| --- | --- |
| About six working sessions of the Product Owner's time within the one-week window | A complete reference solution of the assignment |
| Review time for each artifact and pull request | A repository that others can run and learn from in minutes |
| Maintaining three wiki languages | Reusable documentation practice for the other course projects |
| One runtime dependency (Pillow) to keep installable | JPEG support and correct transparency handling that the standard library cannot provide |

## Stakeholders

| Stakeholder ID (SA) | Interest in this project |
| --- | --- |
| [S01] | Product Owner, developer and reviewer: a complete, reviewable solution |
| [S02] | Udemy course participants: readable, runnable code with the assignment's function names and clear run instructions |
| [S03] | Repository visitors: a clear description, topics and README, and no dependency beyond what is needed |

## Recommendation

Proceed — the scope is small and well bounded, the risks have mitigations, and the only recurring cost is the Product Owner's time.

---

[UCD-001]: use-case-diagram.md
[SA-001]: ./stakeholder-analysis.md
[S01]: ./stakeholder-analysis.md#stakeholder-summary-table
[S02]: ./stakeholder-analysis.md#stakeholder-summary-table
[S03]: ./stakeholder-analysis.md#stakeholder-summary-table
[44b1b5e]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/085-assignment-watermark-image/commit/44b1b5e31086612d7f3fdfb7e709507066247e4a
