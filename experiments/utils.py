#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Shared helpers for the capability-measurement experiments.

Import-safe: numpy/pandas are imported lazily so the module loads on a plain
python3; calling a helper requires the scientific stack (``conda activate lzz``).

All equations and notation follow
``Chinese_University_Patent_Innovation_Capability_Paper/main_body.tex``.
"""
from __future__ import annotations

from typing import Iterable

try:
    import numpy as np
    import pandas as pd
except ImportError:  # pragma: no cover
    np = None  # type: ignore
    pd = None  # type: ignore


# --- column-name variants (Chinese + English) --------------------------------
PATENT_ID = ["patent_id", "专利ID", "申请号", "公开号", "id", "pub_id", "app_id"]
PUB_DATE = ["公开日", "publication_date", "公开日期", "pub_date"]
APPLICANT = ["申请人", "applicant", "申请人原文"]
IPC = ["IPC", "ipc", "分类号", "ipc_maingroup", "主组"]
TITLE = ["标题", "title", "title_zh"]
ABSTRACT = ["摘要", "abstract", "abstract_zh"]
CITED_ID = ["被引专利ID", "cited_id", "cited_patent_id"]
CITING_ID = ["引用专利ID", "citing_id", "citing_patent_id"]
FAMILY_ID = ["同族ID", "family_id", "docdb_family_id"]


def _require() -> None:
    if np is None or pd is None:
        raise RuntimeError(
            "numpy/pandas not available in this Python. Run `conda activate lzz` "
            "then retry."
        )


def resolve_column(df, candidates: Iterable[str]):
    """Return the first column present in df among candidates, else None."""
    for c in candidates:
        if c in df.columns:
            return c
    return None


def omega_up(m_p: int) -> float:
    """Fractional attribution weight: a patent with m_p university applicants
    contributes 1/m_p to each (Section 'Data and observable relations')."""
    return 1.0 / m_p if m_p and m_p > 0 else 0.0


def build_cohorts(pub_dates, cohort_len: int = 3, hist_ref: int = 3):
    """Build non-overlapping first-publication cohorts W_t = [b_t, b_t+1) and
    historical references B_t = [b_t-3, b_t). Returns a list of dicts:
        {"W_t": (start, end), "B_t": (start, end), "index_end": b_t}
    Mature cohorts require b_{t+1} + H <= d_extract (caller enforces H).
    """
    _require()
    years = pd.to_datetime(pub_dates).dt.year.dropna().astype(int)
    if years.empty:
        return []
    start = int(years.min())
    end = int(years.max())
    out = []
    b = start
    while b + cohort_len <= end + 1:
        out.append({
            "W_t": (b, b + cohort_len),
            "B_t": (b - hist_ref, b),
            "index_end": b,
        })
        b += cohort_len
    return out


def harmonize_ipc_subclass_vocab(*cohorts_subclasses):
    """Version-harmonized IPC subclass vocabulary of size K_t across cohorts.
    Placeholder: union of distinct subclasses seen in any cohort. The real
    harmonization must reconcile IPC revisions (audit before T events)."""
    _require()
    vocab = set()
    for sub in cohorts_subclasses:
        vocab |= set(sub.dropna().unique().tolist())
    return sorted(vocab)


def midrank_normalize(values, positives, backoff_section=None, cohort_pool=None):
    """Phi(): transform each value to its midrank among positive values in the
    same primary subclass and cohort (phi(0)=0); back off to IPC section and
    then cohort below 30 positives (Eq 7, knowledge-diffusion measure)."""
    _require()
    pos = np.asarray([v for v in positives if v and v > 0], dtype=float)
    if len(pos) < 30 and backoff_section is not None and cohort_pool is not None:
        pos = np.asarray([v for v in cohort_pool if v and v > 0], dtype=float)
    if len(pos) == 0:
        return 0.0
    order = np.argsort(pos)
    ranks = np.empty_like(order, dtype=float)
    ranks[order] = np.arange(1, len(pos) + 1)
    midranks = (ranks + 1) / (2 * (len(pos) + 1))
    v = float(values)
    if not v or v <= 0:
        return 0.0
    idx = np.searchsorted(np.sort(pos), v)
    idx = min(idx, len(midranks) - 1)
    return float(midranks[idx])


def jsd(p, q) -> float:
    """Jensen--Shannon divergence in [0,1] over base-2 logs (Lin, 1991; Eq 8).
    p, q are normalized distributions over a shared vocabulary."""
    _require()
    p = np.asarray(p, dtype=float)
    q = np.asarray(q, dtype=float)
    p = p / p.sum() if p.sum() else p
    q = q / q.sum() if q.sum() else q
    m = 0.5 * (p + q)
    def _kl(a, b):
        mask = a > 0
        return float(np.sum(a[mask] * np.log2(a[mask] / np.where(b[mask] == 0, 1, b[mask]))))
    return 0.5 * _kl(p, m) + 0.5 * _kl(q, m)


def bootstrap_interval(values, n_boot: int = 2000, stat=np.mean, alpha=0.05):
    """Whole-university bootstrap interval (Efron, 1979)."""
    _require()
    arr = np.asarray([v for v in values if v == v], dtype=float)  # drop NaN
    if arr.size == 0:
        return (float("nan"), float("nan"))
    boots = stat(np.random.choice(arr, size=(n_boot, arr.size), replace=True), axis=1)
    return float(np.quantile(boots, alpha / 2)), float(np.quantile(boots, 1 - alpha / 2))


def eligible_subset(df, min_inventions: int = 20, min_mass_frac: float = 0.8):
    """A university-period enters profile analysis with >=20 attributed
    inventions and >=80% usable attributed mass for each dimension's fields
    (Section 'Observation time'). Returns (P_ut, M_ut)."""
    _require()
    if len(df) < min_inventions:
        return None, 0.0
    mass = df["omega"].sum() if "omega" in df else float(len(df))
    return df, float(mass)
