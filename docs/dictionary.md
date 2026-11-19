# Domain Dictionary: Watermark Image

## Metadata
| Key | Value |
| --- | --- |
| ID | DICT-001 |
| CrossReference | [BC-001], [SA-001], [DM-002] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | Stand-in for S01 | Initial version<br>Accepted on Go in RC-023 | [2a87378] |

---

## Purpose and Scope

The Product Owner's language is English (`en`) and the domain is `it`, as the [registry][REG] says. The dictionary pairs each word of the Domain Model [DM-002] with the professional IT word used in the design artifacts, and fixes the assignment's function names in step with them. It covers every concept and the attributes that have an IT word of their own.

## Dictionary

| PO term | Language | IT term | Definition | Used as PO term in | Used as IT term in |
| --- | --- | --- | --- | --- | --- |
| Logo mark | en | LogoWatermark | A watermark made from a small picture, such as a brand symbol. | DM, UC | OC, SD, DCD |
| Marked picture | en | WatermarkedImage | A picture with a watermark laid over it, kept apart from the original picture. | DM, UC | OC, SD, DCD |
| Picture | en | Image | A photograph or drawing that a person owns and wants to mark. | DM, UC | OC, SD, DCD |
| Place | en | Anchor | The spot on a picture, such as a corner or the centre, that a placement names. | DM, UC | OC, SD, DCD |
| Placement | en | Position | The spot on a picture where a watermark sits. | DM, UC | OC, SD, DCD |
| Text mark | en | TextWatermark | A watermark made of words. | DM, UC | OC, SD, DCD |
| Visibility | en | Opacity | How strongly a watermark shows over the picture, from 0 to 100 percent. | DM, UC | OC, SD, DCD |
| Watermark | en | Watermark | A mark laid over a picture to show who it belongs to. | DM, UC | OC, SD, DCD |
| Wording | en | Text | The words of a text mark. | DM, UC | OC, SD, DCD |

## Rules

- The PO term is used in the Domain Model, the use cases and the user stories; the IT term is used in the Operation Contract, the Sequence Diagram and the Design Class Diagram.
- One IT term stands for one PO term, and the reverse. The rows are in ascending order of the PO term, ignoring case.
- The assignment's function names `upload_image`, `add_watermark` and `save_image` are the system operations of the System Sequence Diagram; they are written in the IT register and carry the IT terms in their parameters.
- A new concept in the Domain Model gets its row in the same change.

---

[REG]: ./artifact-registry.md

---

[BC-001]: ./business-case.md
[SA-001]: ./stakeholder-analysis.md
[DM-002]: ./domain-model.md
[2a87378]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/085-assignment-watermark-image/commit/2a87378078601878cb390c2d31581159df822d6f
