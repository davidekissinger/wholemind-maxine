# Meet Maxine memorial — editorial release record

Release: October 25, 2026. Status: review-only, noindex.
Applies to: `themaxineproject.org/meet-maxine.html` only. Shared layout CSS
also updates, but no WholeMind memorial page, commercial service,
data collection, nonprofit representation, or clinical claim is introduced.

## Intent
Center **Doris Maxine (Ratcliff) Boggs**, before the disease or the caregiving
account. The distinct "Our story" page continues to explain her husband
Rev. John Robert Boggs Jr. and the *I'll Move Over* book. Research & Innovation
remains explicitly exploratory and separate from this family memorial.

## Current evidentiary basis

- Family account: The founder, David E. Kissinger, BSHA, RN, identifies Maxine
  as his grandmother, confirms the personal inspiration for The Maxine Project,
  and describes the family's experience with Alzheimer's disease. The book
  and caregiving account already appear with appropriate attribution in
  `docs/family-story-sources.md`. These are founder-reported family facts,
  not clinical evidence.
- Independent record: Asbury Theological Seminary's *Alumni Obituaries —
  August 2013*, https://alumni.asburyseminary.edu/elink/alumni-obituaries-august-2013/
  identifies the wife of Rev. John Robert Boggs Jr. as Maxine Ratcliff,
  marriage July 10, 1943, Winona Lake residence, and Maxine's death in May
  2000. **This source is her husband's obituary, not Maxine's.**
- Obituary-search lead supplied by the founder:
  https://obituaries.rootsweb.com/obits/searchObits?simplesearch=true&fullsearch=Doris+maxine+boggs%2C+Winona+Lake%2C+I
  This is a *search URL*, not the obituary itself. It could not be retrieved
  for this edition; do not imply it authenticated or supplied original text.

- **New contemporary newspaper source (added October 25, 2026):** A
  founder-supplied screenshot captures the short item **“Mother dies,”
  The Star Press (Muncie, Indiana), Wednesday, May 24, 2000, p. 8**:
  https://www.newspapers.com/image/249162609/?article=ed5496d8-c4f4-44a1-9eb9-58d58e52e0aa
  The item describes Doris Maxine Boggs, age 78, as a homemaker; reports
  that she died at Grace Village Retirement Community, Winona Lake;
  identifies John Robert Boggs Jr. as her husband of 57 years, names
  daughter Carol Van Pelt of Redkey, and also notes another unnamed
  daughter, two sisters, and six grandchildren. The short death notice
  listed services at Grace Village Chapel, planned graveside services at
  Lindenwood Cemetery (Fort Wayne), and Pleasant Grove Mission Fund
  (Warsaw) as a memorial-contribution option. Those announced plans
  do not independently establish that burial took place there.
- **Additional family identification (October 25, 2026):** The founder
  identifies the other daughter mentioned, but not named, in *The Star
  Press* as **Barbara Boggs McMunn**, Maxine's daughter and his aunt.
  This is a founder-provided family statement, not independent verification
  and not a name found in the contemporary newspaper item. Keep that
  attribution explicit in the public biography.
- **New archival PDF, inspected October 25, 2026:** The founder uploaded a
  one-page Newspapers.com PDF export of the May 24, 2000, page 8 clipping,
  titled "Mother dies." The PDF itself displays the newspaper date, page,
  publication location, archive image URL, and October 25, 2026 download
  date. Its SHA-256 checksum is
  `d12684e1cd660b3d2b30250bfb17121c300ed60bb697bb980842962470fa8c36`.
  The PDF is a source artifact in the conversation, **not** part of the
  public repository or website build.
- **Newspaper-reported death date: May 22, 2000.** The notice appeared on
  Wednesday, May 24, and directly reports that Maxine died on "Monday."
  That is Monday, May 22. The archive screenshot's machine-generated
  index indicates May 29, which is later than the published notice and
  conflicts with the contemporary text. Use May 22 as a date attributed
  to the newspaper, not as a separately confirmed civil-record date.
  A civil death certificate could supply independent confirmation.
- **Copyright/access boundary:** The article was reviewed in the founder's
  screenshot and one-page Newspapers.com PDF export. We paraphrase factual
  information, link to the original publisher/archive, and do **not** upload
  or reproduce the newspaper clipping, PDF, or full article text in the
  public repository or on the website. Archive access may require a subscription.

## Editorial boundaries

- The identified newspaper death notice is summarized and attributed,
  but neither its photograph/clipping nor its full wording is reproduced.
  No family photo, book passage or cover is recreated or implied licensed.
  The memorial portrait remains an original typographic monogram, with
  an accurate photograph placeholder.
- No unverified birth date, birthplace, exact date of death, hobbies,
  personality descriptions or attributed words are inserted.
- Source statements are plainly divided from founder account.
- Future photographs and newspaper extracts require verification and
  appropriate permissions prior to publication.
- This page does not claim a funded study, official partnership, nonprofit
  tax exemption, accepted donations, or treatments.
- Existing review banner, noindex headers, preview domains, site-build
  safeguards, and first-release privacy boundaries remain unchanged.

## Implementation

- `src/meet_maxine.py`: memorial content, sources, and obituary archive disclosure
- `build.py`: separate Maxine route, navigation, metadata and home CTA
- `assets/site.css`: responsive, dark/light, reduced-motion-compatible styling
- `test_meet_maxine.py` and `check_site.py`: route, link, source and brand checks

## Future verified amendments

An independent civil death record to corroborate the newspaper-reported
May 22, 2000 date; any longer obituary; any reproduction rights to quote or
display the original newspaper clipping; family photo with publication
permission and descriptive alt text; firsthand memories approved by the
family; exact birth date or other life dates if supported by a reliable record.
