#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""E1 — Build the multi-relation patent knowledge-association structure.

Produces: 124-Double-First-Class roster, deduplicated invention units with
fractional attribution, three relation layers (IPC co-occurrence Eq 2,
semantic TF-IDF cosine, directed citation), 3-year cohorts, and the coverage
audit (Table 1, Figure 3).

Inputs (per refine-logs/DATA_REQUIREMENTS.md):
    --data-dir: directory with patents / citations / entities tables (Parquet/CSV)
    --roster:    124 Double-First-Class university list (name + standard id)
Outputs (experiments/out/):
    e1_corpus.parquet   patent-level table: patent_id, pub_year, cohort, ipc_maingroups,
                        title/abstract, backward_refs, forward_refs, applicants,
                        family_id, omega per university
    e1_layers.npz       adjacency of 3 layers (or separate graph files)
    table1.csv          coverage audit values filling Table 1

Success: primary-key/time logic traceable; main fields available at first
publication; enough 5-year-mature cohorts for trajectory analysis.
Failure: if citation coverage or mature-cohort count too low → STOP; report
infeasible rather than approximate.
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


def build_roster(roster_path: Path) -> "pd.DataFrame":
    """124 Double-First-Class universities; resolve historical names, mergers,
    affiliated hospitals through time-specific linkage. Ambiguous matches stay
    auditable, never silently assigned. Returns (standard_id, name, valid_from, valid_to)."""
    if pd is None:
        raise RuntimeError("pandas required (conda activate lzz)")
    raise NotImplementedError("Load roster; implement name/merger/hospital crosswalk.")


def collect_invention_patents(patents_df, roster_df):
    """Published Chinese invention applications with >=1 university applicant at
    first publication (1990-2019), regardless of grant status. Exclude utility
    models and designs. Collapse publication+grant versions. Invention unit =
    simple family (earliest eligible doc) if family_id available, else dedup'd
    application. Fractional attribution omega_up = 1/m_p."""
    raise NotImplementedError("Filter to 124-DFC invention patents; dedup; attribute.")


def build_technology_layer(corpus_df, cohort):
    """IPC main-group co-occurrence, Eq 2:
        w_ij^(t) = sum_{p in W_t: m_p^C>=2} I{i,j in C_p} / C(m_p^C, 2), i<j
    Each multi-coded invention contributes one unit of pair mass."""
    raise NotImplementedError("Compute fractional co-occurrence over IPC main groups.")


def build_semantic_layer(corpus_df, historical_ref_df):
    """Cosine similarity of char 2-4-gram TF-IDF vectors of normalized titles+
    abstracts; vocab and IDF fitted on B_t only (features in [5, 80%] of ref
    docs, capped 100k; log TF, smoothed IDF, L2). Mutual 15-NN graph for display."""
    raise NotImplementedError("Fit TF-IDF on B_t; compute cosine; build semantic graph.")


def build_citation_layer(corpus_df, citations_df):
    """Directed edges cited->citing; duplicate family pairs collapsed;
    within-family links removed; citing pub strictly later; applicant-overlap
    self-citations excluded from primary reuse/diffusion graph."""
    raise NotImplementedError("Construct directed citation graph with self-cite exclusion.")


def coverage_audit(corpus_df, layers, cohorts) -> "pd.DataFrame":
    """Fill Table 1: DB/provider, retrieval dates, 124-DFC roster size, raw vs
    eligible inventions, IPC vocab sizes, usable title/abstract %, backward-link
    resolution, forward-link count within H, external citing orgs, excluded
    units by reason. No value is an estimate — all audited from frozen source."""
    raise NotImplementedError("Populate Table 1 rows from corpus statistics.")


def main():
    ap = argparse.ArgumentParser(description="E1: build corpus + 3 relation layers + coverage audit")
    ap.add_argument("--data-dir", required=True)
    ap.add_argument("--roster", required=True, help="124 DFC university list")
    ap.add_argument("--out-dir", default="experiments/out")
    ap.add_argument("--cohort-len", type=int, default=3)
    ap.add_argument("--h", type=int, default=5, help="follow-up horizon (years)")
    args = ap.parse_args()

    out = Path(args.out_dir); out.mkdir(parents=True, exist_ok=True)
    roster = build_roster(Path(args.roster))
    # patents = load tables from args.data_dir (schema-flexible, see utils.resolve_column)
    # corpus  = collect_invention_patents(patents, roster)
    # cohorts = utils.build_cohorts(corpus["pub_date"], args.cohort_len)
    # tech, sem, cit = build_technology_layer(...), build_semantic_layer(...), build_citation_layer(...)
    # coverage = coverage_audit(corpus, (tech, sem, cit), cohorts)
    print(f"[E1] skeleton: would write {out}/e1_corpus.parquet, e1_layers.npz, table1.csv")
    print("     implement build_roster/collect/build_*/coverage_audit once data schema is fixed.")


if __name__ == "__main__":
    sys.exit(main() or 0)
