#!/usr/bin/env python3
"""Build, check and publish the release index for this repository. Standard library only.

  release_index.py build                 regenerate releases.json from releases/<radio>/*.patch.json + sidecar .md
  release_index.py check                 releases.json is current, sidecars are well formed, docs links resolve,
                                         and nothing from the private firmware repos has leaked into a public page
  release_index.py publish --radio R --patch P --notes N [--docs D] [--date YYYY-MM-DD]
                                         add one release (and, with --docs, replace docs/<radio>/), then build and
                                         check. Called by the private firmware repos' release workflows.

A release is two files side by side: the patch, byte for byte as the firmware build wrote it, and a sidecar markdown
file with the same stem. The sidecar starts with a front-matter block of `key: value` lines (one line each) and its
body is the release notes, in the subset Codeplug Studio renders: paragraphs, `- ` bullets, **bold** and `code`.
"""

import argparse
import datetime
import hashlib
import json
import pathlib
import re
import shutil
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
RELEASES = ROOT / 'releases'
DOCS = ROOT / 'docs'
INDEX = ROOT / 'releases.json'
RADIOS = json.loads((ROOT / 'radios.json').read_text())

INDEX_FORMAT = 1
VERSION = re.compile(r'^\d+\.\d+\.\d+(-rc\.\d+)?$')
DATE = re.compile(r'^\d{4}-\d{2}-\d{2}$')
SIDECAR_KEYS = ('version', 'channel', 'stock', 'published', 'summary', 'verify')
NOTES_KEYS = ('summary', 'verify')  # what a private repo's notes master must carry; publish fills in the rest

# Things that belong in the private firmware repos only. A hit fails `check` (and so `publish`).
LEAKS = [
    (re.compile(r'github\.com/pskillen/(anytone-d890-firmware|baofeng-dm32-firmware)'), 'link to a private repo'),
    (re.compile(r'\b0x[0-9A-Fa-f]{6,}\b'), 'memory address'),
    (re.compile(r'ghidra|hooks\.toml|make_patch|gate-result', re.I), 'reverse-engineering or build detail'),
    (re.compile(r'(^|[\s(`])(fw|vendor)/|tools/(?!release_index\.py)'), 'path into a firmware repo'),
]
LINK = re.compile(r'\]\(([^)\s]+)\)')


class Problem(Exception):
    pass


def channel_of(version):
    return 'rc' if '-rc.' in version else 'final'


def parse_sidecar(text, where):
    lines = text.split('\n')
    if not lines or lines[0] != '---' or '---' not in lines[1:]:
        raise Problem(f'{where}: no front-matter block')
    end = lines.index('---', 1)
    meta = {}
    for line in lines[1:end]:
        key, sep, value = line.partition(':')
        if not sep or not key.strip():
            raise Problem(f'{where}: bad front-matter line {line!r}')
        meta[key.strip()] = value.strip()
    body = '\n'.join(lines[end + 1:]).strip('\n') + '\n'
    return meta, body


def render_sidecar(meta, body):
    head = '\n'.join(f'{k}: {meta[k]}' for k in SIDECAR_KEYS)
    return f'---\n{head}\n---\n\n{body.strip()}\n'


def notes_problems(body, where):
    out = []
    for n, line in enumerate(body.split('\n'), 1):
        if '](' in line or '<' in line:
            out.append(f'{where}:{n}: links and HTML are not shown by Studio')
        if line.startswith('#'):
            out.append(f'{where}:{n}: use **bold** lines, not headings')
    return out


def result_roles(patch):
    """Result hashes by role, as Studio names them: one image is 'bin'; a package is keyed by lower-case extension."""
    result = patch['result']
    if 'sha256' in result:
        return {'bin': result['sha256']}
    return {ext.lstrip('.').lower(): v['sha256'] for ext, v in sorted(result.items())}


def build_index():
    rows = []
    for radio, info in RADIOS.items():
        folder = RELEASES / radio
        if not folder.is_dir():
            continue
        patches = sorted(folder.glob('*.patch.json'))
        sidecars = {p.name[:-len('.md')] for p in folder.glob('*.md')}
        stems = {p.name[:-len('.patch.json')] for p in patches}
        for orphan in sorted(sidecars - stems):
            raise Problem(f'releases/{radio}/{orphan}.md has no patch')
        for path in patches:
            stem = path.name[:-len('.patch.json')]
            rel = f'releases/{radio}/{path.name}'
            raw = path.read_bytes()
            patch = json.loads(raw)
            sidecar = folder / f'{stem}.md'
            if not sidecar.is_file():
                raise Problem(f'{rel} has no sidecar {stem}.md')
            meta, body = parse_sidecar(sidecar.read_text(), f'releases/{radio}/{stem}.md')
            missing = [k for k in SIDECAR_KEYS if not meta.get(k)]
            if missing:
                raise Problem(f'releases/{radio}/{stem}.md: missing {", ".join(missing)}')
            version = meta['version']
            checks = [
                (VERSION.match(version), f'version {version!r} is not X.Y.Z or X.Y.Z-rc.N'),
                (patch.get('version') == version, f'patch says version {patch.get("version")!r}'),
                (patch.get('name') == info['patchName'], f'patch name {patch.get("name")!r} is not this radio\'s'),
                (stem == info['assetPrefix'] + version, f'file name should be {info["assetPrefix"]}{version}'),
                (meta['channel'] == channel_of(version), f'channel should be {channel_of(version)}'),
                (meta['stock'] == info['stockVersion'], f'stock should be {info["stockVersion"]!r}'),
                (DATE.match(meta['published']), 'published is not YYYY-MM-DD'),
            ]
            for ok, why in checks:
                if not ok:
                    raise Problem(f'{rel}: {why}')
            rows.append({
                'radioId': radio,
                'version': version,
                'channel': meta['channel'],
                'patchName': patch['name'],
                'patchFile': path.name,
                'patchPath': rel,
                'patchSha256': hashlib.sha256(raw).hexdigest(),
                'stockVersion': meta['stock'],
                'publishedOn': meta['published'],
                'summary': meta['summary'],
                'verifyHint': meta['verify'],
                'resultSha256': result_roles(patch),
                'notesPath': f'releases/{radio}/{stem}.md',
                'notes': body,
            })
    rows.sort(key=lambda r: (r['radioId'], r['publishedOn'], [int(x) for x in re.findall(r'\d+', r['version'])]),
              reverse=True)
    rows.sort(key=lambda r: r['radioId'])
    return {'format': INDEX_FORMAT, 'releases': rows}


