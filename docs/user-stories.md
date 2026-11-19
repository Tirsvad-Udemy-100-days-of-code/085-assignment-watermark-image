# User Stories: Watermark Image Desktop App

## Metadata
| Key | Value |
| --- | --- |
| ID | US-001 |
| CrossReference | [BC-001], [MIL-003], [MIL-004], [MIL-005], [MIL-006] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-19 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | [44b1b5e] |

---

## Purpose and Scope

The stories cover the epic "Watermark an image" of [BC-001]: the four build steps of the application, and two stories about reading and running the repository. The actor of the application stories is the user of the program, who is S01 and any participant (S02) who runs the code; the actor is named `User` in the use case diagram that gateway 2 creates. One use case, UC-001, is expected to cover stories US-001.01 to US-001.05. Stories US-001.06 and US-001.07 are not goals of an actor of the system; they stay plain tasks.

## Story List

### US-001.01 — Upload an image

**As a** User, **I want** to upload an image from my computer and see it in the window, **so that** I can choose the picture I want to watermark.

**Acceptance Criteria**

- Given the window is open, when I choose a JPEG, PNG, BMP, GIF or WebP file, then the image appears scaled to fit the preview area.
- Given the window is open, when I choose a file that is not a readable image, then a message tells me so and the previous image stays.

| Traces to | Size | INVEST exceptions | Priority (MoSCoW) | Reason |
| --- | --- | --- | --- | --- |
| [MIL-003] | fits one iteration | none | Must | Every other story needs a loaded image (dependency) |

### US-001.02 — Add a text watermark

**As a** User, **I want** to type a text and have it drawn on the image, **so that** the picture shows who it belongs to.

**Acceptance Criteria**

- Given an image is loaded, when I type a text and confirm, then the preview shows the text on the image.
- Given an image is loaded, when the text is empty, then a message tells me and the image is unchanged.
- Given a watermark was added, then the original file and the original image are unchanged.

| Traces to | Size | INVEST exceptions | Priority (MoSCoW) | Reason |
| --- | --- | --- | --- | --- |
| [MIL-004] | fits one iteration | none | Must | Core goal of the assignment (BC-001 O1) |

### US-001.03 — Place and fade the watermark

**As a** User, **I want** to choose where the watermark goes and how transparent it is, **so that** it is visible without hiding the picture.

**Acceptance Criteria**

- Given a watermark exists, when I choose one of nine positions, then the watermark moves to that position with a margin from the edge.
- Given a watermark exists, when I set the opacity from 0 to 100, then the watermark is as visible as the value says.

| Traces to | Size | INVEST exceptions | Priority (MoSCoW) | Reason |
| --- | --- | --- | --- | --- |
| [MIL-004] | fits one iteration | Not independent of US-001.02 (shares its control), accepted because both ship in one gateway | Must | A watermark that cannot be placed or faded is not usable |

### US-001.04 — Add a logo watermark

**As a** User, **I want** to use a logo image as the watermark and choose its size, **so that** my brand mark can be used instead of text.

**Acceptance Criteria**

- Given an image is loaded, when I choose a logo and a scale from 1 to 100 percent, then the preview shows the logo at that size.
- Given the logo has transparent areas, then the image shows through them.
- Given the file is not a readable image, then a message tells me and the watermark is unchanged.

| Traces to | Size | INVEST exceptions | Priority (MoSCoW) | Reason |
| --- | --- | --- | --- | --- |
| [MIL-005] | fits one iteration | none | Should | Many watermarks are logos, but the text watermark already meets the assignment |

### US-001.05 — Save the result

**As a** User, **I want** to save the watermarked image to a new file, **so that** I can share it and keep the original.

**Acceptance Criteria**

- Given a watermarked image, when I choose a new file name ending in .jpg or .png, then the file is written and a message confirms it.
- Given I choose the original file, then the save is refused with a message and the original is unchanged.
- Given the target cannot be written, then a message gives the reason and the program keeps running.

| Traces to | Size | INVEST exceptions | Priority (MoSCoW) | Reason |
| --- | --- | --- | --- | --- |
| [MIL-006] | fits one iteration | none | Must | Without saving the watermark has no value outside the window |

### US-001.06 — Run the project from the README

**As a** course participant (S02), **I want** step-by-step instructions to create a local `.venv`, upgrade pip, install, run and test the project, **so that** I can run the solution on my own machine.

**Acceptance Criteria**

- Given a fresh clone and Python 3.13 or newer, when I follow only the README, then the program starts in at most six commands.
- Given the same state, when I run the test command in the README, then the tests pass.

| Traces to | Size | INVEST exceptions | Priority (MoSCoW) | Reason |
| --- | --- | --- | --- | --- |
| [MIL-001] documentation task, completed in [MIL-006] | fits one iteration | Not a goal of an actor of the system; a plain task | Must | Required by the Product Owner and by S02's concern CN-005 |

### US-001.07 — Read what each step taught, in my language

**As a** visitor (S03) or participant (S02), **I want** a wiki page for each build step with a screenshot and what the step taught, in English, Danish or Bahasa Malaysia, **so that** I can follow the build and learn from it.

**Acceptance Criteria**

- Given the wiki, when I open a step page in any of the three languages, then it shows the step's screenshot and a section on what was gained.
- Given a page, then a language line links to the same page in the other two languages.

| Traces to | Size | INVEST exceptions | Priority (MoSCoW) | Reason |
| --- | --- | --- | --- | --- |
| [MIL-001], [MIL-003] to [MIL-006] | fits one iteration per step | Not a goal of an actor of the system; plain tasks | Must | Required by the Product Owner; serves CN-003 and CN-006 |

## INVEST Check

Independent: US-001.01 is first; US-001.03 depends on US-001.02 and US-001.04 and US-001.05 on the loaded image, so the order follows the gateways. Negotiable: the acceptance criteria state outcomes, not widgets. Valuable: each story names a benefit. Estimable and Small: each fits one gateway of one day. Testable: each acceptance criterion is a given/when/then that a test can check. One exception (US-001.03 is not independent of US-001.02) is stated in its row.

---

[BC-001]: ./business-case.md
[MIL-001]: ./milestones/mil-001-project-setup.md
[MIL-003]: ./milestones/mil-003-step-1-upload.md
[MIL-004]: ./milestones/mil-004-step-2-text-watermark.md
[MIL-005]: ./milestones/mil-005-step-3-logo-watermark.md
[MIL-006]: ./milestones/mil-006-step-4-save.md
[44b1b5e]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/085-assignment-watermark-image/commit/44b1b5e31086612d7f3fdfb7e709507066247e4a
