# TGCV — VSL-EXP-01 Candidate Compatibility Audit 001

**Date:** 2026-09-19  
**Status:** CLOSED — VALUE_IDENTIFIED_READY (READINESS, NOT EXPERIMENTAL EVIDENCE)  
**Candidates:** A — Built assets/infrastructure LCC; B — Petroleum/petrochemical/natural-gas LCC  
**Protocol:** VSL-EXP-01 v0.1 FROZEN  
**Precondition:** VSL-SPEC-01 v0.1 FROZEN

## 1. Scope

This audit determines whether each retained candidate can support an independently specified and pre-execution frozen Value construct.

It does not select a candidate, rank candidates, establish observed Value, or authorize an experiment.

## 2. Candidate A — Built assets / infrastructure LCC

**Domain evidence:** ISO 15686-5:2017 provides requirements/guidance for LCC of buildings and constructed assets. It covers relevant costs/cash flows over an agreed analysis period and commonly supports comparison between alternatives or estimation of future costs. The standard is current following confirmation in 2024.

### C01–C12

| ID | Requirement | Result | Basis |
|---|---|---|---|
| C01 | Unit can be fixed | PASS | Asset/project/component can be fixed prospectively; experiment can select a single decision unit |
| C02 | Evaluative perspective can be fixed | PASS | Owner/investor/procurer perspective can be declared before execution |
| C03 | Outcome independent of Value | PASS | LCC/cash-flow trajectory is an observable/reconstructable outcome; Value can be derived separately |
| C04 | Reference can be fixed pre-result | PASS | Alternative comparison is part of the domain method; reference/alternative can be frozen before outcomes |
| C05 | Outcome → Value mapping can be pre-specified | PASS | A declared economic objective can map pre-specified LCC outcome to V* without using TGCV results |
| C06 | Directionality can be fixed | PASS | Under a cost-minimization objective, lower declared LCC can be defined as favorable before execution |
| C07 | Time horizon can be fixed | PASS | Agreed analysis period is an explicit part of ISO 15686-5 |
| C08 | Costs/benefits/trade-offs can be specified | PASS | Acquisition, operation, maintenance, replacement and disposal costs are within the LCC architecture; scope must be frozen |
| C09 | Aggregation can be specified | PASS | Single-asset/decision-unit design permits no aggregation; portfolio aggregation can instead be explicitly frozen if required |
| C10 | Uncertainty/missingness can be specified | PASS | ISO 15686-5 includes uncertainty/risk and sensitivity-analysis architecture; experiment-specific missingness rules remain to be frozen |
| C11 | Independence from TGCV variables can be preserved | PASS | Domain outcome and valuation rules can be specified without using T_acc, accessibility or TGCV transformations |
| C12 | Essential rules can be frozen pre-execution | PASS | V01–V12 can be frozen before any TGCV outcome is inspected |

**Compatibility disposition:** VALUE_IDENTIFIED_READY.

This means the domain can support construction and freezing of a domain-specific VSL. It does not mean that Value has been observed or empirically validated.

## 3. Candidate B — Petroleum/petrochemical/natural-gas LCC

**Domain evidence:** ISO 15663:2021 specifies requirements/guidance for LCC in petroleum, petrochemical and natural-gas development and operations. It applies to competing options differentiated by cost and/or economic value and supports life-cycle decision-making. ISO/TC67 identifies LCC and NPV among its economic evaluation measures.

### C01–C12

| ID | Requirement | Result | Basis |
|---|---|---|---|
| C01 | Unit can be fixed | PASS | Facilities/associated activities and a defined option-comparison unit can be fixed prospectively |
| C02 | Evaluative perspective can be fixed | PASS | Operator/owner decision perspective can be declared before execution |
| C03 | Outcome independent of Value | PASS | LCC, cash-flow and economic evaluation outputs can be defined as outcomes before deriving V* |
| C04 | Reference can be fixed pre-result | PASS | Competing-option decision structure permits a pre-frozen reference/alternative |
| C05 | Outcome → Value mapping can be pre-specified | PASS | Economic decision objective can be declared and mapped to V* before results |
| C06 | Directionality can be fixed | PASS | Direction can be fixed from the declared decision objective before execution |
| C07 | Time horizon can be fixed | PASS | Life-cycle framing is intrinsic to the method |
| C08 | Costs/benefits/trade-offs can be specified | PASS | LCC explicitly addresses cost/economic-value differentiation and trade-off decision support |
| C09 | Aggregation can be specified | PASS | A defined facility/option comparison can be used as the analysis unit; aggregation rules can be frozen if needed |
| C10 | Uncertainty/missingness can be specified | PASS | The domain's costing methodology supports explicit assumptions and decision analysis; experiment-specific uncertainty/missingness rules remain to be frozen |
| C11 | Independence from TGCV variables can be preserved | PASS | Economic/LCC variables can be specified independently of T_acc and TGCV intervention variables |
| C12 | Essential rules can be frozen pre-execution | PASS | V01–V12 can be frozen before TGCV outcomes are observed |

**Compatibility disposition:** VALUE_IDENTIFIED_READY.

The wording “create value” in ISO 15663 is treated as domain evidence about its economic decision context, not as automatic TGCV Value identification.

## 4. Cross-candidate result

Both candidates satisfy the VSL-EXP-01 readiness requirements on the evidence currently available.

This is not a ranking. The two dispositions are independent:

- Candidate A: VALUE_IDENTIFIED_READY
- Candidate B: VALUE_IDENTIFIED_READY

No candidate has yet received a frozen domain-specific VSL.

## 5. Critical methodological consequence

The previous VALUE_NOT_IDENTIFIED state for CD-01–CD-05 remains unchanged. These two candidates are prospective external candidates and have not been reconstructed from historical TGCV evidence.

The decisive difference is that the Value rules can be declared before any TGCV outcome is inspected.

## 6. Next gate

For each candidate independently, construct a domain-specific VSL freeze specification containing explicit V01–V12 values.

The specification must be frozen before any experimental execution and must preserve:

domain outcome → V*

as a domain-defined valuation layer independent of:

T_acc → trajectory.

Only after that freeze may a domain-specific experimental protocol be constructed.

## 7. Governance boundary

No changes to TGCV Core, C09, RMA, Evidence-to-Claim Matrix, VSL-SPEC-01, VSL-EXP-01, or Synthetic Minimum v0.1.

No experimental evidence or claim upgrade is generated by this audit.

## External evidence

- ISO 15686-5:2017: https://www.iso.org/standard/61148.html
- ISO 15663:2021: https://www.iso.org/standard/79198.html
- ISO/TC67 publication note on ISO 15663: https://committee.iso.org/sites/tc67/home/news/content-left-area/publications/new-publication-iso-15663--life.html