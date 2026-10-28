"""Dedicated family-account page for The Maxine Project.

This page expands founder-supplied family history with separately attributed
alumni and bookseller records. The book's text, dedication, and cover have
not been examined or reproduced. It is a memorial narrative, not clinical
evidence or an authorized edition of the book.
"""
from html import escape

from family_story import BIOGRAPHY_URL, BOOK_RECORD_URL, ALTERNATE_RECORD_URL

ATS_DEGREE_HISTORY_URL = 'https://www.ats.edu/files/galleries/coa-history.pdf'


def family_account_page() -> str:
    """Build the editorial page without collecting or transmitting user data."""
    alumni = escape(BIOGRAPHY_URL, quote=True)
    degree_history = escape(ATS_DEGREE_HISTORY_URL, quote=True)
    paperback = escape(BOOK_RECORD_URL, quote=True)
    hardcover = escape(ALTERNATE_RECORD_URL, quote=True)

    return f"""
<section class="wrap maxine-memorial-hero maxine-family-hero" aria-labelledby="family-account-heading">
  <div class="maxine-memorial-intro">
    <p class="eyebrow">Our story / The family account</p>
    <h1 id="family-account-heading">The Family Account:<br><em>I'll Move Over.</em></h1>
    <p class="maxine-full-name">Rev. John Robert Boggs Jr., BD (1949)</p>
    <p class="editorial-note">Bachelor of Divinity · Asbury Theological Seminary</p>
    <p class="hero-intro">The story of a family does not stop at a diagnosis. It continues in the everyday choices to adapt, care, and remain connected through change.</p>
    <div class="actions">
      <a class="button primary" href="#partner-witness">Read the account</a>
      <a class="text-link" href="meet-maxine.html">Meet Maxine <span aria-hidden="true">→</span></a>
    </div>
  </div>
  <aside class="maxine-portrait-placeholder maxine-family-book" aria-label="A typographic tribute to the book, not a reproduction of its cover">
    <span class="maxine-portrait-initial" aria-hidden="true">B</span>
    <p class="maxine-portrait-name">I'll Move Over</p>
    <p class="maxine-portrait-caption">J. Robert Boggs</p>
    <p class="maxine-portrait-note">A typographic tribute; original book cover and artwork are not displayed.</p>
  </aside>
</section>

<section class="maxine-memorial-principle">
  <div class="wrap">
    <p class="small-label">The family perspective</p>
    <h2>Caregiving changes a relationship. It does not erase it.</h2>
    <p>A husband remained a husband. A wife remained a whole person. Their shared history mattered even as the circumstances of daily life changed.</p>
  </div>
</section>

<article class="wrap reading section maxine-tribute">
  <p class="eyebrow">A life of service. A family's account.</p>
  <h2 id="partner-witness">A partner's witness</h2>
  <p>Rev. John Robert Boggs Jr. married Maxine Ratcliff on July 10, 1943. They were married for nearly 57 years before her death in May 2000. For the family, their story is about the life they shared as well as the demands that Alzheimer's disease brought into it.</p>
  <p>According to his grandson David E. Kissinger's family account, Rev. Boggs cared for Maxine for more than two decades. The experience became part of the history he sought to preserve in <cite>I'll Move Over</cite>, published under the name J. Robert Boggs.</p>
  <p>His life and work also extended far beyond the caregiving role. Asbury Theological Seminary's alumni memorial lists him as a Bachelor of Divinity (BD) graduate in 1949 and records his service as a United Methodist minister beginning in 1944, his retirement in 1992, ministry in Ohio, North Dakota, and Indiana, and his establishment of a soup kitchen in Elkhart, Indiana.</p>

  <h2 id="elkhart-memories">Remembering the home in Elkhart</h2>
  <p>David remembers visiting his grandparents in Elkhart, including the kitchen, the dining room, and a separate space where his grandfather prepared sermons. He also remembers two doves that Rev. Boggs used in magic shows for children. Those details offer a glimpse of family life and ministry beyond the written record of pastoral appointments.</p>
  <p class="editorial-note">Source: David E. Kissinger’s own memories, revisited while looking through family photographs in October 2026. This is a personal recollection, not a passage from <cite>I'll Move Over</cite> or a separately verified description of the home.</p>

  <h2 id="the-book">The book in the family</h2>
  <p>For this project, <cite>I'll Move Over</cite> is a personal family account and an important historical touchstone. It is not presented as a medical guide, a clinical study, or a substitute for current healthcare information.</p>
  <p>Bookseller records identify a hardcover titled <cite>I'll Move Over: The Story of a Great Love</cite>, attributed to J. Robert Boggs and listed as published by Boggs Books in 1995 (ISBN 9780964888029). Other catalog listings use the broader <cite>I'll Move Over</cite> title with different subtitles and a separate ISBN. The publication records have not been reconciled against physical copies.</p>
  <p>The book's full text and dedication have not yet been examined for this website. The meaning described here comes from the founder's family account, not from a claimed close reading or a quotation from the book.</p>

  <h2 id="robert-earl">Robert Earl Boggs: a life remembered</h2>
  <p>Robert Earl Boggs was the son of Maxine and Rev. John Robert Boggs Jr. He was 19 when he died in a two-car collision on Indiana State Road 9 near Marion. A family-preserved newspaper obituary records that he was salutatorian of Parker High School's class of 1963, entered the U.S. Navy in June 1963, trained at Great Lakes, and was assigned to Philadelphia.</p>
  <p>Robert had announced his intention to enter the ministry after his Navy service. His memorial named his sisters Betty, Carol, and Barbara and listed burial at Lindenwood Cemetery in Fort Wayne. The clipping gives the day of death as Sunday, July 5, but its publication year is not visible; 1964 is consistent with that weekday and the account's chronology, rather than independently confirmed from the clipping.</p>
  <p class="editorial-note">Source: Founder-supplied photograph of an undated newspaper obituary headed “Robert Earl Boggs,” provided October 28, 2026. These details are paraphrased from that record. Its announced burial arrangements are not independently verified; the original newspaper clipping is not reproduced here.</p>

  <h2 id="carrying-forward">Carrying the legacy forward</h2>
  <p>For David E. Kissinger, the story of Maxine and his grandfather connects private family experience with a public purpose: education and resources that honor the person experiencing cognitive change and recognize the people who care for them.</p>
  <p>The Maxine Project draws its human motivation from this history. It can inform which questions deserve attention and how resources are written, while scientific and medical claims must still be evaluated on evidence independent of any single family's experience.</p>
  <div class="maxine-heritage-link">
    <p class="small-label">The woman who inspired the project</p>
    <p>Return to Maxine's life and the contemporary newspaper account that helps preserve her place in the family's history.</p>
    <a class="text-link" href="meet-maxine.html">Meet Maxine <span aria-hidden="true">→</span></a>
  </div>

  <h2 id="historical-records">Historical records &amp; context</h2>
  <p><strong>Education and ministry:</strong> An <a href="{alumni}" rel="noreferrer">Asbury Theological Seminary alumni memorial <span class="external">(external)</span></a> lists Rev. John Robert Boggs Jr. as <strong>1949, BD</strong>, and documents his ministry, his marriage to Maxine, and their family. It does not independently document how many years he provided care or the contents of his book.</p>
  <p><strong>About the degree:</strong> BD means <strong>Bachelor of Divinity</strong>. Despite the name, it was historically a graduate-level professional theological degree, the predecessor in American seminary education of the Master of Divinity (MDiv). This page preserves the degree Rev. Boggs earned in 1949 rather than suggesting that he was later awarded an MDiv. See the <a href="{degree_history}" rel="noreferrer">Association of Theological Schools' historical account <span class="external">(external)</span></a> for the later change in degree terminology.</p>
  <p><strong>Book records:</strong> A <a href="{hardcover}" rel="noreferrer">hardcover bookseller listing <span class="external">(external)</span></a> identifies <cite>I'll Move Over: The Story of a Great Love</cite> (ISBN 9780964888029). A <a href="{paperback}" rel="noreferrer">separate listing <span class="external">(external)</span></a> identifies ISBN 9780964888012 under a different extended title. These are bibliographic leads, not an examination of the book or proof about the relationship between the listed versions.</p>
  <details class="future-note maxine-archive" id="editorial-record">
    <summary>About the family account and source boundaries</summary>
    <p>The family relationship, the caregiving duration, and the personal importance of <cite>I'll Move Over</cite> are attributed to founder David E. Kissinger. The alumni memorial and bookseller listings support only the biographical and bibliographic facts specifically identified above.</p>
    <p>The Robert Earl Boggs account comes from a family-held, undated newspaper obituary rather than Rev. Boggs's book. The death year is inferred, not printed. No book passage, dedication, cover, family photograph, or reproduced newspaper clipping appears on this page. No publisher rights, existing distribution partnership, nonprofit recognition, or research endorsement is claimed.</p>
    <p>This is new website editorial writing, not a transcript of Rev. Boggs's book. The differences among bookseller titles and ISBNs remain an open bibliographic question until copies can be checked directly.</p>
  </details>
</article>

<section class="wrap section maxine-next">
  <div>
    <p class="eyebrow">What we build next</p>
    <h2>A family history that informs the work ahead.</h2>
    <p>Explore practical resources for families, or the early research questions being considered separately from this personal account.</p>
    <a class="text-link" href="story.html#family-story">Read the shorter founder's account <span aria-hidden="true">→</span></a>
  </div>
  <div class="maxine-next-links">
    <a class="button primary" href="resources.html">Family Resources</a>
    <a class="button secondary" href="research/">Research &amp; Innovation</a>
  </div>
</section>
"""
