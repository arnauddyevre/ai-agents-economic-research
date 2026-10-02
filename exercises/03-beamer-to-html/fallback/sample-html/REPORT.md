# Worked conversion report

Source: `../sample-deck/main.tex`, following `sections/content.tex`, `figures/output.png`,
`references.bib` and the compiled `main.pdf`. The output uses the supplied beamer-to-html template.

- **Five source frames**, six PDF pages, **seven HTML slides** including two section dividers.
- The production-function frame’s pause is flattened to its final state (PDF page 3).
- Equation (1), its reference, the two table rows and figure values are preserved.
- The custom maths macro maps to `Y`. KaTeX needs internet to render equations.
- The TikZ diagram is cropped from PDF page 5 into `assets/review.svg`, with alt text; the speaker
  note is kept as an expandable note. The bibliography comes from the compiled `.bbl`.
- No placeholders or omitted source content. Colours use the source’s ink/accent and a white background.

Verification: successful LaTeX rebuild; all six PDF pages rendered and the five final-frame views
inspected; source/HTML counts, titles, order, values, equations, references, image paths and menu
anchors checked. JavaScript parses. The local-file browser preview was blocked by the testing tool,
so interactive navigation, KaTeX rendering and responsive layout still need a visual browser check.

This is a worked example to inspect and adapt, not a claim that arbitrary Beamer input converts
without review. Keep `index.html` and `assets/` together.
