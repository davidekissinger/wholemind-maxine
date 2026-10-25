"""Selected public sources, checked 2026-10-25 against primary records.

These concise annotations are not a systematic review, clinical advice, or evidence
that The Maxine Project has conducted experiments. No private proposal is stored.
"""
VERIFIED_DATE = 'October 25, 2026'
REFERENCES = (
    {
        'id': 'terry-1991', 'number': 1, 'authors': 'Terry RD, Masliah E, Salmon DP, et al.',
        'title': 'Physical basis of cognitive alterations in Alzheimer’s disease: synapse loss is the major correlate of cognitive impairment',
        'publication': 'Annals of Neurology. 1991;30(4):572–580.',
        'kind': 'Human observational study', 'doi': '10.1002/ana.410300410', 'pmid': '1789684',
        'supports': 'Human pathology findings associated lower synaptic density with greater cognitive impairment.',
        'limits': 'An association does not establish that increasing synapse number will restore memory or alter disease progression.',
    },
    {
        'id': 'chen-2018', 'number': 2, 'authors': 'Chen MK, Mecca AP, Naganawa M, et al.',
        'title': 'Assessing Synaptic Density in Alzheimer Disease With Synaptic Vesicle Glycoprotein 2A Positron Emission Tomographic Imaging',
        'publication': 'JAMA Neurology. 2018;75(10):1215–1224.',
        'kind': 'Human imaging study', 'doi': '10.1001/jamaneurol.2018.1836', 'pmid': '30014145',
        'supports': 'A small cross-sectional PET study found lower hippocampal SV2A binding in participants with Alzheimer’s disease than in cognitively normal participants.',
        'limits': 'SV2A binding is a marker related to synaptic density. This was not a treatment trial or a demonstration of restored synaptic function.',
    },
    {
        'id': 'baker-2026', 'number': 3, 'authors': 'Baker JJ, Kogan E, Ma S, Lu J, Zuo Y.',
        'title': '5-HT2A receptors in layer 5 pyramidal neurons mediate the neuroplastic but not the hallucinogenic effects of psilocybin',
        'publication': 'Nature Neuroscience. Published online October 15, 2026.',
        'kind': 'Mouse mechanistic study', 'doi': '10.1038/s41593-026-02490-y', 'pmid': '42881224',
        'supports': 'Cell-type-specific experiments linked cortical layer 5 neuronal 5-HT2A signaling to psilocybin-induced synaptic remodeling, while separating it from the mouse head-twitch response.',
        'limits': 'The head-twitch response is a behavioral proxy, not a direct measure of human hallucinations. The study does not demonstrate recovery in Alzheimer’s disease.',
    },
    {
        'id': 'aarrestad-2025', 'number': 4, 'authors': 'Aarrestad IK, Cameron LP, Fenton EM, et al.',
        'title': 'The psychoplastogen tabernanthalog induces neuroplasticity without proximate immediate early gene activation',
        'publication': 'Nature Neuroscience. 2025;28:1919–1931.',
        'kind': 'Rodent mechanistic study', 'doi': '10.1038/s41593-025-02021-1', 'pmid': '40760185',
        'supports': 'Rodent experiments linked tabernanthalog-induced cortical plasticity to 5-HT2A, TrkB, mTOR, and AMPA signaling without the same immediate gene-activation pattern seen with psychedelics.',
        'limits': 'These preclinical findings do not establish safety or cognitive benefit in people with Alzheimer’s. The publication reports commercial interests involving several authors.',
    },
    {
        'id': 'nia-kinome', 'number': 5, 'authors': 'U.S. Department of Health and Human Services, TAGGS.',
        'title': 'Investigation of active kinome networks in Alzheimer’s dementia',
        'publication': 'NIH / National Institute on Aging award R01AG083628. Recipient: University of Toledo. Performance period: September 15, 2024–May 31, 2029.',
        'kind': 'External NIH/NIA award record',
        'url': 'https://taggs.hhs.gov/Detail/AwardDetail?arg_AwardNum=R01AG083628&arg_ProgOfficeCode=102',
        'supports': 'The award summary describes kinase-network studies using human postmortem tissue and induced-pluripotent-stem-cell-derived systems relevant to Alzheimer’s progression.',
        'limits': 'This is an external funded project, not a result, an award to The Maxine Project, or an agreement to evaluate this proposal. Its scope is not extended by this website.',
    },
    {
        'id': 'shao-2021', 'number': 6, 'authors': 'Shao L-X, Liao C, Gregg I, et al.',
        'title': 'Psilocybin induces rapid and persistent growth of dendritic spines in frontal cortex in vivo',
        'publication': 'Neuron. 2021;109(16):2535–2544.e4.',
        'kind': 'Mouse imaging study', 'doi': '10.1016/j.neuron.2021.06.008', 'pmid': '34228959',
        'supports': 'Longitudinal imaging in mice documented increased dendritic spine formation and persistent structural changes after psilocybin exposure.',
        'limits': 'Mouse cortical remodeling is not proof of repair of Alzheimer’s-affected human circuits, restoration of lost neurons, or lasting cognitive recovery.',
    },
    {
        'id': 'marner-2012', 'number': 7, 'authors': 'Marner L, Frokjaer VG, Kalbitzer J, et al.',
        'title': 'Loss of serotonin 2A receptors exceeds loss of serotonergic projections in early Alzheimer’s disease: a combined [11C]DASB and [18F]altanserin-PET study',
        'publication': 'Neurobiology of Aging. 2012;33(3):479–487. Published online in 2010.',
        'kind': 'Human imaging study', 'doi': '10.1016/j.neurobiolaging.2010.03.023', 'pmid': '20510480',
        'supports': 'A small PET study found reduced cortical 5-HT2A receptor binding in early Alzheimer’s disease.',
        'limits': 'This raises a receptor-availability question for the hypothesis; it does not establish whether an individual would benefit from a plasticity-promoting intervention.',
    },
    {
        'id': 'siciliano-2025', 'number': 8, 'authors': 'Siciliano B, Henkel ND, Ryan WG V, et al.',
        'title': 'Proinflammatory transcriptomic and kinomic alterations in astrocytes derived from patients with familial Alzheimer’s disease',
        'publication': 'Brain, Behavior, & Immunity – Health. 2025;47:101044.',
        'kind': 'Human-derived cell study', 'doi': '10.1016/j.bbih.2025.101044', 'pmid': '40656638',
        'supports': 'Patient-derived astrocyte experiments reported inflammatory and kinase-signaling differences in familial Alzheimer’s models.',
        'limits': 'Cell-model pathway findings do not demonstrate clinical benefit or show that a synaptic-restoration strategy works. They support considering the environment around neurons.',
    },
)
