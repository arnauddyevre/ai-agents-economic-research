---
name: beamer-to-html
description: "Convert a LaTeX Beamer deck (the folder holding its .tex files) into a local, scrolling HTML presentation with a section menu, slide navigation, rendered maths and per-slide references. Use when the user asks to turn Beamer or TeX slides into an HTML page. Never edits the TeX sources."
---

# Beamer to HTML

Turn a Beamer deck into one local HTML page: slides scroll vertically, a menu on the right lists the
sections, a ribbon shows progress, and the arrow keys move between slides. The look comes from
`assets/template.html` in this skill's folder; the conversion rules are in `CONVERSION.md`.

The source folder is read-only. Everything you produce goes in the output folder.

## 1. Locate the inputs

1. The user gives a folder (or a `.tex` file). Find the entry point: the file with
   `\documentclass{beamer}` (or `[…]{beamer}`). If several exist, list them and ask.
2. Follow every `\input`, `\include` and `\subfile` from the entry point, in order. These files,
   not the folder listing, define the deck.
3. Collect what the deck depends on: `\graphicspath` and figure files; `.bib` and `.bbl` files;
   `\newcommand` / `\renewcommand` / `\DeclareMathOperator` definitions; `\usetheme`, `\definecolor`,
   `\setbeamercolor` and any local theme `.sty` files.
4. Find the compiled PDF next to the entry point. It is the reference for what the slides look like,
   for equation numbers, for citation text and for rendering TikZ drawings. If there is none, compile
   into a scratch directory so the source folder stays clean:
   `latexmk -pdf -interaction=nonstopmode -outdir=<scratch> <entry>.tex`. If compilation fails or no
   LaTeX installation exists, tell the user and continue without the PDF, noting what cannot be
   checked.

## 2. Report an inventory and ask before building

Tell the user, briefly:

- number of frames, sections and PDF pages;
- figures (and how many are PDF/EPS that need converting), tables, display equations;
- TikZ or pgfplots drawings, overlays (`\pause`, `\only`, `<2->`), notes, appendix frames;
- custom macros and theme colours found;
- the output folder you propose: `<deck-folder-name>-html/` next to the source folder.

Ask only about real choices: whether to include the appendix, which colours to use if the theme is
ambiguous, whether to overwrite an existing output folder. Do not install software without asking.
For a short deck with no ambiguity, state the plan and proceed.

## 3. Build

1. Create the output folder with `index.html` and an `assets/` subfolder.
2. Copy `assets/template.html` from this skill into `index.html`. Fill `{{TITLE}}`, `{{SHORT_TITLE}}`,
   the colour tokens in `:root`, the KaTeX `macros`, the contents menu and the slides, following
   `CONVERSION.md`. Remove the KaTeX tags if the deck has no maths.
3. Copy or convert every figure into `assets/` and refer to it with a relative path.
4. Convert frame by frame, in source order. Keep all content: every claim, number, qualification,
   equation, figure, table and citation. Do not summarise, merge or reorder slides. If something
   cannot be converted, keep its place with a visible placeholder (`<p class="small-note">[Not
   converted: …]</p>`) and list it in the report.

## 4. Check

Open `index.html` in a browser, or take screenshots with a headless browser if one is available
(for example `chrome --headless --screenshot`). Check, and fix what fails:

- **Count**: one HTML slide per frame, plus divider slides; same order and titles. Frames with
  overlays (`\pause`, `<2->`) span several PDF pages but give one HTML slide.
- **Maths**: no red KaTeX error text (search the rendered page for `katex-error`); equation numbers
  match the PDF.
- **Figures**: every image loads; proportions look right; no figure is missing.
- **Text**: compare at least five slides word by word with the PDF, including the densest one.
- **Layout**: readable at a laptop width (about 1400 px) and a narrow width (about 900 px); no
  horizontal scrolling; the menu jumps to the right slide; previous/next and the arrow keys work.

## 5. Report

Give the path to `index.html`, the slide count against the source, and a short list of:

- frames with flattened overlays, rendered TikZ, or placeholders;
- anything you changed in form (for example, colours you chose);
- checks you could not run.

Do not claim a check passed unless you ran it.

## Make it yours

This skill is a starting point. After each deck you convert:

- note a specific failure (a wrong symbol, a missing figure, a layout you dislike);
- fix the rule that allowed it in `CONVERSION.md`, or the style in `assets/template.html`;
- rerun the conversion and check that earlier decks still convert well.

Typical first changes: your own colours and fonts in the template, a rule for a macro you use often,
how you want speaker notes shown, and whether figures should be embedded in the page.
