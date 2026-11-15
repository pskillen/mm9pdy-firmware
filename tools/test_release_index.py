#!/usr/bin/env python3
"""Tests for release_index.py. Standard library only: python3 -I tools/test_release_index.py

Each test runs the tool on a temporary copy of this repository, so nothing here touches the real tree. The UV-5R Mini
patches are synthetic: the right shape, made-up hashes.
"""

import hashlib
import json
import pathlib
import shutil
import subprocess
import sys
import tempfile
import unittest

REPO = pathlib.Path(__file__).resolve().parent.parent
MINI = 'baofeng-uv5rmini'
FAKE = 'ab' * 32  # a made-up SHA-256


def mini_patch(version='1.0.0', base='nrf-v0.27', **extra):
    patch = {
        'format': 1,
        'name': 'baofeng-uv5rmini-firmware',
        'version': version,
        'base': base,
        'stock': {'.ufw': {'sha256': 'cd' * 32, 'size': 1}},
        'result': {'.ufw': {'sha256': FAKE, 'size': 1}},
    }
    patch.update(extra)
    return json.dumps(patch, indent=2) + '\n'


NOTES = '---\nsummary: First release.\nverify: The boot screen shows the version.\n---\n\nThe first release.\n'


class Tree:
    """A temporary copy of the repository and a way to run the tool in it."""

    def __init__(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = pathlib.Path(self.tmp.name) / 'repo'
        shutil.copytree(REPO, self.root, ignore=shutil.ignore_patterns('.git', '.github', '.claude', 'tmp',
                                                                         '__pycache__'))
        self.inputs = pathlib.Path(self.tmp.name) / 'inputs'
        self.inputs.mkdir()

    def write(self, name, text):
        path = self.inputs / name
        path.write_text(text)
        return str(path)

    def run(self, *args):
        return subprocess.run([sys.executable, '-I', str(self.root / 'tools' / 'release_index.py'), *args],
                              capture_output=True, text=True)

    def publish(self, *args, patch=None, notes=NOTES, radio=MINI, date='2026-11-20'):
        return self.run('publish', '--radio', radio, '--patch', self.write('p.json', patch or mini_patch()),
                        '--notes', self.write('notes.md', notes), '--date', date, *args)

    def index(self):
        return json.loads((self.root / 'releases.json').read_text())['releases']

    def mini_rows(self):
        return [r for r in self.index() if r['radioId'] == MINI]

    def add_base(self, base_id, layout, stock, label):
        path = self.root / 'radios.json'
        radios = json.loads(path.read_text())
        radios[MINI]['bases'][base_id] = {'layout': layout, 'stockVersion': stock, 'fileLabel': label,
                                          'shows': 'made up'}
        path.write_text(json.dumps(radios, indent=2) + '\n')


class ReleaseIndexTest(unittest.TestCase):
    def setUp(self):
        self.tree = Tree()
        self.addCleanup(self.tree.tmp.cleanup)
        self.folder = self.tree.root / 'releases' / MINI
        if self._testMethodName != 'test_build_leaves_todays_index_unchanged':
            shutil.rmtree(self.folder)
            self.ok(self.tree.run('build'))

    def ok(self, result):
        self.assertEqual(result.returncode, 0, result.stderr)
        return result

    def refused(self, result, needle):
        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertIn(needle, result.stderr)

    # Today's index

    def test_build_leaves_todays_index_unchanged(self):
        before = (REPO / 'releases.json').read_bytes()
        self.ok(self.tree.run('build'))
        self.assertEqual((self.tree.root / 'releases.json').read_bytes(), before)
        self.ok(self.tree.run('check'))

    # A Mini release

    def test_mini_release_names_row_and_to_stock(self):
        self.ok(self.tree.publish('--base', 'nrf-v0.27', '--to-stock', self.tree.write('back.json', '{"base": "nrf-v0.27", "x": 1}\n')))
        stem = 'uv5rmini-fw-1.0.0-nrf-v0.27-hw1.7'
        self.assertTrue((self.folder / f'{stem}.patch.json').is_file())
        sidecar = (self.folder / f'{stem}.md').read_text()
        self.assertIn('\nstock: v0.27 (NRF)\nbase: nrf-v0.27\n', sidecar)
        back = self.folder / 'to-stock' / 'uv5rmini-fw-to-stock-nrf-v0.27-hw1.7-1.0.0.patch.json'
        self.assertEqual(back.read_text(), '{"base": "nrf-v0.27", "x": 1}\n')

        [row] = self.tree.mini_rows()
        self.assertEqual(row['version'], '1.0.0')
        self.assertEqual(row['channel'], 'final')
        self.assertEqual(row['patchName'], 'baofeng-uv5rmini-firmware')
        self.assertEqual(row['patchFile'], f'{stem}.patch.json')
        self.assertEqual(row['patchPath'], f'releases/{MINI}/{stem}.patch.json')
        self.assertEqual(row['stockVersion'], 'v0.27 (NRF)')
        self.assertEqual(row['layout'], 'L2')
        self.assertEqual(row['base'], 'nrf-v0.27')
        self.assertEqual(row['resultSha256'], {'ufw': FAKE})
        self.assertEqual(row['toStock'], {'path': back.relative_to(self.tree.root).as_posix(),
                                          'sha256': hashlib.sha256(back.read_bytes()).hexdigest()})
        self.assertEqual(list(row)[list(row).index('resultSha256') + 1], 'toStock')
        self.assertEqual(row['publishedOn'], '2026-11-20')
        self.assertEqual(list(row)[7:10], ['stockVersion', 'layout', 'base'])
        # Other radios' rows carry neither field.
        self.assertFalse(any('layout' in r or 'base' in r or 'toStock' in r
                             for r in self.tree.index() if r['radioId'] != MINI))

    def test_row_without_to_stock_has_no_field(self):
        self.ok(self.tree.publish('--base', 'nrf-v0.27'))
        [row] = self.tree.mini_rows()
        self.assertNotIn('toStock', row)

    def test_republishing_the_same_bytes_is_fine(self):
        back = self.tree.write('back.json', '{"base": "nrf-v0.27"}\n')
        self.ok(self.tree.publish('--base', 'nrf-v0.27', '--to-stock', back))
        self.ok(self.tree.publish('--base', 'nrf-v0.27', '--to-stock', back, date='2026-12-01'))
        [row] = self.tree.mini_rows()
        self.assertEqual(row['publishedOn'], '2026-11-20')

    def test_two_bases_of_one_version_are_two_rows(self):
        self.ok(self.tree.publish('--base', 'nrf-v0.27'))
        self.ok(self.tree.publish('--base', 'nrfb-v0.04', patch=mini_patch(base='nrfb-v0.04')))
        rows = self.tree.mini_rows()
        self.assertEqual(sorted((r['version'], r['base'], r['layout']) for r in rows),
                         [('1.0.0', 'nrf-v0.27', 'L2'), ('1.0.0', 'nrfb-v0.04', 'L1')])

    def test_shared_docs_follow_versions_and_keep_other_base_candidate(self):
        docs = self.tree.inputs / 'docs'
        docs.mkdir()
        page = docs / 'README.md'
        (docs / 'install.md').write_text('# Install\n')
        page.write_text('# Mini\n\nNew features.\n')
        self.ok(self.tree.publish('--base', 'nrf-v0.27', '--docs', str(docs),
                                  patch=mini_patch('1.0.1-rc.2')))
        self.ok(self.tree.publish('--base', 'nrf-v0.27', '--docs', str(docs),
                                  patch=mini_patch('1.0.1-rc.10')))
        rc = self.tree.root / 'docs' / 'rc' / MINI / 'README.md'
        self.assertIn('Release candidate docs: 1.0.1-rc.10', rc.read_text())
        page.write_text('# Mini\n\nOlder features.\n')
        self.ok(self.tree.publish('--base', 'nrfb-v0.04', '--docs', str(docs),
                                  patch=mini_patch('1.0.0', 'nrfb-v0.04')))
        self.assertIn('release candidate 1.0.1-rc.10', rc.read_text())
        page.write_text('# Mini\n\nNew features.\n')
        self.ok(self.tree.publish('--base', 'nrf-v0.27', '--docs', str(docs), patch=mini_patch('1.0.1')))
        self.assertFalse(rc.exists())
        stable = self.tree.root / 'docs' / MINI / 'README.md'
        self.assertIn('Firmware V0.04, Hardware V1.7: latest release 1.0.0', stable.read_text())
        self.assertIn('Firmware V0.27, Hardware V1.7: latest release 1.0.1', stable.read_text())
        page.write_text('# Mini\n\nStale content.\n')
        self.ok(self.tree.publish('--base', 'nrfb-v0.04', '--docs', str(docs),
                                  patch=mini_patch('0.9.0', 'nrfb-v0.04')))
        self.assertIn('New features.', stable.read_text())
        self.assertNotIn('Stale content.', stable.read_text())
        self.assertEqual([r['version'] for r in self.tree.mini_rows() if r['base'] == 'nrf-v0.27'],
                         ['1.0.1', '1.0.1-rc.10', '1.0.1-rc.2'])
        before = (self.tree.root / 'releases.json').read_bytes()
        self.ok(self.tree.run('build'))
        self.assertEqual(before, (self.tree.root / 'releases.json').read_bytes())

    def test_wrong_to_stock_rejected_before_writing(self):
        back = self.tree.write('back.json', '{"base": "nrfb-v0.04"}\n')
        self.refused(self.tree.publish('--base', 'nrf-v0.27', '--to-stock', back), 'to-stock patch says base')
        self.assertFalse(self.folder.exists())

    def test_final_does_not_remove_another_bases_candidate(self):
        docs = self.tree.inputs / 'docs'
        docs.mkdir()
        (docs / 'README.md').write_text('# Mini\n')
        (docs / 'install.md').write_text('# Install\n')
        self.ok(self.tree.publish('--base', 'nrfb-v0.04', '--docs', str(docs),
                                  patch=mini_patch('1.0.0-rc.1', 'nrfb-v0.04')))
        self.ok(self.tree.publish('--base', 'nrf-v0.27', '--docs', str(docs), patch=mini_patch('1.0.1')))
        rc = self.tree.root / 'docs' / 'rc' / MINI / 'README.md'
        self.assertIn('release candidate 1.0.0-rc.1', rc.read_text())

    def test_existing_notes_are_immutable(self):
        self.ok(self.tree.publish('--base', 'nrf-v0.27'))
        self.refused(self.tree.publish('--base', 'nrf-v0.27', notes=NOTES.replace('First release.', 'Changed.')),
                     'releases never change')

    def test_to_stock_is_not_a_release(self):
        """A to-stock patch belongs to a release and does not need its own sidecar."""
        self.ok(self.tree.publish('--base', 'nrf-v0.27', '--to-stock', self.tree.write('back.json', '{"base": "nrf-v0.27"}\n')))
        (self.folder / 'to-stock' / 'stray.patch.json').write_text(mini_patch())
        self.refused(self.tree.run('build'), 'stray.patch.json has no matching release')

    def test_check_refuses_changed_or_missing_to_stock(self):
        self.ok(self.tree.publish('--base', 'nrf-v0.27', '--to-stock', self.tree.write('back.json', '{"base": "nrf-v0.27"}\n')))
        back = self.folder / 'to-stock' / 'uv5rmini-fw-to-stock-nrf-v0.27-hw1.7-1.0.0.patch.json'
        back.write_text('{"changed": true}\n')
        self.refused(self.tree.run('check'), 'releases.json is out of date')
        back.unlink()
        self.refused(self.tree.run('check'), 'releases.json is out of date')

    def test_refuses_bad_to_stock_json_and_wrong_base(self):
        self.ok(self.tree.publish('--base', 'nrf-v0.27', '--to-stock', self.tree.write('back.json', '{"base": "nrf-v0.27"}\n')))
        back = self.folder / 'to-stock' / 'uv5rmini-fw-to-stock-nrf-v0.27-hw1.7-1.0.0.patch.json'
        back.write_text('{bad')
        self.refused(self.tree.run('check'), 'invalid JSON')
        back.write_text('{"base": "wrong"}')
        self.refused(self.tree.run('check'), "patch says base 'wrong'")

    def test_check_link_checks_pages_pointing_at_to_stock(self):
        self.ok(self.tree.publish('--base', 'nrf-v0.27', '--to-stock', self.tree.write('back.json', '{"base": "nrf-v0.27"}\n')))
        docs = self.tree.root / 'docs' / MINI
        docs.mkdir(parents=True, exist_ok=True)
        page = docs / 'README.md'
        page.write_text('# Mini\n\n[Back to stock](../../releases/baofeng-uv5rmini/to-stock/'
                        'uv5rmini-fw-to-stock-nrf-v0.27-hw1.7-1.0.0.patch.json)\n')
        self.ok(self.tree.run('check'))
        page.write_text('# Mini\n\n[Back to stock](../../releases/baofeng-uv5rmini/to-stock/missing.patch.json)\n')
        self.refused(self.tree.run('check'), 'broken link')

    # Refusals

    def test_refuses_a_mini_release_without_base(self):
        self.refused(self.tree.publish(), 'give --base')

    def test_refuses_an_unknown_base(self):
        self.refused(self.tree.publish('--base', 'nrf-v9.99'), 'unknown base')

    def test_refuses_base_on_a_radio_without_bases(self):
        self.refused(self.tree.publish('--base', 'nrf-v0.27', radio='baofeng-dm32uv'), 'have no base')

    def test_refuses_to_stock_on_a_radio_without_bases(self):
        self.refused(self.tree.publish('--to-stock', self.tree.write('back.json', '{"base": "nrf-v0.27"}\n'), radio='baofeng-dm32uv'),
                     'no to-stock')

    def test_refuses_a_patch_on_another_base(self):
        self.refused(self.tree.publish('--base', 'nrf-v0.27', patch=mini_patch(base='nrfb-v0.04')),
                     "patch says base 'nrfb-v0.04'")

    def test_build_refuses_a_sidecar_base_that_disagrees_with_the_patch(self):
        self.ok(self.tree.publish('--base', 'nrf-v0.27'))
        sidecar = self.folder / 'uv5rmini-fw-1.0.0-nrf-v0.27-hw1.7.md'
        sidecar.write_text(sidecar.read_text().replace('stock: v0.27 (NRF)\nbase: nrf-v0.27',
                                                       'stock: v0.04 (NRFB)\nbase: nrfb-v0.04'))
        self.refused(self.tree.run('build'), "patch says base 'nrf-v0.27'")

    def test_build_refuses_a_sidecar_without_base(self):
        self.ok(self.tree.publish('--base', 'nrf-v0.27'))
        sidecar = self.folder / 'uv5rmini-fw-1.0.0-nrf-v0.27-hw1.7.md'
        sidecar.write_text(sidecar.read_text().replace('base: nrf-v0.27\n', ''))
        self.refused(self.tree.run('build'), 'missing base')

    def test_build_refuses_a_version_mismatch(self):
        self.ok(self.tree.publish('--base', 'nrf-v0.27'))
        patch = self.folder / 'uv5rmini-fw-1.0.0-nrf-v0.27-hw1.7.patch.json'
        patch.write_text(mini_patch(version='1.0.1'))
        self.refused(self.tree.run('build'), "patch says version '1.0.1'")

    def test_build_refuses_a_wrong_stock(self):
        self.ok(self.tree.publish('--base', 'nrf-v0.27'))
        sidecar = self.folder / 'uv5rmini-fw-1.0.0-nrf-v0.27-hw1.7.md'
        sidecar.write_text(sidecar.read_text().replace('v0.27 (NRF)', 'v0.04 (NRFB)'))
        self.refused(self.tree.run('build'), "stock should be 'v0.27 (NRF)'")

    def test_build_refuses_a_file_name_without_the_label(self):
        self.ok(self.tree.publish('--base', 'nrf-v0.27'))
        for ext in ('.patch.json', '.md'):
            (self.folder / f'uv5rmini-fw-1.0.0-nrf-v0.27-hw1.7{ext}').rename(self.folder / f'uv5rmini-fw-1.0.0{ext}')
        self.refused(self.tree.run('build'), 'file name should be uv5rmini-fw-1.0.0-nrf-v0.27-hw1.7')

    def test_refuses_changed_patch_bytes(self):
        self.ok(self.tree.publish('--base', 'nrf-v0.27'))
        self.refused(self.tree.publish('--base', 'nrf-v0.27', patch=mini_patch(extra=1)), 'releases never change')

    def test_refuses_changed_to_stock_bytes(self):
        self.ok(self.tree.publish('--base', 'nrf-v0.27', '--to-stock', self.tree.write('back.json', '{"base": "nrf-v0.27"}\n')))
        self.refused(self.tree.publish('--base', 'nrf-v0.27', '--to-stock', self.tree.write('back.json', '{"base": "nrf-v0.27", "changed": true}\n')),
                     'to-stock/uv5rmini-fw-to-stock-nrf-v0.27-hw1.7-1.0.0.patch.json is already published')
        back = self.folder / 'to-stock' / 'uv5rmini-fw-to-stock-nrf-v0.27-hw1.7-1.0.0.patch.json'
        self.assertEqual(back.read_text(), '{"base": "nrf-v0.27"}\n')

    def test_leaks(self):
        page = self.tree.root / 'docs' / 'leak.md'
        for text in ('see github.com/pskillen/baofeng-uv5rmini-firmware', 'github.com/pskillen/retevis-rt95-firmware',
                     'from radio-data/'):
            page.write_text(text + '\n')
            self.refused(self.tree.run('check'), 'leak.md:1')


if __name__ == '__main__':
    unittest.main()
