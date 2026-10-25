#!/usr/bin/env python3
"""Build-level checks for the source-conscious Family Account page."""
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent


class Page(HTMLParser):
    def __init__(self, markup):
        super().__init__(convert_charrefs=True)
        self.ids = []
        self.h1s = 0
        self.images = 0
        self.forms = 0
        self.robots = []
        self.canonicals = []
        self.feed(markup)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a:
            self.ids.append(a['id'])
        if tag == 'h1':
            self.h1s += 1
        if tag == 'img':
            self.images += 1
        if tag == 'form':
            self.forms += 1
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
        account = base / 'maxine' / 'family-account.html'
        check(account.is_file(), mode + ': Family Account page is missing')
        check(not (base / 'wholemind' / 'family-account.html').exists(),
              mode + ': Family Account leaked to WholeMind')
        html = account.read_text(encoding='utf-8')
        doc = Page(html)
        check(doc.h1s == 1 and len(doc.ids) == len(set(doc.ids)),
              mode + ': heading or IDs are invalid')
        check(doc.images == 0 and doc.forms == 0,
              mode + ': unapproved imagery or data form detected')
        check('noindex, nofollow' in doc.robots,
              mode + ': review-only indexing boundary changed')
        check('https://themaxineproject.org/family-account.html' in doc.canonicals,
              mode + ': Family Account canonical is incorrect')
        check('maxine-family-hero' in html and 'maxine-portrait-placeholder' in html,
              mode + ': family design does not match the Maxine memorial')
        check('Rev. John Robert Boggs Jr.' in html and 'J. Robert Boggs' in html,
              mode + ': author and minister identifiers are absent')
        check('The Family Account:' in html and "I'll Move Over" in html,
              mode + ': Family Account title is missing')
        check('A partner' in html and 'Carrying the legacy forward' in html.lower().replace('carrying the legacy forward','Carrying the legacy forward'),
              mode + ': narrative sections are missing')
        check('9780964888029' in html and '9780964888012' in html,
              mode + ': ISBN source distinction has been lost')
        check("The book's full text and dedication have not yet been examined" in html,
              mode + ': unverified book-content boundary is missing')
        check('alumni.asburyseminary.edu' in html and 'abebooks.fr' in html,
              mode + ': historical source links missing')
        check('href="meet-maxine.html"' in html and 'href="story.html#family-story"' in html,
              mode + ': family navigation links missing')
        check('href="resources.html"' in html and 'href="research/"' in html,
              mode + ': resource or research call-to-action missing')

        memorial = (base / 'maxine' / 'meet-maxine.html').read_text(encoding='utf-8')
        story = (base / 'maxine' / 'story.html').read_text(encoding='utf-8')
        check(memorial.count('href="family-account.html"') >= 2,
              mode + ': Meet Maxine family-account links not updated')
        check('href="family-account.html"' in story,
              mode + ': shorter founder story is not connected')
        check('family-account.html' in (base / 'maxine' / 'sitemap.xml').read_text(encoding='utf-8'),
              mode + ': dedicated narrative missing from sitemap')

    return checked


if __name__ == '__main__':
    print(f'PASS: {run_checks()} Family Account integrity checks')
