"""Optional, sequential teaching runner. Uses existing CLI authentication.

Run from the student-pack root. Inspect this file before using it; students may instead
build their own runner. Confirm subscription sign-in before a live classroom call.
Source evidence and the optional answer key are never modified.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile

DATA = Path(__file__).resolve().parents[1] / 'data'


def read(path):
    return json.loads(path.read_text())


def write(path, value):
    temporary = path.with_suffix(path.suffix + '.tmp')
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')
    temporary.replace(path)


def digest(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True).encode()).hexdigest()


def validate(response, count):
    if not isinstance(response, dict) or set(response) != {'labels'}:
        raise ValueError('Expected exactly one JSON key: labels')
    labels = response['labels']
    if not isinstance(labels, list) or len(labels) != count or any(x not in ('L', 'U', 'N') for x in labels):
        raise ValueError('Invalid label or wrong batch length')
    return labels


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--client', choices=['codex', 'claude', 'worked'], required=True)
    p.add_argument('--model', help='Exact model ID or a supported client alias; required for live calls')
    p.add_argument('--effort', help='A reasoning effort supported by the chosen model')
    p.add_argument('--cli', help='CLI executable path if the command is not on PATH')
    p.add_argument('--batch-size', type=int, default=3)
    p.add_argument('--limit', type=int, default=3, help='First n pages, 1–90; start with 3')
    p.add_argument('--timeout', type=int, default=180)
    p.add_argument('--output', type=Path, required=True)
    args = p.parse_args()
    if not 1 <= args.limit <= 90 or not 1 <= args.batch_size <= 10 or args.timeout < 1:
        p.error('Use limit 1–90, batch size 1–10 and a positive timeout')
    if args.client != 'worked' and (not args.model or not args.effort):
        p.error('Choose both --model and --effort for live subscription calls')
    # Do not silently switch a classroom subscription run to separately billed API auth.
    if args.client != 'worked':
        names = ('OPENAI_API_KEY', 'CODEX_API_KEY') if args.client == 'codex' else ('ANTHROPIC_API_KEY', 'ANTHROPIC_AUTH_TOKEN', 'CLAUDE_CODE_USE_BEDROCK', 'CLAUDE_CODE_USE_VERTEX', 'CLAUDE_CODE_USE_FOUNDRY')
        if any(os.environ.get(name) for name in names):
            p.error('API credentials are set. Confirm subscription authentication in a clean terminal; no call made.')
    pages = read(DATA / 'pages.json')[:args.limit]
    assert len({page['page_id'] for page in pages}) == len(pages)
    for page in pages:
        assert hashlib.sha256(page['introduction'].encode()).hexdigest() == page['introduction_sha256']
    rubric, wrapper = (DATA / 'prompt.md').read_text(), (DATA / 'wrapper.md').read_text()
    config = {'client': args.client, 'model': args.model, 'effort': args.effort,
              'batch_size': args.batch_size, 'prompt_sha256': hashlib.sha256(rubric.encode()).hexdigest()}
    identity = digest({'config': config, 'pages': pages})
    out = args.output.resolve()
    out.mkdir(parents=True, exist_ok=True)
    result_path = out / 'results.json'
    if result_path.exists():
        result = read(result_path)
        if result.get('run_identity') != identity:
            p.error('Existing output has different inputs/settings. Use a new output folder.')
    else:
        result = {'run_identity': identity, 'settings': config,
                  'notice': 'Copied previous research model decisions; no new model call' if args.client == 'worked' else 'Classroom subscription CLI run; not human ground truth',
                  'pages': []}
        write(result_path, result)
    saved = result['pages']
    if len(saved) > len(pages):
        p.error('Saved results exceed the selected input')
    for page, answer in zip(pages, saved):
        if answer.get('page_id') != page['page_id'] or answer.get('model_label') not in ('L', 'U', 'N'):
            p.error('Saved output does not match the ordered input')
    worked = {x['page_id']: x['research_label'] for x in read(DATA / 'optional-research-labels.json')['labels']} if args.client == 'worked' else None
    executable = args.cli or shutil.which(args.client)
    if worked is None and not executable:
        p.error('CLI command unavailable. Install/sign in or use the optional worked route.')
    try:
        # Empty scratch cwd keeps project context out of classification calls.
        with tempfile.TemporaryDirectory(prefix='workshop-classification-') as scratch:
            for start in range(len(saved), len(pages), args.batch_size):
                batch = pages[start:start + args.batch_size]
                folder = out / f'batch-{start + 1:03d}'
                folder.mkdir(exist_ok=True)
                evidence = [{k: page[k] for k in ('page_id', 'title', 'introduction')} for page in batch]
                write(folder / 'input-manifest.json', {'page_ids': [x['page_id'] for x in batch]})
                write(folder / 'evidence.json', evidence)
                request = rubric + '\n\n' + wrapper + '\n\n' + json.dumps(evidence, ensure_ascii=False)
                (folder / 'request.txt').write_text(request)
                if worked is not None:
                    response = {'labels': [worked[x['page_id']] for x in batch]}
                else:
                    schema_path = folder / 'schema.json'
                    write(schema_path, read(DATA / 'schema.json'))
                    # A fresh path prevents a failed CLI call from reusing an older response.
                    final_response = Path(scratch) / f'final-{start}.json'
                    if args.client == 'codex':
                        command = [executable, 'exec', '--ignore-user-config', '--ephemeral', '--skip-git-repo-check',
                                   '-s', 'read-only', '-m', args.model, '-c', f'model_reasoning_effort="{args.effort}"',
                                   '-c', 'web_search="disabled"', '--disable', 'shell_tool', '--disable', 'unified_exec',
                                   '--output-schema', str(schema_path), '-o', str(final_response), '-']
                    else:
                        # --bare would disable subscription login, so deliberately do not use it.
                        command = [executable, '-p', '--model', args.model, '--effort', args.effort,
                                   '--tools', '', '--strict-mcp-config', '--mcp-config', '{"mcpServers":{}}',
                                   '--setting-sources', '', '--no-session-persistence', '--output-format', 'json',
                                   '--json-schema', json.dumps(read(schema_path))]
                    print(f'Calling {args.client}: pages {start + 1}–{start + len(batch)}', flush=True)
                    try:
                        process = subprocess.run(command, input=request, capture_output=True, text=True,
                                                 cwd=scratch, timeout=args.timeout)
                    except subprocess.TimeoutExpired:
                        raise RuntimeError('CLI timed out. Stopped without labelling this batch.') from None
                    # Logs may contain account metadata: keep them local under ignored outputs/.
                    (folder / 'stdout.log').write_text(process.stdout)
                    (folder / 'stderr.log').write_text(process.stderr)
                    if process.returncode:
                        raise RuntimeError(f'CLI exited {process.returncode}; inspect local batch logs. No automatic retry.')
                    if args.client == 'codex':
                        response = read(final_response)
                    else:
                        envelope = json.loads(process.stdout)
                        if envelope.get('is_error') or 'structured_output' not in envelope:
                            raise RuntimeError('Claude returned an error or no structured output; inspect local logs.')
                        response = envelope['structured_output']
                labels = validate(response, len(batch))
                write(folder / 'response.json', response)
                saved.extend({'page_id': page['page_id'], 'sample_order': page['sample_order'], 'model_label': label}
                             for page, label in zip(batch, labels))
                write(result_path, result)
    except (RuntimeError, ValueError, OSError) as error:
        with (out / 'failures.jsonl').open('a') as stream:
            stream.write(json.dumps({'time': datetime.now(timezone.utc).isoformat(), 'completed': len(saved), 'error': str(error)}) + '\n')
        raise SystemExit(str(error)) from None
    print(f'{len(saved)} validated labels saved in {result_path}')


if __name__ == '__main__':
    main()
