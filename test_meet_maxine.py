#!/usr/bin/env python3
"""Meet Maxine integration checks; not genealogical or clinical verification."""
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent


class Doc(HTMLParser):
    def __init__(self, html):
        super().__init__(convert_charrefs=True)
        self.h1 = 0
        self.ids = []
        self.links = []
        self.styles = []
        self.images = 0
        self.forms = 0
        self.robots = []
        self.canonicals = []
        self.details = []
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
        if tag == 'details':
            self.details.append(a)
        if tag == 'meta' and a.get('name') == 'robots':
            self.robots.append(a.get('content'))
        if tag == 'link' and a.get('rel') == 'canonical':
            self.canonicals.append(a.get('href'))
        if tag == 'link' and a.get('rel') == 'stylesheet':
            self.styles.append(a.get('href'))


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
        check('To me, she was Grandma Boggs.' in html and
              'By David E. Kissinger, BSHA, RN' in html and 'Her grandson' in html,
              mode + ': personal opening or byline missing')
        check('In December 1999' in html and 'I slept in his recliner.' in html and
              'first with his hand and then with her brush' in html,
              mode + ': approved Grace Village recollection missing')
        # Preserve the approved family-review wording, not just the original story.
        story = html.split('id="her-story"', 1)[1].split('<details', 1)[0]
        check('I have come to appreciate the memories of those mornings more as I’ve grown older.' in story,
              mode + ': family-review memory wording missing')
        check('Grandma was only 57 when Alzheimer’s entered her life.' in story,
              mode + ': approved onset-age wording changed')
        check('July 10, 1943' not in story and 'July 10, 1943' in html,
              mode + ': wedding date must remain in source notes, not the narrative')
        check('she and Grandpa had been married for nearly 57 years.' in story,
              mode + ': marriage duration missing')
        check('helpful information about Alzheimer’s, answers to the questions that arise when caring for someone, and a clearer understanding of the research.' in story,
              mode + ': family-review purpose wording missing')
        check('understandable information about Alzheimer’s' not in story and
              'help with the questions that come with caring for someone' not in story,
              mode + ': superseded purpose wording restored')
        check('That’s why her name is here.' not in html and
              '<p>It’s still early. I’m beginning with our family’s story and building from there.</p>' in story,
              mode + ': approved narrative ending changed')
        check('This is one memory of Grandma' in html and 'It isn’t her whole story.' in html,
              mode + ': partial-life-story qualification missing')
        check('Why I started The Maxine Project' in html and
              'It’s still early.' in html, mode + ': first-person purpose or stage missing')
        check('maxine-portrait-placeholder' not in html and
              'What her name asks us to remember' not in html,
              mode + ': impersonal placeholder or slogan reintroduced')
        check('Am I Ready? A Nurse’s Journey Through Change' in html and
              'not a clinical record or a quotation from Maxine' in html,
              mode + ': memoir provenance missing')
        check('The Star Press' in html and 'May 24, 2000' in html,
              mode + ': identified newspaper source missing')
        check('May 22, 2000' in html and 'May 29, 2000' in html,
              mode + ': newspaper date or index discrepancy not disclosed')
        check('a civil death record has not been reviewed' in html,
              mode + ': reported date not distinguished from civil record')
        check('Newspapers.com PDF' in html and 'not published on this website' in html,
              mode + ': source PDF provenance and non-reproduction missing')
        check('https://www.newspapers.com/image/249162609/' in html,
              mode + ': primary newspaper archive link missing')
        check('The newspaper clipping is not reproduced' in html,
              mode + ': newspaper reproduction boundary missing')
        check('Carol Van Pelt' in html and 'Grace Village' in html,
              mode + ': sourced biographical details missing')
        check('Barbara Boggs McMunn' in html,
              mode + ': family-identified second daughter missing')
        check('The newspaper itself did not name Barbara' in html and
              'his family account, not from the published newspaper notice' in html,
              mode + ': family provenance distinction missing')
        check('It is <strong>his</strong> obituary, not hers.' in html,
              mode + ': Asbury source provenance missing')
        check('verification and permission to publish' in html,
              mode + ': photograph permission boundary missing')
        check(all(anchor in doc.ids for anchor in ('her-story', 'sources', 'obituary')),
              mode + ': existing story or source anchor lost')
        notes = [a for a in doc.details if a.get('id') == 'sources']
        check(len(notes) == 1 and 'open' not in notes[0],
              mode + ': source notes must be collapsed by default')
        check(html.index('In December 1999') < html.index('Why I started') <
              html.index('id="sources"') < html.index('The newspaper notice:'),
              mode + ': narrative must precede historical notes')
        check('assets/meet-maxine.css' in doc.styles and
              (base / 'maxine/assets/meet-maxine.css').is_file(),
              mode + ': page-specific stylesheet missing')
        check('https://themaxineproject.org/meet-maxine.html' in doc.canonicals,
              mode + ': canonical address wrong')
        for href in ('family-account.html', 'resources.html', 'research/'):
            check(href in doc.links, mode + ': missing link ' + href)
        maxine_home = (base / 'maxine' / 'index.html').read_text(encoding='utf-8')
        wholemind_home = (base / 'wholemind' / 'index.html').read_text(encoding='utf-8')
        account = (base / 'maxine' / 'family-account.html').read_text(encoding='utf-8')
        check('href="meet-maxine.html"' in maxine_home,
              mode + ': memorial homepage entry missing')
        check('href="meet-maxine.html"' not in wholemind_home,
              mode + ': wrong brand navigation')
        check('assets/meet-maxine.css' not in wholemind_home and
              'assets/meet-maxine.css' not in account,
              mode + ': narrative styles leaked to another page')
    return checked


if __name__ == '__main__':
    print(f'PASS: {run_checks()} Meet Maxine integration checks')
