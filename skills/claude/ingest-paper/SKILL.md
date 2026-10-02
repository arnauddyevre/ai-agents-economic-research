---
name: ingest-paper
description: "File an academic PDF, read its full text and appendices, write a detailed project-relevance note and update the literature catalogue. Use when asked to ingest, file or summarise a paper; establish storage and tracking conventions on first use."
---

# Ingest paper

Read the bundled [CONVENTIONS.md](CONVENTIONS.md) before filing a paper. It defines the layout,
tracking choices, note structure and catalogue. This is Arnaud's research-reading workflow adapted
for student projects.

## 1. Resolve the project and paper

Read shared project context. Use the literature configuration named there; for a new setup use
root-level `literature.json`, shared by both agents. An existing `.claude/literature.json` remains
supported; do not move it or create a competing config merely for neutrality.

On first setup, follow CONVENTIONS.md section 1: inspect existing folders and catalogue tooling, then
ask the student to confirm the layout, PDF tracking and catalogue conventions together. The default
for this workshop is local literature under `outputs/literature/`, whose outputs remain ignored.
Do not untrack existing PDFs or delete a catalogue generator. An older config missing the tracking
or catalogue choices also needs those choices confirmed before changing them.

Use the provided PDF path. For a partial title, search the configured library, `document_dump/` and
project root; confirm ambiguous matches. Do not search personal folders outside the project without
a supplied location. With no target, list unnoted papers in the library and ask which to ingest.
Process a batch one paper at a time.

If the linked document's full text is inaccessible, ask the student to provide the PDF. Do not
substitute snippets, summaries, mirrors or translations, or describe a partial reading as complete.

## 2. Check and file

Check that the PDF can be read and obtain its page count with available PDF tooling. The procedure
is OS-neutral; do not run macOS-only metadata commands or clear quarantine/permissions routinely.
If access fails, explain the actual problem and request a readable copy or an authorised fix.

Check title, authors, year and identifiers against the catalogue for duplicates or new versions.
Ask before replacing a note or deciding between versions. Find any companion appendices and include
them in the reading plan.

Copy the PDF into the configured library, following its naming examples. First check whether its
current name is referenced in a note, catalogue or tracked file; preserve referenced names. Never
overwrite a different file. Verify the copy's SHA-256 against the original. Leave inbox originals
until the task's archive-and-cleanup procedure has completed; never remove an outside-project source.

## 3. Read comprehensively

Extract searchable text with available tools, for example `pdftotext`, into the task's local working
folder. Map the structure, then read all sections and appendices, including tables and figures.
Use PDF rendering when extraction omits evidence; disclose any unread or inaccessible parts.
Record section, table, figure and page pointers as you read. A main-text-only note cannot claim
comprehensive coverage.

## 4. Write the note

Read the configured shared context and recent history so relevance addresses this project's current
questions. Use CONVENTIONS.md sections 4–8 for the note, tier and tags. Explain methodology and the
authors' identifying assumptions, distinguish calibrated model output from estimates, state what
transfers to this project and what does not, and link related notes by key.

Never inflate relevance to reward the effort of reading. Tier 3 and "this changes nothing for us"
are useful judgements. Mark conceptual claims as such, rather than empirical evidence.

## 5. Catalogue and handoff

Update the catalogue through the agreed manual or generated workflow in CONVENTIONS.md section 9.
Do not replace existing tooling. Draft any consequential changes to the project's research plan for
the student to accept; do not silently convert your interpretation into a project decision.
Record completed ingestion work in the agreed shared history, or supply a proposed entry if that
project reserves logging for the student.

For inputs from `document_dump/`, follow the shared README: archive completed-task documents and
notes under `outputs/archive/<task>/`, verify matching SHA-256 checksums, update references, then remove
the verified inbox copies. Keep the library and note links valid; retain the inbox README and
unfinished-task inputs. If the PDF already has a verified archive, reference it rather than create
another. Archive cleanup must never delete the only copy.

Report the paper in a sentence, tier and rationale, two or three project-relevant findings, effects
on open decisions, paths to the note and catalogue, reading gaps and unresolved issues. On setup,
also report the agreed layout, tracking and catalogue choices.

Do not commit or push; `/close-session` can checkpoint later if installed. Do not modify a
human-maintained review workbook or spreadsheet. Do not rewrite Git history or force-add ignored
files.

**Inspect and adapt:** review the relevance tiers, naming and metadata in CONVENTIONS.md. Agree your
project's storage and tracking choices before the first ingestion.
