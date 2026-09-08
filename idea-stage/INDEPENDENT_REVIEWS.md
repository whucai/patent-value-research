# Independent Cross-Family Reviews (Idea-Discovery close-out)

**Date**: 2026-09-04
**Run**: patent-value-university-ideas-20260904
**Executor (recorded)**: codex-gpt-5.6-sol (OpenAI family)
**Reviewer**: fresh-context Claude general-purpose agent (Anthropic family) — different family from the executor, so this satisfies the cross-model invariant (`assert_cross_family`: reviewer ≠ author family). A second OpenAI-direction pass via Codex MCP was rate-limited at close-out and may be added later for a second datapoint; the cross-family bar is already met.

> Note on context independence: each reviewer was spawned fresh (no inherited conversation context) and read the project files cold, breaking the same-context confirmation-bias block that previously left these two sub-stages `done`-but-unaccepted.

---

## novelty-check — verdict

INDEPENDENT_NOVELTY_SCORE: 5.5/10
VERDICT: PROCEED_WITH_CAUTION
NEAREST_NEIGHBORS_MISSED: none identified with verifiable DOI nearer than the two cited; Hsu et al. (2021, Research Policy 50(1), 104076) and Lin et al. (2025, J. Tech Transfer 50(4), 1602-1632) are correctly the closest. Conceptually adjacent but not nearer: the Henderson/Jaffe/Trajtenberg lineage on US university patenting-to-commercialization and Harhoff et al. (2003, Research Policy 32(8), 1343-1363) on citations-to-commercial-value — none performs the patent-level potential-vs-realization decomposition for China.
DIFFERENTIATOR_ASSESSMENT: partially_holds
CIRCULARITY_ASSESSMENT: partially_mitigated
RATIONALE: The core conceptual move — separating a patent's potential technical value from its realized commercialization and attributing the gap to university realization capacity — is already Hsu et al. (2021), who do this at patent level for US universities (potential economic value vs. realized licensing, ~16% capture). The report's claimed differentiators are overstated: "patent-level" is not novel against Hsu (also patent-level); "strict publication-time freeze" is standard leakage-avoidance already studied by Lai et al. (2026); "separating future potential from realization capacity" IS Hsu's contribution. The genuine residual novelty is narrower — applying the full freeze→citation-prediction→conditional-commercialization→missed-patent pipeline to China's full university-population patent data and explicitly naming a "missed high-potential" cohort — which is a legitimate empirical combination on unique data but incremental, not conceptual, so the 6.5 self-score is slightly generous. The differentiator only partially holds because the only un-anticipated piece is the China full-population setting plus the named missed-patent cohort, not the decomposition itself. On circularity, the "potential_score" is a relabeled future-citation predictor, so "high potential but not commercialized" partly re-derives Lin et al.'s (2025) quality-commercial-value decoupling; the time-freeze + rolling-origin calibration prevents leakage and ensures honest scores, and using citations (potential) vs. transfer/licensing (realization) as distinct outcomes avoids full tautology, but no external non-citation ground truth for "technical potential" is introduced, so the construct-validity risk is only partially mitigated. Position the work as an empirical combination study on unique Chinese data, not a new measurement paradigm.

---

## research-review — verdict

