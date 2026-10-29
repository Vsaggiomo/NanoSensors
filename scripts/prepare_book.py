#!/usr/bin/env python3
"""Rebuild the MyST reading copy from the clean Binder/Colab notebook.

`source/chapter-01.ipynb` is the editable notebook that Binder and Colab open.
`chapter-01.ipynb` is the generated reading copy used by MyST / GitHub Pages.

The reading copy adds:
  * YAML frontmatter for the page title;
  * the "Interactive version" note linking to Binder/Colab;
  * Markdown image paths adjusted for the repository root;
  * MyST cell tags (`hide-input`, `remove-output`, `remove-cell`);
  * static default-state previews for the nine interactive figures.

Run from the repository root:

    python scripts/prepare_book.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import nbformat
from nbformat.v4 import new_markdown_cell

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source" / "chapter-01.ipynb"
OUT = ROOT / "chapter-01.ipynb"

BINDER = (
    "https://mybinder.org/v2/gh/Vsaggiomo/NanoSensors/HEAD"
    "?urlpath=notebooks/source/chapter-01.ipynb"
)
COLAB = (
    "https://colab.research.google.com/github/Vsaggiomo/NanoSensors"
    "/blob/main/source/chapter-01.ipynb"
)
NOTE = (
    "> **Interactive version.** This page is the reading version of the chapter. "
    f"To use the sliders, [open the chapter in Binder]({BINDER}) and run the cells "
    "(`Run` → `Run All Cells`; if asked, click **Trust**). To hide the code in the "
    "interactive notebook, use **View → Collapse All Code**. The first Binder launch "
    f"can take a minute or two. [Colab fallback]({COLAB})."
)
PREVIEW = {
    "measurement_chain_demo": "int_1_measurement_chain.png",
    "ph_indicator_demo": "int_2_ph_indicator.png",
    "fret_ruler_demo": "int_3_fret_ruler.png",
    "calibration_curve_demo": "int_4_calibration_lod.png",
    "selectivity_demo": "int_5_selectivity.png",
    "accuracy_precision_demo": "int_6_accuracy_precision.png",
    "outbreak_demo": "int_8_outbreak.png",
    "surface_to_volume_demo": "int_9_surface_to_volume.png",
    "quantum_dot_demo": "int_10_quantum_dots.png",
}
ASSET = re.compile(r'<img\s+src="(?P<src>[^"]+)"(?:\s+alt="(?P<alt>[^"]*)")?[^>]*>')


def main() -> int:
    if not SOURCE.exists():
        print(f"Missing source notebook: {SOURCE}", file=sys.stderr)
        return 1

    nb = nbformat.read(SOURCE, as_version=4)

    # The source notebook lives in source/, so its relative figure paths are
    # ../figures/...; the reading copy is at the repository root.
    for cell in nb.cells:
        if cell.cell_type != "markdown":
            continue
        cell.source = cell.source.replace("../figures/", "figures/")
        cell.source = cell.source.replace(
            "https://raw.githubusercontent.com/Vsaggiomo/NanoSensors/main/figures/", "figures/"
        )
        cell.source = ASSET.sub(
            lambda m: f"![{m.group('alt') or ''}]({m.group('src')})", cell.source
        )
        cell.source = re.sub(r"\n?<a id=\"[^\"]+\"></a>\n?", "\n", cell.source).strip("\n")

    nb.cells.insert(0, new_markdown_cell("---\ntitle: Chapter 1 · Introduction to Nanosensors\n---"))
    nb.cells.insert(2, new_markdown_cell(NOTE))

    cells = []
    missing_previews = []
    for cell in nb.cells:
        if cell.cell_type == "code":
            source = cell.source
            cell.metadata.setdefault("tags", [])
            if "Chapter 1 - environment setup" in source:
                cell.metadata["tags"] = ["remove-cell"]
            elif "interact(" in source:
                cell.metadata["tags"] = ["hide-input", "remove-output"]
                fname = next((img for fn, img in PREVIEW.items() if f"def {fn}(" in source), None)
                if fname is None or not (ROOT / "figures" / fname).exists():
                    missing_previews.append(fname or "unknown")
                else:
                    cells.append(
                        new_markdown_cell(
                            f"![Static preview of the interactive figure](figures/{fname})\n\n"
                            "*Static preview of the default state. "
                            f"[Open the chapter in Binder]({BINDER}) to move the sliders.*"
                        )
                    )
            else:
                cell.metadata["tags"] = ["hide-input"]
        cells.append(cell)

    nb.cells = cells
    nbformat.write(nb, OUT)

    if missing_previews:
        print(
            "Warning: missing preview images for: " + ", ".join(missing_previews),
            file=sys.stderr,
        )
        print("Run `python scripts/generate_previews.py` first.", file=sys.stderr)
        return 1

    print(f"Wrote {OUT.relative_to(ROOT)} ({len(nb.cells)} cells).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
