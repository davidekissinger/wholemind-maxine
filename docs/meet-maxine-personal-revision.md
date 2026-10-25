# Meet Maxine: personal narrative revision

Approved for implementation by founder David E. Kissinger in the project conversation on October 25, 2026, after review of `Meet_Maxine_Revised.html` and its accompanying text. This revision supersedes the prior institutional-style narrative for `meet-maxine.html`; the historical-source qualifications recorded in the earlier editorial notes remain in force.

## Publication scope

- Replace only the Meet Maxine narrative and its page-local presentation.
- Retain the shared brand switcher, navigation, appearance preference, footer, canonical URL, and current review/noindex setting.
- Leave the family-account, research, and WholeMind Living page content unchanged.
- Keep the existing `her-story`, `sources`, and `obituary` anchors and links to the family account, resources, and research.

## Voice and content

The page now opens, “To me, she was Grandma Boggs,” with David's byline. Its first-person Grace Village recollection follows the founder-approved draft: December 1999, staying in his grandfather's apartment, sleeping in his recliner, their visits after breakfast, and his grandfather brushing Maxine's hair. These details were attributed in the approved draft to David's memoir manuscript, *Am I Ready? A Nurse's Journey Through Change*. They are family recollections, not clinical records, invented dialogue, or quotations from Maxine or *I'll Move Over*.

The page expressly says this is one late-life memory, not Maxine's whole story. The future direction is described as an intention, not an established research program or service. Generic memorial slogans and the typographic portrait placeholder are removed. No portrait is generated or substituted.

## Sources and rights

Historical information remains in a collapsed, keyboard-accessible native `details` element. Preserve the distinctions between the grandfather's Asbury obituary, Maxine's newspaper notice, and founder-supplied family identification. The notice's May 22, 2000 date remains distinguished from the conflicting automated May 29 index and from a civil death record. The prior newspaper PDF provenance is retained; this revision does not claim a new independent archival verification. No clipping, PDF, book excerpt, or family photograph is published.

## Implementation and validation

`src/meet_maxine.py` supplies the replacement page body. `assets/meet-maxine.css` applies only on that route and uses existing theme tokens. The shared styles are not edited. A body-allowed stylesheet link loads the scoped CSS without modifying the shared document renderer.

`test_meet_maxine.py` checks narrative content, source qualifications, collapsed notes, preserved anchors, routes, brand isolation, and absence of images/forms. The existing `check_site.py` invokes this suite for both build modes. Deployment must follow successful repository validation and use the existing Netlify project, not a new site.
