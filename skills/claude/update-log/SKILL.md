---
name: update-log
description: "Add a factual mid-session entry to shared project history, preserving format and agent attribution. Use for checkpoint or log-update requests; do not commit or push."
---

# Update log

Record a mid-session checkpoint in the shared project history, without committing or closing.

1. Locate the history named by project context; prefer `PROJECT_HISTORY.md` for this pack. Preserve an
   established `PROJECT_LOG.md`, `SESSION_LOG.md`, `doc/session_log.md` or `docs/session_log.md`
   rather than creating a second source of truth. If none exists, ask where to create it.
2. Read the current snapshot and latest relevant entries. Use the current conversation and diffs for
   the work actually performed. If recent commits are needed, inspect their full messages including
   trailers; `git log --oneline` cannot establish co-author attribution. Do not infer authorship
   merely from a date or a guessed model name.
3. Incorporate a supplied note. Otherwise write a concise, factual checkpoint from this session;
   ask only when a consequential decision or attribution is unclear. Distinguish completed changes,
   checks actually performed, decisions and unresolved work.
4. Attribute this entry to `Claude Code`. Keep the existing format and ordering. Amend an entry for this
   same session if appropriate; do not merge another agent's entry because it shares today's date.
   Do not invent session numbers or timestamps. When first creating a confirmed history file, use a
   simple date, actor, summary, files and next-step entry.
5. Refresh the current snapshot only if the checkpoint changes it. Leave past entries intact and
   avoid duplicating a full transcript. Report the file and what was recorded.

Do not commit, push, run tests or archive unfinished inputs. Use `/close-session` separately
for a local checkpoint and completed-task cleanup if it is installed.

**Inspect and adapt:** choose one shared history for both agents and preserve a format that a future
session can understand quickly.
