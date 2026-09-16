# C10C-004 — Morocco Gate G4 — Women's Empowerment Operational Reconstruction Result 001

**Case:** `C10C-004 — Morocco microcredit / women's empowerment`
**Gate:** `G4 — semantic / physical / operational reconstruction`
**Status:** `CLOSED — OPERATIONAL RECONSTRUCTION VERIFIED`
**Date:** 2026-09-16
**Source dataset:** `input/Microcredit_EL_mini_anonym.dta`
**Source N:** `5,551`
**Historical specification:** `DoFiles/OutcomeConstruction_endline_Oct2014.do`
**Historical construction block:** lines 1547–1577
**Independent reconstruction environment:** Python 3.14 / pandas, without Stata

## 1. Objective

Verify that the women's-empowerment construct used by the Morocco endline analysis can be traced from questionnaire semantics to physical dataset variables and independently reconstructed from the frozen endline dataset using the historical analysis specification.

This gate is an operationalisation/reconstruction audit. It is not a causal-effect test and does not establish a causal effect of microcredit, accessibility, empowerment, trajectory or value.

## 2. Semantic mapping

The questionnaire defines J1–J9 as a sequence concerning a woman's independent activity and autonomy over:

1. pursuing an independent activity;
2. deciding necessary materials;
3. purchasing materials alone;
4. deciding necessary inputs;
5. purchasing inputs alone;
6. deciding what to produce;
7. producing something potentially tradable;
8. deciding whether to trade products;
9. trading products alone.

The questionnaire coding for J1–J9 is `1 = YES`, `2 = NO`, `-99 = NS/NR`. J9b is a separate historical question and is not conflated with J9.

## 3. Physical mapping

The endline dataset contains the direct indexed variables:

- J1: `j1_1 ... j1_11`
- J2: `j2_1 ... j2_11`
- J3: `j3_1 ... j3_11`
- J4: `j4_1 ... j4_11`
- J5: `j5_1 ... j5_11`
- J6: `j6_1 ... j6_11`
- J7: `j7_1 ... j7_11`
- J8: `j8_1 ... j8_11`
- J9: `j9_1 ... j9_11`

The `j1_num1 ... j1_num11` variables identify the woman's household-order slot where present; these are not the J1 response variables themselves.

J9b is represented separately as `j9b1 ... j9b11`.

## 4. Historical operational specification

`OutcomeConstruction_endline_Oct2014.do` constructs J1–J9 as household-level indicators. For each `i = 1...9`, it initializes `women_i = 0` and sets it to `1` if any of F1–F11 has `j_i_j == 1`.

Thus the operational rule is:

`women_i(h) = 1 iff exists j in {1,...,11} such that j_i_j(h) = 1`.

J9b is separately constructed as `women_10` using the same F1–F11 existential rule.

J10–J13 are constructed differently: `women_11...women_14` are equal to one when the corresponding response is `3` or `4`.

Each `women_i` is then standardized using the sample mean and sample standard deviation, producing `outcome1...outcome14`.

The historical index is constructed as:

`women_index = rowtotal(outcome1 outcome2 outcome2 outcome4 outcome5 outcome6 outcome7 outcome8 outcome9 outcome10 outcome11 outcome12 outcome13 outcome14)`

The duplicate `outcome2` and omission of `outcome3` are preserved exactly as historical code. They are not corrected in this reconstruction.

## 5. Independent reconstruction results

The independent Python reconstruction on the endline dataset produced:

| Dimension | `women_i = 1` |
|---|---:|
| J1 / women_1 | 510 |
| J2 / women_2 | 383 |
| J3 / women_3 | 125 |
| J4 / women_4 | 373 |
| J5 / women_5 | 121 |
| J6 / women_6 | 353 |
| J7 / women_7 | 240 |
| J8 / women_8 | 121 |
| J9 / women_9 | 73 |
| J9b / women_10 | 326 |
| J10 / women_11 | 1,680 |
| J11 / women_12 | 1,847 |
| J12 / women_13 | 3,141 |
| J13 / women_14 | 3,256 |

The reconstructed means and sample standard deviations were:

| i | mean | sample SD |
|---:|---:|---:|
| 1 | 0.091875338 | 0.288875913 |
| 2 | 0.068996577 | 0.253471149 |
| 3 | 0.022518465 | 0.148375705 |
| 4 | 0.067195100 | 0.250382132 |
| 5 | 0.021797874 | 0.146036190 |
| 6 | 0.063592146 | 0.244046950 |
| 7 | 0.043235453 | 0.203405020 |
| 8 | 0.021797874 | 0.146036190 |
| 9 | 0.013150784 | 0.113930588 |
| 10 | 0.058728157 | 0.235136388 |
| 11 | 0.302648172 | 0.459445626 |
| 12 | 0.332732841 | 0.471234232 |
| 13 | 0.565843992 | 0.495690259 |
| 14 | 0.586560980 | 0.492494560 |

The historical index reconstruction, including the duplicated `outcome2`, produced:

- `N = 5,551`
- mean = `0.000000000` (floating-point zero)
- sample SD = `8.218129454`
- minimum = `-5.965017097`
- maximum = `53.466739700`
- missing = `0`

## 6. Coding integrity audit

An independent audit of every observed non-missing value across F1–F11 for J1–J9 found no values outside `{1, 2, -99}`:

`J1: []`, `J2: []`, `J3: []`, `J4: []`, `J5: []`, `J6: []`, `J7: []`, `J8: []`, `J9: []`.

The `.dta` files did not contain precomputed `women_*`, `outcome*` or `women_index` variables. The outcome is therefore demonstrably constructed by the analysis code rather than imported as a precomputed field.

## 7. Execution-source verification

The endline DoFile explicitly states `Microcredit_EL_mini_anonym.dta` as its input and executes `use Input\\Microcredit_EL_mini_anonym.dta, clear;` near line 15. It saves the resulting endline outcome dataset as `Output\\endline_minienquete_outcomes.dta` near line 1943.

Therefore the physical source and historical construction path are unambiguous.

## 8. Closure

**G4 disposition:** `CLOSED — OPERATIONAL RECONSTRUCTION VERIFIED`.

The evidence establishes a complete bounded chain:

`questionnaire semantics → physical variables → observed coding → historical transformation rule → independent reconstruction → reconstructed index`.

No Stata installation was required. Python was used as an independent implementation of the already-audited historical specification.

This closure does not imply causal identification, treatment effectiveness, empowerment causality, trajectory modification, value creation, transversal validity, or any TGCV Core/RMA modification.

## 9. Historical-code anomaly retained

The duplicated `outcome2` and omitted `outcome3` in the historical `rowtotal` expression are retained as an explicit code anomaly. No corrective re-specification is incorporated into the evidence result. Any corrected-index analysis would constitute a separate, explicitly governed analysis.
