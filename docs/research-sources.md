# Research & Innovation — editorial record

Version 1.0 / October 25, 2026.

## Public scope

This release adds three Maxine-only routes: `/research/`, `/research/synaptic-restoration/`, and `/research/references/`, plus a homepage entry point and a founder section on `/connect.html#founder`. It presents an independent exploratory hypothesis. It does not establish an active study, treatment, funded research program, academic affiliation, or endorsement.

The full proposal, experimental protocol, correspondence, potential recipients, and personal records are intentionally absent from this public repository and the deployed site. No dosing, recruitment, data collection, payments, or donations are added. The existing legal disclosures and review/noindex settings remain unchanged.

## Source verification and claim boundaries

The machine-readable bibliography and concise annotations are in `src/research_references.py`. Publication metadata and abstracts were checked against PubMed records; the external award was checked against the official HHS TAGGS record. This is not a systematic literature review, full-text critical appraisal of every paper, or independent scientific peer review.

1. Terry et al. (1991), PMID 1789684, DOI 10.1002/ana.410300410: human synaptic pathology/cognition association; not evidence that increasing synapse count restores memory.
2. Chen et al. (2018), PMID 30014145, DOI 10.1001/jamaneurol.2018.1836: cross-sectional SV2A PET marker; no treatment experiment.
3. Baker et al. (2026), PMID 42881224, DOI 10.1038/s41593-026-02490-y: cell-specific mouse synaptic remodeling and head-twitch dissociation; no human hallucination or Alzheimer recovery conclusion.
4. Aarrestad et al. (2025), PMID 40760185, DOI 10.1038/s41593-025-02021-1: rodent plasticity/pathway evidence; no Alzheimer clinical efficacy; commercial interests are disclosed in the publication.
5. NIH/NIA R01AG083628, University of Toledo, HHS TAGGS: external project scope and performance dates; not project funding, endorsement, findings, or an agreement to evaluate the proposal. https://taggs.hhs.gov/Detail/AwardDetail?arg_AwardNum=R01AG083628&arg_ProgOfficeCode=102
6. Shao et al. (2021), PMID 34228959, DOI 10.1016/j.neuron.2021.06.008: mouse structural plasticity; no restoration of human Alzheimer circuits.
7. Marner et al. (2012), PMID 20510480, DOI 10.1016/j.neurobiolaging.2010.03.023: reduced human 5-HT2A binding; an obstacle/question rather than a response predictor.
8. Siciliano et al. (2025), PMID 40656638, DOI 10.1016/j.bbih.2025.101044: familial Alzheimer astrocyte-model kinomic/inflammatory changes; no clinical or synaptic-restoration efficacy.

The founder's nursing credentials and family motivation are user-provided. They do not constitute independent validation of the hypothesis. AI assistance is disclosed on the pages. No researcher is named as a prospective collaborator and no institutional logo is used.

## Contact release gate

No operational project mailbox has been verified. Do not display `david@themaxineproject.org` as active until delivery is confirmed. The founder's portfolio contact page was a non-submitting preview when inspected; the website link is for background, not a verified communication channel. The public founder section states the limitation. No email is sent by this release.

## Engineering checks

`check_site.py` enforces both brand builds, all internal targets, original PDF hashes, publish integrity, and the 57 research scope/routing assertions in `test_research.py`. Existing appearance and family-story tests remain in GitHub Actions. Six original PDFs are unchanged.

Local offline Chromium rendering covered six relevant pages at five widths in light and dark mode (60 checks), using fallback fonts because external fonts were unavailable; no horizontal overflow or JavaScript page errors was found. Manual appearance controls and light print styles were checked. This is not a hosted browser/navigation test or a complete accessibility audit.

Before future changes, maintain the distinction between published observations, proposed inferences, external funding, and actual project activities. Verify additions against original sources, retain direct citation targets, and do not commit confidential protocols or correspondence to this repository.
