# 3 — Turn your Beamer deck into an HTML presentation

Use the supplied `beamer-to-html` skill on a deck of your choice, compare the result with the PDF,
then adapt the skill to your preferences. You can use your own deck or the optional
[sample deck](fallback/sample-deck/README.md).

## Inputs and tools on macOS

Bring the deck’s whole folder: `.tex` files, figures, `.bib` and the compiled PDF if available.
A browser is required. `latexmk` is needed to compile missing PDFs; Poppler helps convert PDF/EPS
figures and drawings. The fallback already includes its PDF, so recompiling it is optional.
The skill template loads KaTeX from a CDN for maths and needs internet when opening the page.

Ask the agent to inspect installed tools first. If needed, MacTeX supplies LaTeX and `latexmk`;
Homebrew users can install Poppler with `brew install poppler`. Do not install a large toolchain
just to try the small fallback: use the supplied PDF and tell the agent about unavailable tools.
See [MacTeX](https://tug.org/mactex/) and [Homebrew](https://brew.sh/) for installation guidance.

## Steps

1. Copy the **whole** `skills/claude/beamer-to-html/` folder to `.claude/skills/beamer-to-html/`,
   or `skills/codex/beamer-to-html/` to `.agents/skills/beamer-to-html/`. Check for an existing
   version before copying. Follow the [skill installation guide](../../skills/README.md#install-a-selected-skill).
2. Copy your deck folder into `document_dump/<my-deck>/`. If you lack one, copy
   `exercises/03-beamer-to-html/fallback/sample-deck/` to `document_dump/sample-deck/`.
3. Invoke `/beamer-to-html` (Claude Code) or `$beamer-to-html` (Codex):

   > Use the beamer-to-html skill to convert the deck in `document_dump/<my-deck>/` into
   > `outputs/03-beamer-to-html/<my-deck>-html/`. Keep my source files unchanged. Report anything
   > you could not convert.

4. Open the resulting `index.html`. Compare equations and numbering, figures, table values,
   citations, titles and slide order with the PDF. Try the menu, Previous/Next and arrow keys.
5. Pick one preference to change. Ask the agent to edit the installed `CONVERSION.md` rule or
   `assets/template.html` style, rerun and check the result again.

## Optional worked conversion

If you hit a usage limit, inspect [sample-html/index.html](fallback/sample-html/index.html) beside
the sample PDF and read its [conversion report](fallback/sample-html/REPORT.md). It demonstrates
the expected output, but making and testing your own change to the skill remains the activity.

## Finish

Keep the HTML and its assets together under `outputs/03-beamer-to-html/`. Each frame should have
one HTML slide, with section dividers added where appropriate. Record overlays flattened, items
rendered from PDF and any unsupported content. Archive the inbox copy of your deck with verified
checksums after completing the task, following the [activity index](../README.md).
