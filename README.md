# WholeMind Living + The Maxine Project

Shared source for two separate websites:

- WholeMind Living: https://wholemindliving.com
- The Maxine Project: https://themaxineproject.org

The websites share layouts, resource templates, and Auto / Light / Dark appearance controls, while retaining separate brand colors, content, domains, and disclosures.

## Netlify publishing

Link **each existing project**, `wholemindliving` and `themaxineproject`, to this repository. Do not create replacement Netlify projects or change DNS.

| Setting | Both existing projects |
| --- | --- |
| Production branch | `main` |
| Base directory | Leave blank (repository root) |
| Build command | `python3 build.py --deploy && python3 check_site.py` |
| Publish directory | `publish` |
| Package directory | Leave blank |

`netlify.toml` defines the build command and publish directory. The builder uses Netlify's `SITE_ID` to select the correct brand for the two existing projects. **No additional environment variable is required for these projects.** On another project, set `SITE_BRAND=wholemind` or `SITE_BRAND=maxine` explicitly. A conflicting brand on either existing project fails the build rather than publishing the wrong website.

Once the projects are linked, pushes to `main` trigger their Netlify builds. Use pull requests and Netlify Deploy Previews for changes that need review. The GitHub validation workflow checks both builds and appearance-state behavior; Netlify performs production publishing. No Netlify token is stored in this repository.

## Local builds

Python 3.10+ is sufficient; the website build uses only the standard library.

```sh
python3 build.py
python3 check_site.py
node test_appearance_state.js
```

This creates `dist/wholemind`, `dist/maxine`, and a two-site local preview in `preview/`. To serve the preview:

```sh
python3 -m http.server 8000 --directory preview
```

To simulate a deployment:

```sh
SITE_BRAND=wholemind python3 build.py --deploy
SITE_BRAND=maxine python3 build.py --deploy
```

## Source map

- `src/content.py`: both brands' copy, resource contents, and source references.
- `src/meet_maxine.py`: The Maxine Project's source-labeled memorial page, with an authentic family-supplied portrait, newspaper source notes, and first-person recollections.
- `src/family_account.py`: A dedicated historical family account about Rev. John Robert Boggs Jr. and *I'll Move Over*.
- `docs/family-account-editorial.md`: provenance, bibliographic uncertainties, and release boundaries for that page.
- `build.py`: shared page templates, headers, navigation, and build selection.
- `assets/site.css`: shared responsive layout, light/dark palettes, and light-only print styles.
- `assets/appearance-init.js`: appearance preference and first-paint initialization.
- `assets/site.js`: appearance controls, brand-link handoff, and local worksheet interactions.
- `downloads/`: six original PDF resources, committed to the repository. The additional Maxine-only *Preserving Their Story* guide is a print-friendly HTML worksheet without a separate PDF download.
- `BASELINE_PDF_HASHES.json`: SHA-256 integrity baseline for those PDFs.
- `check_site.py`: dependency-free page/link/resource and deployment checks.
- `test_appearance_state.js`: isolated appearance behavior tests (not a live-browser audit).

The Netlify build reads PDF files from this repository. It does not regenerate PDFs or download them from an older deployment. PDF revisions must be deliberate, reviewed, and accompanied by updated baseline hashes.

See `docs/family-visit-supplement-2026-10-28.md` for provenance and privacy boundaries for the new memory material. The private source recording and borrowed family photographs are not in the repository.\n\n## Release boundaries

The Maxine Project's `meet-maxine.html` is an editable memorial first edition; see `docs/meet-maxine-editorial.md` for provenance, its newspaper death notice and image permissions. The `family-account.html` page is likewise source-labeled and editable; see `docs/family-account-editorial.md` for the book's bibliographic boundaries and the distinction between founder family history and independent records. The review banner and `noindex` remain enabled. This migration does **not** approve final legal status, change operator disclosures, activate donations or paid products, or remove the content-review requirement. `LAUNCH_MODE=public` changes the banner and indexing only, not legal facts or access controls; use it only after approval. A review banner is not password protection.

Worksheet responses stay in the page and are not sent to a server or saved by application code. Only the appearance preference is saved when browser storage is available. Brand-switching links pass the appearance choice to the other domain. Printing remains light. Google Fonts is a third-party request as disclosed in the privacy page.

No credentials, customer data, completed worksheets, business records, or private launch notes belong in this repository. Keep any future secrets in the hosting provider's environment settings, never in client code.
