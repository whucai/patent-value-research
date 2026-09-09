#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""E2 — Compute the five capability dimensions per university-period.

A (knowledge sourcing, Eq 3), R (recombination, Eq 4-5), E (technological
exploration, Eq 6), D (knowledge diffusion, Eq 7) per eligible university-period;
T (dynamic transformation, Eq 8) per consecutive transition. Plus descriptive
stats (Table 2) and pairwise correlations + residual variance after
log-volume/field/period adjustment (Figure 4A).

Inputs:
    --corpus: experiments/out/e1_corpus.parquet (+ layers from E1)
Outputs:
    e2_profiles.parquet   one row per (university, cohort): A,R,E,D + components
    e2_T.parquet          one row per (university, transition): T, null_thresh, sustained
    table2.csv            distribution of the five dimensions (fills Table 2)
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
    pd = None  # type: ignore

from experiments import utils


def acquisition(df_ut, subclass_vocab) -> float:
    """A_ut = q_ut * [1/2 + 1/2 * (-sum_k pi log pi)/log K_t]   (Eq 3)
    q_ut = attributed share with >=1 resolved external backward reference;
    pi_ut,k = fractional distribution of those refs over version-harmonized IPC
    subclass vocab of size K_t. A=0 when no external sourcing; positive baseline
    distinguishes narrow sourcing from none. Measures source reach+diversity,
    NOT absorptive capacity."""
    raise NotImplementedError


def recombination(df_ut, historical_pair_mass) -> float:
    """R_ut = mean_p omega * mean_(i,j in L_p) r_ij,t   (Eq 5)
    r_ij,t = -log p^-_ij,t / -log(alpha/(C_t+alpha Q_t)), alpha=1/2  (Eq 4)
    p^-_ij,t = (c^-_ij,t + alpha)/(C_t + alpha Q_t), historical fractional pair mass in B_t.
    Unresolved codes -> one OOV category; no valid pair -> missing, not zero."""
    raise NotImplementedError


def exploration(df_ut, historical_index) -> float:
    """E_ut = mean_p omega * n_p,t * g_p,t   (Eq 6)
    n_p,t = 1 - max_q in B_t s_pq  (semantic novelty over historical index, excl. same-family)
    g_k,t = max(0, (rho_k,t - rho^-_k,t)/(rho_k,t + rho^-_k,t + 1e-12))  (field growth vs ref)
    g_p,t averages over the patent's subclasses. Novelty+growth must coincide
    in the same invention -> exploration of novel directions. Early-information
    measure, available at publication. E_rec (secondary) multiplies by 1yr-ext-cite indicator."""
    raise NotImplementedError


def diffusion(df_ut, forward_cites) -> float:
    """D_ut = 1/(2 M_ut^D) * sum_p omega * [phi_b(b_p) + phi_v(v_p)]   (Eq 7)
    b_p = distinct external citing orgs (or families); v_p = 1 - Delta_p/H (first
    external citation after Delta_p years; 0 if uncited). Each component midrank-
    normalized among positives in same primary subclass/cohort (phi(0)=0; back-off
    to section then cohort below 30 positives). Measures documented knowledge
    diffusion among observed citers; NOT economy-wide diffusion."""
    raise NotImplementedError


def transformation(dist_t, dist_t1) -> float:
    """T_{u,t->t+1} = [JSD(a_ut,a_{u,t+1}) + JSD(r_ut,r_{u,t+1})] / (2 log 2) in [0,1]  (Eq 8)
    a_ut, r_ut = normalized subclass and pair distributions on shared vocabularies.
    Event requires T > 95th pct of within-university null (E5). Sustained event
    additionally: 3rd period closer to new composition, still distinguishable from old.
    Audits mergers + IPC revisions before retaining. Measures portfolio reorganization,
    NOT paradigm shift; diversity is distinct."""
    raise NotImplementedError


def descriptive_table(profiles_df) -> "pd.DataFrame":
    """Table 2: per-dimension valid n, mean, SD, median, IQR, zero %. Component
    summaries, missing counts, coverage shares accompany each row."""
    raise NotImplementedError


def residual_variance(profiles_df):
    """Regress A,R,E,D on log-volume + field composition + period; report R^2
    and residual variance share = evidence that relational profiles add info
    beyond size and field (feeds 'Scale versus structure')."""
    raise NotImplementedError


def main():
    ap = argparse.ArgumentParser(description="E2: compute A,R,E,D,T (Eq 3-8)")
    ap.add_argument("--corpus", required=True)
    ap.add_argument("--layers", default="experiments/out/e1_layers.npz")
    ap.add_argument("--out-dir", default="experiments/out")
    ap.add_argument("--min-inventions", type=int, default=20)
    ap.add_argument("--min-mass-frac", type=float, default=0.8)
    args = ap.parse_args()

    out = Path(args.out_dir); out.mkdir(parents=True, exist_ok=True)
    print(f"[E2] skeleton: would read {args.corpus} and write "
          f"{out}/e2_profiles.parquet, e2_T.parquet, table2.csv")
    print("     implement acquisition/recombination/exploration/diffusion/transformation.")


if __name__ == "__main__":
    sys.exit(main() or 0)
