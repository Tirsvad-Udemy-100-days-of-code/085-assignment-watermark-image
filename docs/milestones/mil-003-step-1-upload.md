# Gateway 3: Step 1, window and image upload

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-003 |
| CrossReference | [BC-001], [US-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-19 | Accepted | Jens Tirsvad Nielsen | Stand-in for S01 | Initial version<br>Accepted on Go in RC-006 | [44b1b5e] |

---

## Purpose

Decide whether step 1 is done: the application opens a window, the user uploads an image with `upload_image`, and sees it scaled to fit the preview area.

## Deliverable

A running application that uploads JPEG, PNG, BMP, GIF and WebP images and shows them in the preview, with unit, integration and graphical tests, two screenshots (empty window and loaded image) in the README and the wiki, and the step 1 wiki page in English, Danish and Bahasa Malaysia.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `python -m watermark_image` opens the main window | The container graphical test exits 0 | The window does not open |
| 2 | `upload_image` loads each supported format and rejects an unreadable file with a clear message | Tests for each format and for a corrupt file pass | A test fails |
| 3 | The code follows the accepted design | The code review record states each class and operation traces to the design class diagram | A deviation is not recorded |
| 4 | Tests and static checks pass | `scripts/check.sh` exits 0, with 0 opengrep WARNING or ERROR findings | Any failure |
| 5 | Two screenshots exist and are used | `docs/screenshots/step-1-*.png` are linked from `README.md` and from the three step 1 wiki pages | A link or language is missing |
| 6 | The code review has a Go verdict | A review record against `QC-PY-001` with verdict Go | No-Go |
| 7 | The pull request is open with its closing issue lines and no failing check | Body lists one `Closes #N` per line | A check fails |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-002 | The code is written from the accepted design artifacts |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O1, O2, O4 | [BC-001] |
| US-001.01 Upload an image | [US-001] |
| Success criteria 1, 2, 5, 6 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-22 — inside the Business Case window that ends 2026-11-26.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Implement the domain and the upload use case | Write the image entity and the domain error for an unreadable image, and the `upload_image` use case with the port it needs to read an image. Test the use case with a fake of the port, so no file or window is involved. | Yes | UC-001, US-001.01 |
| 2 | Implement the Pillow image reader | Write the adapter that reads JPEG, PNG, BMP, GIF and WebP files with Pillow and turns every Pillow failure into the domain error with the original cause kept. Test it against real files created in a temporary folder. | Yes | UC-001, US-001.01 |
| 3 | Implement the main window and view model | Write the Tkinter main window with an "Upload image" button and a preview area that scales the image to fit, and its view model that calls the use case. The view holds no rule, as the MVVM pattern requires. Test the view model without a window. | Yes | UC-001, US-001.01 |
| 4 | Add the composition root and entry point | Wire the layers once in one place and start the application with `python -m watermark_image`. | No | ADR-0002 |
| 5 | Test the window and capture screenshots in Docker | Run a graphical test in the Docker harness that opens the window, loads a sample image and writes two screenshots, `step-1-empty.png` and `step-1-loaded.png`, to `docs/screenshots/`. No host desktop is used. The environment is a Docker container (Linux). | Yes | UC-001, framework/process/gui-testing.md |
| 6 | Update the README for step 1 | Add the step 1 section with both screenshots and the command to run the program, and keep the table of contents current. | No | BC-001 O4 |
| 7 | Write the step 1 wiki pages in three languages | Write `Step-1-Upload`, `Step-1-Upload-da` and `Step-1-Upload-ms` with the screenshots and a section on what step 1 taught (a layered design, a port with a fake, a view that holds no rule). Add them to the sidebar. | No | BC-001 O4; US-001.07 |
| 8 | Run quality gates, code review and open the pull request for Gateway 3 | Run the local quality gate, review the code against the Python checklist and record it, resolve pending commit links, push the branch and open the pull request that closes the issues of this gateway. | No | BC-001 O6 |

---

[BC-001]: ../business-case.md
[US-001]: ../user-stories.md
[44b1b5e]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/085-assignment-watermark-image/commit/44b1b5e31086612d7f3fdfb7e709507066247e4a
