---
name: close-session
description: "Close a session by updating shared history and stale context, archiving completed-task inputs, and committing attributable work locally. Use only when explicitly invoked as $close-session or requested by name; do not push."
---

# Close session

Update shared history, refresh context changed by this session, then commit the completed work
locally. The explicit invocation authorises this routine. It does not authorise a push.

## 1. Look

Inspect the current Git status, staged changes and recent commits if Git is available. If the working
folder is inside a larger repository, keep every staging and commit operation scoped to this project
and the work attributable to this session.

Find the history named by the project context, otherwise prefer `PROJECT_HISTORY.md`. Use an existing
`PROJECT_LOG.md`, `SESSION_LOG.md` or `doc/session_log.md` if that is the established convention.
Read the latest entry and preserve its format. If there is no history, ask where to create it.

## 2. Write

Add one history entry: date, actor `Codex`, decisions or results, files touched, checks already
performed, and remaining work. Update an entry for this same session if one already exists; do not
merge another agent's session just because it has today's date. Do not invent completed checks.

Refresh only context made stale by this session: a changed decision, moved path or resolved open
item. Stable workflow belongs in the shared `README.md`, current state in `PROJECT_HISTORY.md`.
Keep `AGENTS.md` and `CLAUDE.md` as equivalent entry points.

For completed tasks, apply the project's `document_dump/` policy: archive the task's documents and
notes under `outputs/archive/<task>/`, record and verify matching SHA-256 checksums, update references,
then remove only the verified inbox copies. Reuse an existing verified archive rather than creating
a duplicate. Retain inputs for unfinished tasks and always retain `document_dump/README.md`.
If a checksum differs or a destination conflicts, retain the inbox copy and report the unresolved
archive. An incomplete archive need not prevent logging the session's other completed work.

## 3. Commit locally

Review diffs and stage only completed changes attributable to this session, using explicit paths or
selected hunks. Never use blanket staging. Do not force-add ignored files: `outputs/` outputs and
`document_dump/` inputs remain local under the workshop defaults. Do not change ignore rules merely
to create a commit.

Review the staged diff before committing. Existing staged changes belonging to someone else must
remain staged and uncommitted by this routine. If attribution cannot be separated safely, leave the
index untouched and report that no commit was made. Do not reset or discard anyone's changes.

Use a substantive commit subject under 72 characters; keep the configured Git author and the
project's established co-author convention. Do not invent a model version or another agent's
attribution. Skip an empty commit. If Git is absent, the repository is new without configuration,
or a merge/rebase/conflict is in progress, finish the safe history/context work and explain why the
local commit was skipped. Do not initialise Git or alter identity settings as part of closing.

Do not fetch or push. A push requires a separate user request. Do not launch new test suites,
linters or broad verification rounds; report existing validation and unresolved failures honestly.

## 4. Report

State what was logged, context changes, archive status when relevant, local commit subject/hash (or
why no commit), and that nothing was pushed. Name any work left uncommitted.

**Inspect and adapt:** review the archive and Git conventions before using this in another project.
Keep local checkpointing separate from publishing or synchronising with a remote.
