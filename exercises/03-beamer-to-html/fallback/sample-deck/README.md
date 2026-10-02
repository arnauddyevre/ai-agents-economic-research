# Optional sample Beamer deck

Copy this whole folder to `document_dump/sample-deck/` and use the exercise 3 prompt.
`main.tex` follows `sections/content.tex`, uses `figures/output.png`, reads `references.bib`,
and defines one maths macro. `main.pdf` is supplied, so you can compare without installing LaTeX.
All numerical values are invented teaching examples.

The five source frames produce six PDF pages because the production-function frame has a pause.
The HTML conversion has five content slides plus two section dividers. Compare the final overlay
(page 3), the figure (page 4), TikZ diagram and speaker note (page 5), and references (page 6).

Optional rebuild from this folder: `latexmk -pdf main.tex`.
Keep source inputs unchanged during conversion; use a scratch output directory if recompiling.
