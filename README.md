# Nanosensors — interactive open book

This repository contains the web edition of **Nanosensors: from single molecules to smart devices**.

- **Read the book:** <https://vsaggiomo.github.io/NanoSensors/>
- **Run the notebook in Binder:** <https://mybinder.org/v2/gh/Vsaggiomo/NanoSensors/HEAD?labpath=chapter-01.ipynb>

The site is built with Jupyter Book 2 / MyST and deployed to GitHub Pages by GitHub Actions. Interactive figures use `ipywidgets` and are connected to a live Binder kernel through MyST’s in-page execution (Thebe).

## Repository layout

```text
.
├── myst.yml                  # MyST/Jupyter Book configuration (TOC, Binder, theme)
├── index.md                  # landing page
├── chapter-01.ipynb          # the chapter notebook (book build copy)
├── figures/                  # all figures used by the chapter
├── requirements.txt          # Binder environment
└── .github/workflows/deploy.yml
```

## Local preview

```bash
# Node 18+ and npm are required by MyST
npm install -g mystmd

# from this repository root
myst start
```

Or, using the Jupyter Book CLI:

```bash
pip install jupyter-book
jupyter-book start
```

The site is served at <http://localhost:3000> by default.

## Build the static site

```bash
myst build --html
```

The output is written to `_build/html`.

## Updating the chapter

`chapter-01.ipynb` in this repository is the book-build version of the chapter. It differs from the Jupyter working copy only in that the two raw HTML `<img>` figure tags have been converted to Markdown images, so MyST can copy the figures into the built site. Keep the notebook code and prose in sync with the working copy when you make changes.

## Deployment

Every push to `main` triggers `.github/workflows/deploy.yml`, which builds the site and deploys it to GitHub Pages. GitHub Pages must be set to use **GitHub Actions** as its source (Settings → Pages).

The Binder environment is built from `requirements.txt`. The first Binder launch can take a minute or two while the image is built and cached.
