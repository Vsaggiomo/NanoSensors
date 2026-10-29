# Nanosensors — interactive open book

**Read the book:** <https://vsaggiomo.github.io/NanoSensors/>

**Interactive chapter (live Jupyter kernel):** <https://mybinder.org/v2/gh/Vsaggiomo/NanoSensors/HEAD?urlpath=notebooks/chapter-01.ipynb>

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Vsaggiomo/NanoSensors/HEAD?urlpath=notebooks/chapter-01.ipynb)

The site is built with **Jupyter Book 2 / MyST** and deployed to **GitHub Pages** by GitHub Actions.

The chapter contains nine interactive `ipywidgets` + `matplotlib` figures. They require a live Jupyter kernel, so the interactive version opens in **Binder** (full JupyterLab). The GitHub Pages site is the reading version with static figures. A **Colab fallback** is available at:

<https://colab.research.google.com/github/Vsaggiomo/NanoSensors/blob/main/chapter-01.ipynb>

> **Why not in-page execution?** MyST/Thebe can execute the notebook against a Binder kernel, but the current MyST theme does not render `ipywidgets` controls reliably: the widget outputs are replaced by placeholders. The Binder route uses the full Jupyter widget stack, so the sliders work. In-page support may improve as MyST/Thebe matures.

## Repository layout

```text
.
├── myst.yml                  # MyST/Jupyter Book configuration (TOC, theme)
├── index.md                  # landing page
├── chapter-01.ipynb          # the chapter notebook (book build copy)
├── figures/                  # all figures used by the chapter
├── requirements.txt          # Binder environment
└── .github/workflows/deploy.yml
```

## Reading locally

```bash
# Node 18+ and npm are required by MyST
npm install -g mystmd

# from this repository root
myst start
```

Or with the Jupyter Book CLI:

```bash
pip install jupyter-book
jupyter-book start
```

The site is served at <http://localhost:3000> by default.

## Build the static site

```bash
myst build --html
```

The output is written to `_build/html`. For GitHub Pages, set the base URL first:

```bash
BASE_URL=/NanoSensors myst build --html
```

## Updating the chapter

`chapter-01.ipynb` in this repository is the **book-build version** of the chapter. It differs from the Jupyter working copy in two ways:

1. the raw HTML `<img>` figure tags are converted to Markdown images, so MyST copies the figures into the built site;
2. a short “Interactive version” link to Binder is added at the top.

Keep the notebook code and prose in sync with the working copy when you make changes.

## Deployment

Every push to `main` triggers `.github/workflows/deploy.yml`, which builds the site with MyST and deploys it to GitHub Pages. GitHub Pages must use **GitHub Actions** as its source (Settings → Pages).

The Binder environment is built from `requirements.txt`. The first Binder launch can take a minute or two while the image is built and cached.
