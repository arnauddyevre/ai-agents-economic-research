---
name: start-session
description: "Start a working session by reading shared project context, the latest history entry and Git state. Use only when explicitly invoked as $start-session or requested by name."
---

# Start session

Orient to the current project without changing it. This student example follows Arnaud's shared
Claude Code and Codex workflow.

## Look

1. Follow the applicable agent entry point and read the shared `README.md`.
2. Read the current snapshot and latest entry in `PROJECT_HISTORY.md`. If the project names a
   different history file, use that file instead. For older projects, check `PROJECT_LOG.md`,
   `SESSION_LOG.md`, `doc/session_log.md` or `docs/session_log.md`; do not create a second log.
   Read deeper only when the latest entry needs context. If no history exists, report that.
3. If this is a Git repository, inspect `git status --short --branch` and
   `git log --oneline -5`. With no commits yet, report that rather than treating it as a failure.
   If this folder is inside another repository, identify that enclosing repository so the student
   knows which history they are viewing. Do not initialise or change Git configuration.

## Report

Briefly state the last recorded work and actor, recorded open item or next step, branch, uncommitted
changes and recent commits. Uncommitted changes may belong to the student or another agent; do not
assume they are mistakes. If Git is unavailable, report the recorded project state only.

Do not run builds, tests, broad audits or network operations. Do not start the next task implicitly.
Mention `$update-log` or `$close-session` only if those skills are installed.

**Inspect and adapt:** choose the overview and history files your project actually uses. Both agents
should read the same shared state; keep client-specific files thin.
