# TGCV — C09 Charlotte-Mecklenburg School Choice TR-132 Operational Preflight 001

**Status:** `COMPLETED — PRE-FLIGHT BLOCKED / EXECUTION NOT ADMITTED`
**Date:** 2026-09-13
**Candidate:** Charlotte-Mecklenburg School Choice Lottery
**Parent:** `TGCV_C09_RETROSPECTIVE_TR132_CANDIDATE_REVIEW_001.md`
**Execution authorization:** `NONE`

## 1. Candidate definition

Charlotte-Mecklenburg introduced district-wide open enrollment in 2002. Oversubscribed non-neighborhood schools used priority groups and lottery numbers to determine admission. The historical research identifies randomized applicants whose first-choice admission was determined by lottery; the underlying study used district administrative data and linked outcome records. citeturn0search9turn0search1

The evidence base is a genuine randomized design, including a randomized subset in the historical school-choice data. citeturn0search23turn0search26

## 2. Proposed bounded C09 representation

`U* = school-enrollment transformations from a student's pre-lottery school state to the parent's declared first-choice school during the frozen 2002–2003 lottery assignment window.`

`P0(τ) = first-choice enrollment transformation is not available under the student's control/priority state.`

`P1(τ) = first-choice enrollment transformation is admitted by the randomized lottery within the student's priority group.`

Intervention: randomized admission offer. The causal treatment is the accessibility change created by lottery-based admission, not realized attendance itself.

## 3. Operational gates

### P1 — Randomized intervention

**PASS.**

Lottery numbers within relevant priority groups determined admission to oversubscribed schools. The historical evidence explicitly identifies lottery-determined randomized groups. citeturn0search9turn0search23

### P2 — Decision-time unit and baseline state

**PASS — DESIGN LEVEL.**

The source data include student choices, lottery numbers, assignments, demographics and prior academic achievement; the research design uses information available before the lottery. citeturn0search25turn0search9

### P3 — Accessibility intervention

**PASS — CONCEPTUAL / BOUNDED.**

The intervention directly changes admission accessibility to a specific declared school transformation: a lottery winner can be offered the first-choice school where a comparable lottery loser cannot. This is a clean bounded accessibility mechanism.

### P4 — Unit-level `T_acc,0/T_acc,1`

**CONDITIONAL PASS — DATA PROVENANCE BLOCKER.**

The historical data are sufficiently rich in principle to identify the student's choices, lottery number and assignment, and the study's randomized subset. citeturn0search25turn0search23

However, the cited research infrastructure is district administrative data supplied to researchers, not an established unrestricted public-use unit-level package. The public research articles and replication materials do not establish that a complete per-student `T_acc,0/T_acc,1` representation for the frozen `U*` can be reconstructed without the underlying administrative records.

### P5 — Independent trajectory endpoint

**PASS — SCIENTIFICALLY / CONDITIONAL OPERATIONALLY.**

Longitudinal endpoints are unusually strong: the literature includes test scores, disciplinary outcomes, arrests and postsecondary enrollment/degree completion. citeturn0search2turn0search1turn0search26

The endpoint can therefore be fixed independently of the accessibility rule, but unit-level reproducibility still depends on access to the underlying linked administrative records.

### P6 — Public reproducibility

**FAIL — CURRENT C09 PACKAGE.**

The strongest evidence states that the school district provided researchers with student choices, lottery numbers, assignments and achievement data, while later work uses rich administrative data on peers, teachers, course offerings and other inputs. citeturn0search25turn0search2

The existence of article replication materials does not establish unrestricted access to the underlying randomized student-level accessibility and longitudinal administrative records required for TGCV reconstruction.

### P7 — TR-132 omitted-path sufficiency

**NOT ADMITTED.**

The bounded accessibility mechanism is conceptually strong, and the randomized design substantially reduces causal-identification concerns. But the operational sufficiency proof cannot be certified without an admissible unit-level data package demonstrating `T_acc,0/T_acc,1` and the independent endpoint together.

No inference from lottery number or admission offer alone to the full transformation space is permitted.

## 4. Decision

**CHARLOTTE-MECKLENBURG SCHOOL CHOICE = PRE-FLIGHT BLOCKED / EXECUTION NOT ADMITTED.**

This candidate is a strong methodological reference: it provides a particularly clear randomized admission-access intervention and rich longitudinal outcomes. citeturn0search2turn0search9

Nevertheless, current public materials do not establish the unrestricted unit-level data provenance required for a reproducible TGCV C09 execution. The candidate therefore remains outside execution.

No restricted-data request.
No substitution of lottery assignment, realized attendance or published effects for `T_acc`.
No causal execution.
No matrix upgrade.
No Core change.
No execution authorization.

## 5. Candidate disposition

Retain as a **strong methodological reference / conditional C09 candidate**. Reopening requires an admissible dataset package satisfying the TR-132 unit-level accessibility and endpoint requirements.

**Next operation:** controlled review of the remaining retrospective candidate set and determination of whether any candidate can pass the public-reproducibility gate without restricted-data dependence.
