"""Family history for the story pages, separate from clinical resource content.

Provenance and the limits of the edition records are documented in
``docs/family-story-sources.md``. No book text or cover art is reproduced.
"""
from html import escape
from urllib.parse import urljoin, urlsplit
import posixpath


BIOGRAPHY_URL = 'https://alumni.asburyseminary.edu/elink/alumni-obituaries-august-2013/'
BOOK_RECORD_URL = 'https://www.amazon.com/-/es/ILl-Move-Over-Dealing-Alzheimers/dp/0964888017'
ALTERNATE_RECORD_URL = 'https://www.abebooks.fr/9780964888029/Move-Over-Story-Great-Love-0964888025/plp'


def family_story(brand: str, sibling: str) -> str:
    """Render an accessible section, preserving preview and cross-brand links."""
    if brand not in ('wholemind', 'maxine'):
        raise ValueError('Unknown story brand')
    heading = '<h2 id="family-story">A family story, carried forward</h2>'
    if brand == 'wholemind':
        target = (urljoin(sibling, 'story.html#family-story') if urlsplit(sibling).scheme
                  else posixpath.join(posixpath.dirname(sibling), 'story.html#family-story'))
        destination = escape(target, quote=True)
        return heading + (
            '<p>Founder David E. Kissinger’s grandmother, Maxine Boggs, is the personal inspiration behind this work. '
            'His grandfather, Rev. John Robert Boggs Jr., wrote <cite>I’ll Move Over</cite> under the name J. Robert Boggs '
            'about the family’s experience with Alzheimer’s.</p>'
            '<p>That history connects WholeMind Living with The Maxine Project. WholeMind Living carries the shared '
            'commitment into a broader focus on everyday well-being, meaningful routines, and relationships. '
            'The Maxine Project holds the fuller family story and focuses on people and families facing cognitive change.</p>'
            '<p><a class="text-link" data-brand-link href="' + destination + '">Read the family story at The Maxine Project '
            '<span aria-hidden="true">→</span></a></p>'
        )
    return heading + (
        '<p class="small-label">From the founder · David E. Kissinger, BSHA, RN</p>'
        '<p>My grandmother, Maxine Boggs, is the inspiration behind The Maxine Project. Her experience with Alzheimer’s '
        'is part of our family’s history, but it is not the whole of who she was.</p>'
        '<p>My grandfather, Rev. John Robert Boggs Jr., BD (1949), cared for her for more than two decades. In <cite>I’ll Move Over</cite>, '
        'published under the name J. Robert Boggs, he wrote about our family’s experience with Alzheimer’s.</p>'
        '<p>The Maxine Project grows from that personal history. My purpose is to honor my grandmother while developing '
        'practical education and resources for people and families facing cognitive change. Her life, my grandfather’s '
        'account, and my own experience as a nurse inform the questions at the heart of this work: How do we keep seeing '
        'the person? How do we support those close to them? How do we make room for meaningful life through change?</p>'
        '<p>This is a continuation of a family’s concern for one another, not a claim that one family’s experience '
        'provides every answer. The work begins with listening, useful information, and respect for each person’s own life.</p>'
        '<h2 id="family-book">The book in our family’s story</h2>'
        '<p><cite>I’ll Move Over</cite> belongs here as a family account and part of the project’s inspiration—not as '
        'a clinical study or a substitute for current health information.</p>'
        '<p>Bookseller records identify the author as J. Robert Boggs and include the following titles:</p>'
        '<p><cite>I’ll Move Over: Spouse and Family Stress in Dealing With Alzheimer’s Disease</cite><br>'
        'ISBN 9780964888012. <a href="' + BOOK_RECORD_URL + '" rel="noreferrer">View this title’s bookseller record '
        '<span class="external">(external)</span></a>.</p>'
        '<p><cite>I’ll Move Over: The Story of a Great Love</cite><br>'
        'A hardcover listing identifies Boggs Books as publisher and 1995 as its publication year. '
        'ISBN 9780964888029. <a href="' + ALTERNATE_RECORD_URL + '" rel="noreferrer">View the alternate title’s bookseller record '
        '<span class="external">(external)</span></a>.</p>'
        '<p class="editorial-note">These are bibliographic listings, not a comparison of the books’ contents. '
        'The title and copyright pages have not yet been examined for this website. Boggs Books is identified here '
        'as the historical publisher; no current affiliation, publishing rights, or book sales by either website are claimed.</p>'
        '<p><a class="text-link" href="family-account.html">Explore Rev. Boggs’s dedicated family account '
        '<span aria-hidden="true">→</span></a></p>'
        '<details class="future-note"><summary>About the family history and sources</summary>'
        '<p>The family relationships, caregiving duration, and connection between the book and this project are supplied '
        'by founder David E. Kissinger. The first-person text above is the founder’s story, not a quotation from the book.</p>'
        '<p>The <a href="' + BIOGRAPHY_URL + '" rel="noreferrer">Asbury Theological Seminary alumni obituary '
        '<span class="external">(external)</span></a> identifies John Robert Boggs Jr. as a minister, lists his Bachelor of Divinity (BD), 1949, and records his marriage '
        'to Maxine Ratcliff. The bookseller links provide publication-record context, not medical evidence or endorsements.</p>'
        '<p>No passages, cover artwork, or family photographs from the book are reproduced here. Any future excerpts '
        'or images will require source review and appropriate permission.</p></details>'
    )
