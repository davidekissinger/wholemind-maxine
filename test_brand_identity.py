"""Verify authentic portrait reuse and separation of both static brands."""
from hashlib import sha1
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parent
PORTRAIT_BLOB = 'e589de2a439480cdbb93dbec2955876b6a09b8da'

class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.images = []
        self.stylesheets = []
        self.brands = 0
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'img' and a.get('src', '').endswith('maxine-portrait.webp'):
            self.images.append(a)
        if tag == 'span' and 'maxine-brand' in a.get('class', '').split():
            self.brands += 1
        if tag == 'link' and a.get('rel') == 'stylesheet':
            self.stylesheets.append(a.get('href', ''))

def git_blob(data):
    return sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()

def main():
    original = (ROOT / 'maxine-assets/maxine-portrait.webp').read_bytes()
    assert git_blob(original) == PORTRAIT_BLOB, 'Authentic portrait changed'
    total = 0
    for mode in ('preview', 'dist'):
        for brand in ('maxine', 'wholemind'):
            base = ROOT / mode / brand
            pages = list(base.rglob('*.html'))
            assert pages, f'Build {mode}/{brand} first'
            for path in pages:
                text = path.read_text()
                page = Page(); page.feed(text)
                styles = [s for s in page.stylesheets if 'brand-identity.css' in s]
                if brand == 'wholemind':
                    assert page.brands == 0 and not styles, path
                    continue
                assert page.brands == 2, path
                assert len(styles) == 1, path
                for image in page.images:
                    src = urlsplit(image['src']).path
                    target = base / src.lstrip('/') if src.startswith('/') else path.parent / src
                    assert target.is_file(), (path, target)
                    assert target.read_bytes() == original, target
                assert text.count('class="maxine-brand__the">The </span>') == 2, path
                assert text.count('class="maxine-brand__name">Maxine </span>') == 2, path
                assert text.count('class="maxine-brand__project">Project</span>') == 2, path
                total += 1
    print(f'PASS: {total} Maxine pages use the authentic portrait in header and footer; WholeMind identity is unchanged.')

if __name__ == '__main__':
    main()
