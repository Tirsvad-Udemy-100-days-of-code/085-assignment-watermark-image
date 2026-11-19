# ADR-0002: Architecture: layers, MVVM and the assignment function names

## Metadata
| Key | Value |
| --- | --- |
| ID | ADR-0002 |
| CrossReference | [BC-001], [SA-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-19 | Accepted | Jens Tirsvad Nielsen | Stand-in for S01 | Initial version<br>Accepted on Go in RC-011 | pending |

Allowed Status values: `Proposed`, `Accepted`, `Rejected`, `Deprecated`, `Superseded by ADR-NNNN`.

---

## Context

The framework's `clean-architecture` skill asks for layers whose dependencies point inward, with Model-View-ViewModel (MVVM) for a user interface. The course participants (S02) want the assignment's function names, `upload_image`, `add_watermark` and `save_image`, and readable code (concern CN-004). Options:

1. A single script with functions, as most course solutions do. It is short, but the rules, the Pillow calls and the Tkinter calls are mixed, so the rules cannot be tested without a window.
2. Layers `domain`, `application`, `infrastructure` and `presentation` with MVC.
3. The same layers with MVVM, as the framework's default for a user interface: a view that shows data and raises events, and a view model that exposes data and commands and calls the use cases.

## Decision

The source is laid out in the layers `domain`, `application`, `infrastructure` and `presentation` under `src/watermark_image/`, with MVVM in `presentation`, as the framework's default. The adapters and the infrastructure are merged into `infrastructure`, because the project is small. The three assignment names are the public commands of the view model and the names of the use cases; the domain dictionary records the pair of Product Owner term and technical term. `constants.py` sits in the package root and is imported by every layer.

## Consequences

**Positive:**

- The rules (value objects, use cases) are tested with fakes, without Pillow or a window.
- The import-linter contract keeps the dependency direction from drifting.
- S02 finds the assignment's function names in one place per layer.

**Negative:**

- More files than a single script, which a beginner may find heavy; the wiki step pages explain each layer when it is introduced.
- Mapping between view model data and domain objects adds small amounts of code.

## Affected Artifacts

- [BC-001] — objective O2.
- [SA-001] — concern CN-004 of S02.

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
