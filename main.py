"""convince-the-ai-judge-to-visit-your-house-20261125 entrypoint (Python 3.13, standard library only).

Copies the invitation image held in this repository to the output directory
(/output, or $MAKEFUN_OUTPUT_DIR / $OUTPUT_DIR when set). Deterministic: the same bytes
are written on every run; no network, no randomness. The image itself is drawn
by draw.py in this repo (PIL, original artwork, no external assets).
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR")
           or os.environ.get("OUTPUT_DIR", "/output"))

OUT.mkdir(parents=True, exist_ok=True)
shutil.copyfile(HERE / "entry.png", OUT / "entry.png")
