#!/usr/bin/env python3
"""Dependency-free build checks. No network requests or clinical validation."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urljoin, urlsplit, unquote
import hashlib
import json
import os

ROOT = Path(__file__).resolve().parent
ORIGINS = {'wholemindliving.com': 'wholemind', 'themaxineproject.org': 'maxine',
           'wholemindliving.netlify.app': 'wholemind', 'themaxineproject.netlify.app': 'maxine'}

class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.links, self.ids = [], set()
        self.brand = None
        self.appearance = False
        self.feed(text)
    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if values.get('id'):
            self.ids.add(values['id'])
        if tag == 'html':
            self.brand = values.get('data-brand')
        if tag == 'fieldset' and 'data-appearance' in values:
            self.appearance = True
        for key in ('href', 'src'):
            if values.get(key):
                self.links.append(values[key])


def main():
    pages = {}
    for brand in ('wholemind', 'maxine'):
        root = ROOT / 'dist' / brand
        paths = sorted(root.rglob('*.html'))
        expected_pages = 17 if brand == 'maxine' else 12
        assert len(paths) == expected_pages, f'{brand}: expected {expected_pages} pages, found {len(paths)}'
        for path in paths:
            page = Page(path.read_text(encoding='utf-8'))
            assert page.brand == brand, f'Wrong brand: {path}'
            assert page.appearance, f'Missing appearance control: {path}'
            assert any('appearance-init.js' in link for link in page.links), path
            pages[path.resolve()] = page
    checked = 0
    for path, page in pages.items():
        brand = path.relative_to(ROOT / 'dist').parts[0]
        root = ROOT / 'dist' / brand
        domain = 'wholemindliving.com' if brand == 'wholemind' else 'themaxineproject.org'
        address = 'https://' + domain + '/' + path.relative_to(root).as_posix()
        for value in page.links:
            url = urlsplit(urljoin(address, value))
            target_brand = ORIGINS.get(url.hostname)
            if target_brand is None:
                continue
            target_root = ROOT / 'dist' / target_brand
            target = (target_root / (unquote(url.path).lstrip('/') or 'index.html')).resolve()
            assert target.is_relative_to(target_root.resolve()), f'Unsafe path: {value}'
            if target.is_dir():
                target /= 'index.html'
            if not target.exists() and not target.suffix:
                target = target.with_suffix('.html')
            assert target.is_file(), f'Missing target: {path}: {value}'
            if url.fragment and target.suffix == '.html':
                assert unquote(url.fragment) in pages[target.resolve()].ids, f'Missing anchor: {value}'
            checked += 1
    hashes = json.loads((ROOT / 'BASELINE_PDF_HASHES.json').read_text())
    assert len(hashes) == 6
    for name, expected in hashes.items():
        data = (ROOT / 'downloads' / name).read_bytes()
        assert data.startswith(b'%PDF-'), name
        assert hashlib.sha256(data).hexdigest() == expected, f'Changed PDF: {name}'
        outputs = list((ROOT / 'dist').glob('*/downloads/' + name))
        assert len(outputs) == 1, f'PDF assigned to wrong brands: {name}'
        assert hashlib.sha256(outputs[0].read_bytes()).hexdigest() == expected, name
    publish = ROOT / 'publish'
    if publish.exists():
        deployed = Page((publish / 'index.html').read_text())
        assert deployed.brand in ('wholemind', 'maxine')
        selected_root = ROOT / 'dist' / deployed.brand
        expected_files = {p.relative_to(selected_root) for p in selected_root.rglob('*') if p.is_file()}
        actual_files = {p.relative_to(publish) for p in publish.rglob('*') if p.is_file()}
        assert expected_files == actual_files, 'Publish file set differs from the selected brand'
        for relative in expected_files:
            assert (selected_root / relative).read_bytes() == (publish / relative).read_bytes(), relative
    from test_research import run_checks
    research_checks = run_checks(ROOT)
    from test_meet_maxine import run_checks as memorial_checks_run
    memorial_checks = memorial_checks_run(ROOT)
    from test_family_account import run_checks as account_checks_run
    family_account_checks = account_checks_run(ROOT)
    print(f'PASS: {research_checks} research integrity checks, {memorial_checks} memorial integrity checks, '
          f'{family_account_checks} family account checks.')
    print(f'PASS: {len(pages)} pages, {checked} internal references, six unchanged PDFs, and publish integrity.')

if __name__ == '__main__':
    main()
