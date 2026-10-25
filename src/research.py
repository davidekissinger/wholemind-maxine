"""Public research introduction. Intentionally excludes the private study protocol."""
from html import escape as E
from research_references import REFERENCES, VERIFIED_DATE

RESEARCH_PAGES = {
    'research/index.html': ('Research & Innovation', 'Independent scientific questions inspired by Maxine’s story, with evidence, limitations, and an invitation to scientific critique.'),
    'research/synaptic-restoration/index.html': ('Kinome-Guided Synaptic Restoration in Alzheimer’s Disease', 'An independent exploratory hypothesis about kinase signaling and useful, durable synaptic function—not an established treatment or active study.'),
    'research/references/index.html': ('Scientific References', 'Selected primary publications and an external NIH/NIA award record, with the relevance and limits of each source stated explicitly.'),
}

STATUS = 'Independent exploratory proposal · October 2026'
BOUNDARY = ('The Maxine Project is an initiative in development. This is an independent scientific proposal, '
            'not an established treatment, funded study, or active research program. No experiments or clinical '
            'outcomes are reported by the project. No university affiliation, investigator participation, '
            'NIH support for this proposal, or institutional endorsement is claimed.')


def refs(prefix, *numbers):
    return ' <span class="research-citations">' + ' '.join(
        '<a href="' + prefix + 'research/references/#' + next(r['id'] for r in REFERENCES if r['number'] == n)
        + '" aria-label="Scientific reference ' + str(n) + '">[' + str(n) + ']</a>' for n in numbers
    ) + '</span>'


def subnav(prefix, active):
    items = [('research/index.html', 'research/', 'Overview'),
             ('research/synaptic-restoration/index.html', 'research/synaptic-restoration/', 'Research concept'),
             ('research/references/index.html', 'research/references/', 'Scientific references')]
    return '<nav class="research-subnav wrap" aria-label="Research navigation">' + ''.join(
        '<a href="' + prefix + url + '"' + (' aria-current="page"' if path == active else '') + '>' + label + '</a>'
        for path, url, label in items) + '</nav>'


def status_note():
    return '<aside class="research-status"><p class="small-label">Research questions, not treatment claims</p><p>' + E(BOUNDARY) + '</p></aside>'


def editorial(prefix):
    return ('<div class="research-editorial"><p><strong>Public overview · Version 1.0 · October 25, 2026.</strong> '
            'Prepared for The Maxine Project by David E. Kissinger, BSHA, RN. Drafting and source checking were AI-assisted. '
            'This proposal has not undergone independent scientific peer review.</p><p>This website does not provide treatment '
            'instructions, recruit research participants, or accept medical records. The detailed proposal and experimental '
            'protocol are not published here. <a href="' + prefix + 'connect.html#founder">Founder &amp; scientific correspondence</a>.</p></div>')


def home_feature():
    return ('<section class="wrap section research-feature" aria-labelledby="research-feature-title">'
            '<p class="eyebrow">Research &amp; Innovation</p><h2 id="research-feature-title">Honoring a life. Asking what comes next.</h2>'
            '<p>Alongside practical family resources, we are developing independent scientific questions for academic consideration. '
            'Our first concept asks whether kinase signaling could help explain the potential—and the limits—of synaptic restoration.</p>'
            '<p class="research-label">Independent exploratory proposal · Not an active study</p>'
            '<a class="button primary" href="research/">Explore Research &amp; Innovation</a></section>')


def founder_section():
    return ('<section class="wrap reading section" id="founder" aria-labelledby="founder-name">'
            '<p class="eyebrow">Founder &amp; scientific correspondence</p><h2 id="founder-name">David E. Kissinger, BSHA, RN</h2>'
            '<p class="story-credit">Founder, The Maxine Project</p><p>David brings a nursing and healthcare-leadership background '
            'and a family connection to Alzheimer’s disease. His grandmother, Maxine Boggs, is the inspiration behind the initiative.</p>'
            '<p>His role in this concept is to frame a question for scientific evaluation—not to claim that the neuroscience has been '
            'independently validated. Scientific critique, including reasons the hypothesis may fail, is welcome.</p>'
            '<p><a class="text-link" href="research/synaptic-restoration/">Read the public research concept</a></p>'
            '<h2>Correspondence status</h2><p>A dedicated project email address has not yet been confirmed for publication. '
            'This page does not currently provide a working message form. Do not use it for clinical advice, urgent help, '
            'study enrollment, or sharing medical records.</p><p>The founder’s website is linked below for background; '
            'it is not represented here as a verified message-delivery service.</p></section>')


