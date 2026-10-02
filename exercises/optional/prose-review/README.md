# Optional — Reviewing prose while retaining ownership

**Readiness:** ready with a research paragraph you wrote. No supplied paragraph or worked solution is included.

## Aim and prerequisites

Request useful editorial feedback while retaining the final wording and all decisions about claims, evidence and uncertainty. Put your own paragraph in `outputs/optional-prose-review/paragraph-original.md`. Keep an unchanged copy so that you can compare the meaning after editing.

Inspect the shared prose workflow in the [skills library](../../../skills/README.md): [Claude version](../../../skills/claude/prose/SKILL.md) or [Codex version](../../../skills/codex/prose/SKILL.md). Its treatment of human-written prose is review-first; it distinguishes this from editing text the agent generated. Follow the library’s deliberate installation instructions if you want to invoke it as a skill.

## Activity and prompt

Point the agent at your paragraph and use the workshop prompt:

> Review this research paragraph without rewriting the file. For each useful change, give the location, the issue and a proposed wording. Look for unclear actors, unnecessary words, missing logical links and claims stronger than the evidence. Preserve technical meaning, qualifications and citations. Flag substantive questions for me to decide. I will choose which changes to make.

Read each suggestion and decide whether to accept, adapt or reject it. Make the chosen changes yourself, or explicitly ask the agent to apply only the changes you selected. Save the edited version and your decisions under `outputs/optional-prose-review/`.

## Outputs and completion checks

- Your original paragraph, location → issue → proposed wording feedback, and your edited version or decision note.
- The review did not silently rewrite the original.
- Claims, technical meaning, qualifications and citations survive the edits you accept.
- Substantive questions remain yours to resolve; stronger wording is not mistaken for stronger evidence.
- A comparison of the original and edited paragraph shows only intended changes.

No additional classroom material is missing. The student supplies their own writing. If a document arrived through `document_dump/`, follow the archive-and-checksum procedure in the [activity index](../../README.md) after the task is complete.
