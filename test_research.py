#!/usr/bin/env python3
"""Public research scope and routing checks, not scientific validation."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
import sys

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'src'))
from research import RESEARCH_PAGES, BOUNDARY
from research_references import REFERENCES

class Document(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.headings = 0
        self.canonicals = []
        self.links = []
        self.scripts = []
        self.forms = 0
        self.feed(text)
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'h1': self.headings += 1
        if tag == 'form': self.forms += 1
        if tag == 'script': self.scripts.append(a.get('src', ''))
        if tag == 'a': self.links.append(a.get('href', ''))
        if tag == 'link' and a.get('rel') == 'canonical': self.canonicals.append(a.get('href'))


def run_checks(root=ROOT):
    count = 0
    def check(condition, message):
        nonlocal count
        assert condition, message
        count += 1
    check(len(REFERENCES) == 8, 'Expected eight selected source records')
    check(len({r['id'] for r in REFERENCES}) == 8, 'Duplicate source identifiers')
    check([r['number'] for r in REFERENCES] == list(range(1, 9)), 'Reference ordering')
    for path in RESEARCH_PAGES:
        target = root / 'dist/maxine' / path
        check(target.is_file(), 'Missing research route: ' + path)
        text = target.read_text(encoding='utf-8')
        doc = Document(text)
        check(doc.headings == 1, path + ': expected one primary heading')
        check(doc.forms == 0, path + ': must not collect submissions')
        check(doc.canonicals == ['https://themaxineproject.org/' + path[:-10]], path + ': wrong canonical')
        check('data-appearance' in text and 'research.css' in text, path + ': appearance support')
        check('protocol are not published here' in text, path + ': private-protocol boundary')
        check('independent scientific peer review' in text, path + ': review-status disclosure')
        check(not any('netlify.app' in url for url in doc.links), path + ': temporary domain in navigation')
        check(not any(urlsplit(url).path.lower().endswith(('.pdf', '.docx')) for url in doc.links), path + ': unexpected proposal download')
        check(not any('david@themaxineproject.org' in url for url in doc.links), path + ': unverified mailbox')
        check(not (root / 'dist/wholemind' / path).exists(), 'Research section leaked into other brand')
    for path in ('research/index.html', 'research/synaptic-restoration/index.html'):
        text = (root / 'dist/maxine' / path).read_text(encoding='utf-8')
        check(BOUNDARY in text, 'Missing visible research status')
    library = (root / 'dist/maxine/research/references/index.html').read_text(encoding='utf-8')
    for r in REFERENCES:
        check('id="' + r['id'] + '"' in library, 'Missing citation target')
        if 'doi' in r:
            check('https://doi.org/' + r['doi'] in library, 'Missing primary publication URL')
        else:
            check('R01AG083628' in library and 'not a result, an award to The Maxine Project' in library, 'Grant attribution')
    contact = (root / 'dist/maxine/connect.html').read_text(encoding='utf-8')
    check('id="founder"' in contact, 'Missing founder contact section')
    check('does not currently provide a working message form' in contact, 'Unverified contact must be explicit')
    check('Research &amp; Innovation' in (root / 'dist/maxine/index.html').read_text(), 'Missing research entry point')
    return count

if __name__ == '__main__':
    print(f'PASS: {run_checks()} research integrity checks')
