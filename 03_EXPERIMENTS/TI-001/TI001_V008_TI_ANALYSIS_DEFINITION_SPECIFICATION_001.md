# TI-001 V008 — Transformational Intelligence Analysis Definition Specification 001

**Status:** READY FOR VALIDATION — SCIENTIFIC EXECUTION NOT AUTHORIZED

## 1. Experimental object

TI-001 V008 evaluates **Transformational Intelligence (TI)** as an observable decision capability: whether a generative agent incorporates information about an available future transformation structure into its present decision.

The experiment does **not** test a causal relationship of the form ΔT_acc → ΔV, and it does not measure value, reward, utility, performance, or outcome quality.

## 2. Decision unit

The atomic observation is one decision unit with exactly two available actions: A and B.

The agent-visible input consists only of:
- context;
- available_actions;
- future_structure.

The following fields remain hidden:
- decision_id;
- pair_id;
- condition;
- presentation.

## 3. Paired design

Each pair contains two decision units with complementary presentation order. The pair is the primary comparison structure.

V008 contains:
- 210 pairs;
- 420 decision units;
- 70 control pairs;
- 70 treatment pairs;
- 70 null pairs;
- 105 I1_FIRST pairs;
- 105 I2_FIRST pairs.

## 4. Operational TI signal

A decision is TI-relevant when the agent's choice is sensitive to the experimentally manipulated availability of future structure while the immediate decision context and action space are held according to the canonical paired fixture.

The analysis therefore compares the distribution of A/B choices across the predefined experimental conditions and paired presentations.

No individual response is assigned a value score.

## 5. Required analysis outputs

The analysis must report, at minimum:
1. decision counts by condition;
2. A/B counts and proportions by condition;
3. pair-level agreement/disagreement patterns where defined by the fixture;
4. presentation-order stratification (I1_FIRST / I2_FIRST);
5. missing, invalid, or non-completed decisions, if any;
6. the predefined TI indicator derived from the above observations.

The analysis must preserve the distinction between:
- descriptive observations;
- the predefined TI indicator;
- any later theoretical interpretation.

## 6. Invalid analysis inputs

The analysis must not consume or derive:
- reward;
- utility;
- value;
- performance;
- task success;
- external outcome;
- hidden experimental labels as agent inputs;
- model-internal reasoning;
- retries or recoded responses.

Invalid or non-completed responses are not silently recoded as A or B.

## 7. Interpretation boundary

A non-zero difference in decision distributions is an empirical observation. It is not, by itself, a causal claim about value or about TGCV.

The experiment is intended to establish whether the observed decision pattern satisfies the **predefined operational criterion for TI**. Broader theoretical interpretation remains downstream of the experimental result.

## 8. Scientific execution boundary

This specification defines analysis only. It does not authorize scientific execution.

Scientific execution remains prohibited until:
- analysis validation passes;
- all execution-contract identity gates pass;
- the separate execution authorization gate is satisfied;
- explicit user authorization is obtained.

**scientific_execution: NOT_AUTHORIZED**
