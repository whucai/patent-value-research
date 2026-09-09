#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""E6 — Robustness and sensitivity (Table 5).

Reruns E2/E4 under each setting and reports the change in profile values /
pattern counts. Families:
  invention unit      application vs family; common-sample profile change
  attribution         university-fractional vs all-applicant and full counts
  text representation char TF-IDF vs frozen Chinese-capable encoder
                      (Reimers & Gurevych 2019); novelty rank agreement
  window length        non-overlapping 2/3/4-year cohorts; pattern-category agreement
  reuse horizon/scope  H=3 vs 5; self-citation exclusion; org- vs family-level b_p
  eligibility         min 10/20/30 inventions; completeness 70/80/90%
  emergence variant    E vs E_rec; nonzero shares
  transformation null  label permutation vs size-matched subsampling; event counts
If results hinge on a single representation/threshold -> report continuous
indicators and bound the interpretation; common-sample agreement reported
separately from sample retention.

Inputs:
    --corpus: experiments/out/e1_corpus.parquet (or raw data-dir to rebuild)
Outputs:
    table5.csv   per-family: common-sample n, change in profile/pattern, interval, coverage delta
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

try:
    import numpy as np
    import pandas as pd
except ImportError:
    np = None  # type: ignore


FAMILIES = {
    "invention_unit": {"application", "family"},
    "attribution": {"fractional", "all_applicant", "full"},
    "text_representation": {"char_tfidf", "frozen_encoder"},
    "window_length": {2, 3, 4},
    "reuse_horizon": {3, 5},
    "eligibility_min": {10, 20, 30},
    "eligibility_complete": {0.7, 0.8, 0.9},
    "emergence_variant": {"E", "E_rec"},
    "transformation_null": {"label_perm", "size_matched"},
}


def run_family(family: str, setting, corpus_df):
    """Rebuild the affected layer/dimension under this setting and recompute
    A,R,E,D (and patterns where relevant) on the common sample. Returns dict
    with common_n, profile_change, pattern_change, interval, coverage_delta."""
    raise NotImplementedError


def main():
    ap = argparse.ArgumentParser(description="E6: sensitivity sweep (Table 5)")
    ap.add_argument("--corpus", required=True)
    ap.add_argument("--out-dir", default="experiments/out")
    args = ap.parse_args()
    out = Path(args.out_dir); out.mkdir(parents=True, exist_ok=True)
    print(f"[E6] skeleton: would sweep {list(FAMILIES)} -> {out}/table5.csv")
    print("     implement run_family per setting.")


if __name__ == "__main__":
    sys.exit(main() or 0)
