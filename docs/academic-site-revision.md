# Academic website revision report

## Method

The site content was derived from the structured LaTeX files in `cv-resume/structured_cv/data/`, treating those files as the canonical source. Identity and contact fields came from `cv_data.tex`; research themes from `summary.tex` and `skills.tex`; positions from `experience.tex`; degrees from `education.tex`; publications from `publications.tex`; and service and awards from their respective data files.

The homepage prioritizes an academic visitor's likely path: identity and research focus, recent news, research themes, selected publications, experience, education, service, and technical methods. Publications with URLs in the source data retain those links. No links were invented for records whose source URL was empty.

## Results

- Replaced all demonstration text and profiles with Gökçe Uludoğan's information.
- Added a responsive research overview, selected publication list, career timeline, education, service, recognition, and skills.
- Updated navigation, metadata, timezone, email, GitHub, and Google Scholar settings.
- Added a neutral monogram avatar because no portrait was present in the repository.
- Added a direct link to the existing PDF CV.
- Introduced a restrained visual system using academic navy, cool blue, charcoal, serif display typography, cards, and a mobile layout.
- Reformatted selected publications as visual cards with neutral image placeholders, venue tags, verified paper links, disabled missing-code states, and expandable BibTeX citations.
- Replaced the education table with a responsive degree timeline that gives each program, date range, institution, and research detail a clear hierarchy.
- Added small, keyboard-accessible feather tooltips to PUFFIN and TURNA; each bird note floats above the title while hovered or focused.
- Positioned publication venue tags in their own row above thumbnails so they never obscure figure content.
- Replaced BibTeX disclosure elements with direct one-click copy buttons, hidden citation sources, success feedback, and an older-browser fallback.

## Reproduction and validation

Run the content checks from the repository root:

```bash
python3 scripts/validate_academic_site.py
```

Build the Jekyll site with the locked dependencies:

```bash
bundle exec jekyll build
```

The homepage remains hand-authored Markdown/HTML so that editorial changes are straightforward. When the CV changes, update the corresponding homepage entries and extend the validation script if new canonical fields should be enforced.
