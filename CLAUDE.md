# Claude Code entry point

This is a dual-agent workshop workspace and reusable workflow library. Start each task by reading
[README.md](README.md) and the latest relevant entry in [PROJECT_HISTORY.md](PROJECT_HISTORY.md).
Follow the shared conventions there; keep stable facts and current state in those files rather
than duplicating them here. Codex uses the same context through `AGENTS.md`.

Use `outputs/<exercise>/` for student outputs. The shared `document_dump/` is the temporary landing
zone for documents, screenshots and handoffs. After a task ends, archive its documents and notes
under `outputs/archive/<task>/`, record and verify matching SHA-256 checksums, and update references
before removing inbox copies. Retain unfinished-task inputs and always keep `document_dump/README.md`.
Never delete the only copy. Follow the full workflow in the README and inbox guide.

Read only the exercise and skill needed for the current task. The library is not pre-installed;
follow [skills/README.md](skills/README.md) when the student chooses to install a skill. Record
outcomes, checks and the next step before handing work to Codex or back to the student.
Preserve the other agent's unfinished work. Commit only when requested or when an explicitly
invoked skill calls for it; pushing needs a separate request.
