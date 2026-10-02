# 5 — Review the results in HTML

This is the **last in-class exercise**, in “Alleviating the bottleneck (us, humans!)”. Use the pages
and model labels from exercise 4; ask your agent to create a lightweight local HTML review tool.
Your PhD-level judgement is the scarce input, so give it a clear, useful interface.

The workflow follows the instructor’s `idea_space` reviewer: one page at a time, an independent
judgement before the model label is revealed, then a comparison and any revision. You need a browser;
the optional worked example runs offline without a server or another model call.

## Build your tool

Tell your agent the path to your saved exercise 4 results, then use this exact slide prompt:

> Create a local HTML review tool using my classification results and the source pages from exercise 4. Use their existing format; join by page ID, or map ordered labels back to the input manifest if IDs are stored separately. Load every page in its original input order and show one at a time, with its page ID, exact title and the same supplied introduction the model received. Give me large L/U/N buttons, a comment box, previous/next controls and a progress counter. Keep the model's label hidden until I save my own judgement for that page, then reveal it for comparison. Preserve the original model label and my first independent label; save any later revision separately. Let me skip a page and return later, save and resume progress, and export the review as CSV keyed by page ID. Keep unrevealed model labels out of exports too. Add reviewed/unreviewed filters; keep model-label filters and aggregate agreement hidden until all first judgements are recorded. Check that my labels and comments survive navigation, filtering and reopening, and explain how to save them. Keep the source evidence and model outputs unchanged. Do not fetch new Wikipedia text or run another classification. After review, produce a final table with the original model label, my first label, my reviewed label and my comment.

Save your tool and reviews under `outputs/05-review-in-html/`. If your classification run was
incomplete or unavailable, use exercise 4’s **complete worked results**, record the fallback and
leave the optional research key closed while judging.

## Try it and check it

1. Read the first supplied introduction, pick L/U/N and add a comment before revealing the model.
2. Save your first judgement, reveal the model label and consider whether to revise. A revision must
   keep the original model label and first human label intact.
3. Navigate, skip a page and return. Check that comments and labels survive. Test both filters.
4. Save a backup, close and reopen the tool, and check persistence. Browser storage is convenient;
   a downloaded JSON backup is the portable copy if you change browsers, move the file or clear storage.
5. Export CSV. Unanswered pages must have a blank model-label field. After all initial judgements,
   check the final table against the saved review and the exercise 4 page IDs.

Work through as many pages as class time permits and continue later. Agreement with a model measures
consistency, not correctness; disagreements are useful review targets. Do not make a quality claim
from this deliberately balanced sample without a separate representative evaluation.

## Optional worked tool

Open [worked-review.html](fallback/worked-review.html) directly in your browser. It contains all 90
pages and the earlier research model decisions, hidden by the interface until you judge each page.
It contains **no prefilled human labels**. Do not inspect the embedded labels if you want an independent
comparison. This is a learning interface, not a secure assessment.

To use the example with **your own complete runner-format results**, run from the pack root:

```bash
python3 exercises/05-review-in-html/fallback/build_review.py --pages exercises/04-wikipedia-classification/data/pages.json --results outputs/04-wikipedia-classification/full/results.json --output outputs/05-review-in-html/review.html
```

The builder requires one `model_label` per page ID and checks complete coverage; ask your agent to
adapt a copy if your own runner uses a different format. It refuses to overwrite an existing review.
The example’s [template](fallback/review-template.html) is supplied for inspection and adaptation.

## Finish

Keep the HTML, a JSON review backup and CSV export. Preserve the model label, first human label,
reviewed human label and comment as separate fields. Record how to reopen the review and what remains
unreviewed in the shared history. The optional [research answer key](../04-wikipedia-classification/data/optional-research-labels.json)
is available after your independent judgements.