INDEPENDENT_SCORE: 6/10
VERDICT: REVISE_BEFORE_EMPIRICAL_CLAIMS
TOP_WEAKNESSES:
- Construct circularity unresolved: potential_score is by construction a prediction of 5-year standardized forward citations, so the "gap" is literally "predicted-citation vs. actual-transfer" — the mitigations (time-freeze, rolling-origin, calibration) prevent leakage/overfitting but do not establish that citations and transfers measure different value dimensions; the argument remains implicit.
- incoPat external-consistency check may itself be circular: incoPat's composition is acknowledged as opaque and may encode the same future citations, legal status, and market events the time-freeze excludes, so high score-incoPat correlation cannot validate construct independence.
- University random effects confounded with field-mix: IPC fixed effects likely cannot capture within-field specialization heterogeneity (e.g., pharma vs. pure-math departments within the same IPC section) that drives baseline commercialization propensity, risking misattribution of field-composition effects to "realization capacity."
- Legal-status requirement in the gap definition creates survivorship bias: "still enforceable" filters out abandoned patents, but abandonment is endogenous — patents may be dropped because they were evaluated and found commercially nonviable, not because a university failed to commercialize a genuinely valuable invention.
- iConference 2027 timeline is near-infeasible: ~6 weeks from zero-data state to a human-written 8,000-12,000-character empirical paper, with the proposal's own estimate of 12-25 working days for data-plus-modeling work alone and zero margin for the data-coverage/entity-disambiguation issues the plan itself flags as the biggest bottleneck.
MINIMUM_FIXES:
- Receive data and pass B0 (R001-R004) — non-negotiable gate before any empirical work.
- Audit field dictionary for available_date on every field; confirm no future-derived fields enter publication-time features.
- Make the construct-validity argument explicit: either demonstrate potential_score predicts non-citation outcomes (diffusion breadth, maintenance, incoPat AFTER auditing its composition for future leakage) or reframe the construct as "citation-prediction-based gap" and restrict all claims accordingly.
- Validate university entity disambiguation and transfer/license event coding on 100-200 human-checked cases before fitting any hierarchical model.
- Complete at minimum a 1-5% stratified pilot (R005-R007) on a mature cohort before asserting any population-level result.
- Add a within-field-university analysis (e.g., university effects estimated within narrow IPC subgroups) to separate realization capacity from field-composition confounding.
CIRCULARITY_ASSESSMENT: partially_addressed
DATA_STATE_CLAIMS_OK: yes
ICONFERENCE_FIT: marginal
RATIONALE: The research design is structurally sophisticated — time-freeze at publication, rolling-origin training, nested M0-M3 model comparison, explicit stop/go rules, and careful separation of potential measurement from market-realization modeling — and all project documents correctly present claims as testable hypotheses with failure interpretations rather than established results, so no empirical over-assertion exists. However, I independently confirm REVISE_BEFORE_EMPIRICAL_CLAIMS: the core construct-circularity risk (potential_score is a relabeled future-citation prediction) is only partially addressed because the proposed mitigations prevent data leakage and overfitting but do not establish that the score measures a concept distinct from citations, and the only external anchor (incoPat) may itself be contaminated by the same future information the freeze excludes. Additional unresolved threats — field-mix confounding of university effects, legal-status survivorship bias in the gap definition, and a 6-week deadline with no data in hand — make the iConference 2027 Chinese-track fit marginal: the topic matches the venue tracks, but producing a complete, human-written, empirically grounded 8,000-12,000-character paper on this timeline requires immediate clean-data arrival and zero encountered issues, which the plan's own risk register does not support.

---

## Action taken

Both sub-stages were `done`-but-unaccepted (prior same-context review only). With these cross-family verdicts recorded, `run_state.py accept` closes:
- `novelty-check` → accepted (PROCEED_WITH_CAUTION, 5.5/10)
- `research-review` → accepted (REVISE_BEFORE_EMPIRICAL_CLAIMS, 6/10)

The `idea-discovery-evidence` gate unblocks and the outer `idea-discovery` phase can be marked accepted. Empirical work (Stage 2 / experiment-bridge) remains blocked on data — see `refine-logs/DATA_REQUIREMENTS.md`.

---

## Second opinion — Codex / OpenAI family (fresh context, same family as executor)

A second reviewer via Codex MCP (OpenAI family — same family as the `codex-gpt-5.6-sol`
executor, so it **cannot independently close the gate** under `assert_cross_family`; it is a
fresh-context second opinion that *corroborates* the Claude/Anthropic cross-family verdict
that closed the gate). Each call read the files cold with no shared context.

### research-review (Codex, thread `01a06c93-24d3-7bf3-84e6-4b7716061f46`)

