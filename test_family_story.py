#!/usr/bin/env python3
"""Story integration checks; no network access or clinical validation."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urljoin, urlsplit
import unittest
import sys

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'src'))
from family_story import family_story


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.ids, self.links, self.h1s = [], [], 0
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get('id'):
            self.ids.append(attrs['id'])
        if tag == 'a':
            self.links.append(attrs)
        if tag == 'h1':
            self.h1s += 1


class FamilyStoryTests(unittest.TestCase):
    def test_both_story_pages_have_section_and_unique_ids(self):
        for mode in ('preview', 'dist'):
            for brand in ('wholemind', 'maxine'):
                text = (ROOT / mode / brand / 'story.html').read_text()
                page = Page(text)
                with self.subTest(mode=mode, brand=brand):
                    self.assertIn('family-story', page.ids)
                    self.assertEqual(len(page.ids), len(set(page.ids)))
                    self.assertEqual(page.h1s, 1)
                    self.assertIn('J. Robert Boggs', text)
                    self.assertIn('data-appearance', text)
                    self.assertIn('FIRST RELEASE', text)

    def test_production_story_link_and_preference_transfer_marker(self):
        text = (ROOT / 'dist/wholemind/story.html').read_text()
        links = Page(text).links
        self.assertTrue(any(a.get('href') == 'https://themaxineproject.org/story.html#family-story'
                            and 'data-brand-link' in a for a in links))

    def test_preview_story_link_stays_local(self):
        text = (ROOT / 'preview/wholemind/story.html').read_text()
        links = Page(text).links
        self.assertTrue(any(a.get('href') == '../maxine/story.html#family-story'
                            and 'data-brand-link' in a for a in links))

    def test_sources_and_scope_are_present(self):
        text = (ROOT / 'dist/maxine/story.html').read_text()
        for expected in ('9780964888012', '9780964888029', 'Boggs Books',
                         'not a quotation from the book', 'title and copyright pages',
                         'supplied by founder David E. Kissinger', 'no current affiliation'):
            self.assertIn(expected, text)
        self.assertIn('alumni.asburyseminary.edu', text)
        self.assertIn('Rev. John Robert Boggs Jr., BD (1949)', text)
        self.assertIn('Bachelor of Divinity (BD), 1949', text)
        self.assertNotIn('<blockquote', text)
        self.assertNotIn('January 1, 1994', text)

    def test_no_new_book_sale_or_embedded_image(self):
        block = family_story('maxine', 'https://wholemindliving.com/')
        for excluded in ('<img', '<form', '<script', 'Add to cart', 'Buy now'):
            self.assertNotIn(excluded, block)

    def test_unknown_brand_is_rejected(self):
        with self.assertRaises(ValueError):
            family_story('other', '/')

    def test_netlify_preview_hostname_and_escaping(self):
        html = family_story('wholemind', 'https://themaxineproject.netlify.app/')
        self.assertIn('https://themaxineproject.netlify.app/story.html#family-story', html)
        html = family_story('wholemind', 'https://example.org/a"b/index.html')
        self.assertNotIn('/a"b/', html)
        self.assertIn('&quot;', html)


if __name__ == '__main__':
    unittest.main(verbosity=2)
