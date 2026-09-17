from pathlib import Path
import json, re

ROOT = Path('.')
old = ROOT/'00_GOVERNANCE/EVIDENCE_TO_CLAIM_MATRIX_v1.13.md'
text = old.read_text(encoding='utf-8')
marker = '## Material methodological evidence — TSTC v004 Application-Fit Demonstrator'
if marker not in text:
    raise SystemExit('TSTC marker missing in v1.13')
pre = text.split(marker, 1)[0]
pre = re.sub(r'^# TGCV — Evidence-to-Claim Matrix — Current v1\.13\n\n.*?\n## Matrix preservation rule', '''# TGCV — Evidence-to-Claim Matrix — Current v1.14

**Status:** GOVERNANCE CONTROL ARTIFACT — CURRENT  
**Date:** 2026-09-17  
**Predecessor:** v1.13  
**Incremental governance update:** v1.14 preserves the complete material evidentiary content and schema of v1.13. This documentation correction expands the TSTC v004 material section into an autocontained evidentiary record. No evidence is deleted, collapsed, downgraded, or reinterpreted; no claim-level status is changed.

**TSTC material-section correction:** The previously abbreviated TSTC v004 material record is expanded to cover provenance, frozen scope, execution contract, fixture-level results, baseline reconstruction, eight comparison dimensions, negative controls, cross-domain paths, trajectory checks, claim routing, interpretation limits and closure.

## Matrix preservation rule''', pre, count=1, flags=re.S)

