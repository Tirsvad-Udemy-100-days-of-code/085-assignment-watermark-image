# Gateway 5: Step 3, logo watermark

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-005 |
| CrossReference | [BC-001], [US-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-19 | Accepted | Jens Tirsvad Nielsen | Stand-in for S01 | Initial version<br>Accepted on Go in RC-008 | pending |

---

## Purpose

Decide whether step 3 is done: the user chooses a logo image, scales it, places it and sets its opacity, and `add_watermark` shows the result, using the same placement and opacity controls as the text watermark.

## Deliverable

An application that adds a logo watermark (including a PNG with transparency) with scale, position and opacity, with unit, integration and graphical tests, two screenshots (logo chosen, logo placed) in the README and the wiki, and the step 3 wiki page in English, Danish and Bahasa Malaysia.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `add_watermark` places a logo at each of the nine positions with the chosen scale and opacity | Tests compare pixels of a known image and a known logo, including a logo with transparency | A test fails |
| 2 | A logo that cannot be read, or a scale outside 1 to 100 percent, is refused | The domain error is raised and the window shows a message | A case is accepted |
| 3 | The text and logo watermark share one placement and opacity implementation | The code review record shows no duplicated placement code | Duplicated rule |
| 4 | The code follows the accepted design | The code review record states each class and operation traces to the design class diagram | A deviation is not recorded |
| 5 | Tests and static checks pass | `scripts/check.sh` exits 0, with 0 opengrep WARNING or ERROR findings | Any failure |
| 6 | Two screenshots exist and are used | `docs/screenshots/step-3-*.png` are linked from `README.md` and from the three step 3 wiki pages | A link or language is missing |
| 7 | The code review has a Go verdict | A review record against `QC-PY-001` with verdict Go | No-Go |
| 8 | The pull request is open with its closing issue lines and no failing check | Body lists one `Closes #N` per line | A check fails |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-004 | The watermark model, the placement and opacity logic and the controls that this step reuses |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O1, O2, O4 | [BC-001] |
| US-001.04 Add a logo watermark | [US-001] |
| Success criteria 1, 2, 5, 6 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-24 — inside the Business Case window that ends 2026-11-26.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Extend the domain with the logo watermark | Add the logo watermark as a value object with a scale of 1 to 100 percent, next to the text watermark, and share the position and opacity rules. Test the new rules without any library or window. | Yes | UC-001, US-001.04 |
| 2 | Extend add_watermark and the Pillow compositor for logos | Scale the logo with high-quality resampling, keep its transparency, and blend it with the chosen opacity at one of nine positions, reusing the placement code of the text watermark. Test against known pixels. | Yes | UC-001, US-001.04 |
| 3 | Add logo controls to the window | Add a "Choose logo" button, a scale slider and a watermark-type switch to the window and the view model, reusing the position and opacity controls, with a message when the logo cannot be read. | Yes | UC-001, US-001.04 |
| 4 | Test the window and capture screenshots in Docker | Extend the graphical test in the Docker harness to choose a logo, place it and write `step-3-logo.png` and `step-3-placed.png`. No host desktop is used. The environment is a Docker container (Linux). | Yes | UC-001, framework/process/gui-testing.md |
| 5 | Update the README for step 3 | Add the step 3 section with both screenshots and a short description of the logo controls. | No | BC-001 O4 |
| 6 | Write the step 3 wiki pages in three languages | Write `Step-3-Logo-Watermark`, `Step-3-Logo-Watermark-da` and `Step-3-Logo-Watermark-ms` with the screenshots and a section on what step 3 taught (extending by adding a type instead of editing branches, resampling, transparency). Update the sidebar. | No | BC-001 O4; US-001.07 |
| 7 | Run quality gates, code review and open the pull request for Gateway 5 | Run the local quality gate, review the code against the Python checklist and record it, resolve pending commit links, push the branch and open the pull request that closes the issues of this gateway. | No | BC-001 O6 |

---

[BC-001]: ../business-case.md
[US-001]: ../user-stories.md
