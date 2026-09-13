# TGCV — C09 EFA Operational Preflight 001

**Status:** `COMPLETED — PRE-FLIGHT BLOCKED / EXECUTION NOT ADMITTED`
**Date:** 2026-09-13
**Candidate:** Emergency Financial Assistance randomized trial at a Texas community college
**Execution authorization:** `NONE`

## 1. Scope

Determine whether the public OpenICPSR replication package is sufficient to operationalize the EFA intervention as a bounded accessibility change `T_acc,0 → T_acc,1` at unit level, under TR-132, without substituting treatment, take-up or outcomes for accessibility.

The OpenICPSR package is public and contains replication syntax, a README and project materials. The public project description confirms that the study evaluates access to emergency financial assistance within a randomized controlled trial. citeturn0search0turn2search8

## 2. Preflight results

### P1 — Randomized assignment

**PASS.**

The study is explicitly an RCT evaluating access to EFA. citeturn2search0turn2search8

### P2 — Ex-ante bounded intervention rule

**CONDITIONAL / NOT FROZEN.**

The scientific description identifies emergency expenses such as medical, legal and car-repair shocks, but the public package listing does not expose a sufficiently explicit intervention rule defining the complete bounded transformation class, eligibility conditions, timing and amount at unit level. citeturn2search8

The replication package contains cleaning and variable-generation syntax, but the currently accessible public index does not establish that the underlying raw unit-level intervention/eligibility records needed for TGCV reconstruction are themselves publicly reproducible. citeturn0search0turn0search1

### P3 — `T_acc,0/T_acc,1` reconstruction

**FAIL — OPERATIONAL IDENTIFIABILITY.**

Randomized assignment can identify the causal treatment contrast, but it cannot by itself be used as `T_acc`.

Likewise, EFA receipt, amount received, or observed educational outcomes cannot be substituted for accessibility. The public package listing does not establish a reconstructible unit-level representation of the pre-treatment financial-shock transformation universe and its accessibility predicates.

### P4 — Independent trajectory endpoint

**PASS — DESIGN LEVEL.**

Educational progression/completion is downstream of the intervention and is distinct from the accessibility rule. The study explicitly evaluates educational outcomes. citeturn2search0

### P5 — Public reproducibility

**FAIL FOR C09 OPERATIONALIZATION.**

The replication package is publicly indexed and contains code/readme materials, but public availability of replication syntax is not equivalent to public availability of the unit-level data required to reconstruct `T_acc,0/T_acc,1`. The package index lists syntax and documentation rather than demonstrating a public raw accessibility dataset. citeturn0search0turn2search11

### P6 — TR-132 sufficiency

**FAIL / NOT ADMITTED.**

Because `U*` and the corresponding ex-ante accessibility predicates cannot be frozen and reconstructed at unit level from the admissible public package, the omitted-path sufficiency condition cannot be established operationally.

## 3. Decision

**EFA = PRE-FLIGHT BLOCKED / EXECUTION NOT ADMITTED.**

This candidate is closed for current C09 execution screening. It remains a useful methodological reference because its intervention is conceptually much closer to a direct accessibility change than CHESS, but conceptual fit is insufficient without operational identifiability.

No treatment-as-T_acc substitution.
No take-up-as-T_acc substitution.
No outcome-as-T_acc substitution.
No restricted-data request.
No model fitting.
No causal execution.
No matrix upgrade.
No Core change.
No execution authorization.

## 4. Search implication

The next search should prioritize **public individual-level datasets in which the intervention rule itself is encoded as a pre-treatment eligibility/permission/access variable**, not merely a randomized assignment and downstream outcomes.

This excludes candidates where the accessibility rule exists only in institutional records, even when a replication package provides analysis syntax.

**Next operation:** targeted discovery of public rule/eligibility/access interventions with explicit unit-level intervention predicates.
