"""Build the optional offline review example from the supplied JSON formats."""
import argparse
import hashlib
import json
from pathlib import Path


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--pages', type=Path, required=True)
    p.add_argument('--results', type=Path, required=True)
    p.add_argument('--output', type=Path, required=True)
    args = p.parse_args()
    pages = json.loads(args.pages.read_text())
    results = json.loads(args.results.read_text())
    rows = results['pages']
    labels = {x['page_id']: x['model_label'] for x in rows}
    if len(labels) != len(rows) or set(labels) != {x['page_id'] for x in pages}:
        p.error('Missing, duplicated or unknown page IDs: results must cover the source input exactly')
    if any(x not in ('L', 'U', 'N') for x in labels.values()):
        p.error('Invalid model label')
    data = {'notice': results.get('notice', 'Model decisions, not human ground truth'),
            'pages': [{**page, 'model_label': labels[page['page_id']]} for page in pages]}
    data['dataset_id'] = hashlib.sha256(json.dumps(data, sort_keys=True, ensure_ascii=False).encode()).hexdigest()
    # Prevent source article text from ending the script element or introducing HTML.
    payload = json.dumps(data, ensure_ascii=False).replace('<', '\\u003c').replace('>', '\\u003e').replace('&', '\\u0026')
    template = Path(__file__).with_name('review-template.html').read_text()
    assert template.count('__REVIEW_DATA__') == 1
    args.output.parent.mkdir(parents=True, exist_ok=True)
    if args.output.exists():
        p.error('Output exists; choose a new file to keep your previous review')
    args.output.write_text(template.replace('__REVIEW_DATA__', payload))
    print(f'{len(pages)} pages; standalone review saved in {args.output}')


if __name__ == '__main__':
    main()
