# ADR-0001: Technology: Tkinter, Pillow and Python 3.13 or newer

## Metadata
| Key | Value |
| --- | --- |
| ID | ADR-0001 |
| CrossReference | [BC-001], [SA-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-19 | Accepted | Jens Tirsvad Nielsen | Stand-in for S01 | Initial version<br>Accepted on Go in RC-010 | [44b1b5e] |

Allowed Status values: `Proposed`, `Accepted`, `Rejected`, `Deprecated`, `Superseded by ADR-NNNN`.

---

## Context

The assignment asks for a desktop program that uploads images and adds a watermark. The Business Case wants few runtime dependencies (objective O5), and the stakeholder S03 asks for none beyond what is needed (concern CN-008). Options:

1. Tkinter with the standard library only. Tkinter reads only PNG, GIF and PGM files, cannot read JPEG or WebP, cannot blend with transparency, and writes only PNG and GIF, so a watermark on a JPEG photograph is not possible.
2. Tkinter with Pillow. Tkinter is part of Python; Pillow reads and writes the common formats, draws text, scales images and blends with an alpha channel.
3. A GUI toolkit such as PySide6 or Qt for Python with its own image classes. It reads the formats but adds a large dependency and a licence to explain.
4. A web interface served locally. It needs a browser, a server and more code, and the assignment asks for a desktop program.

Python 3.13 is installed on the development machine, and the Product Owner asked for "greater than 3.13", read as 3.13 or newer. The project needs one file for configuration (`pyproject.toml`), a virtual environment (`venv`), pytest, and development tools that check style and types.

## Decision

The application uses Tkinter for the window and Pillow as its single runtime dependency, requires Python 3.13 or newer (`requires-python = ">=3.13"`), and builds with setuptools from `pyproject.toml`. pytest, pytest-cov, ruff, mypy and import-linter are optional development dependencies in the `dev` group.

## Consequences

**Positive:**

- One small runtime dependency that ships wheels for current Python versions.
- JPEG, PNG, BMP, GIF and WebP are readable; JPEG and PNG are writable; transparency is handled correctly.
- Tkinter needs no installation on the standard Python installers.

**Negative:**

- S03's wish for no runtime dependency is met only in the sense "none beyond what is needed"; the conflict is recorded in the Stakeholder Analysis.
- Pillow must stay installable on every supported Python version; the container check in gateway 6 covers this.
- Tkinter looks different on each operating system, so screenshots from the Linux container differ from the Windows look.

## Affected Artifacts

- [BC-001] — objective O5 and the assumption about the reading of "greater than 3.13".
- [SA-001] — the conflict between S03's concern CN-008 and the need for Pillow.

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[44b1b5e]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/085-assignment-watermark-image/commit/44b1b5e31086612d7f3fdfb7e709507066247e4a
