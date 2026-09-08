"""Compile both manuscripts with XeLaTeX and Biber (Python standard library)."""
from pathlib import Path
import shutil
import subprocess

root = Path(__file__).resolve().parent
for tool in ("xelatex", "biber"):
    if not shutil.which(tool):
        raise SystemExit(f"Missing {tool}; install a current TeX distribution with biblatex-apa.")
for name in ("main", "extended"):
    for cmd in (["xelatex", "-interaction=nonstopmode", "-halt-on-error", name + ".tex"],
                ["biber", name],
                ["xelatex", "-interaction=nonstopmode", "-halt-on-error", name + ".tex"],
                ["xelatex", "-interaction=nonstopmode", "-halt-on-error", name + ".tex"]):
        subprocess.run(cmd, cwd=root, check=True)
print("Built main.pdf and extended.pdf")
