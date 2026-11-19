# Use Case Diagram: Watermark Image Desktop App

## Metadata
| Key | Value |
| --- | --- |
| ID | UCD-001 |
| CrossReference | [SA-001], [BC-001], [US-001], [UC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | Stand-in for S01 | Initial version<br>Accepted on Go in RC-016 | [2a87378] |

---

## Purpose and Scope

The diagram shows the boundary of the Watermark Image Desktop App: one actor, the User, and the one goal the system serves, "Watermark an image". It serves the stories US-001.01 to US-001.05 of [US-001]. The stories US-001.06 and US-001.07 are not goals of an actor of the system and are not shown.

## Diagram

```plantuml
@startuml
left to right direction
actor "User" as A1 <<Actor>>
rectangle "Watermark Image Desktop App <<System>>" {
  usecase "Watermark an image" as UC1
}
A1 --> UC1
@enduml
```

Crossings of the chosen layout: 0 (one actor, one use case, one association).

## Actor Table

| Actor | Stereotype | Stakeholder ID (SA) | Goals (use cases) |
| --- | --- | --- | --- |
| User | `<<Actor>>` | S01, S02 | Watermark an image |

## Use Case Table

| Use Case | Actor(s) | Goal | Source story | Priority (MoSCoW) | Reason |
| --- | --- | --- | --- | --- | --- |
| Watermark an image | User | Put a text or logo watermark on a picture and keep the result | US-001.01 to US-001.05 | Must | The core goal of the assignment (objective O1 of [BC-001]) |

## Role Matrix

Not applicable: there is one primary actor, so there is no role to separate and no matrix to approve.

## Relationships

| From | Relationship (`<<include>>` / `<<extend>>`) | To | Justification |
| --- | --- | --- | --- |
| - | - | - | There is one use case, so no `<<include>>` or `<<extend>>` exists |

---

[UC-001]: use-cases/uc-001/uc.md
[SA-001]: ./stakeholder-analysis.md
[BC-001]: ./business-case.md
[US-001]: ./user-stories.md
[2a87378]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/085-assignment-watermark-image/commit/2a87378078601878cb390c2d31581159df822d6f
