# Frozen V12 teaching sample

`pages.json` has 90 English Wikipedia pages in classroom order, with exact titles and introductions
from accepted calls in the completed bulk V12 research packet `v12_full_forty_workers_20260928_v1`.
It uses the 1 August 2026 Wikipedia snapshot (`20260801`). A [clickable page list](page-links.md) is also supplied, without labels. Current web pages may have changed;
classify and review the supplied frozen evidence, rather than replacing it with live text.

The sample contains 30 pages for each **previous model label** L/U/N, selected by seeded reservoir
sampling over page-ID-ordered decisions, then shuffled once (seed `20261002`). Source scope excludes
prior evaluations/pilots, exception recovery and unclassified pages. Its balanced composition is
intentional and is not representative of Wikipedia. The key is a research model’s output
(`gpt-5.6-luna`, high effort), not independently verified human truth.

`sample-manifest.json` records source counts, selected IDs, accepted-call provenance, resource hashes
and the sampling method. Every exported introduction and model label was checked against its accepted
research call. `link-check.json` records the 2 October 2026 Wikipedia API existence check for all 90 IDs.
No research job was restarted and no source research file was changed.

`prompt.md`, `wrapper.md` and `schema.json` are verbatim copies, with these SHA-256 checksums:

| File | SHA-256 |
|---|---|
| prompt.md | `b566a8d76c449924dd465320f9fc5cff45bdb7d2a364a3eb768a0bfe3e4963fc` |
| wrapper.md | `8b4feb441ab76bef9444421dcc536b8ae968ba51522cc053bf2ee6704f34675c` |
| schema.json | `b09c92a0107e876e1eda61199cad6ce8350f3b83db7ab1b41f944a5e4a973b21` |

Keep `optional-research-labels.json` separate from classifier inputs. Open it only after making
independent judgements, if you want to compare your own model and reviews with the research run.

## Attribution and reuse

Article text is by **Wikipedia contributors**, supplied under
[Creative Commons Attribution-ShareAlike 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
Each page includes its source link (`wikipedia_url`). Follow that page’s History tab for contributors;
[Wikipedia’s reuse policy](https://en.wikipedia.org/wiki/Wikipedia:Copyrights#Reusers'_rights_and_obligations)
explains attribution and share-alike requirements. Introductions retain the accepted research evidence
exactly; they are excerpts prepared from the snapshot, rather than full current articles. No article
images are included. Preserve these attributions when sharing the sample or a derived review tool.
