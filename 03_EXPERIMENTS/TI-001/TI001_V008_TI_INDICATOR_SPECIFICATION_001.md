# TI-001 V008 — Transformational Intelligence Indicator Specification 001

**Status:** READY FOR VALIDATION — SCIENTIFIC EXECUTION NOT AUTHORIZED

## 1. Purpose

This specification defines the predefined operational indicator for Transformational Intelligence (TI) in V008.

The indicator measures whether present A/B decisions systematically incorporate the experimentally available future transformation structure.

It does not measure value, reward, utility, performance, task success, or outcome quality.

## 2. Unit of observation

The atomic observation is one decision unit with exactly two available actions: A and B.

The primary comparison structure is the canonical pair. Each pair contains two decision units with complementary presentation order.

## 3. Predefined comparison

For each canonical pair p, let x_{p,1}, x_{p,2} ∈ {A,B} denote the observed decisions in the two complementary presentations.

The pair-level agreement indicator is:

I_agree(p) = 1 if x_{p,1} = x_{p,2}; otherwise 0.

The pair-level switch indicator is:

I_switch(p) = 1 if x_{p,1} ≠ x_{p,2}; otherwise 0.

These are descriptive pair-level observations and are not themselves TI scores.

## 4. TI indicator

The primary predefined TI indicator is the condition-sensitive decision-distribution contrast.

For each condition c ∈ {control, treatment, null}, define:

q_c(A) = N_c(A) / N_c

where N_c(A) is the number of valid completed decisions selecting A and N_c is the number of valid completed decisions in condition c.

The primary indicator is the treatment-vs-control contrast:

TI_DC = q_treatment(A) - q_control(A)

The null condition is reported separately as a reference condition:

TI_NULL = q_null(A) - q_control(A)

The sign and magnitude of these contrasts are descriptive properties of the observed decision distributions. They are not causal claims about value or TGCV.

## 5. Pair-level reporting

The analysis must additionally report:

- agreement rate by condition;
- switch rate by condition;
- presentation-order stratification;
- valid, invalid, missing, and non-completed decision counts.

No invalid or non-completed response may be silently recoded as A or B.

## 6. Interpretation rule

The numerical contrasts are the predefined TI indicator outputs.

A non-zero TI_DC is evidence of a difference in observed decision distributions between treatment and control; it is not, by itself, a causal claim.

Whether the observed pattern satisfies the broader theoretical interpretation of Transformational Intelligence remains a downstream scientific interpretation governed by the pre-specified decision rule and the complete experimental record.

No value, reward, utility, performance, or external outcome enters the indicator.

## 7. Scientific execution boundary

This specification defines the indicator only. It does not authorize scientific execution.

**scientific_execution: NOT_AUTHORIZED**
