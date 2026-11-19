# Review Record: Wiki

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-039 |
| CrossReference | [MIL-006], [QC-WIKI-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | Stand-in for S01 | Review record; mode autonomous, not independent | pending |

---

## Artifact Under Review

- Instance reviewed: the wiki sources in docs/wiki/ (18 pages and the sidebar) of milestone [MIL-006]
- Checklist used: [QC-WIKI-001]
- Scope: full review of the wiki sources
- Language and domain: n/a
- Language reviewer: none
- Mode: autonomous, not independent (the reviewer is a stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The wiki has a `_Sidebar.md`, because the host lists subpages only through it | Pass | _Sidebar.md exists |
| 2 | The sidebar starts with the wiki's title in bold, then one list of the pages in the primary language (English), `Home` first | Pass | Bold title, then one list with Home first |
| 3 | The page list holds a link to every English page of the wiki, and no link points to a page that does not exist | Pass | All six English pages are linked; a script found no link to a missing page |
| 4 | A `**Related**` section follows the page list only when the wiki has related wikis (for example the checklists wiki for a framework wiki); each entry is a link to that wiki's Home. A wiki with nothing related has no such section | N-A | No related wikis |
| 5 | A `**Languages**` section is the last section of the sidebar. It has one line per language, the language written in that language, linking to that language's `Home` page | Pass | Languages is the last section, one line per language, each to its Home |
| 6 | The sidebar does not repeat the page list per language | Pass | The page list appears once |
| 7 | A sidebar produced by a generator carries a comment that says so and names the generator; the generator is changed, not the page | N-A | The sidebar is written by hand, not generated |
| 8 | The wiki has a `Languages` line on each page (criterion 11), so the sidebar is not the only way to switch language | Pass | Language line on every page |
| 9 | Every wiki exists in English and, as a minimum, in the language the project's registry names as the PO language; further languages are added on top, never instead of English | Pass | English exists, as the PO language |
| 10 | Every English page has a page in each other language of the wiki: the page sets are identical | Pass | Six English pages, each with -da and -ms: 18 pages |
| 11 | Every page starts with the language line, with the current language in bold and a link to the same page in each other language | Pass | Every page starts with the language line, current language in bold |
| 12 | A page in a language other than English is named `<Page>-<code>.md`, with a BCP 47 code; English has no suffix | Pass | Suffixes -da and -ms |
| 13 | Code blocks, commands, file names and IDs stay in English in every language | Pass | Commands, file names and code names stay English |
| 14 | The sidebar, every page and every link were checked on the published wiki after the change, not only in the repository | Fail | The published wiki can only be checked after the merge; the pages are published by the workflow after it |
| 15 | A change to the layout rules (sections, order, naming) is made in the generator or template and in this checklist's source rules together | N-A | No change to layout rules |
| 16 | The wiki folder (`docs/wiki/`) is flat: every page, `Home.md` and `_Sidebar.md` included, is directly in it, and languages are told apart by file name, never by a subfolder | Pass | docs/wiki is flat |

## Overall Verdict

Go-with-conditions — every criterion passes except criterion 14, which needs the published wiki; the Danish and Bahasa Malaysia wording was written by the author of the pages and has not been read by a native speaker

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Check the sidebar, every page and every link on the published wiki after the merge | S01 | 2026-11-26 |
| Read the Danish and Bahasa Malaysia pages as a native speaker would and correct the wording | S01 | 2026-11-26 |

---

[MIL-006]: ../../milestones/mil-006-step-4-save.md
[QC-WIKI-001]: ../../../framework/qc/artifacts/qc-wiki.md
