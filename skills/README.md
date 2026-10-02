# Arnaud's skill library

These are portable examples from Arnaud Dyèvre's research workflow, adapted for students on
1 October 2026. Each skill has a complete Claude Code folder and a complete Codex folder. Choose
the variant for your agent, inspect its behaviour, and adapt it to your project before installation.

## Choose a workflow

| Skill | Purpose | Claude Code | Codex |
| --- | --- | --- | --- |
| `start-session` | Recover the current state and next step. | [Read](claude/start-session/SKILL.md) | [Read](codex/start-session/SKILL.md) |
| `close-session` | Update context and commit the session locally. | [Read](claude/close-session/SKILL.md) | [Read](codex/close-session/SKILL.md) |
| `prose` | Review human writing; revise agent writing. | [Read](claude/prose/SKILL.md) | [Read](codex/prose/SKILL.md) |
| `ingest-paper` | Read, file, assess and catalogue a paper. | [Read](claude/ingest-paper/SKILL.md) | [Read](codex/ingest-paper/SKILL.md) |
| `compile-paper` | Compile LaTeX and report diagnostics. | [Read](claude/compile-paper/SKILL.md) | [Read](codex/compile-paper/SKILL.md) |
| `status` | Check Git state during a session. | [Read](claude/status/SKILL.md) | [Read](codex/status/SKILL.md) |
| `update-log` | Record progress without closing the session. | [Read](claude/update-log/SKILL.md) | [Read](codex/update-log/SKILL.md) |
| `beamer-to-html` | Turn a Beamer deck folder into a local HTML presentation. | [Read](claude/beamer-to-html/SKILL.md) | [Read](codex/beamer-to-html/SKILL.md) |

The retired `sync` alias is omitted. `beamer-to-html` is the starting point for
[exercise 3](../exercises/03-beamer-to-html/README.md): you use it on your own deck, then adapt
its `CONVERSION.md` rules and `assets/template.html` style.

## Inspect and adapt first

Read `SKILL.md` and the support files it names. In particular, `prose/STYLE.md` offers an example
style guide without named authors, and `ingest-paper/CONVENTIONS.md` demonstrates a literature
workflow. They are examples to discuss and adapt to your own voice and research conventions.

You can give either agent this prompt:

> Read the selected skill and its supporting files. Explain its inputs, outputs, dependencies and
> the changes it can make. Identify conventions I should personalise. Ask about choices you cannot
> infer from my project, then adapt a copy for my workflow. Preserve my existing instructions and
> skills. Install only the skill and client variant I select, after resolving any name collision.

The student versions deliberately differ from Arnaud's originals in these ways:

- Both clients use shared project context and history conventions; old command references and
  machine-specific dependencies have been removed.
- `close-session` commits attributable changes locally and does not push. Ignored student work
  stays on disk; a commit is not a backup of that work.
- `ingest-paper` asks about layout, PDF tracking and catalogue handling on first setup. It preserves
  existing project choices rather than automatically untracking files or removing generators.
- `prose` protects the student's authorship. Feedback on human text is a list of proposed changes;
  agent-written text can be revised within the requested scope.

Git is needed for Git operations; LaTeX tools for `compile-paper`; a readable full paper and a PDF
text reader for `ingest-paper`. The skill describes any additional dependency. Ask the agent to
inspect what is already installed before choosing macOS or Windows setup steps.

## Install a selected skill

Copy the **whole skill folder**, not just `SKILL.md`. The visible library itself is not an
installation directory. Project-level installation is a useful place to start; user-level
installation makes the skill available across projects.

| Client | Copy from this library | Project destination | User destination | Invoke |
| --- | --- | --- | --- | --- |
| Claude Code | `claude/<skill>/` | `.claude/skills/<skill>/` | `~/.claude/skills/<skill>/` | `/skill-name` |
| Codex | `codex/<skill>/` | `.agents/skills/<skill>/` | `~/.agents/skills/<skill>/` | `$skill-name` |

Paths and invocation checked on 1 October 2026 against the
[Claude Code skills documentation](https://code.claude.com/docs/en/skills) and
[OpenAI skill documentation](https://learn.chatgpt.com/docs/build-skills).
Here `~` means your home directory; these are folder locations, not OS-specific shell commands.

Check for an existing skill with the same name before copying. Keep its contents and decide which
version you want rather than overwriting it silently. After installation, ask the agent to identify
the selected skill's actual path and describe its behaviour before invoking a workflow that edits
files. If the new skill is missing from the client, reopen the session and check its discovery settings.

Both variants include their own real copies of support files, so either can be copied independently.
If you use both agents, make equivalent changes to both copies of a shared procedure or style guide.
The library copies are the teaching source; installed copies are yours to adapt. No install script
or symlink outside the pack is required.
