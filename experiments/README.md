# Experiment suite — University patent innovation capability

Implements the measurement-and-analysis pipeline for the paper *Measuring
University Patent Technological Innovation Capability from Patent Knowledge
Association Structures* (`Chinese_University_Patent_Innovation_Capability_Paper/main_body.tex`).
Each step maps to a paper artifact (table/figure/finding). Outputs land in
`experiments/out/` and feed the LaTeX `[Pending]`/`\TBD` slots.

Data schema follows `refine-logs/DATA_REQUIREMENTS.md` (Parquet preferred,
Chinese + English column-name variants accepted). The corpus is invention
patents for **124 Double-First-Class universities, 1990–2019**.

## Run order

| Step | Script | Produces | Paper artifact |
|---|---|---|---|
| E1 | `e1_build_corpus.py` | roster + corpus + 3 relation layers + coverage audit | Table 1, Figure 3 |
| E2 | `e2_compute_dimensions.py` | A,R,E,D per university-period; T per transition | Table 2, Figure 4A |
| E3 | `e3_structure_vs_scale.py` | within-stratum dispersion + residual variance + traditional-indicator comparison | "Scale versus structure" subsection |
| E4 | `e4_patterns.py` | 3-pattern assignment + GMM + Markov transitions | Table 3, Table 4 |
| E5 | `e5_transformation_test.py` | T permutation null + "exploration→transformation" proposition | T-event counts |
| E6 | `e6_robustness.py` | sensitivity sweep across unit/attribution/text/window/horizon/threshold | Table 5 |
| E7 | `e7_cases.py` | 12 sampled trajectories + blinded rater sheet | "Cases and sensitivity" |

E1 must precede E2; E2 precedes E3/E4/E5; E6 reruns E2/E4 under each setting.

## Measures (equations reference main_body.tex)

- **Knowledge sourcing** $A$ — Eq 3: backward-ref reach × Shannon diversity over IPC subclasses.
- **Recombination** $R$ — Eq 4–5: rarity of IPC main-group pairs against historical baseline $B_t$.
- **Technological exploration** $E$ — Eq 6: semantic novelty $n_{p,t}$ × field growth $g_{k,t}$.
- **Knowledge diffusion** $D$ — Eq 7: forward-citation breadth + first-uptake velocity (midrank-normalized).
- **Dynamic transformation** $T$ — Eq 8: JSD of subclass + pair distributions across periods.

Three development patterns: **steady utilization** (low T, low E, moderate–high D),
**exploratory innovation** (high E and/or high R), **structural recombination**
(sustained T above null).

## Usage

```bash
conda activate lzz          # or any env with pandas/numpy/scipy/scikit-learn
python3 -m experiments.e1_build_corpus   --data-dir <patent-db> --out-dir experiments/out
python3 -m experiments.e2_compute_dimensions --corpus experiments/out/e1_corpus.parquet
# ... E3–E7 chain from experiments/out/e2_profiles.parquet
```

## Stop / go rules

- E1 coverage audit fails (citation coverage or mature-cohort count too low) → stop; report infeasible rather than approximate.
- E2: if a university-period has <20 attributed inventions or <80% usable mass → exclude (missing, not zero).
- E4: if <3 consecutive mature cohorts → restrict pattern analysis to description; Markov test reported infeasible.
- E6: if results hinge on a single representation / threshold → report continuous indicators only, bound the interpretation.

## Dependencies

numpy, pandas, scipy, scikit-learn, networkx (layers); sentence-transformers
optional (E6 frozen Chinese-capable encoder). Heavy imports are lazy.
