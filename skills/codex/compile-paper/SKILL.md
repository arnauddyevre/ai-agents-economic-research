---
name: compile-paper
description: "Compile a selected LaTeX document with the project toolchain or latexmk, diagnose build errors and report references, citations and box warnings. Use for build requests; do not edit manuscript content."
---

# Compile paper

Build a LaTeX document and report its diagnostics. This skill does not edit the source, commit or
open a viewer.

## 1. Choose one entry point

Use a supplied `.tex` path if it exists. Otherwise read the project's documented build command and
look for likely entry points (`paper/main.tex`, `main.tex`, `manuscript.tex`, `paper/manuscript.tex`,
`paper/draft.tex`, `grant.tex`, `cv.tex`). Collect matches rather than selecting the first one.
If needed, search project `.tex` files for `\documentclass`, excluding dependencies and build output.

If more than one plausible target remains and the request does not disambiguate them, list the
candidates and ask which to build. Do not silently prefer `paper/main.tex`. If there is no candidate,
ask for the source. Verify that the selected file is an entry point, not an included chapter.

Record its absolute path, directory and filename. Run the build **from that directory using just the
filename**, so `paper/main.tex` never turns into `paper/paper/main.tex`. Quote paths with spaces using
the active shell's syntax or pass argument arrays to a process runner.

## 2. Select the toolchain

Use an existing project build recipe and its engine. Inspect `.latexmkrc` and the preamble before
assuming pdfLaTeX: fontspec, for example, requires XeLaTeX or LuaLaTeX. Check for the required tools
with a shell-appropriate command (`command -v` in a POSIX shell, `Get-Command` in PowerShell).
Report missing tooling; do not install software implicitly.

With latexmk available, use the documented recipe, or this baseline for a pdfLaTeX project from the
entry-point directory:

```text
latexmk -pdf -interaction=nonstopmode -halt-on-error "main.tex"
```

Here `main.tex` is the selected filename, not a fixed target. Use the corresponding latexmk engine
option when the project requires another engine. Do not enable shell escape unless the project's
trusted build recipe already requires it and the user has authorised that build.

Without latexmk, use the project's TeX engine with `-interaction=nonstopmode -halt-on-error`, then the
bibliography backend indicated by the source and generated files (BibTeX or Biber), followed by two
successful TeX passes. Stop at a failed command. A `.bib` file merely existing in the directory is
not a reason to run a bibliography backend.

## 3. Handle stale output narrowly

A previous `!` line in a log does not prove the cause was stale output. Start with an incremental
build. If diagnostics identify stale generated auxiliaries, clean only generated files attributable
to the selected target, then retry once. Never blanket-delete all auxiliaries in its directory or
subdirectories: another entry point may use them. Do not delete a tracked `.bbl` or any uncertain
file; report it and leave it in place. Preserve source, figures, bibliographies and the last PDF.

Do not change `.tex`, `.sty`, bibliography content or build configuration to make a failing build
pass unless the user separately requests that fix.

## 4. Report

State success or failure from the process exit status and current build evidence; an old PDF on disk
does not establish success. Give the output PDF path on success, errors with useful surrounding
context, distinct unresolved references/citations, and overfull/underfull warning counts when
available. Do not call missing diagnostics a clean build.

**Inspect and adapt:** record your project's entry points, engine and build recipe in the shared
README so both agents use the same command. To checkpoint later, invoke `$close-session`
separately if installed.
