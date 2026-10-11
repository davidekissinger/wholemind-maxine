# Family story: source and editorial record

Updated: October 11, 2026.
Scope: the two `story.html` pages only. This addition does not change any
educational resource PDF, clinical scope, organizational status, or access setting.

## Founder-supplied family history

David E. Kissinger identifies Maxine Boggs as his grandmother and Rev. John
Robert Boggs Jr. as his grandfather. In the March 22, 2026 concept discussion,
he described his grandfather's book *I'll Move Over* as an account of caring
for Maxine for over 20 years. Later project discussions supplied the full name
and identified the book again. The founder approved incorporating this family
history into these websites. The first-person copy is founder-story website
copy, not a quotation from the book.

These statements are attributed to the founder. Do not describe the caregiving
duration as independently verified by the publication records below.

## External records inspected

- Asbury Theological Seminary, **Alumni Obituaries – August 2013**,
  published July 25, 2013:
  https://alumni.asburyseminary.edu/elink/alumni-obituaries-august-2013/
  Identifies John Robert Boggs Jr. as a minister and records his marriage to
  Maxine Ratcliff. The page supports that identity and marital relationship;
  it does not establish the caregiving duration or reproduce the book.
- Amazon bookseller record, ISBN **9780964888012**:
  https://www.amazon.com/-/es/ILl-Move-Over-Dealing-Alzheimers/dp/0964888017
  Search-indexed title/author metadata identifies *I'll Move Over: Spouse and
  Family Stress in Dealing With Alzheimer's Disease*, J. Robert Boggs.
  The full retail page could not be fetched during this update. No page count,
  precise release date, availability, price, or content synopsis is inferred.
- AbeBooks edition/listing, ISBN **9780964888029**:
  https://www.abebooks.fr/9780964888029/Move-Over-Story-Great-Love-0964888025/plp
  The accessed page lists *I'll Move Over: The Story of a Great Love*,
  hardcover; seller metadata identifies J. Robert Boggs, Boggs Books, 1995.
  The website labels this as a listing, not an examination of a physical copy.

The former response's Times-Union article could not be reopened during this
update and is not used as independent evidence for the new website copy.

## Boundaries

No title page, copyright page, table of contents, or full book was available
for examination. Do not assert that the two listed titles are identical,
revised, expanded, or successive editions without checking actual copies.
The exact first publication date remains outside this update. The book is
presented as family history, not a clinical study or evidence for treatment.

No passages, cover artwork, family photographs, or download of the book are
included. Do not infer copyright ownership or permission from kinship. Future
excerpts or images require source review and appropriate permission.
Boggs Books is identified as a historical publisher, not a current operator,
legal predecessor, affiliate, or new brand in this website system.

## Implementation

`src/family_story.py` contains the new story sections. `build.py` inserts them
on story pages only. The WholeMind link retains `data-brand-link`, allowing
the existing appearance script to carry the visitor's selection. It resolves
to a local path in offline previews and a custom-domain path in production.
`test_family_story.py` checks both forms, source caveats, headings/IDs, and
absence of new image, form, purchase, or book-quotation elements.
