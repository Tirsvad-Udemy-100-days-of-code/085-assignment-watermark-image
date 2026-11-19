# Use Case UC-001: Watermark an image

## Metadata
| Key | Value |
| --- | --- |
| ID | UC-001 |
| CrossReference | [UCD-001], [US-001], [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | Stand-in for S01 | Initial version<br>Accepted on Go in RC-017 | pending |

---

## Format and Level

Format: Fully Dressed. Level: user-goal.

## Scope

The Watermark Image Desktop App, seen as a black box.

## Primary Actor

User (S01, S02), as named in [UCD-001].

## Stakeholders and Interests

- S01 wants a correct, reviewable solution of the assignment: the original picture is never changed.
- S02 wants the three assignment functions, `upload_image`, `add_watermark` and `save_image`, to be easy to find and follow.
- S03 wants a result that can be seen at a glance in the screenshots.

## Preconditions

The application is running and shows an empty window. Python 3.13 or newer and the project's dependency are installed.

## Postconditions (Success Guarantee)

A new picture file exists that shows the chosen picture with the chosen watermark at the chosen place and visibility. The original picture file is unchanged.

## Main Success Scenario

1. The User asks to upload a picture and names a picture file.
2. The system shows the picture.
3. The User asks to add a watermark and gives the watermark: a text with its size and colour, or a logo picture with its size, together with a place on the picture and a visibility.
4. The system shows the picture with the watermark laid over it.
5. The User repeats step 3 until satisfied.
6. The User asks to save the result and names a new picture file.
7. The system keeps the marked picture under that name and confirms it.

## Extensions

- 2a. The file is not a readable picture: the system says so and keeps the previous picture. The scenario continues at step 1.
- 3a. The text is empty, the size is below 1, the logo size is outside 1 to 100 percent or the visibility is outside 0 to 100: the system says what is wrong and shows the picture as before. The scenario continues at step 3.
- 3b. The logo file is not a readable picture: the system says so and shows the picture as before. The scenario continues at step 3.
- 6a. The User names the original picture file: the system refuses, says why and changes nothing. The scenario continues at step 6.
- 6b. The file name does not end in .jpg, .jpeg or .png, or the file cannot be written: the system says why and keeps the marked picture. The scenario continues at step 6.

## Special Requirements and Business Rules

- Step 2: the picture is scaled to fit the display; supported formats are JPEG, PNG, BMP, GIF and WebP (BC-001 scope).
- Step 3: nine places (corners, edge middles and centre) with a margin from the edge; visibility 0 to 100 percent; logo size 1 to 100 percent of the picture width.
- Step 4: a watermark never changes the original picture.
- Step 7: a transparent logo lets the picture show through; JPEG has no transparency, so a solid background is used.
- The screen design is in the wireframe `wireframe.md` of this folder.

## Open Issues

None.

---

[UCD-001]: ../../use-case-diagram.md
[US-001]: ../../user-stories.md
[SA-001]: ../../stakeholder-analysis.md
