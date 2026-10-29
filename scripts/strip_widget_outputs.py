#!/usr/bin/env python3
"""Remove saved widget outputs from the clean Binder/Colab notebook.

`source/chapter-01.ipynb` is the editable notebook. Earlier interactive runs
leave `application/vnd.jupyter.widget-view+json` outputs in the file; when the
notebook is opened in Binder, those can appear as stale or frozen widgets
until the reader runs the cells. Static figure outputs are kept.

Run from the repository root:

    python scripts/strip_widget_outputs.py
"""
from __future__ import annotations

import sys
from pathlib import Path

import nbformat

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source" / "chapter-01.ipynb"
WIDGET_MIME = "application/vnd.jupyter.widget-view+json"


def main() -> int:
    if not SOURCE.exists():
        print(f"Missing source notebook: {SOURCE}", file=sys.stderr)
        return 1

    nb = nbformat.read(SOURCE, as_version=4)
    removed = 0
    for cell in nb.cells:
        if cell.cell_type != "code":
            continue
        kept = []
        for output in cell.get("outputs", []):
            data = output.get("data", {})
            if WIDGET_MIME in data:
                removed += 1
                continue
            kept.append(output)
        cell.outputs = kept

    nbformat.write(nb, SOURCE)
    print(f"Removed {removed} saved widget output(s) from {SOURCE.relative_to(ROOT)}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
