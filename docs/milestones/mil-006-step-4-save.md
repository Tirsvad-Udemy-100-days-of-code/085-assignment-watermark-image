# Gateway 6: Step 4, save the result

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-006 |
| CrossReference | [BC-001], [US-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-19 | Accepted | Jens Tirsvad Nielsen | Stand-in for S01 | Initial version<br>Accepted on Go in RC-009 | pending |

---

## Purpose

Decide whether step 4 and the whole project are done: the user saves the watermarked image with `save_image` without overwriting the original, and every success criterion of the Business Case is met and verified.

## Deliverable

An application that saves the watermarked image as JPEG or PNG, with tests, two screenshots (save dialog and saved confirmation) in the README and the wiki, the step 4 wiki page in English, Danish and Bahasa Malaysia, the completed wiki home pages, and a verification of the Business Case success criteria in a clean container.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `save_image` writes JPEG and PNG, converting transparency for JPEG | Tests read the saved files back and compare pixels | A test fails |
| 2 | The original file is never overwritten | A test shows that saving to the original path is refused with a message | The original is overwritten |
| 3 | Save errors (read-only folder, unsupported extension) are reported without a crash | Tests for each error pass | A crash |
| 4 | The code follows the accepted design | The code review record states each class and operation traces to the design class diagram | A deviation is not recorded |
| 5 | Tests and static checks pass | `scripts/check.sh` exits 0, with 0 opengrep WARNING or ERROR findings | Any failure |
| 6 | Coverage of the domain and application layers | At least 85 percent line coverage | Below 85 percent |
| 7 | From a fresh clone to the running application | The README commands, run in a clean container, take at most six commands and the program starts | More commands or a failure |
| 8 | The README and every wiki language show all four steps | At least four screenshots, and 18 wiki pages with their sidebar and language links | A page or image is missing |
| 9 | The wiki follows its checklist | A review record against `QC-WIKI-001` | No-Go |
| 10 | The code review has a Go verdict | A review record against `QC-PY-001` with verdict Go | No-Go |
| 11 | The pull request is open with its closing issue lines and no failing check | Body lists one `Closes #N` per line | A check fails |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-005 | The complete watermark function that the saved result contains |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O1 to O7 | [BC-001] |
| US-001.05 Save the result | [US-001] |
| Success criteria 1 to 9 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-25 — inside the Business Case window that ends 2026-11-26, leaving one day of reserve.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Implement the save_image use case and its port | Write the use case that saves the result through a port, and the rule that the target must not be the original file. Test it with a fake of the port. | Yes | UC-001, US-001.05 |
| 2 | Implement the Pillow image writer | Write the adapter that chooses the format from the file extension, converts transparency to a solid background for JPEG, and turns every write failure into the domain error with the cause kept. Test it with files in a temporary folder. | Yes | UC-001, US-001.05 |
| 3 | Add the save control to the window | Add a "Save image" button with a file dialog and a status message for success and failure, and the matching view model commands. | Yes | UC-001, US-001.05 |
| 4 | Test the window and capture screenshots in Docker | Extend the graphical test in the Docker harness to save a result and write `step-4-save.png` and `step-4-saved.png`. No host desktop is used. The environment is a Docker container (Linux). | Yes | UC-001, framework/process/gui-testing.md |
| 5 | Complete the README | Add the step 4 section and screenshots, and make the README the single place that shows the four steps in order, with the final run and test instructions. | No | BC-001 O3, O4 |
| 6 | Write the step 4 wiki pages and complete the wiki | Write `Step-4-Save` in three languages with the screenshots and a section on what step 4 taught (ports at both ends, protecting the original, error handling). Complete the home pages and sidebar, and review the wiki against its checklist. | No | BC-001 O4; US-001.07 |
| 7 | Verify the success criteria in a clean container | Clone the repository into a clean container, follow only the README, and record the result for each success criterion of the Business Case. | No | BC-001 Success Criteria |
| 8 | Run quality gates, code review and open the pull request for Gateway 6 | Run the local quality gate, review the code against the Python checklist and record it, resolve pending commit links, push the branch and open the pull request that closes the issues of this gateway. | No | BC-001 O6 |

---

[BC-001]: ../business-case.md
[US-001]: ../user-stories.md
