# ADR-0003: GUI tests and screenshots run in a Docker container

## Metadata
| Key | Value |
| --- | --- |
| ID | ADR-0003 |
| CrossReference | [BC-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-19 | Accepted | Jens Tirsvad Nielsen | Stand-in for S01 | Initial version<br>Accepted on Go in RC-012 | pending |

Allowed Status values: `Proposed`, `Accepted`, `Rejected`, `Deprecated`, `Superseded by ADR-NNNN`.

---

## Context

The framework forbids testing or driving a graphical interface on the host desktop, because the test would take the user's mouse and keyboard (`framework/process/gui-testing.md`). The Product Owner needs a screenshot for each build step in the README and the wiki. Options:

1. The host desktop. Forbidden by the framework.
2. Windows Sandbox. Isolated, but Windows only, and slower to script.
3. A Docker container with a virtual display (Xvfb), running the application and a test that grabs the screen with Pillow. Linux, scriptable, and the result is read from files.

## Decision

Graphical tests and screenshots run in a Linux Docker container under Xvfb, started by `scripts/run-gui-tests.sh`. The test reports through an exit code and screenshot files written to `docs/screenshots/`. Unit and integration tests run on the host as usual.

## Consequences

**Positive:**

- The host desktop is never used; the run is repeatable on any machine with Docker.
- Screenshots are produced by the same script for every step.

**Negative:**

- Screenshots show the Linux look of Tkinter; the README says so.
- The first run downloads a large image and installs the project in the container, which takes time.
- Docker must be installed to refresh the screenshots; other contributors can still run all other tests without it.

## Affected Artifacts

- [BC-001] — risk "graphical interface cannot be tested on the host desktop" and objective O4.

---

[BC-001]: ../business-case.md
