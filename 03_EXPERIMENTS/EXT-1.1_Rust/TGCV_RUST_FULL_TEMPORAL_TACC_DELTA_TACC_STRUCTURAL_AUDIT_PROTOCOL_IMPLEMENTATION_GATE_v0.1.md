# TGCV — Rust Full Temporal T_acc / ΔT_acc Structural Audit Protocol & Implementation Gate v0.1

**Status:** PASS — FULL OUTCOME-BLIND STRUCTURAL AUDIT PROTOCOL FROZEN FOR IMPLEMENTATION

## 1. Purpose

This gate freezes the protocol required to move from the successful fixed-candidate accessibility shadow audit to a complete structural reconstruction of:

`U_τ → P_τ(t0), P_τ(t1) → T_acc,t0, T_acc,t1 → ΔT_acc`

The audit is strictly outcome-blind. It is not a predictive, causal, value, or confirmatory outcome test.

## 2. Locked scientific architecture

The following architecture is inherited without modification:

- `Core_ontological = S`
- `T_acc,t = {τ ∈ U_τ | P_τ(S_t,C_t,L)=1}`
- `ΔT_acc(t0,t1) = T_acc,t1 ≄ T_acc,t0`
- `ΔT_acc → ΔReach → ΔTrajectory → Outcome → Value`
- `I` is explanatory and is not a Core primitive.

The Rust implementation is a domain instantiation of the analytical layer and does not establish universal validity.

## 3. Evidence boundary

The protocol is based on the accepted shadow result:

- 516,061 successive focal-version pairs inspected;
- 39,238,220 fixed candidates tested;
- 1,475,648 accessibility changes `1→0`;
- 827,361 accessibility changes `0→1`;
- 2,303,009 total declaration-driven fixed-candidate accessibility changes;
- target-release availability was not used as the temporal change driver;
- candidate identity excluded the declaration;
- no execution, outcome, value, future activity, or model was used.

The shadow result is structural evidence for proceeding; it is not itself the full `T_acc/ΔT_acc` audit.

## 4. Final candidate universe contract

### 4.1 Candidate identity

The canonical candidate identity is:

`τ_id = (origin_version_id, target_package_id, target_version_id)`.

The dependency declaration string is **not** part of candidate identity.

### 4.2 Universe independence

The candidate universe must be constructed independently of declaration membership and independently of the temporal comparison outcome.

For each focal origin version `e_o`, the implementation must maintain a stable candidate identity universe sufficient to evaluate present accessibility at both comparison times.

The universe must not be defined as:

`{τ | created_at(target) <= t}`

when that definition would make target-release availability itself the driver of `ΔT_acc`.

### 4.3 Shadow isolation versus final reconstruction

The shadow audit used target versions existing by the initial comparison time to isolate declaration-driven switching. The full audit must preserve this causal-isolation property while explicitly documenting the universe boundary and any candidates excluded because their identity cannot be established independently of the comparison.

Excluded candidates must be classified, not silently treated as inaccessible.

## 5. Temporal pairing

The frozen primary temporal pair is:

- focal unit: package-version;
- `t0 = created_at(e_o)`;
- `t1 = created_at(next release of the same focal package)`;
- terminal focal versions are not paired;
- no outcome-optimized pairing;
- no 180-day window;
- no future activity criterion.

The same focal identity must be used at both times.

## 6. Present-state accessibility predicate

For a candidate `τ=(e_o,p_d,v_d)` at time `t`:

`P_τ(e_o,t)=1` iff all frozen conditions hold:

1. focal package-version is canonical and valid;
2. candidate transformation identity is canonical and valid;
3. a focal dependency declaration for the target package exists at `t`;
4. the declaration is supported by frozen R* v0.2;
5. target version is canonical and supported by R* v0.2;
6. target version existed by the relevant frozen present-time boundary;
7. target version satisfies the declaration under R* v0.2;
8. no frozen historical exclusion applies.

