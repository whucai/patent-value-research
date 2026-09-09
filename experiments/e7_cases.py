#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""E7 — Case study and qualitative validation.

Sample 12 trajectories across profile regions x size strata; two technically
qualified raters assess each from dated patent evidence WITHOUT model values
(blinded). Report agreement (Cohen's kappa, J. Cohen 1960), disagreements, and
adjudication. Cases rejecting the a-priori category reading are flagged.

Inputs:
    --profiles: experiments/out/e2_profiles.parquet
    --T:        experiments/out/e2_T.parquet
    --patterns: experiments/out/e4_patterns assignment (Table 3/4)
Outputs:
    e7_case_sheet.csv   12 sampled (university, trajectory) + pattern + rater A/B + kappa
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

try:
    import numpy as np
    import pandas as pd
    from sklearn.metrics import cohen_kappa_score
except ImportError:
    np = None  # type: ignore


def sample_cases(profiles_df, patterns_df, n=12):
    """Stratified sample across profile regions and size strata; return
    (university, cohort_seq) tuples ensuring both steady/exploratory/
    structural regions and small/medium/large sizes are represented."""
    raise NotImplementedError


def rater_sheet(cases, corpus_df, out_path: Path):
    """Emit a blinded sheet: per case, the dated patent evidence (titles,
    IPC, refs, forward cites, dates) WITHOUT computed A/R/E/D/T or pattern.
    Raters fill pattern + reasoning; coordinator adjudicates."""
    raise NotImplementedError


def kappa(rater_a, rater_b) -> float:
    """Cohen's kappa between the two raters' pattern assignments (J. Cohen 1960)."""
    if np is None:
        raise RuntimeError("numpy/sklearn required (conda activate lzz)")
    return float(cohen_kappa_score(rater_a, rater_b))


def main():
    ap = argparse.ArgumentParser(description="E7: case sampling + blinded rater sheet")
    ap.add_argument("--profiles", required=True)
    ap.add_argument("--T", required=True)
    ap.add_argument("--patterns", required=True)
    ap.add_argument("--corpus", default="experiments/out/e1_corpus.parquet")
    ap.add_argument("--out-dir", default="experiments/out")
    ap.add_argument("--n", type=int, default=12)
    args = ap.parse_args()
    out = Path(args.out_dir); out.mkdir(parents=True, exist_ok=True)
    print(f"[E7] skeleton: would sample {args.n} cases -> {out}/e7_case_sheet.csv")
    print("     implement sample_cases/rater_sheet/kappa.")


if __name__ == "__main__":
    sys.exit(main() or 0)
