#!/usr/bin/env python3
"""Build checks for the Maxine-only, print-friendly family-history guide."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def run_checks(root=ROOT):
    checked = 0

    def check(ok, message):
        nonlocal checked
        assert ok, message
        checked += 1

    for mode in ('dist', 'preview'):
        base = root / mode
        path = base / 'maxine' / 'resources' / 'preserving-their-story.html'
        check(path.is_file(), mode + ': missing family guide')
        check(not (base / 'wholemind' / 'resources' / 'preserving-their-story.html').exists(),
              mode + ': guide leaked to WholeMind')
        html = path.read_text(encoding='utf-8')
        check(html.count('<h1>') == 1 and '<form' not in html and '<img ' not in html,
              mode + ': malformed guide or unnecessary data/image collection')
        check('<meta name="robots" content="noindex, nofollow">' in html,
              mode + ': review indexing boundary removed')
        check('Preserving Their Story' in html and
              'permission to copy or share it?' in html and
              'not a memory test or clinical tool' in html,
              mode + ': guide content or publication-consent note missing')
        check(html.count('data-worksheet') == 5 and 'data-print hidden' in html,
              mode + ': worksheet or print control missing')
        check('href="../downloads/' not in html,
              mode + ': nonexistent PDF download offered')
        check('Use the browser’s Print command to print or save a PDF.' in html,
              mode + ': print-only instructions missing')
        check('https://themaxineproject.org/resources/preserving-their-story.html' in html,
              mode + ': guide canonical missing')
        for entry in ('index.html', 'resources.html'):
            maxine = (base / 'maxine' / entry).read_text(encoding='utf-8')
            wholemind = (base / 'wholemind' / entry).read_text(encoding='utf-8')
            check('resources/preserving-their-story.html' in maxine,
                  mode + ': missing Maxine resource card in ' + entry)
            check('resources/preserving-their-story.html' not in wholemind,
                  mode + ': cross-brand resource leak in ' + entry)
        account = (base / 'maxine' / 'family-account.html').read_text(encoding='utf-8')
        check('id="elkhart-memories"' in account and 'two doves' in account,
              mode + ': Elkhart family recollection missing')
    return checked


if __name__ == '__main__':
    print(f'PASS: {run_checks()} family memory guide checks')
