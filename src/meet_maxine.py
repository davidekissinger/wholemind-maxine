"""Meet Maxine: founder-approved personal narrative and separate source notes.

The Grace Village recollection is adapted from David E. Kissinger's memoir,
not invented dialogue or a quotation from Maxine. Historical qualifications
remain in an expandable section. A founder-supplied family portrait is shown;
newspaper obituary clippings are summarized, not reproduced. This module
changes only The Maxine Project's memorial page.
"""
from html import escape as E

ASBURY = 'https://alumni.asburyseminary.edu/elink/alumni-obituaries-august-2013/'
ROOTSWEB_SEARCH = 'https://obituaries.rootsweb.com/obits/searchObits?simplesearch=true&fullsearch=Doris+maxine+boggs%2C+Winona+Lake%2C+I'
STAR_PRESS_NOTICE = 'https://www.newspapers.com/image/249162609/?article=ed5496d8-c4f4-44a1-9eb9-58d58e52e0aa'


def meet_maxine_page() -> str:
    asbury = E(ASBURY, quote=True)
    rootsweb = E(ROOTSWEB_SEARCH, quote=True)
    newspaper = E(STAR_PRESS_NOTICE, quote=True)
    # A stylesheet link is body-allowed HTML. Keep these overrides page-local
    # so the companion brand and family-account layout are not changed.
    return f'''<link rel="stylesheet" href="assets/meet-maxine.css">
<section class="wrap maxine-memorial-hero maxine-narrative-hero" aria-labelledby="meet-maxine-heading">
  <div class="maxine-memorial-intro">
    <p class="eyebrow">The woman behind the name</p>
    <h1 id="meet-maxine-heading">Meet <em>Maxine.</em></h1>
    <p class="maxine-full-name">Doris Maxine (Ratcliff) Boggs</p>
    <p class="hero-intro">To me, she was Grandma Boggs.</p>
    <p class="story-credit">By David E. Kissinger, BSHA, RN <span class="maxine-narrative-relationship">Her grandson</span></p>
  </div>
  <figure class="maxine-family-portrait">
    <img src="assets/maxine-portrait.webp" width="400" height="475" loading="eager" decoding="async" alt="Portrait of Doris Maxine Boggs smiling in glasses with a pink corsage">
    <figcaption>Doris Maxine Boggs · Family portrait, date not recorded</figcaption>
  </figure>
</section>
<article class="wrap reading section maxine-tribute maxine-narrative-story" id="her-story" aria-label="A grandson’s memory">
  <p>In December 1999, I spent a few weeks with my grandfather at Grace Village in Winona Lake, Indiana. He had an apartment there, and Grandma was being cared for in the nursing home. I slept in his recliner. Each morning, after breakfast, we would go over to see her.</p>
  <p>By then, Grandma was bedridden and no longer responding to us. Grandpa still greeted her every day. He would tell her what good care the nurses and staff were giving her.</p>
  <p>Then he would gently move her soft white hair away from her face, first with his hand and then with her brush. He talked to her as he did it.</p>
  <p>I watched him and could see how much he loved her. I have come to appreciate the memories of those mornings more as I’ve grown older.</p>
  <h2>Grandma and Grandpa</h2>
  <p>Our family remembers Grandma as being around 57 when changes first became noticeable, although the exact beginning is difficult to identify. By the time she died in May 2000, at 78, she and Grandpa had been married for nearly 57 years.</p>
  <p>My grandfather, Rev. John Robert Boggs Jr., wrote about their experience in a book called <cite>I’ll Move Over</cite>. His account is part of our family’s history. Those mornings at Grace Village are part of mine.</p>
  <p>This is one memory of Grandma, from late in her life. It isn’t her whole story. I want this page to grow as our family brings together more of our memories and photographs, including the years before Alzheimer’s.</p>
  <section class="maxine-family-recollections" id="years-of-change" aria-labelledby="years-of-change-heading">
    <p class="eyebrow">Family recollections · October 2026</p>
    <h2 id="years-of-change-heading">Remembering the years of change</h2>
    <p>Looking through family photographs brought back memories of the years Grandma and Grandpa lived at Lake James. I remember nights when Grandma was awake and the family was concerned for her safety. The passage of time has made it difficult to place those moments on a precise timeline.</p>
    <p>Those memories are only one part of her story. I also want to preserve the faces, places, and everyday experiences that shaped Grandma’s life, and to learn what the photographs can tell us about the years before her illness.</p>
    <p class="editorial-note">Personal family recollections revisited in October 2026. This is not a clinical history or a verified timeline.</p>
    <a class="text-link" href="resources/preserving-their-story.html">Preserve a family story with our free guide <span aria-hidden="true">→</span></a>
  </section>
  <h2>Why I started The Maxine Project</h2>
  <p>I’m a nurse, but my connection to Alzheimer’s began in my own family. When I think about what families need, I think about Grandma and Grandpa, too.</p>
  <p>I started this project to remember her and to work toward something useful for other families. I want it to become a place where people can find helpful information about Alzheimer’s, answers to the questions that arise when caring for someone, and a clearer understanding of the research.</p>
  <p>It’s still early. I’m beginning with our family’s story and building from there.</p>
  <div class="maxine-heritage-link">
    <a class="text-link" href="family-account.html">Read about Grandpa and <cite>I’ll Move Over</cite> <span aria-hidden="true">→</span></a>
  </div>
  <section class="maxine-archive-life" id="life-beyond-alzheimers" aria-labelledby="maxine-life-heading">
    <p class="eyebrow">From the family archive</p>
    <h2 id="maxine-life-heading">More of Maxine’s life</h2>
    <p>Maxine was born on April 5, 1922, in Brush, Colorado, to Charles and Henrietta (Johnson) Ratliff, according to a memorial obituary published in 2000. She married Rev. John Robert Boggs Jr. in 1943.</p>
    <p>The memorial describes her as a homemaker who assisted her husband in his ministry and took part in Child Evangelism Clubs and United Methodist Women. During 1981–1985, her husband served as pastor of Grace United Methodist Church in Elkhart, Indiana.</p>
    <p>Maxine died on May 22, 2000, at age 78 in Winona Lake, Indiana. Her memorial names her surviving daughters Carol Van Pelt and Barbara McMunn, along with six grandchildren and four great-grandchildren. These details belong to the history of her life, beyond the illness that shaped its later years.</p>
    <p class="editorial-note"><strong>Source:</strong> Family-preserved memorial obituary for Doris M. Boggs, published as a tribute in <cite>The Elkhart Truth</cite>, Elkhart, Indiana, May 24, 2000. The facts are paraphrased here; the newspaper clipping is not reproduced. This obituary is not a clinical record of Alzheimer’s disease.</p>
    <a class="text-link" href="family-account.html#robert-earl">Robert Earl Boggs: another life in the family story <span aria-hidden="true">→</span></a>
  </section>
  <details class="future-note maxine-archive maxine-narrative-sources" id="sources">
    <summary>Family memories and historical sources</summary>
    <div id="obituary" class="maxine-narrative-notes">
      <p><strong>The personal memory:</strong> The Grace Village passage is adapted from David E. Kissinger’s own recollections of December 1999, recorded in his memoir manuscript <cite>Am I Ready? A Nurse’s Journey Through Change</cite>. The approximate age of 57 when changes first appeared is from his family account; this has not been verified against medical records. This is a grandson’s recollection, not a clinical record or a quotation from Maxine.</p>
      <p><strong>October 2026 family recollections:</strong> The Lake James passage reflects David’s personal memories revisited during a family photograph visit on October 28, 2026. The recording is a private source and is not published here. No dates or clinical conclusions are derived from it.</p>
      <p><strong>Marriage and family history:</strong> An <a href="{asbury}" rel="noreferrer">Asbury Theological Seminary alumni obituary <span class="external">(external)</span></a> for Rev. John Robert Boggs Jr. records his marriage to Maxine Ratcliff on July 10, 1943, their residence in Winona Lake, and her death in May 2000. It is <strong>his</strong> obituary, not hers.</p>
      <p><strong>The family memorial obituary:</strong> A photographed memorial notice for Doris M. Boggs, printed as a tribute in <cite>The Elkhart Truth</cite> on May 24, 2000, records her birth on April 5, 1922, in Brush, Colorado, her parents Charles and Henrietta (Johnson) Ratliff, and her participation in church and community activities. The printed notice names Carol Van Pelt and Barbara McMunn as her surviving daughters and lists six grandchildren and four great-grandchildren. The original print was supplied by the founder on October 28, 2026. Her birth surname is spelled <em>Ratliff</em> there, while the previously cited Asbury alumni memorial spells it <em>Ratcliff</em>; the discrepancy has not been independently resolved.</p>
      <p><strong>The newspaper notice:</strong> A short item titled <cite>Mother dies</cite> appeared in <cite>The Star Press</cite>, Muncie, Indiana, on May 24, 2000, page 8. It reported that Maxine died at age 78 at Grace Village Retirement Community. The notice says she died on Monday, corresponding to May 22, 2000. The archive’s automated May 29, 2000 date conflicts with the contemporary notice; a civil death record has not been reviewed.</p>
      <p><a href="{newspaper}" rel="noreferrer">View the archived newspaper notice <span class="external">(external; access may require a subscription)</span></a>. The newspaper clipping is not reproduced on this website. A Newspapers.com PDF export downloaded October 25, 2026 was checked for the earlier archive update. It is retained as source material, not published on this website.</p>
      <p><strong>Family names in the shorter notice:</strong> The <cite>Star Press</cite> item named Carol Van Pelt and mentioned another daughter, two sisters, and six grandchildren. David previously identified the unnamed daughter as his aunt Barbara Boggs McMunn. The newspaper itself did not name Barbara; that identification comes from his family account, not from the published newspaper notice. The newly supplied, longer <cite>Elkhart Truth</cite> memorial independently prints Barbara McMunn's name.</p>
      <p><strong>Memorial arrangements:</strong> The notice listed a service at Grace Village Chapel and plans for private graveside services at Lindenwood Cemetery in Fort Wayne. These were announced arrangements, not independently verified records of burial. It named Pleasant Grove Mission Fund in Warsaw as a suggested recipient of memorial contributions at that time; this page does not solicit donations.</p>
      <p>The earlier <a href="{rootsweb}" rel="noreferrer">RootsWeb search <span class="external">(external)</span></a> remains a research lead, not a substitute for the identified newspaper notice.</p>
      <p><strong>Photograph and publication boundaries:</strong> The family-supplied studio portrait shown above was provided by David E. Kissinger for the project; its original photographer and date are unverified. No newspaper obituary clipping, book cover, or book passage is reproduced on this site. The <a href="family-account.html">family account</a> and exploratory research questions remain separate; this page makes no claim of a funded study, institutional partnership, tax-exempt status, or established treatment.</p>
      <p class="editorial-note">Archival sources added October 28, 2026. A personal family account and selected historical facts, not a complete biography or clinical history.</p>
    </div>
  </details>
</article>
<section class="wrap section maxine-next" aria-label="Continue exploring">
  <div><h2>Explore the project</h2></div>
  <div class="maxine-next-links">
    <a class="button primary" href="resources.html">Family resources</a>
    <a class="button secondary" href="research/">Exploratory research</a>
  </div>
</section>'''
