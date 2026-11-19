# Review Record: Shell scripts of gateway 1

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-015 |
| CrossReference | [MIL-001], [QC-SH-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | Stand-in for S01 | Review record; mode autonomous, not independent | [44b1b5e] |

---

## Artifact Under Review

- Instance reviewed: Shell scripts (SH) of gateway 1, `scripts/check.sh`, `scripts/run-gui-tests.sh`, `docker/gui/entrypoint.sh`, in the pull request of milestone MIL-001
- Checklist used: [QC-SH-001]
- Scope: full review of the shell scripts of gateway 1
- Language and domain: n/a
- Language reviewer: none
- Mode: autonomous, not independent (the reviewer is a stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Starts with `#!/usr/bin/env bash` and `set -euo pipefail` (or a comment explains the exception) | Pass | Each script starts with `#!/usr/bin/env bash` and `set -euo pipefail` |
| 2 | Every expansion is quoted; lists are arrays; tests use `[[ ]]` and `$(...)` | Pass | Expansions are quoted; `[[ ]]` and `$(...)` are used |
| 3 | Names follow the conventions: `kebab-case.sh` files, `snake_case` functions and variables, `UPPER_SNAKE` constants and environment variables | Pass | kebab-case file names, snake_case variables |
| 4 | Passes `shellcheck` and `bash -n` with no unexplained `disable` comments | Pass | shellcheck (koalaman/shellcheck:stable) reports nothing; one `disable=SC1091` for a file that exists only in the container, with the reason |
| 5 | Errors go to standard error with an `error:` message and a non-zero exit code; bad or missing arguments print a usage line | Pass | check.sh and run-gui-tests.sh print `error:` to standard error and exit non-zero |
| 6 | Temporary files use `mktemp` with a `trap ... EXIT` cleanup; no fixed `/tmp` names | Pass | No temporary file is used |
| 7 | No secret is written in the script, echoed, or put on a command line; secrets come from the environment or a gitignored file | Pass | No secret in any script |
| 8 | A script that changes state outside its own directory defaults to a dry run or needs an explicit flag, and says so in its header | Pass | Scripts change only the project's own folders (build output, docs/screenshots) |
| 9 | A header comment states purpose, usage, options, environment variables and exit codes | Pass | Each header gives purpose, usage, environment and exit codes |
| 10 | The script implements a task or design it cites; deviations are recorded | Pass | The scripts implement the tasks of gateway 1 that cite them |
| 11 | Behaviour is tested for success, failure and any disabled or bypass path | Pass | Manual run recorded: check.sh exits 0 on the project; run-gui-tests.sh exits 0 and writes docs/screenshots/harness-smoke.png; check.sh exits 2 without .venv |
| 12 | Formatted with `shfmt` (or the project's formatter) | Pass | shfmt (mvdan/shfmt:v3.14.1) with `-i 2 -ci` reports no difference |
| 13 | Safe to re-run: a second run does not duplicate or corrupt what the first did | Pass | A second run repeats the same checks and rewrites the same screenshot |
| 14 | Bash version and external tools it needs are stated; GNU-only options are named | Pass | Bash and the needed tools (Docker, opengrep) are named in the headers |
| 15 | A command sequence, constant, path or message used more than once is defined once (a function, a variable or a sourced helper); a helper is shared between scripts only where it expresses the same knowledge | Pass | The opengrep and python lookup is defined once in check.sh |

## Overall Verdict

Go — every Mandatory criterion passes

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | 2026-11-20 |

---

[MIL-001]: ../../milestones/mil-001-project-setup.md
[QC-SH-001]: ../../../framework/qc/code/qc-programming-shell.md
[44b1b5e]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/085-assignment-watermark-image/commit/44b1b5e31086612d7f3fdfb7e709507066247e4a
