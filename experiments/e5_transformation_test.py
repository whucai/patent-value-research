#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""E5 — Dynamic-transformation mechanism (T-event counts + proposition test).

(a) Within-university null for T (Eq 8): pool the two adjacent cohorts, permute
    their period labels preserving cohort sizes, take the 95th percentile as
    threshold; confirm under size-matched subsampling. Audit mergers + IPC
    revisions before retaining any event.
(b) Test the proposition "sustained exploration/recombination precedes
    transformation": compare observed frequency of 'high-R/E followed by
    sustained T' with its frequency under within-university order permutations
    preserving each university's profile values. Nonpositive or unstable
    contrast -> proposition unsupported.

Inputs:
    --profiles: experiments/out/e2_profiles.parquet
    --T:        experiments/out/e2_T.parquet
    --dist:     per-university subclass+pair distributions per cohort (from E1/E2)
Outputs:
    e5_T_events.csv   per-transition: T, null_95, is_event, is_sustained, audit_flag
    e5_proposition.csv observed vs permuted contrast + interval
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

from experiments import utils


def transformation_null(dist_t, dist_t1, n_perm=1000, seed=0):
    """(a) Pool adjacent cohorts, permute period labels preserving sizes; 95th
    pct of permuted T is the threshold. Confirm with size-matched subsampling."""
    raise NotImplementedError


def audit_events(events_df, merger_log=None, ipc_revision_log=None):
    """Remove events explainable by mergers or IPC revisions before retention."""
    raise NotImplementedError


def proposition_test(profiles_df, T_events_df, n_perm=1000):
    """(b) 'high-R/E then sustained-T' frequency: observed vs within-university
    order permutations preserving profile values. Effect + bootstrap interval;
    nonpositive/unstable -> unsupported."""
    raise NotImplementedError


def main():
    ap = argparse.ArgumentParser(description="E5: T permutation null + proposition test")
    ap.add_argument("--profiles", required=True)
    ap.add_argument("--T", required=True)
    ap.add_argument("--dist", default="experiments/out/e2_distributions.parquet")
    ap.add_argument("--out-dir", default="experiments/out")
    args = ap.parse_args()
    out = Path(args.out_dir); out.mkdir(parents=True, exist_ok=True)
    print(f"[E5] skeleton: would read {args.profiles},{args.T} -> "
          f"{out}/e5_T_events.csv, e5_proposition.csv")
    print("     implement transformation_null/audit_events/proposition_test.")


if __name__ == "__main__":
    sys.exit(main() or 0)
