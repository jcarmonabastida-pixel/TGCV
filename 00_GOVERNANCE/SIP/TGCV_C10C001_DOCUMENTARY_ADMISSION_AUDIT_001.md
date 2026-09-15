# TGCV C10-C — C10C-001 Egypt Documentary Admission Audit 001

## Status

`COMPLETED — DOCUMENTARY AUDIT; EMPIRICAL DATA ACQUISITION NOT AUTHORIZED`

## Candidate

C10C-001 — *Exporting and Firm Performance: Evidence from a Randomized Experiment*, Atkin, Khandelwal & Osman (QJE 2017).

## Evidence boundary

This audit uses public study documentation and replication-access metadata only. No empirical dataset was downloaded or executed. No causal estimate was reproduced.

J-PAL identifies 219 eligible rug producers, with 74 randomly assigned to treatment and 145 to comparison. Treatment consisted of an opportunity to fill export orders secured through Hamis Carpets and foreign buyers. The study followed firms periodically from 2011–2014 and collected production, price, quality and knowledge-flow information. citeturn2view0turn0search0

## D1 — Provenance

**PASS.** Peer-reviewed QJE article, AEA RCT registration `AEARCTR-0000069`, named researchers and a Harvard Dataverse data route are publicly documented. citeturn2view0

## D2 — Experimental identification

**PASS — strong.** Random assignment generated exogenous variation in access to foreign markets. The treatment assignment is distinct from subsequent take-up/exporting. The published specification explicitly treats the randomized treatment as ITT and notes that take-up is non-random. citeturn0search16turn1search0

## D3 — Structural accessibility transition

**PROMISING — material operational gap remains.** Documentary evidence supports an intervention that changes the firm's opportunity set: firms receive an opportunity to produce for foreign buyers, with externally established prices, delivery timing and product specifications. This is conceptually compatible with a TGCV transformation-space change. citeturn2view0

However, the documentary evidence does not yet establish an admissible variable-level representation of `S_0`, `S_1`, `U_τ*`, and `P_τ(S,C,L)`. In particular, **treatment assignment cannot itself be used as `T_acc`**, and actual exporting/take-up cannot be substituted for accessibility. The published study explicitly distinguishes treatment from take-up. citeturn0search16

## D4 — Independent value endpoint

**PASS — strong.** Monthly firm profit is an economic endpoint distinct from treatment assignment and from the accessibility concept. J-PAL reports a 26% increase in monthly profits under the randomized opportunity-to-export intervention. citeturn2view0

## D5 — Counterfactual

**PASS.** The 74 treated versus 145 comparison firms provide the randomized counterfactual at the assignment level. citeturn2view0

## D6 — Downstream pathway

**PROMISING.** Documentary evidence provides a rich temporal pathway: opportunity to export → actual export production/take-up → repeated interaction with buyers → knowledge transfer and learning → quality/productivity changes → profit. The study reports that quality/productivity improvements appeared after approximately five months, supporting a potentially identifiable trajectory rather than a purely contemporaneous treatment/value association. citeturn2view0

For TGCV purposes these downstream events must remain distinct from `ΔT_acc`.

## D7 — Competing mechanisms and interference

**CONDITIONALLY SUPPORTED.** Subsequent orders could depend on firm performance and buyer interest, so post-treatment access is partly endogenous. The published analysis explicitly warns that take-up is non-random. The paper also reports no support for geographic spillovers between treatment and control firms in its spillover analysis. citeturn0search18

This does not by itself solve the TGCV operationalization problem; the relevant mechanisms and post-treatment opportunity changes must be separated from the initial randomized access intervention.

## D8 — Reproducibility/provenance route

**PROMISING.** J-PAL provides a Harvard Dataverse route and identifies the experiment and sample clearly. Exact file inventory, hashes, variable labels, coding, missingness, time structure and derived-variable provenance remain unverified because dataset acquisition is outside this audit boundary. citeturn2view0

## D9 — TGCV bounded-universe feasibility

**NOT YET ADMITTED.** A plausible bounded universe could concern export-production transformations defined by documented buyer specifications, delivery requirements and production capabilities. But selecting concrete transformations, predicates and state variables before inspecting the actual replication metadata would be speculative.

No `U_τ*`, `P_τ`, `T_acc,0`, `T_acc,1` or `ΔT_acc` is therefore admitted at this stage.

## Admission decision

**C10C-001: PROMISING / EVIDENCE GAP REMAINS.**

The candidate is admitted to the next controlled data-level inspection gate, but not to empirical execution.

### Principal unresolved questions

1. Which exact variables encode the firm's pre/post structural capabilities and constraints relevant to export production?
2. Can a small, outcome-independent `U_τ*` be defined from those variables?
3. Can `T_acc,0`, `T_acc,1` and `ΔT_acc` be reconstructed reproducibly without using treatment, take-up or outcomes as proxies?
4. What exact profit endpoint, unit, time horizon and missingness rules are present in the replication data?
5. Can subsequent buyer orders and take-up be represented as downstream trajectory/mechanism rather than conflated with initial accessibility?
6. What exact file-level provenance and independent reproduction route are available?

## Authorization boundary

**Authorized next step:** controlled data-level acquisition/inspection package, after freezing the corresponding admission specification.

**Not authorized:** dataset download, replication execution, causal estimation, outcome-informed variable selection, or claim upgrade under this audit.

## Sources

J-PAL documents the experiment, sample, randomized assignment, intervention mechanics, follow-up period, quality measures, outcomes and Harvard Dataverse data route. citeturn2view0

The QJE article documents the randomized access-to-foreign-markets design and distinguishes ITT treatment assignment from non-random take-up. citeturn0search0turn0search16
