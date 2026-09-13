# TGCV — C09 Santiago Fare-Free RCT Data Provenance Audit 001

**Status:** `COMPLETED — PUBLIC UNIT-LEVEL REPRODUCIBILITY NOT ESTABLISHED / CANDIDATE NOT ADMITTED`
**Date:** 2026-09-13
**Candidate:** Santiago fare-free public transport RCT (Bull, Muñoz & Silva)
**Execution authorization:** `NONE`

## 1. Scope

Audit only whether the published Santiago RCT provides an admissible public package from which the randomized unit, bounded transit transformation universe, `T_acc,0/T_acc,1`, and independent trajectory endpoint can be reconstructed.

The study randomized 106 workers to a two-week unlimited fare-free transit pass and 101 controls. The experiment was individual-level and used baseline and treatment-period travel information. citeturn0search0turn0search6

## 2. Provenance findings

### A. Randomization / unit

**PASS — DOCUMENTED.**

Individual-level randomization and sample sizes are explicitly reported. Baseline information included home address, household income, household size, gender and age. citeturn0search0turn0search6

### B. Bounded intervention rule

**PASS — DOCUMENTED.**

The treatment pass allowed unlimited fare-free travel on subway and buses for two weeks, while controls did not receive the pass. The intervention therefore supplies a concrete rule-level accessibility contrast for a bounded transit-use domain. citeturn0search0turn0search1

### C. Unit-level accessibility representation

**FAIL — NOT PUBLICLY ESTABLISHED.**

The published evidence demonstrates the randomized treatment and travel outcomes, but does not establish an openly reproducible participant-level representation of all relevant transit transformations under treatment and control. In particular, the paper's accessibility analysis uses proximity to subway stations, while the observed travel outcomes are survey/travel-diary measures rather than a released transformation-space dataset. citeturn0search0turn0search2

Proximity to a station cannot by itself be promoted to `T_acc`, and observed trips cannot be substituted for pre-outcome accessibility.

### D. Independent trajectory endpoint

**CONDITIONAL PASS.**

Detailed travel behavior during the experiment is observed and can serve as a bounded immediate trajectory endpoint. However, public evidence located for this audit does not establish a downloadable unit-level raw dataset containing the randomized assignment and all underlying individual travel records needed for independent reconstruction.

### E. Public reproducibility

**FAIL / NOT ESTABLISHED.**

The sources located establish the article, working paper and institutional publication records, but do not establish an unrestricted public replication package containing the randomized participant-level assignment plus the underlying individual travel records. citeturn0search0turn0search5turn0search7

## 3. TR-132 assessment

TR-132 cannot be passed operationally because the required unit-level `T_acc,0/T_acc,1` representation is not demonstrated as reconstructible from an admissible public package.

The candidate therefore fails the same critical operational condition that closed the previous retrospective lottery pool, despite having a cleaner conceptual accessibility intervention.

## 4. Decision

**SANTIAGO FARE-FREE RCT = NOT ADMITTED FOR C09 EXECUTION.**

Disposition: **strong conceptual/methodological reference, public-reproducibility blocker.**

No treatment-assignment proxy for `T_acc`.
No realized-trip proxy for `T_acc`.
No inference from station proximity to full transformation accessibility.
No restricted-data request.
No causal execution.
No matrix upgrade.
No Core change.
No execution authorization.

## 5. Search implication

This audit confirms that the new-domain criterion is useful but that the Santiago RCT does not yet satisfy its public-reproducibility requirement. The next discovery should therefore prioritize datasets where the intervention itself is encoded in an openly reconstructible operational rule or state transition, rather than relying on participant-level travel diaries whose raw records are not demonstrably public.