def overview(prefix):
    return ('<section class="wrap research-hero"><p class="eyebrow">The Maxine Project / Research &amp; Innovation</p>'
            '<h1>Understanding the Brain.<br><em>Exploring the Possibility of Recovery.</em></h1>'
            '<p class="hero-intro">Alzheimer’s disease changes lives long before it takes them. We believe scientific discovery, '
            'human experience, and thoughtful collaboration can help advance the search for better treatments.</p>'
            '<p class="research-label">Recovery is a research question—not an outcome demonstrated by this initiative.</p>'
            '<div class="actions"><a class="button primary" href="' + prefix + 'research/synaptic-restoration/">Explore the research concept</a>'
            '<a class="text-link" href="' + prefix + 'research/references/">Review the scientific references</a></div></section>'
            '<div class="wrap">' + status_note() + '</div>'
            '<section class="wrap section"><div class="section-heading"><p class="eyebrow">Our scientific interests</p>'
            '<h2>From a family’s experience to questions worth testing.</h2><p>Our mission is to make a clearly reasoned, '
            'source-linked case for scientific consideration. Our vision is a dialogue in which lived experience helps frame '
            'important questions and rigorous research determines what holds up.</p></div>'
            '<div class="three-grid research-topics"><article><h3>Synapses &amp; function</h3><p>What would count as useful communication '
            'between surviving neurons—not simply more visible connections?</p></article><article><h3>Signaling &amp; disease context</h3>'
            '<p>Could differences in kinase activity help explain why a plasticity response succeeds, fails, or becomes harmful?</p>'
            '</article><article><h3>Durability &amp; safety</h3><p>What evidence would distinguish a short-lived structural change '
            'from a stable, beneficial functional response?</p></article></div></section>'
            '<section class="wrap research-feature"><p class="eyebrow">Featured research concept</p>'
            '<h2>Kinome-Guided Synaptic Restoration in Alzheimer’s Disease</h2>'
            '<p>Exploring whether targeted neural plasticity could restore useful functional connections in Alzheimer’s-affected '
            'brain networks—and what might prevent that from happening.</p><p class="research-label">' + STATUS + '</p>'
            '<a class="text-link" href="' + prefix + 'research/synaptic-restoration/">Research concept and supporting literature →</a></section>'
            '<section class="wrap reading section"><h2>Why this belongs in Maxine’s story</h2><p>The project begins with a person '
            'and a family, not a laboratory result. The research section extends that concern into a careful invitation to examine '
            'new questions; it does not replace the practical resources already available.</p><p><a href="' + prefix + 'story.html#family-story">'
            'Read the family story</a> · <a href="' + prefix + 'resources.html">Explore family resources</a></p>' + editorial(prefix) + '</section>')


