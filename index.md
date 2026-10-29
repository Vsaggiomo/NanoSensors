---
title: Nanosensors
---

# Nanosensors

**An interactive open book — from single molecules to smart devices.**

This is the web edition of the book, built with Jupyter Book 2 / MyST and deployed on GitHub Pages.

<p style="margin: 28px 0 24px 0;">
<a href="chapter-01/" style="display:inline-block; padding:12px 20px; margin:0 10px 10px 0; background:#1f4e79; color:#fff; border-radius:6px; text-decoration:none; font-weight:600;">Read Chapter 1 &rarr;</a>
<a href="https://mybinder.org/v2/gh/Vsaggiomo/NanoSensors/HEAD?labpath=chapter-01.ipynb" style="display:inline-block; padding:12px 20px; margin:0 10px 10px 0; background:#e76f51; color:#fff; border-radius:6px; text-decoration:none; font-weight:600;">Open the interactive chapter in Binder &rarr;</a>
</p>

## How to use the interactive figures

The chapter contains nine interactive figures built with `ipywidgets` and `matplotlib`. They need a live Jupyter kernel, so they run in **Binder**, not in the static page:

1. Click **Open the interactive chapter in Binder** above (or the link at the top of Chapter 1).
2. Wait for Binder to build/start the environment. The first launch can take a minute or two; later launches are faster.
3. The chapter opens in JupyterLab. Run the cells (`Run` &rarr; `Run All Cells`) and use the sliders.
4. If Binder is unavailable, use the [Colab fallback](https://colab.research.google.com/github/Vsaggiomo/NanoSensors/blob/main/chapter-01.ipynb).

**Why not in-page?** MyST’s in-page execution (Thebe) can execute the Python cells, but the current MyST theme does not render `ipywidgets` controls reliably; it shows placeholders instead of sliders. The Binder route uses the real JupyterLab widget stack, so the sliders work.

## Chapter 1

The first chapter builds the conceptual toolkit for the rest of the book:

- what a sensor is, and how it differs from a device;
- chemical versus physical sensors;
- sensitivity, limit of detection, selectivity, accuracy and precision;
- why sensors matter for exploration, AI and public health;
- what changes at the nanoscale, and what a “nanosensor” actually is.

[Start reading Chapter 1 &rarr;](chapter-01.ipynb)
