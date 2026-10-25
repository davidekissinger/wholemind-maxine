#!/usr/bin/env python3
"""Meet Maxine review-page integration tests; not genealogical verification."""
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent


class Doc(HTMLParser):
    def __init__(self, html):
        super().__init__(convert_charrefs=True)
        self.h1 = 0
        self.ids = []
        self.links = []
        self.images = 0
        self.forms = 0
        self.robots = []
        self.canonicals = []
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'h1':
            self.h1 += 1
        if 'id' in a:
            self.ids.append(a['id'])
        if tag == 'img':
            self.images += 1
        if tag == 'form':
            self.forms += 1
        if tag == 'a':
            self.links.append(a.get('href', ''))
        if tag == 'meta' and a.get('name') == 'robots':
            self.robots.append(a.get('content'))
        if tag == 'link' and a.get('rel') == 'canonical':
            self.canonicals.append(a.get('href'))


def run_checks(root=ROOT):
    checked = 0
    def check(value, message):
        nonlocal checked
        assert value, message
        checked += 1

    for mode in ('dist', 'preview'):
        base = root / mode
        memorial = base / 'maxine' / 'meet-maxine.html'
        check(memorial.is_file(), mode + ': memorial route missing')
        check(not (base / 'wholemind' / 'meet-maxine.html').exists(),
              mode + ': memorial copied to wrong brand')
        html = memorial.read_text(encoding='utf-8')
        doc = Doc(html)
        check(doc.h1 == 1, mode + ': memorial must have one H1')
        check(len(doc.ids) == len(set(doc.ids)), mode + ': duplicate IDs')
        check(doc.images == 0 and doc.forms == 0, mode + ': no stock portrait or data form')
        check('noindex, nofollow' in doc.robots, mode + ': review indexing boundary removed')
        check('Meet Maxine' in html and 'Doris Maxine (Ratcliff) Boggs' in html,
              mode + ': missing memorial identity')
        check('A verified family photograph may be added' in html,
              mode + ': photograph placeholder missing')
        check('full text of Maxine’s obituary has not yet been recovered' in html,
              mode + ': obituary status inaccurately stated')
        check('It is <strong>his</strong> obituary, not hers.' in html,
              mode + ': Asbury source provenance missing')
        check('https://themaxineproject.org/meet-maxine.html' in doc.canonicals,
              mode + ': canonical address wrong')
        check('href="story.html#family-story"' in html, mode + ': family link missing')
        check('href="research/"' in html, mode + ': research link missing')
        maxine_home = (base / 'maxine' / 'index.html').read_text(encoding='utf-8')
        wholemind_home = (base / 'wholemind' / 'index.html').read_text(encoding='utf-8')
        check('href="meet-maxine.html"' in maxine_home,
              mode + ': memorial homepage entry missing')
        check('href="meet-maxine.html"' not in wholemind_home,
              mode + ': wrong brand navigation')
    return checked


if __name__ == '__main__':
    print(f'PASS: {run_checks()} Meet Maxine integration checks')
