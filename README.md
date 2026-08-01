# Gökçe Uludoğan — Academic Website

Source for [gokceuludogan.github.io](https://gokceuludogan.github.io), the academic website of Gökçe Uludoğan. The site presents research in computational biology, machine learning, cheminformatics, and natural language processing.

## Content

- Research profile and current news
- Selected publications with figures, paper and code links, and copyable BibTeX
- Research and teaching experience
- Education and academic profiles

The primary homepage content is in [`_pages/about.md`](_pages/about.md). Site identity and profile links are configured in [`_config.yml`](_config.yml), while custom presentation styles live in [`assets/css/main.scss`](assets/css/main.scss).

## Run locally

Install Ruby and the Jekyll prerequisites, then run:

```bash
bundle install
bundle exec jekyll serve
```

Open <http://127.0.0.1:4000>. Jekyll watches source files and rebuilds the site while the server is running.

## Deploy

The [GitHub Pages workflow](.github/workflows/pages.yml) builds and deploys the site whenever a commit is pushed to `main`. It can also be run manually from the repository's **Actions** tab.

Before the first deployment, open **Settings → Pages** in [gokceuludogan/gokceuludogan.github.io](https://github.com/gokceuludogan/gokceuludogan.github.io) and select **GitHub Actions** as the publishing source.

Deployment details and validation instructions are documented in [`docs/pages-deployment.md`](docs/pages-deployment.md).

## Acknowledgements

This website is adapted from [RayeRen/acad-homepage.github.io](https://github.com/RayeRen/acad-homepage.github.io), released under the MIT License. That project builds on ideas and components from [Minimal Mistakes](https://github.com/mmistakes/minimal-mistakes) and [Academic Pages](https://github.com/academicpages/academicpages.github.io). Icons are provided by Font Awesome and Academicons under their respective licenses.

Personal content, publication metadata, imagery, and custom interface work in this repository belong to their respective authors and rights holders.

## License

The inherited website code remains available under the terms in [`LICENSE`](LICENSE). Publication figures, photographs, CV materials, and personal content are not relicensed by that software license unless explicitly stated.
