# Literature ingestion conventions

A portable version of Arnaud Dyèvre's procedure for filing, reading and assessing research papers.
The bundled [SKILL.md](SKILL.md) gives the workflow; this file defines its artefacts. Both agents
receive an ordinary copy of this file. Keep the copies aligned if you adapt them.

These are starting conventions. Existing project rules and the student's confirmed choices take
precedence. Paths and subject tags belong in the project's shared configuration, not in this skill.

## 1. Layout and first setup

Use the configuration named in the shared README. For a new project, create `literature.json` at its
root after confirming the choices below. If an existing project uses `.claude/literature.json`, both
agents can read that file; keep it unless the student requests migration. If both files exist and
project context does not identify the source of truth, ask which governs instead of merging them.

Illustrative configuration for using the workshop pack directly:

```json
{
  "pdf_dir": "outputs/literature/pdfs",
  "notes_dir": "outputs/literature/notes",
  "catalogue": "outputs/literature/CATALOGUE.md",
  "inbox": "document_dump",
  "pdf_naming_example": "Author2026_ShortTitle.pdf",
  "note_naming_example": "Author2026_ShortTitle.md",
  "log": "PROJECT_HISTORY.md",
  "context": ["README.md", "PROJECT_HISTORY.md"],
  "tags": ["identification", "data", "growth"],
  "pdf_tracking": "local",
  "catalogue_mode": "manual"
}
```

Paths are project-relative, with their actual on-disk casing. `pdf_dir` may equal `notes_dir` if
existing conventions require it. `*_naming_example` holds a real example to imitate when one exists;
otherwise agree a naming pattern with the student. `log` and `context` identify shared state to read
before assessing project relevance. `inbox` and `tags` are optional. `pdf_tracking` is `local` or
`tracked`; `catalogue_mode` is `manual` or `generated`. For generated catalogues, also record the
existing command or documented procedure in `catalogue_command` after confirming it.

Before the first ingest:

1. Inspect the project's PDF and note folders, current catalogue, applicable ignore rules and any
   catalogue generator. List parent directories to capture actual casing; a case-insensitive
   filesystem can conceal a casing error that breaks on another OS.
2. Identify the shared overview and history. Prefer `README.md` and `PROJECT_HISTORY.md` here;
   retain established alternatives in another project.
3. Ask one combined question confirming the proposed layout, naming examples, PDF tracking,
   note tracking and catalogue workflow. When a choice is already explicit in project context,
   confirm only what remains unspecified. An older config missing tracking/catalogue choices
   requires the same targeted confirmation before changing those conventions.
4. Write the confirmed config and create missing directories/indexes. For a new manual catalogue,
   create a brief purpose statement and the sections in §9. Update the shared README with the
   config location and decisions. Do not duplicate the detailed configuration in both wrappers.
5. Respect existing tooling and tracked files (§2 and §9). Installation of a skill is not consent
   to migrate a literature library.

If there is no library, propose the workshop paths above when working in this pack. For a separate
research project, propose an appropriate `literature/` layout and ask. All workshop outputs under
`outputs/` stay local and ignored, including notes; moving to tracked notes in a research project is a
separate deliberate choice.

## 2. Tracking is a project decision

Arnaud's usual preference is local PDFs and versioned notes. The workshop pack instead keeps all
exercise outputs local under `outputs/`. Explain this distinction on setup and record the student's
choice. Do not imply ignored files are backed up by Git.

- `pdf_tracking: local`: leave PDFs untracked. If the directory is not already ignored, propose a
  narrowly scoped PDF ignore rule as part of the setup decision. Do not alter unrelated rules.
- `pdf_tracking: tracked`: preserve the project's choice. This skill still does not stage or commit.
  If an ignore rule conflicts, report it for the student to resolve; never force-add files.
- Already tracked PDFs remain tracked. Do not run `git rm --cached`, delete local copies or rewrite
  history as part of ingestion. A requested migration needs its own plan because removing a
  tracked file affects collaborators and does not remove the historical Git objects.
- Keep existing note-tracking conventions. In this pack, notes under `outputs/` remain ignored; in a
  research repository, versioning notes is usually useful but must be agreed.

## 3. Naming and versions

Match the configured examples. Existing conventions may use `AuthorsYear_ShortTitle.pdf`,
`Author Author & Author (Year) Title.pdf`, or sidecar notes named `<PDF stem> - summary.md`.
The note key equals its filename stem and serves as the link anchor for other notes.

Check references before renaming any file, including publisher filenames such as `w35523.pdf`.
If a catalogue, note, review workbook or tracked document already uses its name, preserve it and
record a mapping. Copy rather than destructively move a supplied original; verify SHA-256 equality.

A probable duplicate or new version needs the student's decision before changing an existing note.
When an update is authorised, keep version dates/identifiers, describe what changed and preserve
prior judgements where useful. Do not silently overwrite a different file or merge unrelated papers.

## 4. Tiers and tags

**Tier means relevance to this project, not general importance.**

- **Tier 1 — Load-bearing.** Estimates, design or data enter our own design, calibration or
  measurement. If this paper were wrong, something in our work would change.
- **Tier 2 — Supporting.** It informs a channel, robustness argument or comparison. We cite it,
  while our design does not depend on it.
