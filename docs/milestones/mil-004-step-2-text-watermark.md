# Gateway 4: Step 2, text watermark

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-004 |
| CrossReference | [BC-001], [US-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-19 | Accepted | Jens Tirsvad Nielsen | Stand-in for S01 | Initial version<br>Accepted on Go in RC-007 | [44b1b5e] |

---

## Purpose

Decide whether step 2 is done: the user types a text, chooses its size, colour, position and opacity, and `add_watermark` shows the watermarked image in the preview without changing the original.

## Deliverable

An application that adds a text watermark with a nine-position grid and an opacity control, with unit, integration and graphical tests, two screenshots (text typed, watermark placed) in the README and the wiki, and the step 2 wiki page in English, Danish and Bahasa Malaysia.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `add_watermark` draws the text at each of the nine positions with the chosen opacity | Tests compare the pixels of a known image at each position and at opacity 0 and 100 | A test fails |
| 2 | Invalid input is refused | Empty text, size below 1 and opacity outside 0 to 100 raise the domain error and the window shows a message | A case is accepted |
| 3 | The original image object and file are unchanged | A test compares the original before and after | The original changes |
| 4 | The code follows the accepted design | The code review record states each class and operation traces to the design class diagram | A deviation is not recorded |
| 5 | Tests and static checks pass | `scripts/check.sh` exits 0, with 0 opengrep WARNING or ERROR findings | Any failure |
| 6 | Two screenshots exist and are used | `docs/screenshots/step-2-*.png` are linked from `README.md` and from the three step 2 wiki pages | A link or language is missing |
| 7 | The code review has a Go verdict | A review record against `QC-PY-001` with verdict Go | No-Go |
| 8 | The pull request is open with its closing issue lines and no failing check | Body lists one `Closes #N` per line | A check fails |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-003 | The window, the upload and the view model that this step extends |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O1, O2, O4 | [BC-001] |
| US-001.02 Add a text watermark, US-001.03 Place and fade the watermark | [US-001] |
| Success criteria 1, 2, 5, 6 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-23 — inside the Business Case window that ends 2026-11-26.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Implement the watermark domain model | Write the text watermark, the position and the opacity as immutable value objects that validate themselves (non-empty text, size of at least 1, opacity from 0 to 100). Test every rule without any library or window. | Yes | UC-001, US-001.02, US-001.03 |
| 2 | Implement the add_watermark use case | Write the use case that takes the loaded image and a watermark and returns a new image, with the port for the compositor. Test it with a fake of the port. | Yes | UC-001, US-001.02 |
| 3 | Implement the Pillow text compositor | Draw the text on a transparent layer and blend it onto a copy of the image with the chosen opacity at one of nine positions with a margin from `constants.py`. Test the result against known pixels. | Yes | UC-001, US-001.02, US-001.03 |
| 4 | Add text and placement controls to the window | Add a text field, size and colour controls, a nine-position selector and an opacity slider to the window and the view model, with the preview updated when a control changes and a message for invalid input. | Yes | UC-001, US-001.02, US-001.03 |
| 5 | Test the window and capture screenshots in Docker | Extend the graphical test in the Docker harness to type a text, place it and write `step-2-text.png` and `step-2-placed.png`. No host desktop is used. The environment is a Docker container (Linux). | Yes | UC-001, framework/process/gui-testing.md |
| 6 | Update the README for step 2 | Add the step 2 section with both screenshots and a short description of the controls. | No | BC-001 O4 |
| 7 | Write the step 2 wiki pages in three languages | Write `Step-2-Text-Watermark`, `Step-2-Text-Watermark-da` and `Step-2-Text-Watermark-ms` with the screenshots and a section on what step 2 taught (value objects that validate themselves, alpha blending, never changing the original). Update the sidebar. | No | BC-001 O4; US-001.07 |
| 8 | Run quality gates, code review and open the pull request for Gateway 4 | Run the local quality gate, review the code against the Python checklist and record it, resolve pending commit links, push the branch and open the pull request that closes the issues of this gateway. | No | BC-001 O6 |

---

[BC-001]: ../business-case.md
[US-001]: ../user-stories.md
[44b1b5e]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/085-assignment-watermark-image/commit/44b1b5e31086612d7f3fdfb7e709507066247e4a
