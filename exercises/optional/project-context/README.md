# Optional — Opening a project and building shared context

**Readiness:** ready with your own short project note. No classroom dataset is required.

## Aim and prerequisites

Make a project understandable in a fresh session, then check that either Claude Code or Codex can resume from the same files. Start with an installed, signed-in agent, this pack open at its root, and a research or teaching task you can describe in a few sentences.

Read the [pack README](../../../README.md), [AGENTS.md](../../../AGENTS.md), [CLAUDE.md](../../../CLAUDE.md) and [PROJECT_HISTORY.md](../../../PROJECT_HISTORY.md). The README holds stable facts and conventions; the history holds the current state, decisions and next steps. The two agent entry points refer to that shared information.

## Activity and prompts

Write `outputs/optional-project-context/project-note.md` with the task, desired output and anything the agent needs to preserve. Try this prompt from the workshop:

> Read my project note in `outputs/optional-project-context/project-note.md`. Summarise the task in three bullets and list what is still unclear. Name the file you read. Do not edit any files yet.

Compare the response with your note. Correct omissions or misunderstandings. Then try the shared context files in a fresh session:

> Read README.md and PROJECT_HISTORY.md. Summarise the project, the latest decisions and the next task. List the files you read and flag anything that conflicts. Do not edit any files yet.

Before ending a session, use the workshop’s handoff prompt:

> Write a short handoff in `outputs/optional-project-context/handoff.md` with the objective, decisions made, files changed, checks completed, unresolved questions and the next action. Link to source files rather than copying them in full. Mark uncertainties. I will review this note before the next session starts.

Review the note, record the useful decisions in the shared history, and open another session. Ask it to read the instructions and handoff and restate the next task and the evidence it needs. If you have both agents, use the other one for this step.

## Outputs and completion checks

- A project note, a checked summary and a reviewed handoff under `outputs/optional-project-context/`.
- The summary names the source actually read and preserves your task and constraints.
- The handoff distinguishes completed work, uncertainties and next actions.
- A fresh session can identify the next action without relying on the old conversation.

No additional teaching files are missing. Your project note is the input. If you used the temporary inbox, complete the archive-and-checksum procedure in the [activity index](../../README.md) after this task; otherwise keep your working outputs in place.
