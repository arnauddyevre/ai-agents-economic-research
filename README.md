# Coding agents for economic research: student materials

Workshop materials and examples from **Arnaud Dyèvre’s dual-agent workflow**, prepared for the
LSE workshop on **2 October 2026**. Claude Code and Codex share the same project context; neither
is the default agent. You can use either, switch between them, or ask one to review the other's work.

**Workshop pack: 2 October 2026.** The presentation, five numbered exercise guides, eight complete
skills for each client, V12 Wikipedia inputs and optional worked fallbacks are included.
Start with the [setup guide](SETUP.md) and [exercise index](exercises/README.md).

## Start here

1. Open this folder in your preferred coding agent. Read this README and
   [PROJECT_HISTORY.md](PROJECT_HISTORY.md) together.
2. Open the [presentation](presentation/index.html), then choose an activity from the [exercise index](exercises/README.md). Follow its prerequisites
   and readiness note before starting.
3. Save your outputs in `outputs/<exercise>/`. Put incoming documents and screenshots in
   [document_dump/](document_dump/README.md) when you want either agent to work on them.
4. Browse the [skill library](skills/README.md), inspect a skill, then copy and adapt it if useful.
   Skills are examples from Arnaud's workflow; they are not installed merely by downloading this pack.

You can work in this folder or copy selected guides and skills into an existing research project.
When reusing the context files, adapt the purpose, folder map and commands to that project. Merge
with existing instructions rather than replacing them wholesale.

## What is where

| Location | Purpose |
| --- | --- |
| [README.md](README.md) | Stable project facts, shared conventions and this folder map. |
| [AGENTS.md](AGENTS.md) / [CLAUDE.md](CLAUDE.md) | Thin entry points for Codex and Claude Code. |
| [PROJECT_HISTORY.md](PROJECT_HISTORY.md) | Current state, decisions, checks and the next handoff. |
| [SETUP.md](SETUP.md) | macOS prerequisites (with a Windows note), CLI sign-in and first prompt. |
| [exercises/](exercises/README.md) | Five in-class activities, model/effort discussion and optional practice; inputs and worked fallbacks. |
| [skills/](skills/README.md) | Eight reusable workflows, with independent copies for each agent. |
| [handouts/](handouts/README.md) | Optional read-only X connector setup guide. |
| [presentation/](presentation/README.md) | The local workshop presentation, with working pack links. |
| [document_dump/](document_dump/README.md) | Temporary inbox shared by the human and both agents. |
| [outputs/](outputs/README.md) | Your local exercise outputs and permanent document archives. |
| [index.html](index.html) | Opens the presentation when the pack is served as a website. |
| [LICENSE](LICENSE) | CC BY 4.0 for the teaching material; exceptions are listed under Licence below. |

## Shared workflow for Claude Code and Codex

- Read this README and the latest relevant history entry at the start of a task. Read the chosen
  exercise or skill when needed, rather than loading the entire pack into every conversation.
- Keep stable facts here and current state in the history. Update whichever became stale; keep
  the agent entry points short and consistent.
- Before switching agents, record the outcome, files changed, checks performed, unresolved
  questions and next step. The incoming agent should inspect the actual files before continuing.
- When both agents are active, give them distinct tasks or files. Do not overwrite or commit the
  other agent's unfinished work. A second agent can review an output without editing it.
- Preserve human ownership of research claims and prose. In prose review, suggest changes to
  human-authored text; apply them only when the author requests it.
- Use British English. Distinguish supplied evidence, the agent's inference and missing material.
- Treat `outputs/` as the default output area. Edit distributed teaching files only when that is the
  requested task. Record enough in the shared history to resume, without copying private source text.

### Document intake and archiving

`document_dump/` is a temporary landing zone for documents, screenshots, pasted material and
handoffs that either agent may need. Inspect its contents when a task uses incoming material.

When the task is complete:

1. Copy each used document and resulting note to `outputs/archive/<task>/`, or verify that its
   permanent copy is already there. Give the task a descriptive folder name.
2. Calculate and compare SHA-256 checksums of each inbox file and its archived copy. Record the
   filenames and checksums in that task's archive note. Keep originals as well as derived notes.
3. Update references to the old inbox paths, including links in notes and the project history.
4. Only after verification, remove the corresponding inbox copies. Leave files for unfinished
   tasks in place. Never delete the only copy of a document.

Always keep `document_dump/` and its README, even when the inbox is otherwise empty. No blanket
cleanup: process each file explicitly. The [inbox guide](document_dump/README.md) describes this
same rule for the person or agent handling intake.

### Local work and Git

The supplied `.gitignore` excludes the contents of `document_dump/` and `outputs/`, apart from their
READMEs. This includes archived documents and exercise outputs. Ignoring a folder is not a backup:
keep your own backup of work you want to retain.

The shared `close-session` skill updates context and commits attributable, tracked changes locally.
It does not push. Ignored work remains on disk and is not included in that commit. If you copy this
workflow into another project, choose its tracking policy deliberately; changing ignore rules does
not automatically untrack existing files. Git-dependent skills report when Git is unavailable;
the workshop guides can still be used from an extracted folder.

## Requirements and reuse

Start with an installed, signed-in coding agent and sufficient usage for your chosen activity.
You do not need both subscriptions to use the pack. Additional requirements are listed in each
exercise and skill. Instructions are written for **macOS**; [SETUP.md](SETUP.md) has a short Windows note. Live connections and phone pairing depend on your account and client;
fallbacks let you continue with the main research activities if usage or connection setup is blocked.
The optional X guide is **paid** and is not needed for the workshop.

These are portable teaching adaptations of Arnaud's own files. Shared skills retain his approach,
with student-specific choices explained in the [library guide](skills/README.md). Exercise briefs
come from the LSE presentation; the exact V12 research prompt, frozen page evidence and X guide retain their source versions.
Examples are starting points to inspect and adapt, not universal research conventions.

The pack is self-contained: clone the repository or download it as a ZIP, and the slides are also
online at <https://arnauddyevre.github.io/ai-agents-economic-research/>. The optional Wikipedia
research answer key is included separately; keep it closed until after your independent judgements.
It contains model decisions, not human ground truth.

## Licence

© 2026 Arnaud Dyèvre. The teaching material is licensed under [CC BY 4.0](LICENSE): you may share
and adapt it, including commercially, with credit to Arnaud Dyèvre. Two exceptions: the Wikipedia
excerpts in exercise 4 remain under CC BY-SA 4.0 (see its [data README](exercises/04-wikipedia-classification/data/README.md)),
and product names and logos (Anthropic, Claude, OpenAI, ChatGPT, Codex, Gmail, Slack, Zoom, X,
LinkedIn and others) are trademarks of their owners, shown for identification only.
