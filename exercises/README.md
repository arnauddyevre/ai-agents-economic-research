# Workshop activities

These guides follow the five numbered exercises in the **2 October 2026** workshop presentation.
Open the **pack root** in Claude Code or Codex; every prompt’s working path is relative to that root.
Use either agent: you do not need both subscriptions.

| In-class exercise | Output | Supplied material and fallback |
|---|---|---|
| [1 — Connect your tools](01-connect-tools/README.md) | A checked, sourced note | macOS connection routes; fictional message export and worked note if connection is unavailable |
| [2 — Continue from your phone](02-phone-continuation/README.md) | A verified continuation of the local session | Both clients’ pairing steps; account/feature access still required |
| [3 — Beamer to HTML](03-beamer-to-html/README.md) | A local HTML deck and your adapted skill | Complete skill; small Beamer source, PDF and worked HTML conversion |
| [4 — Wikipedia classification](04-wikipedia-classification/README.md) | Saved L/U/N model labels keyed by page ID | 90 frozen V12 pages and active links, exact prompt/wrapper/schema; optional runner, worked results and separate optional research answer key |
| [5 — Review in HTML](05-review-in-html/README.md) | Your independent judgements, revisions and CSV | Build brief using exercise 4 results; optional offline reviewer with no prefilled human labels |

The [model and effort discussion](model-and-effort/README.md) sits between exercises 3 and 4; its
three cases and optional answers match the presentation. It does not need a model call.

[Project context practice](optional/project-context/README.md) and
[prose review](optional/prose-review/README.md) are **optional extensions**, using your own project
note or research paragraph. They are not additional numbered exercises in class. The instructor’s
Zoom and work-expense examples are demonstrations, not student tasks requiring private inputs.

## Shared working method

1. Read the [pack README](../README.md) and [setup guide](../SETUP.md), then the chosen exercise.
2. Keep supplied inputs unchanged. Save work under `outputs/<exercise-folder-name>/`, such as
   `outputs/04-wikipedia-classification/`. Exercise 5 has its own output folder and reads exercise 4’s results.
3. Use [document_dump](../document_dump/README.md) for temporary documents and screenshots. When a
   task is complete, archive inputs and notes under `outputs/archive/<task>/`, verify matching
   SHA-256 checksums and update references before removing inbox copies. Never remove the only copy.
4. Check the output yourself. Record decisions, checks, limitations and next steps in
   [PROJECT_HISTORY.md](../PROJECT_HISTORY.md), so a fresh session can resume from the files.

Start with a three-page classification smoke test, then the full sample if your allowance permits.
Keep the optional research answer key closed until you have judged independently. Fallbacks are
explicitly labelled: a worked output is not evidence that you made a new model call.

The [skills library](../skills/README.md) contains eight complete examples for each client. The
[presentation](../presentation/index.html) is included locally. The [X handout](../handouts/x_readonly_connector_for_agents.md)
is a paid, macOS take-home extension, not a prerequisite for the five exercises.