tstc = '''## Material methodological evidence — TSTC v004 Application-Fit Demonstrator

**Case:** `TSTC — Synthetic Fixture-003 / Freeze-003`  
**Status:** `CLOSED — BOUNDED METHODOLOGICAL EVIDENCE REGISTERED`  
**Execution mode:** `TSTC_SYNTHETIC_EXECUTION_V004`  
**Fixture version:** `003`  
**Execution artifact:** `03_EXPERIMENTS/TSTC/tstc_execution_v004.py`  
**Post-execution audit:** `00_GOVERNANCE/SIP/TGCV_APPLICATION_FIT_WP2_TSTC_POST_EXECUTION_AUDIT_002.md`  
**Evidence-to-claim propagation:** `00_GOVERNANCE/SIP/TGCV_APPLICATION_FIT_WP2_TSTC_EVIDENCE_TO_CLAIM_PROPAGATION_001.md`  
**Execution source commit:** `bdb8477089b3b141ebf8231a9ad678cca9cbdce8`  
**Fixture manifest SHA-256:** `1ac8e7ca8c8a3e7afdc125a1d5021b386206205ec486664b362be0136e90bced`  
**Ruleset SHA-256:** `9a0c757ee8e166e991f60d898018a4ee424fae0e0e9c955458252ce7f56221c2`  
**Transformation-universe SHA-256:** `c6d4dfec24877318f466f7736f587557111d8524170f76b71e9596fe42868d3c`  
**Configuration SHA-256:** `ce274a9bc723989451b0ae2a5318efa92ccca86cf30c4403267a1c1123afaa84`  
**Output SHA-256:** `6afaffa091984b9b2e7823194b9170cfcdbef98f337d38d6f143f8c3e887bb38`  
**Environment:** Windows `10.0.26200`; Python `3.8.10`  
**Random seed:** `null`

### 1. Purpose and frozen scope
TSTC v004 is the executed form of the frozen **TGCV Application Fit — WP2 TSTC Minimum Demonstrator Specification 001**, using **Synthetic Fixtures Freeze-003** and **Execution Authorization Gate 003**. Its purpose is methodological application-fit: instantiate the TGCV translation representation reproducibly across heterogeneous synthetic domains while explicitly representing state/context, candidate transformations, admissibility, `T_acc`, transition, `Delta_T_acc` and bounded subsequent trajectory.

The demonstrator is not a scientific validation experiment, causal identification study, explanatory-superiority comparison, value/ROI test, industrial validation or deployment-readiness test. It covers **FX-C01 technical orchestration**, **FX-C03 agent/tool/permission**, and **FX-C05 resource/constraint**.

The frozen output contract requires explicit `fixture_id`, `fixture_version`, `connector_id`, `intervention_id`, `S0`, `C0`, `L_version`, `U_tau`, `T_acc_0`, transition, `S1`, `C1`, `T_acc_1`, `Delta_T_acc`, trajectory, baseline model, baseline representation, baseline reconstruction, comparison observations, limitations, non-claims and execution metadata.

### 2. Execution integrity and comparison contract
The result is `TSTC_EXECUTION_COMPLETE` under `TSTC_SYNTHETIC_EXECUTION_V004`, fixture version `003`, with the provenance hashes recorded above. The v004 execution corrected the earlier v003 output-contract deficiency. The post-execution audit PASS covers schema completeness, execution metadata, independent baseline reconstruction, all eight comparison dimensions, negative controls, controlled cross-domain propagation and trajectory/boundary checks.

The eight comparison dimensions are **(1)** transformation identities, **(2)** admissibility conditions, **(3)** state/context dependencies, **(4)** transition causing accessibility change, **(5)** cross-domain dependency, **(6)** trajectory consequence, **(7)** assumptions, and **(8)** information omitted. The conventional baseline is independently reconstructed; the three local comparisons are `EQUIVALENT_REPRESENTATION` within the frozen synthetic universes. This is representational agreement, not explanatory or predictive superiority.

### 3. Fixture-level results
**FX-C01 — technical orchestration.** Baseline: finite-state/orchestration rule model. Intervention: `trust_B: trusted → untrusted`. Result: `c01.deploy_B` closes; `c01.deploy_A` and `c01.restrict_security` remain admissible. `T_acc_1` changes through an explicit state/context-dependent admissibility rule and the bounded post-transition trajectory is restricted accordingly. Independent baseline reconstruction matches the feasible set.

**FX-C03 — agent/tool/permission.** Baseline: capability/access-control matrix plus workflow model. Intervention: `permission_repo: granted → denied`. Result: `c03.inspect_repo`, `c03.open_pr` and `c03.modify_repo` close; `c03.query_db` and `c03.complete_task` remain admissible. The record separates enabling condition, accessibility-space change and subsequent trajectory. Baseline reconstruction matches.

**FX-C05 — resource/constraint.** Baseline: finite constrained-resource feasibility model. Intervention: `grid_capacity: high → low`. Result: `c05.start_A` and `c05.start_B` close. The transition is represented as a bounded accessibility change without equating it with a downstream outcome. Baseline reconstruction matches.

### 4. Negative controls
`N-C01`, `N-C03` and `N-C05` all pass with empty `Delta_T_acc` and no opened, closed or changed transformations. `N-C01` changes `routing` while accessibility remains unchanged. Thus a context/state change is not automatically classified as an accessibility change; the admissibility predicate must change the feasible transformation set.

### 5. Controlled cross-domain paths
**C01 → C03:** the declared synthetic rule `security = restricted → permission_repo = denied` propagates the source condition into C03 and closes `c03.modify_repo`.  
**C03 → C05:** the C03 transition `c03.modify_repo` changes `repo` to `changed`; the declared rule propagates to `mobility_requirement_A = urgent` in C05 and closes `c05.redirect_A_to_B`.

Both are synthetic rule propagation, not empirical causal estimates or evidence of a universal mechanism.

### 6. Trajectory and representation checks
Each local record keeps transition, post-transition state/context, `T_acc_1` and bounded subsequent trajectory separate. Trajectories contain only transformations admissible under the post-transition space. The baseline independently reconstructs the same feasible transformation sets. `EQUIVALENT_REPRESENTATION` therefore means agreement under frozen synthetic rules; no explanatory, predictive, computational or downstream-performance superiority metric was executed.

### 7. Evidence-to-claim routing
**Primary: C16.** The experiment provides bounded methodological evidence that one frozen contract can be instantiated across three heterogeneous synthetic connector types while preserving distinctions among state/context, `U_tau`, admissibility/accessibility, `T_acc`, intervention, `Delta_T_acc`, trajectory, baseline reconstruction, cross-domain dependency, omitted information and non-claims.

**C02:** bounded qualification only; deterministic synthetic admissibility predicates and `T_acc` are explicitly represented, but general empirical accessibility is not validated.  
**C08:** bounded qualification only; accessibility change and bounded trajectory are represented, but no causal trajectory estimand is identified.  
**C11:** bounded qualification only; synthetic heterogeneity and two cross-domain paths are covered, but no transversal empirical validity is established.

Claim statuses remain **C02 = E0, C08 = H, C11 = H, C16 = H**. No TGCV Core primitive, relation, threshold or falsification criterion changes.

### 8. Scientific and interpretive boundaries
TSTC v004 does **not** establish scientific validity; empirical causality; a causal `Delta_T_acc → trajectory` estimand; `Delta_T_acc → Delta_V`; value creation; ROI; explanatory superiority; predictive superiority; real-world generality; industrial validation; or deployment readiness. Predicates and transformation universes are rule-defined and frozen; trajectories are generated within the demonstrator; cross-domain links are declared synthetic propagation rules. Negative controls validate only the frozen implementation logic, not external-world accessibility predicates.

### 9. Reproducibility and closure
The provenance fields and hashes identify the exact execution inputs, ruleset, transformation universe, configuration and output. The post-execution audit closes the execution as conformant, and the propagation record closes registration as **`CLOSED — BOUNDED METHODOLOGICAL CONTRIBUTION`**. This is closed methodological/application-fit evidence and **not authorization to reopen or repeat TSTC**.

### 10. Canonical governance effect
This v1.14 change corrects documentation completeness only. The v1.13 cumulative evidence is preserved, the TSTC material record is made autocontained, and no experiment is rerun. Canonical claim statuses, TGCV Core and RMA remain unchanged.
'''
new = pre.rstrip() + '\n\n' + tstc
(ROOT/'00_GOVERNANCE/EVIDENCE_TO_CLAIM_MATRIX_v1.14.md').write_text(new, encoding='utf-8')
(ROOT/'00_GOVERNANCE/EVIDENCE_TO_CLAIM_MATRIX_CURRENT.md').write_text(new, encoding='utf-8')
(ROOT/'00_GOVERNANCE/EVIDENCE_TO_CLAIM_MATRIX_CURRENT_POINTER.md').write_text('''# TGCV — Evidence-to-Claim Matrix — CURRENT POINTER

**Status:** CURRENT CONTROL POINTER  
**Current matrix:** `00_GOVERNANCE/EVIDENCE_TO_CLAIM_MATRIX_CURRENT.md`  
**Current version:** v1.14  
**Versioned artifact:** `00_GOVERNANCE/EVIDENCE_TO_CLAIM_MATRIX_v1.14.md`  
**Predecessor:** v1.13  
**Established:** 2026-09-17

v1.14 expands the TSTC v004 material evidence section into an autocontained record. No claim-level status changes.
''', encoding='utf-8')
c = json.loads((ROOT/'00_GOVERNANCE/CANONICAL_STATE.json').read_text(encoding='utf-8'))
c['current_versions']['claim_matrix'] = 'v1.14'
(ROOT/'00_GOVERNANCE/CANONICAL_STATE.json').write_text(json.dumps(c, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')
s = (ROOT/'STATUS.md').read_text(encoding='utf-8')
s = s.replace('Evidence→Claim Matrix `v1.13`', 'Evidence→Claim Matrix `v1.14`')
s += '\n\n## TSTC material-record correction\n- v1.14 expands the TSTC v004 material evidence section into an autocontained evidentiary record.\n- Underlying TSTC execution unchanged; no rerun.\n- Claim statuses, TGCV Core and RMA unchanged.\n'
(ROOT/'STATUS.md').write_text(s, encoding='utf-8')
