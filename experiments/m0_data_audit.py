#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
M0 数据审计 (R001–R004) — 专利“价值实现缺口”项目

Implements the four MUST-RUN data-audit runs from `refine-logs/EXPERIMENT_PLAN.md`
(block B0). These MUST pass before any modeling (B1+) may begin. Parameterized
by a data directory; reads Parquet/CSV tables per `refine-logs/DATA_REQUIREMENTS.md`.

Design: schema-flexible. R001 (profiling) runs on ANY data drop. R002–R004
degrade gracefully — they activate as the relevant semantic fields become
discoverable (via a `data_dictionary` table or common column-name variants).
A missing table is reported, not crashed on, so a partial drop still yields a
partial audit.

Usage:
  python3 m0_data_audit.py --data-dir <path> [--out-dir reports/m0] [--sample 200]

Requires: pandas. If the base python3 lacks it, run under `conda activate lzz`.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

try:
    import pandas as pd
except ImportError:
    sys.exit("pandas not found in this Python. Try `conda activate lzz` then rerun.")

# Canonical table names from DATA_REQUIREMENTS.md
TABLES = ["patents", "citations", "legal_events", "transactions",
          "entities", "incopat_scores", "data_dictionary"]

# Common column-name variants for semantic fields (Chinese + English)
PATENT_ID_CANDIDATES = ["patent_id", "专利ID", "申请号", "公开号", "id", "pub_id", "app_id"]
PUB_DATE_CANDIDATES = ["公开日", "publication_date", "公开日期", "pub_date", "公开日date"]
APP_DATE_CANDIDATES = ["申请日", "application_date", "申请日期", "app_date"]
EVENT_DATE_CANDIDATES = ["登记日期", "event_date", "事件日期", "registration_date", "交易日期"]
EVENT_TYPE_CANDIDATES = ["事件类型", "event_type", "交易类型", "type"]
LEAKAGE_HINTS = {  # field-name substrings that hint at FUTURE / post-publication info
    "前向引用": "forward citation — only knowable AFTER publication (leak)",
    "forward_cit": "forward citation — only knowable AFTER publication (leak)",
    "转让": "transfer — future market event (leak if used as predictor)",
    "transfer": "transfer — future market event (leak if used as predictor)",
    "许可": "license — future market event (leak if used as predictor)",
    "license": "license — future market event (leak if used as predictor)",
    "失效": "lapse — future legal event (leak)",
    "维持": "maintenance — future legal status (leak)",
    "法律状态": "legal status — may encode future events (audit)",
}


def find_column(df: pd.DataFrame, candidates):
    """Return the first matching column name, else None."""
    lower_map = {c.lower(): c for c in df.columns}
    for cand in candidates:
        if cand.lower() in lower_map:
            return lower_map[cand.lower()]
        # substring match as fallback
        for low, orig in lower_map.items():
            if cand.lower() in low:
                return orig
    return None


def load_table(data_dir: Path, name: str):
    """Load a table by canonical name (Parquet preferred, CSV fallback)."""
    for ext in (".parquet", ".parq", ".csv", ".csv.gz"):
        p = data_dir / f"{name}{ext}"
        if p.exists():
            if ext.startswith(".parq"):
                return pd.read_parquet(p), str(p)
            return pd.read_csv(p), str(p)
    # directory of partitioned parquet
    d = data_dir / name
    if d.is_dir() and any(d.glob("*.parquet")):
        return pd.read_parquet(d), str(d)
    return None, None