The predicate must not use:

- resolver-selected target version;
- actual dependency execution;
- later focal release information except the pre-frozen `t1` pairing boundary;
- subsequent activity;
- outcome;
- model predictions/features;
- value.

## 7. R* v0.2 coverage rule

R* v0.2 remains frozen.

Unsupported requirement strings and unsupported target version strings must be represented explicitly as `UNSUPPORTED`, excluded from resolved accessibility membership, and counted in the audit.

They must **not** be recoded as `P_τ=0` merely because the grammar cannot parse them.

A future expansion of R* requires a separate ex-ante grammar gate and a new semantic version.

## 8. Construction of T_acc

The primary representation is membership-level:

`T_acc,t = {(e_o, τ_id) | P_τ(e_o,t)=1}`.

Cardinality is secondary and diagnostic only.

For each paired focal origin:

- construct `T_acc,t0`;
- construct `T_acc,t1`;
- preserve unresolved and unsupported counts separately;
- do not infer inaccessible membership from unresolved status.

An empty `T_acc,t` is a valid structural state.

## 9. Construction of ΔT_acc

For each focal pair:

`Add = T_acc,t1 \ T_acc,t0`

`Rem = T_acc,t0 \ T_acc,t1`

Classification:

- **PERSISTENCE:** `Add=∅` and `Rem=∅`;
- **EXPANSION:** `Add≠∅` and `Rem=∅`;
- **CONTRACTION:** `Add=∅` and `Rem≠∅`;
- **RECONFIGURATION/SUBSTITUTION:** `Add≠∅` and `Rem≠∅`.

The classification is based on membership changes, not on cardinality alone.

## 10. Critical interpretation rule

A change in declaration may produce several candidate-level membership changes. These must be aggregated into `T_acc` before `ΔT_acc` is classified.

Therefore:

`candidate accessibility changes ≠ ΔT_acc classification`.

The latter is a property of the complete accessible transformation membership relation for the focal unit.

## 11. Structural audit outputs

The implementation must report at minimum:

### Dataset integrity

- package count;
- version count;
- dependency rows scanned;
- malformed rows;
- duplicate rows;
- temporal ordering violations.

### Universe

- candidate universe count;
- candidate identity uniqueness;
- universe exclusions and reasons;
- unsupported target versions;
- unsupported requirements.

### Accessibility

- resolved accessibility evaluations;
- unresolved evaluations;
- unsupported evaluations;
- `P_τ(t0)=1` count;
- `P_τ(t1)=1` count;
- `1→0` count;
- `0→1` count;
- persistent accessible count;
- persistent inaccessible count.

### T_acc / ΔT_acc

- paired origins;
- terminal origins;
- empty T_acc at t0;
- empty T_acc at t1;
- T_acc membership counts;
- Add membership count;
- Rem membership count;
- persistence pairs;
- expansion pairs;
- contraction pairs;
- reconfiguration/substitution pairs;
- unchanged pairs;
- changed pairs.

### Integrity / leakage

Explicit Boolean checks must confirm:

- declaration not in candidate identity;
- universe membership not driven by declaration;
- target-release availability not used as the temporal change driver;
- execution not used;
- outcome not used;
- value not used;
- future activity not used;
- old EXT-1.1 resolver not used;
- old EXT-1.1 outcome/window/model not used;
- R* v0.2 unchanged;
- deterministic canonicalization;
- row-order invariance;
- provenance completeness.

## 12. Canonicalization and reproducibility

The implementation must produce deterministic canonical representations for:

1. candidate universe;
2. `T_acc,t0`;
3. `T_acc,t1`;
4. `Add`;
5. `Rem`;
6. pair classifications;
7. final audit report.

Canonical ordering must be independent of input row order.

At minimum, canonical SHA-256 hashes must be emitted for the principal structural artifacts.

## 13. Empty, unsupported and unresolved cases

These states are analytically distinct:

