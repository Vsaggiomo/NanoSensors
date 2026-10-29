#!/usr/bin/env python3
"""Regenerate the static previews for the interactive figures.

The previews are the *default* state of each `ipywidgets.interact` demo.
This script executes the code cells from `source/chapter-01.ipynb`, replacing
`interact` with a small shim that calls each demo with its default values.
Each demo's `save_fig(...)` then writes the corresponding
`figures/int_*.png` file.

Run from the repository root:

    python scripts/generate_previews.py
"""
from __future__ import annotations

import os
import sys
import tempfile
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", os.path.join(tempfile.gettempdir(), "mplconfig-nanosensors-previews"))

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import nbformat
import ipywidgets as iw

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source" / "chapter-01.ipynb"


def fake_interact(f, **kwargs):
    """Call a demo function once with the default widget values."""
    values = {k: getattr(v, "value", v) for k, v in kwargs.items()}
    f(**values)
    plt.close("all")


def main() -> int:
    if not SOURCE.exists():
        print(f"Missing source notebook: {SOURCE}", file=sys.stderr)
        return 1

    os.chdir(ROOT)
    iw.interact = fake_interact
    plt.show = lambda *args, **kwargs: None  # Agg backend: keep execution quiet

    nb = nbformat.read(SOURCE, as_version=4)
    namespace = {"__name__": "__main__"}
    for index, cell in enumerate(nb.cells):
        if cell.cell_type != "code":
            continue
        try:
            exec(compile(cell.source, f"<source cell {index}>", "exec"), namespace)
        except Exception as exc:  # pragma: no cover - surfaced for the user
            print(f"Failed in source cell {index}: {exc}", file=sys.stderr)
            raise
        plt.close("all")

    expected = [
        "int_1_measurement_chain.png",
        "int_2_ph_indicator.png",
        "int_3_fret_ruler.png",
        "int_4_calibration_lod.png",
        "int_5_selectivity.png",
        "int_6_accuracy_precision.png",
        "int_8_outbreak.png",
        "int_9_surface_to_volume.png",
        "int_10_quantum_dots.png",
    ]
    missing = [name for name in expected if not (ROOT / "figures" / name).exists()]
    if missing:
        print("Missing previews: " + ", ".join(missing), file=sys.stderr)
        return 1

    print("Regenerated default-state previews:")
    for name in expected:
        print(f"  figures/{name}")
    print("Done.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
