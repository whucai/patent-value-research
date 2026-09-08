# Stage 2 Handoff — Experiment Bridge

**Date**: 2026-09-04
**Outer run**: patent-value-university-20260904
**Resume point**: `experiment-bridge` (idea-discovery ✅ accepted)
**Status**: BLOCKED on data intake — no empirical work can run yet.

## Why Stage 2 is blocked

`refine-logs/EXPERIMENT_TRACKER.md` lists runs R001–R004 (milestone M0, block B0) as
`BLOCKED — 待提供数据`. R005–R026 are `TODO`, gated on M0. The project directory contains
**no raw patent tables, no field dictionary, and no prior experimental results**
(`REFINE_STATE.json` phase = `data_intake`; `PIPELINE_SUMMARY.md` Next Action = provide
field dictionary + table samples). The B0 stop/go rule is explicit: *"B0 不通过：停止建模，
修复数据或改做标签审计"* — so no modeling may begin until the data audit passes.

Additional block on the full `/experiment-bridge` skill: `CODE_REVIEW=true` (default)
routes experiment code through GPT-5.6-Sol xhigh review, and the Codex MCP backend was
rate-limited at close-out (usage limit, resets ~21:19 local). Re-run when Codex is available.

## What is already prepared

- `experiments/m0_data_audit.py` — schema-flexible M0 audit (R001–R004). R001 (profiling)
  runs on any data drop; R002–R004 activate as the relevant fields/dictionary are discovered.
  Verified: on an empty data dir it reports `R001 done / R002–R004 BLOCKED / M0 GATE: NOT YET`
  and exits cleanly (no crash). Requires `pandas` (present in base `python3`; also in the
  `lzz` conda env).

  ```
  python3 experiments/m0_data_audit.py --data-dir <path-to-tables> --out-dir experiments/reports/m0
  ```

## What the user must provide to unblock Stage 2

Per `refine-logs/DATA_REQUIREMENTS.md`, the minimum for a first audit round:

1. **Field dictionary** (`data_dictionary`) — per field: table, name, type, meaning, missing
   code, source, **first-available time point**, and whether it can be computed from future events.
2. **Sample rows** — 100–1,000 rows per table (`patents`, `citations`, `legal_events`,
   `transactions`, `entities`, `incopat_scores`).
3. **Scale** — per-table row counts, earliest/latest dates, file paths.
4. **ID match rate** — `patents` ↔ `transactions` ID match.
5. **University coverage** — whether the data covers all Chinese universities, and the
   university-identification rule.

Preferred format: Parquet (CSV/UTF-8 acceptable). Dates as `YYYY-MM-DD` (no fake `01` for
unknown days). Stable patent ID across tables.

## Once data is provided

1. Run `python3 experiments/m0_data_audit.py --data-dir <path>` — confirm `M0 GATE: PASS`.
2. Re-resume the pipeline: `/research-pipeline — resume patent-value-university-20260904`.
   The outer run's `experiment-bridge` phase re-enters; `/experiment-bridge` then implements
   B1+ (R005–R026) per `refine-logs/EXPERIMENT_PLAN.md`, routes by job count (≤5 →
   `/run-experiment`, ≥10 → `/experiment-queue`), and runs the Codex code review.

## What will NOT be done without data (and must not be claimed)

No `EXPERIMENT_RESULTS.md`, no `NARRATIVE_REPORT.md`, no Stage 3 (auto-review-loop), no
empirical claims. Per the independent research-review verdict
(`idea-stage/INDEPENDENT_REVIEWS.md`): REVISE_BEFORE_EMPIRICAL_CLAIMS — the design is sound
and no claims are over-asserted, but B0 + a 1–5% pilot must pass first.
