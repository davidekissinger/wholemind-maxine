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

## Editorial boundaries

- No Maxine obituary text, quotation, family photo, book passage or cover
  is recreated, quoted or implied to be licensed. The memorial portrait is
  an original typographic monogram, with an accurate photograph placeholder.
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

Original obituary text and publication metadata; family photo with
publication permission and descriptive alt text; firsthand memories
approved by the family; exact life dates if supported by a reliable record.
