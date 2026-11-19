"""Copy the bundled front page (entry.png) to the output directory.

The entry is the bundled front-page image shipped with this repo.
"""
import os
import shutil
from pathlib import Path

src = Path(__file__).resolve().parent / "entry.png"
out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out_dir.mkdir(parents=True, exist_ok=True)  # create output dir if missing
# Copy the bundled entry.png to the output location.
out_file = out_dir / "entry.png"
shutil.copyfile(src, out_file)
# Guard: ensure the copied file exists and is non-empty.
if not out_file.is_file() or out_file.stat().st_size == 0:
    raise RuntimeError(f"copy failed: {out_file} is missing or empty")