def serialise(index):
    return json.dumps(index, indent=2, ensure_ascii=False) + '\n'


def public_pages():
    yield from sorted(ROOT.glob('*.md'))
    yield from sorted(DOCS.rglob('*.md'))
    yield from sorted(RELEASES.rglob('*.md'))


def check():
    problems = []
    try:
        index = build_index()
    except Problem as e:
        return [str(e)]
    if not INDEX.is_file() or INDEX.read_text() != serialise(index):
        problems.append('releases.json is out of date: run tools/release_index.py build')
    for row in index['releases']:
        problems += notes_problems(row['notes'], row['notesPath'])
    for page in public_pages():
        rel = page.relative_to(ROOT)
        text = page.read_text()
        for n, line in enumerate(text.split('\n'), 1):
            for pattern, why in LEAKS:
                if pattern.search(line):
                    problems.append(f'{rel}:{n}: {why}: {line.strip()[:100]}')
            for target in LINK.findall(line):
                if re.match(r'^[a-z]+:', target) or target.startswith('#'):
                    continue
                dest = (page.parent / target.split('#')[0]).resolve()
                if not dest.exists() or ROOT not in dest.parents and dest != ROOT:
                    problems.append(f'{rel}:{n}: broken link {target}')
    return problems


def publish(args):
    if args.radio not in RADIOS:
        raise Problem(f'unknown radio {args.radio!r}; known: {", ".join(RADIOS)}')
    info = RADIOS[args.radio]
    raw = pathlib.Path(args.patch).read_bytes()
    patch = json.loads(raw)
    version = patch.get('version', '')
    if not VERSION.match(version):
        raise Problem(f'patch version {version!r} is not a release version')
    meta, body = parse_sidecar(pathlib.Path(args.notes).read_text(), args.notes)
    missing = [k for k in NOTES_KEYS if not meta.get(k)]
    if missing:
        raise Problem(f'{args.notes}: missing {", ".join(missing)}')
    problems = notes_problems(body, args.notes)
    if problems:
        raise Problem('\n'.join(problems))

    folder = RELEASES / args.radio
    folder.mkdir(parents=True, exist_ok=True)
    stem = info['assetPrefix'] + version
    dest = folder / f'{stem}.patch.json'
    if dest.exists() and dest.read_bytes() != raw:
        raise Problem(f'{dest.relative_to(ROOT)} is already published with different bytes; releases never change')
    dest.write_bytes(raw)
    sidecar = folder / f'{stem}.md'
    published = args.date
    if sidecar.exists():  # a re-run keeps the first publication date
        published = parse_sidecar(sidecar.read_text(), str(sidecar))[0].get('published') or published
    sidecar.write_text(render_sidecar({
        'version': version, 'channel': channel_of(version), 'stock': info['stockVersion'],
        'published': published, 'summary': meta['summary'], 'verify': meta['verify'],
    }, body))

    if args.docs:
        src = pathlib.Path(args.docs)
        if not (src / 'README.md').is_file():
            raise Problem(f'{src} has no README.md')
        target = DOCS / args.radio
        if target.exists():
            shutil.rmtree(target)
        shutil.copytree(src, target, ignore=shutil.ignore_patterns('releases'))

    INDEX.write_text(serialise(build_index()))
    print(f'published {args.radio} {version}')


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest='cmd', required=True)
    sub.add_parser('build')
    sub.add_parser('check')
    p = sub.add_parser('publish')
    p.add_argument('--radio', required=True)
    p.add_argument('--patch', required=True)
    p.add_argument('--notes', required=True, help='notes master with summary and verify front matter')
    p.add_argument('--docs', help='folder that replaces docs/<radio>/ (its releases/ subfolder is skipped)')
    p.add_argument('--date', default=datetime.datetime.now(datetime.timezone.utc).date().isoformat())
    args = ap.parse_args()
    try:
        if args.cmd == 'build':
            INDEX.write_text(serialise(build_index()))
        elif args.cmd == 'publish':
            publish(args)
        if args.cmd in ('check', 'publish'):
            problems = check()
            if problems:
                print('\n'.join(problems), file=sys.stderr)
                return 1
            print('check: OK')
    except Problem as e:
        print(f'error: {e}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
