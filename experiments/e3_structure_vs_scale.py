#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""E3 — Capability structure differs beyond output scale (Finding 1).

Tests that universities with similar patent output differ materially in their
five-dimension knowledge-capability structure, so that traditional output
indicators do not fully reveal the capability.

Steps:
 (a) Group universities into patent-volume quartiles; within each stratum,
     bootstrap-test that the five-dim profile dispersion is > 0.
 (b) Regress each dimension on log-volume + field composition + period;
     report residual variance share = info added by relations.
 (c) Correlate the 5-dim capability scores with traditional output indicators
     (patent count, grant count, forward-citation frequency, incoPat rating
     where available) -> partial correlations after volume control.
 (d) Rank universities under traditional vs capability scores; Kendall's tau.

Inputs:
    --profiles: experiments/out/e2_profiles.parquet
    --trad:     optional table of traditional indicators (count/grant/cite/incoPat)
Outputs:
    e3_scale_structure.csv   within-stratum dispersion, residual variance, partial corr, tau
    e3_residual.png          residual-variance figure
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

try:
    import numpy as np
    import pandas as pd
    from scipy import stats
except ImportError:
    np = None  # type: ignore

from experiments import utils


def within_stratum_dispersion(profiles_df, n_boot=2000):
    """(a) Volume-quartile strata; test profile dispersion != 0 by bootstrap."""
    raise NotImplementedError


def residual_variance(profiles_df):
    """(b) R^2 and residual share after log-volume/field/period regression."""
    raise NotImplementedError


def traditional_comparison(profiles_df, trad_df):
    """(c)+(d) partial correlations with count/grant/cite/incoPat + Kendall tau
    between traditional and capability rankings. Low partial corr + divergent
    rankings => output indicators do not fully reveal the capability."""
    raise NotImplementedError


def main():
    ap = argparse.ArgumentParser(description="E3: capability structure vs scale (Finding 1)")
    ap.add_argument("--profiles", required=True)
    ap.add_argument("--trad", default=None)
    ap.add_argument("--out-dir", default="experiments/out")
    args = ap.parse_args()
    out = Path(args.out_dir); out.mkdir(parents=True, exist_ok=True)
    print(f"[E3] skeleton: would read {args.profiles} -> {out}/e3_scale_structure.csv")
    print("     implement within_stratum_dispersion/residual_variance/traditional_comparison.")


if __name__ == "__main__":
    sys.exit(main() or 0)