- **EMPTY:** no resolved accessible transformations exist for the focal unit/time;
- **UNSUPPORTED:** required grammar is outside frozen R* v0.2;
- **UNRESOLVED:** candidate identity or required source metadata cannot be established;
- **INACCESSIBLE:** candidate identity and semantics are resolved, but `P_τ=0`.

No category may be silently converted into another.

## 14. Required pre-confirmatory checks

Before accepting the full structural audit, implementation must verify:

- candidate identity uniqueness;
- fixed-universe consistency;
- no target-release monotonicity artifact;
- non-circular predicate evaluation;
- declaration-driven switches remain possible under the full aggregation;
- `T_acc,t0` and `T_acc,t1` are reconstructable;
- `ΔT_acc` is reconstructable from membership differences;
- empty/unsupported/unresolved cases are preserved;
- deterministic replay produces identical canonical hashes.

## 15. Falsifiers

The full construction must be rejected or returned for redesign if any of the following is established:

**FT-1:** candidate identity is contaminated by declaration content.

**FT-2:** universe membership is determined by accessibility or declaration membership.

**FT-3:** temporal differences are again driven by target-release appearance rather than present accessibility.

**FT-4:** `P_τ` is circular or depends on execution/outcome/value.

**FT-5:** complete `T_acc` cannot be reconstructed deterministically.

**FT-6:** `ΔT_acc` cannot be determined from canonical membership differences.

**FT-7:** unsupported/unresolved cases are silently classified as inaccessible.

**FT-8:** the construction collapses back into the previous monotonic temporal artifact.

**FT-9:** the result depends on row ordering or non-deterministic canonicalization.

**FT-10:** provenance cannot establish which frozen semantics generated the result.

## 16. Gate criteria

| Criterion | Decision |
|---|---|
| FT-G1 fixed candidate identity | PASS — frozen |
| FT-G2 declaration-independent identity | PASS — frozen |
| FT-G3 declaration-independent universe | PASS — frozen |
| FT-G4 target availability not temporal change driver | PASS — frozen |
| FT-G5 present-state accessibility predicate | PASS — frozen |
| FT-G6 R* v0.2 frozen | PASS |
| FT-G7 explicit unsupported/unresolved handling | PASS |
| FT-G8 membership-level T_acc | PASS |
| FT-G9 canonical ΔT_acc operator | PASS |
| FT-G10 empty-set handling | PASS |
| FT-G11 deterministic canonicalization | PASS |
| FT-G12 leakage firewall | PASS |
| FT-G13 implementation executed | NOT YET |
| FT-G14 full T_acc reconstruction accepted | NOT YET |
| FT-G15 full ΔT_acc reconstruction accepted | NOT YET |
| FT-G16 downstream Reach/Trajectory | OUT OF SCOPE |
| FT-G17 outcome/model/value | OUT OF SCOPE |

## 17. Gate decision

**PASS — FULL OUTCOME-BLIND STRUCTURAL AUDIT PROTOCOL FROZEN FOR IMPLEMENTATION.**

The next implementation may now reconstruct the complete paired temporal `T_acc` membership relations and their `ΔT_acc` differences under the frozen semantics.

The implementation result itself must receive a separate human-review/acceptance decision before any downstream outcome or predictive layer is introduced.

## 18. Integrity lock

- Core `S` unchanged.
- `T_acc` remains derived analytical object.
- `ΔT_acc` remains primary differentiated candidate.
- `I` remains explanatory.
- SLR-1 remains closed.
- TR-130–TR-140 remain closed.
- EXT-1.1 predictive result remains excluded.
- R* v0.2 remains frozen.
- No outcome/model/value execution is authorized.
- No post-hoc semantic redesign is authorized.

## 19. Next controlled operation

**TGCV Rust Full Temporal T_acc / ΔT_acc Structural Audit v0.1 — implementation and outcome-blind execution.**

Only after that execution has been reviewed and accepted may a separate gate authorize any outcome/model/value layer.