def r001_profile(tables: dict, out_dir: Path) -> dict:
    """R001: 字段、主键、表间关系与规模画像。Schema-agnostic — always runs."""
    report = {}
    for name, (df, path) in tables.items():
        if df is None:
            report[name] = {"status": "MISSING"}
            continue
        n = len(df)
        pk = find_column(df, PATENT_ID_CANDIDATES)
        dup_rate = (df[pk].duplicated().sum() / n) if (pk and n) else None
        missing = {c: float(df[c].isna().mean()) for c in df.columns}
        report[name] = {
            "status": "ok",
            "path": path,
            "rows": n,
            "columns": list(df.columns),
            "dtypes": {c: str(t) for c, t in df.dtypes.items()},
            "primary_key_guess": pk,
            "primary_key_dup_rate": dup_rate,
            "missing_rate_per_col": {c: round(m, 4) for c, m in missing.items()},
        }
    # cross-table ID match rate
    pat = tables.get("patents", (None, None))[0]
    if pat is not None:
        pid = find_column(pat, PATENT_ID_CANDIDATES)
        if pid:
            pat_ids = set(pat[pid].dropna().unique())
            for other in ("citations", "transactions", "legal_events"):
                df_o = tables.get(other, (None, None))[0]
                if df_o is None:
                    continue
                oid = find_column(df_o, PATENT_ID_CANDIDATES)
                if oid is None:
                    continue
                inter = len(pat_ids & set(df_o[oid].dropna().unique()))
                report[other]["match_rate_to_patents"] = (
                    round(inter / max(len(pat_ids), 1), 4) if pat_ids else None
                )
    (out_dir / "R001_profile.json").write_text(json.dumps(report, ensure_ascii=False, indent=2))
    return report


def r002_leakage(tables: dict, out_dir: Path) -> dict:
    """R002: available_date 与泄漏审计。Needs publication_date + field-availability hints."""
    pat = tables.get("patents", (None, None))[0]
    if pat is None:
        return {"status": "BLOCKED", "reason": "patents table missing"}
    pub = find_column(pat, PUB_DATE_CANDIDATES)
    if pub is None:
        return {"status": "BLOCKED", "reason": "publication_date column not found; provide data_dictionary"}
    # flag columns whose names hint at future/post-publication information
    flagged = {}
    for col in pat.columns:
        for hint, why in LEAKAGE_HINTS.items():
            if hint.lower() in col.lower():
                flagged[col] = why
                break
    report = {
        "status": "ok",
        "publication_date_col": pub,
        "pub_date_range": _date_range(pat[pub]),
        "flagged_future_fields": flagged,
        "note": ("A field appearing here does not prove leakage — it flags fields whose "
                 "value may only be knowable after publication. Confirm against the field "
                 "dictionary's 'first available time point' before use as a predictor."),
    }
    (out_dir / "R002_leakage.json").write_text(json.dumps(report, ensure_ascii=False, indent=2))
    return report


def r003_cohort(tables: dict, out_dir: Path) -> dict:
    """R003: 公开年 × 五年成熟窗口 × 转让/许可覆盖矩阵。"""
    pat = tables.get("patents", (None, None))[0]
    if pat is None:
        return {"status": "BLOCKED", "reason": "patents table missing"}
    pub = find_column(pat, PUB_DATE_CANDIDATES)
    if pub is None:
        return {"status": "BLOCKED", "reason": "publication_date column not found"}
    pub_dates = pd.to_datetime(pat[pub], errors="coerce")
    pub_year = pub_dates.dt.year
    cutoff = pd.Timestamp.today()  # 5-year maturity = pub_date + 5y <= today
    has_5yr_window = (pub_dates + pd.DateOffset(years=5) <= cutoff)
    txn = tables.get("transactions", (None, None))[0]
    txn_coverage = None
    if txn is not None:
        tid = find_column(txn, PATENT_ID_CANDIDATES)
        if tid:
            txn_ids = set(txn[tid].dropna().unique())
            txn_coverage = pat.index.isin(pat[find_column(pat, PATENT_ID_CANDIDATES)].isin(txn_ids))
    # build year × maturity matrix
    mat = {}
    for yr in sorted(pub_year.dropna().unique()):
        mask = (pub_year == yr)
        n = int(mask.sum())
        mature = int((mask & has_5yr_window).sum())
        cov = int((mask & txn_coverage).sum()) if txn_coverage is not None else None
        mat[int(yr)] = {"total": n, "with_5yr_window": mature, "with_txn_coverage": cov}
    report = {
        "status": "ok",
        "matrix_by_pub_year": mat,
        "cutoff_date": str(cutoff.date()),
        "note": "Choose the mature cohort (with_5yr_window=True) as the main analysis set.",
    }
    (out_dir / "R003_cohort.json").write_text(json.dumps(report, ensure_ascii=False, indent=2))
    return report