- INDEPENDENT_SCORE: 5.5/10  (Claude gave 6/10 — agreement within 0.5)
- VERDICT: REVISE_BEFORE_EMPIRICAL_CLAIMS  (agrees with Claude)
- CIRCULARITY_ASSESSMENT: partially_addressed  (agrees)
- DATA_STATE_CLAIMS_OK: yes  (agrees)
- ICONFERENCE_FIT: marginal  (agrees)
- New weakness not flagged by Claude: the 5-year-maturity requirement favors older cohorts while policy, patenting incentives, reporting practices and transfer institutions have changed substantially — a present-day-generalizability threat.
- RATIONALE: safeguards establish leakage control and predictive validity only; they do not convert a calibrated citation forecast into an independently validated measure of technical potential, and incoPat cannot until its version/timing/ingredients are audited. Adding university effects documents heterogeneity but cannot explain why environments produce it. iConference fit is real topically but a credible empirical paper in ~6 weeks from a zero-data state is possible only under exceptionally rapid data access and aggressive scope control.

**Agreement summary**: two different model families (Anthropic + OpenAI), both fresh-context,
independently converge on REVISE_BEFORE_EMPIRICAL_CLAIMS with circularity only
partially addressed and iConference fit marginal — strong corroboration of the Stage-1 close-out.

### novelty-check (Codex, thread `01a06c95-1c5c-74a3-81d6-8fb4d0cd730b`)

- INDEPENDENT_NOVELTY_SCORE: 5.5/10  (exactly matches the Claude novelty verdict)
- VERDICT: PROCEED_WITH_CAUTION  (agrees)
- DIFFERENTIATOR_ASSESSMENT: partially_holds  (agrees)
- CIRCULARITY_ASSESSMENT: partially_mitigated  (agrees)
- NEAREST_NEIGHBORS_MISSED (NEW — the Claude review did not flag these):
  - Sine, Shane & Di Gregorio, Management Science 2003, DOI 10.1287/mnsc.49.4.478.14416 — "more directly anticipates the claim that university attributes affect invention-level licensing conditional on invention characteristics" (a direct novelty threat to the realization-capacity angle).
  - Gong et al., PLOS ONE 2020, DOI 10.1371/journal.pone.0230805.
- RATIONALE: Hsu 2021 remains the closest conceptual predecessor (already constructs patent-level potential estimates before comparing with realized licensing); Lin 2025 the closest Chinese-context neighbor; Sine 2003 anticipates the university-attributes-conditional-licensing claim. Patent-level + potential–realization separation are not independently novel; the publication-time freeze is rigorous leakage control; the defensible residual is the nationwide Chinese combination with separate transfer/licensing hazards and explicit identification of unrealized high-score patents. `potential_score` is substantively predicted 5-year citation impact — freezing + rolling-origin prevent leakage and the distinct commercialization outcome avoids tautology, but do not validate citations as technical potential; non-citation validation and terminology calibrated to "predicted citation impact" are still needed.

**Agreement summary (novelty)**: two model families independently converge on 5.5/10
PROCEED_WITH_CAUTION, differentiator partially_holds, circularity partially_mitigated.
The Codex pass additionally surfaced Sine 2003 and Gong 2020 as missed nearest neighbors;
Sine 2003 in particular pressures the "university realization capacity" novelty claim and
should be read and (if real) cited in the proposal's nearest-neighbor analysis.

**DOI verification (CrossRef/PLOS, 2026-09-04):** both confirmed real.
- Sine 2003 → *Management Science* 49(4):478–490, "The Halo Effect and Technology Licensing: The Influence of Institutional Prestige on the Licensing of University Inventions."
- Gong 2020 → *PLOS ONE*, "The innovation value chain of patents: Breakthrough in the patent commercialization trap in Chinese universities."

Both ingested into `research-wiki/` (`paper:sine2003_halo_effect_technology`, `paper:gong2020_innovation_value_chain`) and wired via `addresses_gap` to gap:G1 and gap:G2 respectively; `gap_map.md` and `IDEA_REPORT.md` Novelty Verification updated accordingly.