- **Tier 3 — Peripheral.** Background or adjacent literature, kept for completeness or scoping.

When uncertain between two tiers, choose the less central tier and explain why. Tier 3 is a normal
and useful result. Do not inflate relevance to justify reading time.

Framework and review papers have their own catalogue section, regardless of importance, and omit a
numeric tier. Label conceptual claims as framing or interpretation. A review may report empirical
findings, but use the primary study before treating an estimate as verified evidence for this project.

Tags are project-defined. Use the configured suggestions and add a useful term when needed; mention
the addition in the report. No closed vocabulary is required.

## 5. Note frontmatter

This is an illustrative shape, not an actual paper or finding. The corresponding filename is
`Author2026_ShortTitle.md`:

```yaml
---
key: Author2026_ShortTitle
citation: "Author (2026)"
title: "Paper title"
venue: "Journal or working-paper series and version"
year: 2026
pdf: "../pdfs/Author2026_ShortTitle.pdf"
tier: 2
tags: [identification, growth]
evidence: empirical
setting: "Population, period and unit of analysis"
one_line: "The most useful contribution to this project, stated after reading."
ingested: 2026-10-02
ingested_by: Codex
---
```

Replace illustrative values with verified metadata. `key` must equal the filename stem. `pdf` is
relative to the note and must resolve locally. `evidence` is one of `empirical`, `theoretical`,
`framework`, `review` or `data`. Omit `tier` for `framework` or `review`. Record the actual ingestion
date and actor: Claude Code, Codex or the human author; do not guess a model version.

## 6. Note structure

Use this order unless the project has an established equivalent:

1. **Title:** `# <citation>: <short title>`.
2. **Reference and reading status:** full citation, local PDF link, public URL when provided or
   verified, page count and exactly what was read. Identify missing appendices, unread pages,
   unreadable figures and any findings taken from the authors' description instead of a table.
3. **Summary:** a paragraph on what the paper does and concludes, without a preamble.
4. **Setting, data and measurement:** population, period, sample sizes and construction of key
   variables. For theory, describe the environment.
5. **Methodology and identification:** §7. Required.
6. **Relevance to this project:** §8. Required.
7. **What does not transfer:** honest limits; required and never empty.
8. **Open questions for us:** unresolved decisions for the student.
9. **Section map:** where to find material on rereading.

Give a section, table, figure or page pointer for each reported quantity. Read appendices and
supplementary material; do not claim full coverage if they are unavailable. A summary based only on
an abstract or search result is not a completed ingestion.

## 7. Methodology and identification

State:

- The design: RD, DiD, IV, event study, structural estimation, selection on observables, or none.
- The identifying assumption as the authors state it, accurately paraphrased or briefly quoted
  where permitted, with a source pointer. Distinguish your interpretation from their claim.
- Their supporting checks: pre-trends, placebos, balance, falsification and overidentification.
- Your assessment of the assumption's strength and how it compares with this project's design.

For theoretical and structural work, give the model structure, consequential assumptions,
calibration versus derivation, and which results are model output rather than estimates. A welfare
number from a calibrated model is not a direct measurement.

For frameworks and reviews, distinguish conceptual arguments, illustrative examples and empirical
findings reported from other studies. State when there is no identification design of its own.

## 8. Project relevance

Read configured context and recent history first. Address the project's actual questions, open
decisions, design and threats to validity. A relevance section that would fit any project is too
vague.

Use these subsections:

- **What it gives us:** usable parameters, designs, measures or framing.
- **What it changes:** implications for open or past decisions. "Nothing at present" is legitimate.
- **Cross-links:** other notes that it supports, extends or contradicts, linked by key.

Do not turn an interpretation into a project decision. Propose consequential follow-up actions for
the student to accept. Do not exaggerate relevance.

## 9. Catalogue and boundaries

The catalogue is the index of ingested papers. Follow `catalogue_mode` and existing project rules.

For a new manual catalogue, group rows by tier and put conceptual/review work in a separate section.
Link paper names to their local notes and include tags, setting and what each contributes:

```markdown
## Tier 1 — Load-bearing

| Paper | Tags | Setting | What it gives us |
| --- | --- | --- | --- |

## Tier 2 — Supporting

## Tier 3 — Peripheral

## Frameworks and reviews

Distinguish conceptual claims from empirical findings; consult primary evidence when needed.
```

For a generated catalogue, update its documented source fields and use the agreed existing command.
Read the command's purpose before running it. If it is missing, fails or would replace manual work,
stop that catalogue update and report the issue; preserve the completed note. Do not delete the
script, remove build targets, strip generated markers or hand-edit generated output as a shortcut.
If manual versus generated ownership is unclear, ask before changing the catalogue.

Boundaries:

- Never commit or push during ingestion. A separate close-session invocation can checkpoint the
  attributable tracked changes locally.
- Never edit a human-maintained review workbook or spreadsheet. Cross-reference it and propose the
  change to the student.
- Never delete or overwrite an existing note without resolving the version decision first.
- Never untrack PDFs, rewrite Git history or force-add ignored files.
- Archive completed-task inbox material only after verifying matching checksums and updating links;
  retain unfinished-task inputs and the `document_dump/` README.
