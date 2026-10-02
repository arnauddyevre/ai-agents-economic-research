# Beamer → HTML conversion rules

Read this file before converting. Each rule says what to write in `index.html`. When a conversion
goes wrong, add or correct a rule here; this file is where the skill learns.

## Document structure

| Beamer source | HTML |
| --- | --- |
| `\title`, `\subtitle`, `\author`, `\institute`, `\date` | Title slide: `<section class="slide title-slide" id="title">` with `<h1>`, `<p class="subtitle">`, `<p class="byline">Name <span class="institute">Institute</span></p>`, `<p class="date">`. Also fill `{{TITLE}}` (full title) and `{{SHORT_TITLE}}` (the `[short]` title if given). |
| `\section{X}` | A divider slide `<section class="slide section-divider" id="x">` listing every section; the current one is `<li class="is-current"><h2>X</h2></li>`, the others `<li><a href="#id">Y</a></li>`. Add one `<details>` group to the contents menu. |
| `\subsection` | No slide of its own. Use it only to group links inside the section's menu group. |
| `\begin{frame}{Title}` … `\end{frame}` | `<section class="slide" id="short-slug"><h2>Title</h2>…</section>`. One section per frame, in source order. |
| `[allowframebreaks]` | One section per page of the compiled PDF; titles get ` (1)`, ` (2)`. |
| A frame that only holds `\bibliography` or `thebibliography` | A "References" slide listing every entry as `<li>`, from the `.bbl` file. |
| `[plain]`, `[noframenumbering]`, `[fragile]` | Ignore the option; keep the content. |
| `\appendix` and backup frames | Keep them, after a divider titled "Appendix". |
| `\frametitle`, `\framesubtitle` | `<h2>` and a following `<p class="muted">`. |
| `\note{…}` | `<details class="notes"><summary>Speaker notes</summary>…</details>` at the end of the slide. |

Slide ids: lower-case, hyphenated, unique, from the frame title (`id="identification-strategy"`).
Add every slide to its section's menu group, using its title as the link text.

## Text

| Beamer source | HTML |
| --- | --- |
| `itemize`, `enumerate` | `<ul>`, `<ol>`; nested lists stay nested. |
| `\item[label]` | `<li><strong>label</strong> …</li>`. |
| `\textbf`, `\emph`/`\textit`, `\texttt` | `<strong>`, `<em>`, `<code>`. |
| `\alert{…}`, `\textcolor{accentcolour}{…}` | `<strong class="alert">…</strong>`. Other colours: `<span style="color: …">`, only if the colour carries meaning. |
| `block`, `alertblock`, `exampleblock` | `<div class="block">` (or `class="block alert-block"`) with `<p class="block-title">Title</p>`. |
| `columns` / `column` | `<div class="columns" style="--cols: 2">`, one `<div>` per column. Widths other than equal: `style="grid-template-columns: 3fr 2fr"`. |
| `\vspace`, `\vfill`, `\hfill`, `\centering`, `\pause` spacing | Drop. Layout comes from the CSS. |
| `\pause`, `\only`, `\onslide`, `\uncover`, `\visible`, `<2->` overlays | Show the **final** state of the frame. List the frame in the report as "overlays flattened". |
| `\footnote` | A `<p class="small-note">` just above the references footer. |
| `\href{url}{text}`, `\url{url}` | `<a href="url" target="_blank" rel="noopener noreferrer">text</a>`. |
| Accents and symbols (`\'e`, `\&`, `--`, `---`, ``` `` '' ```, `~`) | The Unicode character: é, &amp;, –, —, “ ”, non-breaking space. |
| Custom text macros (`\newcommand{\muted}[1]{…}`) | Expand them to the HTML they mean (`<span class="muted">…</span>`). |

Keep every claim, number, qualification and example. Do not shorten, summarise or reword. If a
frame is too dense to read, say so in the report; do not cut it on your own.

## Mathematics

The template renders maths with KaTeX. In the HTML, use only `\( … \)` for inline maths and
`\[ … \]` for display maths, so that dollar amounts in the text are never mistaken for maths.

| Beamer source | HTML |
| --- | --- |
| `$…$`, `\(…\)` | `\( … \)` |
| `$$…$$`, `\[…\]`, `equation*` | `\[ … \]` |
| `equation` | `\[ … \tag{n} \]`, with `n` the number printed in the PDF. |
| `align`, `eqnarray` | `\[ \begin{align} … \end{align} \]` with `\tag{n}` on every numbered line and `\notag` on unnumbered lines. Never leave a line untagged: KaTeX would number it from (1). |
| `align*` | `\[ \begin{align*} … \end{align*} \]` |
| `\label`, `\eqref{…}` | Drop `\label`; replace `\eqref` with the printed number, e.g. `(3)`. |
| Math macros (`\newcommand{\E}{\mathbb{E}}`) | Add them to `macros` in the template's KaTeX call: `"\\E": "\\mathbb{E}"`. |
| `\$` in text | The character `$` in plain text. |

Copy maths character for character. Never simplify, rename variables or "fix" an equation.

## Figures and tables

| Beamer source | HTML |
| --- | --- |
| `\includegraphics[…]{file}` | Copy the file to `assets/` and write `<figure><img src="assets/file.png" alt="…"></figure>`. Resolve the file through `\graphicspath`; try `.pdf`, `.png`, `.jpg`, `.eps` when no extension is given. |
| PDF or EPS figure | Convert: `pdftocairo -svg in.pdf assets/name.svg` (sharp) or `pdftoppm -png -r 200 -singlefile in.pdf assets/name`. |
| `width=0.6\linewidth` (or `\textwidth`) | `<img style="width: 60%">`. |
| `\caption` | `<figcaption>`. |
| Alt text | Describe what the figure shows, from its caption and the surrounding text. |
| `tabular`, `booktabs` | `<table class="slide-table">` with `<thead>`/`<tbody>`. Follow the column spec on every cell, header included: `c` → `class="c"`, `r` → `class="r"`, `l` → no class. Add `num` to cells holding numbers. Keep every row, column and number. |
| `tikzpicture`, `pgfplots`, `forest` and other drawings | Browsers cannot run TikZ. Render the drawing from the compiled PDF: `pdftocairo -svg -f N -l N deck.pdf assets/slide-N.svg` (page `N`) and crop with the `viewBox` if needed; otherwise use the whole page image. List these frames in the report. |

## References

| Beamer source | HTML |
| --- | --- |
| `\cite`, `\citet`, `\citep`, `\footcite` | Author–year text as it appears in the PDF, e.g. "Card and Krueger (1994)". |
| Bibliography entries cited on a frame | `<footer class="slide-references"><strong>References</strong><p>Full reference.</p></footer>` at the end of that slide. Take the text from the `.bbl` file if present, else the `.bib` file. |
| Source notes printed at the bottom of a frame | The same footer. |

## Colours

Look for `\definecolor`, `\setbeamercolor` and the theme files in the source folder. Map them to the
template's tokens in `:root`:

- the structure / title colour → `--ink`;
- the `\alert` or accent colour → `--accent`;
- the background, if not white → `--paper`;
- the section-page colour, if any → `--divider-bg`.

Convert `RGB` (0–255) and `rgb` (0–1) definitions to hex. If the deck uses a stock theme with no
custom colours, keep the template's defaults and say so in the report.