def concept(prefix):
    return ('<section class="page-intro wrap research-intro"><p class="eyebrow">Exploratory research concept</p>'
            '<h1>Kinome-Guided Synaptic Restoration in Alzheimer’s Disease</h1><p class="hero-intro">Could the signaling state '
            'of surviving neurons help determine whether induced plasticity leads to useful, lasting connections?</p>'
            '<p class="research-label">' + STATUS + '</p></section><div class="wrap">' + status_note() + '</div>'
            '<article class="wrap reading section research-reading"><h2>The idea in plain language</h2>'
            '<p>Synapses are the connections through which neurons communicate. Human pathology and imaging studies link '
            'Alzheimer’s disease with synaptic deficits. They do not show that adding connections alone restores memory.' + refs(prefix, 1, 2) + '</p>'
            '<p>Separate studies in mice and other rodent models show that certain compounds can change neuronal structure and '
            'plasticity-related signaling. Those findings motivate questions about surviving circuits, but are not evidence of '
            'recovery in people with Alzheimer’s.' + refs(prefix, 3, 4, 6) + '</p>'
            '<div class="research-hypothesis"><p class="small-label">Proposed, not demonstrated</p><h2>The central question</h2>'
            '<p>Could disease-associated kinase-network states help explain which surviving Alzheimer’s-affected neurons can '
            'undergo beneficial, durable functional remodeling—and which cannot?</p></div>'
            '<h2>What “kinome-guided” means</h2><p>The kinome is the collection of protein kinases, enzymes involved in cellular '
            'signaling. Here, “kinome-guided” means asking whether patterns of kinase activity could inform a future assessment '
            'of plasticity. It is not a validated test, biomarker, or treatment-selection method.' + refs(prefix, 5, 8) + '</p>'
            '<p>An external NIH/NIA award, R01AG083628, describes investigations of kinase networks across Alzheimer’s-relevant '
            'human tissue and cell models. It provides scientific context, not funding, access to a laboratory, or institutional '
            'approval for this independent proposal.' + refs(prefix, 5) + '</p>'
            '<h2>What the evidence does—and does not—say</h2>'
            '<div class="research-evidence"><section><h3>Observed in published work</h3><p>Synaptic deficits in human Alzheimer’s '
            'studies; plasticity-related structural and signaling changes in rodent studies; and altered kinase activity in '
            'human-derived familial Alzheimer’s astrocytes.' + refs(prefix, 1, 2, 3, 4, 6, 8) + '</p></section>'
            '<section><h3>Still an open hypothesis</h3><p>That kinase patterns predict a beneficial response in Alzheimer’s-relevant '
            'neurons, that structural remodeling produces sustained functional improvement, or that either would improve human '
            'memory or everyday life. This project has generated no data establishing these outcomes.</p></section></div>'
            '<h2>Why caution is part of the science</h2><p>More connections do not necessarily mean better-organized signaling. '
            'Functional usefulness, persistence, and safety would all need examination. One human imaging study also found '
            'reduced 5-HT2A receptor binding in early Alzheimer’s, raising questions about whether a response observed in other '
            'models would carry over.' + refs(prefix, 7) + '</p>'
            '<p>The recent mouse study separated a cell-specific plasticity mechanism from the head-twitch response, a rodent '
            'behavioral proxy. It did not establish that subjective psychedelic effects are unnecessary for benefit in humans.' + refs(prefix, 3) + '</p>'
            '<h2>What scientific evaluation would need to address</h2><p>Is the hypothesis biologically plausible and distinguishable '
            'from existing work? Can a structural response be linked to useful function rather than a single marker? What disease '
            'context, durability limits, or adverse effects could make the approach fail? These are questions for qualified '
            'investigator review, not a public experimental protocol.</p>'
            '<h2>What “restoration” does not mean</h2><p>Here, restoration names a hoped-for functional outcome in surviving circuits. '
            'It does not mean regrowing lost brain tissue, reversing established atrophy, or offering an established cure. '
            'The cited papers do not validate this proposed approach as an Alzheimer’s treatment.</p>'
            '<aside class="scope-note">This page provides no dosing or self-treatment guidance. The Maxine Project is not offering '
            'psilocybin, other investigational compounds, or participation in a clinical trial.</aside>'
            '<div class="actions"><a class="button primary" href="' + prefix + 'research/references/">Examine the references</a>'
            '<a class="text-link" href="' + prefix + 'connect.html#founder">Founder &amp; correspondence</a></div>' + editorial(prefix) + '</article>')


def reference_library(prefix):
    cards = []
    for r in REFERENCES:
        links = ('<a href="https://doi.org/' + E(r['doi'], quote=True) + '" rel="noreferrer">Original publication (DOI)</a>'
                 ' · <a href="https://pubmed.ncbi.nlm.nih.gov/' + r['pmid'] + '/" rel="noreferrer">PubMed record &amp; abstract</a>'
                 if 'doi' in r else '<a href="' + E(r['url'], quote=True) + '" rel="noreferrer">Official HHS / NIH award record</a>')
        cards.append('<article class="research-reference" id="' + r['id'] + '"><p class="small-label">' + str(r['number']) + ' / '
                     + E(r['kind']) + '</p><h2>' + E(r['title']) + '</h2><p class="research-bibliography">' + E(r['authors']) + ' '
                     + E(r['publication']) + '</p><p><strong>What it supports.</strong> ' + E(r['supports']) + '</p>'
                     '<p><strong>What it does not establish.</strong> ' + E(r['limits']) + '</p><p class="research-source-links">' + links + '</p></article>')
    return ('<section class="page-intro wrap research-intro"><p class="eyebrow">Research &amp; Innovation</p><h1>Scientific References</h1>'
            '<p class="hero-intro">Follow each idea back to its source—and read the limits alongside the findings.</p>'
            '<p class="research-label">Selected primary publications and an external NIH/NIA award record · Checked ' + VERIFIED_DATE + '</p></section>'
            '<div class="wrap reading"><aside class="scope-note">Publication details and these concise annotations were checked '
            'against PubMed abstracts and the official award summary. This is a selected reading list, not a systematic review '
            'or an independent peer review of the proposal. An award record describes a funded project, not a completed result. '
            'Citing authors or institutions does not imply their participation or endorsement.</aside>'
            '<nav class="research-reference-index" aria-label="Jump to a scientific reference">' + ''.join(
                '<a href="#' + r['id'] + '">[' + str(r['number']) + '] ' + E(r['authors'].split(',')[0]) + '</a>' for r in REFERENCES)
            + '</nav>' + ''.join(cards) + editorial(prefix) + '</div>')


def research_page(path, prefix):
    render = {'research/index.html': overview, 'research/synaptic-restoration/index.html': concept,
              'research/references/index.html': reference_library}
    return subnav(prefix, path) + render[path](prefix)