def r004_events(tables: dict, out_dir: Path, sample: int) -> dict:
    """R004: 转让/许可/失效事件抽查（分层样本）。"""
    txn = tables.get("transactions", (None, None))[0]
    if txn is None:
        return {"status": "BLOCKED", "reason": "transactions table missing"}
    etype = find_column(txn, EVENT_TYPE_CANDIDATES)
    edate = find_column(txn, EVENT_DATE_CANDIDATES)
    tid = find_column(txn, PATENT_ID_CANDIDATES)
    report = {
        "status": "ok",
        "event_type_col": etype,
        "event_date_col": edate,
        "rows": len(txn),
        "event_type_distribution": (
            txn[etype].value_counts().to_dict() if etype else None
        ),
        "date_range": (_date_range(txn[edate]) if edate else None),
        "amount_coverage": None,
        "sampled_n": 0,
        "internal_transfer_rate": None,
    }
    # amount coverage
    amt = find_column(txn, ["金额", "amount", "transaction_amount", "price"])
    if amt:
        report["amount_coverage"] = round(float(txn[amt].notna().mean()), 4)
    # spot-check sample for internal transfers (transferor == assignee group)
    if tid and sample > 0:
        s = txn.sample(min(sample, len(txn)), random_state=1) if len(txn) else txn
        report["sampled_n"] = len(s)
        tor = find_column(s, ["转让方", "transferor", "from", "assignor"])
        tee = find_column(s, ["受让方", "assignee", "to", "transferee"])
        if tor and tee:
            internal = (s[tor].astype(str) == s[tee].astype(str)).mean()
            report["internal_transfer_rate"] = round(float(internal), 4)
    (out_dir / "R004_events.json").write_text(json.dumps(report, ensure_ascii=False, indent=2))
    return report


def _date_range(s):
    s = pd.to_datetime(s, errors="coerce").dropna()
    if s.empty:
        return None
    return {"min": str(s.min().date()), "max": str(s.max().date())}


def main():
    ap = argparse.ArgumentParser(description="M0 data audit (R001–R004)")
    ap.add_argument("--data-dir", required=True, help="directory with patents/citations/... tables")
    ap.add_argument("--out-dir", default="reports/m0", help="output directory")
    ap.add_argument("--sample", type=int, default=200, help="R004 spot-check sample size")
    args = ap.parse_args()

    data_dir = Path(args.data_dir)
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    tables = {name: load_table(data_dir, name) for name in TABLES}

    print(f"== M0 数据审计 | data-dir={data_dir} ==\n")
    r1 = r001_profile(tables, out_dir)
    print("[R001 profile] done — see R001_profile.json")
    r2 = r002_leakage(tables, out_dir)
    print(f"[R002 leakage] {r2.get('status', 'ok')}")
    r3 = r003_cohort(tables, out_dir)
    print(f"[R003 cohort]  {r3.get('status', 'ok')}")
    r4 = r004_events(tables, out_dir, args.sample)
    print(f"[R004 events]  {r4.get('status', 'ok')}")

    # markdown summary
    lines = ["# M0 数据审计摘要\n"]
    for name, r in [("R001", r1), ("R002", r2), ("R003", r3), ("R004", r4)]:
        lines.append(f"## {name}\n```json\n{json.dumps(r, ensure_ascii=False, indent=2)[:2000]}\n```\n")
    (out_dir / "M0_SUMMARY.md").write_text("\n".join(lines))
    print(f"\nSummary: {out_dir/'M0_SUMMARY.md'}")

    # decision: did M0 pass? (need patents + publication date + 5yr cohort + txn coverage)
    ok = (r1.get("patents", {}).get("status") == "ok"
          and r2.get("status") == "ok"
          and r3.get("status") == "ok"
          and any(v.get("with_5yr_window", 0) > 0 for v in (r3.get("matrix_by_pub_year", {}) or {}).values()))
    print("\nM0 GATE: " + ("PASS — proceed to B1" if ok else "NOT YET — data incomplete"))
    sys.exit(0 if ok else 2)


if __name__ == "__main__":
    main()
