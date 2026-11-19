# Operation Contracts: UC-001 Watermark an image

## Metadata
| Key | Value |
| --- | --- |
| ID | OC-001 |
| CrossReference | [SSD-001], [DM-002], [DICT-001], [SSD-001], [DICT-001], [DM-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | Stand-in for S01 | Initial version<br>Accepted on Go in RC-024 | pending |

---

Terms are the IT terms of [DICT-001]. The affected concepts are those of [DM-001]. The contracts trace to the messages of [SSD-001].

## Operation: upload_image

**Signature:** `upload_image(source: ImageFile) -> ImageView`

**Cross References:** SSD-001 message `upload_image`; use case step 1 and 2; concepts Image.

**Preconditions:**
- None: the operation can run in any state.

**Postconditions:**
- An Image instance was created from the picture file, with its width and height.
- Any earlier Image and any WatermarkedImage were dropped.
- The returned ImageView shows the new Image.

**Exceptions:**
- The file is not a readable picture: no instance is created, the earlier Image and WatermarkedImage stay as they were, and the message says so (UC-001 extension 2a).

## Operation: add_watermark

**Signature:** `add_watermark(request: WatermarkRequest) -> ImageView`

**Cross References:** SSD-001 message `add_watermark`; use case steps 3, 4 and 5; concepts Image, Watermark, TextWatermark, LogoWatermark, Position, WatermarkedImage.

**Preconditions:**
- An Image exists (an `upload_image` has completed).
- The request holds either a TextWatermark with Text, size and colour, or a LogoWatermark with a logo Image and size; and an Anchor and an Opacity.

**Postconditions:**
- A Watermark instance was created from the request and associated with a Position that has the given Anchor.
- A WatermarkedImage instance was created, associated with the Image and with the Watermark, and any earlier WatermarkedImage was dropped.
- The Image was not modified.
- The returned ImageView shows the WatermarkedImage.

**Exceptions:**
- No Image exists: nothing changes and the message asks for an upload first.
- The Text is empty, the size is below 1, the logo size is outside 1 to 100 percent or the Opacity is outside 0 to 100: nothing changes and the message says what is wrong (extension 3a).
- The logo file is not a readable picture: nothing changes and the message says so (extension 3b).

## Operation: save_image

**Signature:** `save_image(target: ImageFile) -> Confirmation`

**Cross References:** SSD-001 message `save_image`; use case steps 6 and 7; concepts Image, WatermarkedImage.

**Preconditions:**
- A WatermarkedImage exists (an `add_watermark` has completed).
- The target names a file other than the file the Image came from, and its ending is `.jpg`, `.jpeg` or `.png`.

**Postconditions:**
- The WatermarkedImage was stored under the target name.
- The Image and the WatermarkedImage were not modified.
- The returned Confirmation holds the target name.

**Exceptions:**
- No WatermarkedImage exists: nothing is stored and the message says so.
- The target is the file of the Image: nothing is stored and the message says why (extension 6a).
- The ending is not supported or the file cannot be written: nothing is stored, the WatermarkedImage is kept and the message says why (extension 6b).

---

---

[SSD-001]: ./ssd.md
[DM-002]: ../../domain-model.md
[DICT-001]: ../../dictionary.md
[SSD-001]: ./ssd.md
[DICT-001]: ../../dictionary.md
[DM-001]: ./dm.md
