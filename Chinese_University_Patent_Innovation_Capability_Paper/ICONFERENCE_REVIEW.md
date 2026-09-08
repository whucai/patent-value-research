# iConference-style review notes (internal)

Date: 2026-09-08  
Artifact: `main_body.tex` (+ abstract in `title_abstract.tex`)  
Scope: narrative / contribution / data feasibility; experiments ignored as uncomputed.

---

## Mock review (iConference / information science)

**Recommendation:** Major Revision / borderline Reject as currently framed  
**Confidence:** High on narrative; Medium-High on data-feasibility (depends on exact citation graph scope)

### Summary
The manuscript proposes a multi-layer patent-knowledge framework for Chinese universities: four contemporaneous process dimensions (acquisition, recombination, recognized emergence, diffusion), independent structural transformation, GMM states, transition matrices, and four interpretive trajectory paths. The writing is careful about construct boundaries and temporal leakage. However, as an iConference paper the contribution is over-instrumented and under-focused: the reader cannot tell whether the paper is (a) a measurement framework, (b) a typology of university knowledge trajectories, or (c) a predictive/validation study. With no results yet, the draft reads as a full analysis protocol rather than a conference paper with one clear story.

### Strengths
1. Temporal accountability is unusually explicit (publication clock, mature windows, no future leakage into early indicators).
2. Refusal to collapse IPC / text / citations into one adjacency matrix is conceptually sound for information science.
3. Separating transformation \(T\) from the contemporaneous profile \((A,R,E,D)\) avoids a circular “state explains change that defined the state” design.
4. Honest scoping language (university-only diffusion ≠ economy-wide; recognized emergence ≠ full emergence construct).

### Weaknesses (main)
1. **Main line is unclear.** Three RQs already equal three papers. Four dimensions + \(T\) + GMM states + four named paths create vocabulary collision; readers will treat paths as GMM clusters despite disclaimers.
2. **Methods are a preregistration, not a conference Method section.** Eligibility rules, bootstrap protocols, BIC degrees of freedom, FDR, PPML, blinded 24-case design, etc. bury the contribution.
3. **Contribution claim is defensive rather than assertive.** Repeated “not X” statements (not absorptive capacity, not paradigm shift, not causal, not introducing patents into mapping) leave little positive claim for an iSchool audience.
4. **Venue fit risk.** Dense combinatorial-innovation + GMM + Markov package fits scientometrics / JOI / Scientometrics better than a short iConference research paper unless drastically cut and reframed around knowledge organization / representation.
5. **Several planned analyses exceed typical “Chinese university patents + citations” graphs** (esp. two-step diffusion depth; economy-wide citing orgs; family-clean invention units; dated merger roster). See data section below.

### Questions for authors
1. After one reading, what single sentence should a reviewer remember as the paper’s contribution?
2. Are Maintenance / Expansion / Recombination / Transformation *findings to discover* or *labels to impose*? If the latter, why GMM?
3. With university-only citation coverage, what diffusion claim remains scientifically interesting?
4. How many mature three-year cohorts exist once \(H=5\) and historical reference \(B_t\) are enforced?

### What would move toward Accept
- One spine: complementary patent relations → temporally valid university-period profiles → interpretable longitudinal patterns.
- Cut or demote: predictive PPML horse-race, second-order Markov, full robustness table farm, governance section.
- Pre-commit to what the data *can* support (academic technological reuse among observed citers), and redesign \(D\) / \(E\) accordingly.
- Replace four path names with empirically grounded profile language until results exist.
