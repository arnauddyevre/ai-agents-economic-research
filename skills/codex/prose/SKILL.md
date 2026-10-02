---
name: prose
description: "Review human-authored prose without editing it, or revise agent-generated prose using the bundled example style guide. Use only when explicitly invoked as $prose or requested by name, not for routine drafting or documentation."
metadata:
  short-description: Review prose with an example style guide
---

# Prose

Read the bundled [STYLE.md](STYLE.md) first. It provides example preferences to inspect and adapt
to the writer's voice and project.

## 1. Establish scope and authorship

Use the supplied file, range or pasted passage. If none was supplied, ask what to review. Identify the
register in STYLE.md section 2: paper body, notes, email or slides, and state your choice.

Check whose text this is before editing:

- **Human-authored text:** review only. Give the location, issue and proposed wording; leave the
  source unchanged. This includes typing slips. The author's voice remains theirs to develop.
- **Agent-generated text:** revise directly within the requested scope.
- **Mixed or unknown authorship:** ask, or review without changing the source. Do not infer
  authorship from style alone.

Respect project-specific read-only files and review boundaries. Do not add another project's
protected paths to this project.

## 2. Apply the procedure

Work through STYLE.md section 1 in order. State the passage's claim in one sentence. If you cannot,
explain that the argument needs clarification before prose revision. Cut material that does not
advance the claim and name the actor in each sentence, then apply the read-aloud test, checklist,
sentence-length variation and hedge pass.

For human-authored text these are proposed changes, not edits. Preserve technical meaning, citations,
epistemic hedges and informative contrasts. If a passage is already effective, say so; do not create
changes merely to appear useful.

## 3. Protect the voice

Use STYLE.md section 3 to distinguish slips, clear non-native phrasing, ambiguous phrasing and filler.
Its "fix silently" category applies only to agent-generated text in this skill. Flag issues in human
writing, including slips, for the author to decide. Never smooth clear text into generic fluency.

## 4. Report

For human-authored text: show only the review flags with locations, explanations and proposed wording.
No rewritten file. For agent-generated text: give the register, before/after or a few representative
examples, unresolved flags, and word counts before/after. Explain an increase when one is justified.

Do not compile, commit, push or send messages. If a LaTeX build is needed later, use
`$compile-paper` separately if installed. This skill does not apply to code comments, error
messages or terse status output.

**Inspect and adapt:** keep the authorship boundary, then personalise the register, examples and
preferences in your installed STYLE.md. If using both agents, keep their copies aligned.
