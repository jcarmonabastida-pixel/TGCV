# TGCV C10-C — C10C-003 India Documentary Admission Audit Result 001

## Status

`CLOSED — DOCUMENTARY ADMISSION PASS WITH STRUCTURAL READINESS LIMITATION; DATA-LEVEL AUDIT REQUIRED`

## Candidate identified

**C10C-003 — India: Does basic energy access generate socioeconomic benefits? A field experiment with off-grid solar power in India.**

Aklin, Bayer, Harish & Urpelainen, *Science Advances* 3(5), e1602153 (2017), DOI `10.1126/sciadv.1602153`.

The study is a randomized field experiment in rural Uttar Pradesh. The experimental population is 81 nonelectrified habitations in Barabanki district, with household-level longitudinal observation. The study reports 1,281 households observed at baseline, midline and endline in the main experimental sample.

## Documentary evidence reviewed

- peer-reviewed article and supplementary-material description;
- documented randomized treatment/control design;
- documented intervention mechanism and installation rule;
- public replication package metadata;
- public provenance for data and replication code.

The replication package is deposited in Harvard Dataverse as `doi:10.7910/DVN/QXKPHH`, with the University of Strathclyde record identifying it as the replication package and recording India as geographical coverage.

## Admission criteria

### A1 — Exact intervention and experimental unit

**PASS.**

Treatment is a randomized offer to households in treatment habitations to subscribe to an off-grid solar microgrid service. The intervention is operationally distinct from realized subscription/take-up. The randomized unit is the habitation, with repeated household observations nested within habitations.

### A2 — Stable longitudinal structural state `S`

**PASS at documentary level.**

The study has a pre-treatment baseline and repeated midline/endline observations. Relevant structural state candidates include household electricity-access status, primary lighting source, hours of electricity availability, mobile-charging access and other documented household characteristics.

A definitive TGCV state dictionary is **not** frozen by this audit; that requires inspection of the actual replication files.

### A3 — Independent transformation universe `U_tau`

**PARTIAL.**

The intervention context supplies distinguishable energy-service changes, including gaining access to the MGP microgrid service, changes in electricity availability/hours and changes in lighting/charging configurations. However, the documentary record does not establish a closed, exhaustive universe of all admissible transformations at the household level.

The study's intervention is therefore not treated as an exhaustive definition of `U_tau`.

### A4 — Non-circular accessibility predicate `P_tau(S,C,L)`

**PARTIAL / PROMISING.**

The documented service has explicit operational constraints: the microgrid is installed only where sufficient demand exists, with a minimum of 10 subscribing households per habitation; the service supplies a specified basic electricity package. These constraints provide a potentially native basis for an accessibility predicate.

However, documentary evidence alone does not establish that every relevant transformation's accessibility can be evaluated prospectively from `S,C,L` without using realized take-up, installation outcome or downstream variables. This must be tested against the replication data and code before empirical execution.

### A5 — Reconstructable `T_acc,0`, `T_acc,1`, `Delta T_acc`

**PARTIAL / NOT YET ESTABLISHED.**

The study clearly distinguishes the randomized offer, installation and household take-up. It therefore has a stronger starting point for accessibility analysis than a case where only realized configurations are observed. Nevertheless, documentary evidence does not establish a complete operational mapping from the frozen variables to `T_acc` at both time points.

No `Delta T_acc` is claimed at this stage.

### A6 — Accessibility separated from execution/take-up/outcome

**PASS at documentary level.**

The paper explicitly distinguishes randomized offer (ITT), actual installation and subscription/take-up (LATE), and downstream outcomes. This separation is suitable for TGCV admission and is a material strength of the candidate.

### A7 — Independent outcome/value endpoint

**PASS.**

The study contains independently measured energy-access outcomes and socioeconomic outcomes, including savings, expenditure, business activity, work/study time and phone charging. These are downstream measurements and are not used here to define accessibility.

The candidate is particularly useful because the published results include both substantial access effects and null/weak socioeconomic effects, reducing the risk that candidate selection is driven by an expectation of universally positive value.

### A8 — Counterfactual / identification integrity

**PASS at documentary level.**

The treatment was randomized across habitations, with a separate control group and documented wait-list/randomization procedures. The paper reports balance checks and placebo/robustness analyses. Geographic spillovers were explicitly considered.

This audit does not independently re-estimate or validate the causal estimates.

### A9 — Provenance and reproducibility route

**PASS.**

A public replication package with data and code is identified through Harvard Dataverse (`10.7910/DVN/QXKPHH`). The article explicitly states that the replication package contains the data and code needed for replication.

### A10 — Finite readiness blockers

**PASS — blockers identified and bounded.**

The remaining blocker is specific rather than open-ended:

> Determine from the frozen replication package whether a non-circular, prospectively evaluable `P_tau(S,C,L)` and a closed enough `U_tau` can be constructed without using treatment realization, subscription/take-up or downstream outcomes.

If this fails, the candidate must receive a bounded structural-accessibility limitation analogous to C10C-001. If it passes, a separate data-level execution specification is required.

## Documentary admission decision

**ADMITTED TO CONTROLLED DATA-LEVEL AUDIT.**

C10C-003 is materially stronger than a candidate whose only observable evidence is realized treatment or configuration: the study has randomized opportunity-to-access, explicit service constraints, repeated observations, separate take-up/installation information, and a public replication package.

However, this documentary audit does **not** establish `T_acc`, `Delta T_acc`, a TGCV causal estimand, or a value pathway.

## Authorization boundary

This result authorizes **only the next controlled data-level admission/preflight operation**. It does not authorize:

- causal estimation;
- replication of published estimates as a scientific result;
- outcome-informed variable selection;
- freezing `U_tau` from observed post-treatment configurations;
- treating take-up/subscription as accessibility;
- treating treatment assignment as `T_acc`;
- claiming positive `Delta T_acc`;
- value inference;
- modification of TGCV Core;
- reopening any closed gate or prior candidate.

## Recommended next controlled operation

Freeze the exact Harvard Dataverse source version and replication archive for C10C-003, then perform a non-executing data/code inspection focused specifically on:

`S0, S1, U_tau, P_tau(S,C,L), T_acc,0, T_acc,1, Delta T_acc`

before any causal execution is considered.
