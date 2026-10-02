# Document inbox

Keep this folder and README present at all times. This is the temporary landing zone for documents,
screenshots, pasted material and handoffs shared by you, Claude Code and Codex. Its contents are
Git-ignored, except this README.

For each incoming file, establish which task uses it. Both agents follow the same
[project workflow](../README.md); a handoff should identify the input, current result and next step.

## When the task is complete

1. Archive each used document and resulting note in `outputs/archive/<task>/`, relative to the pack
   root. If an archive copy exists, verify it instead of making unnecessary duplicates.
2. Compare SHA-256 checksums of the inbox file and archive copy, and record filenames and hashes
   in the task's archive note. A matching filename alone is not sufficient. Preserve the source
   document even when a summary has also been written.
3. Update links and references that point to the inbox, including the shared project history.
4. Remove only the verified inbox copies belonging to the completed task.

Retain materials for unfinished tasks. Never delete a file whose only copy is here. Inspect and
process files individually; do not clear the folder indiscriminately. When all tasks are complete,
only this README should remain. Archive content remains local and ignored; back it up separately.
