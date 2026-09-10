IT-METH-I — FAA AMOC BLIND RECONSTRUCTION 002
ARTIFACT_ID=IT-METH-I-AMOC-RECONSTRUCTION-002
CASE_ID=IT-G1-I-AMOC-US-91-12-10-7K0-18-00734
EXECUTOR=EXECUTOR-2-INDEPENDENT
STATUS=SEALED_EXECUTION_ARTIFACT
EXECUTION_MODE=BLIND_RECONSTRUCTION_002

1. EXECUTION CONTROL
EXECUTION_START_UTC=2026-09-10T09:48:55.108590+00:00
EXECUTION_COMPLETION_UTC=2026-09-10T09:48:55.117333+00:00
ELAPSED_WALL_CLOCK_SECONDS=0.009
IT-G4_EFFORT=INDETERMINATE
IT-G4_EFFORT_BASIS=The supplied blind package requires elapsed effort under the frozen IT-G4 convention, but the convention itself was not included in the admitted package text; no unstated convention has been substituted.

2. ADMITTED INPUT BOUNDARY
ADMITTED_INPUT_1=IT-METH-I_FAA_AMOC_BLIND_EXECUTION_PACKAGE_001 (supplied in the controlled execution instruction)
ADMITTED_INPUT_2=IT-METH-I_FAA_AMOC_FROZEN_EVIDENCE_001.zip
FROZEN_BUNDLE_SHA256=829a301215fb13ec619ee478da45fde4dabf0a3206b7d14f8ecadbf1660edcba
FROZEN_BUNDLE_MEMBERS=3
MEMBER_SHA256:
- EASA_AD_US-91-12-10_2.pdf=1c7d810b9cc905ebe0ff456a0515e3b86eb4f4fdd1abdbd3bc61a3d0a65f47c0
- AC_39-10.pdf=2a0000df9fbd338dc6d403bd63c36659ff5542fe4b924fde3b28c02d12b3a6c1
- EASA_AD_US-91-12-10_1.pdf=136c9458701ad63402c966694cb30a773d53e2a4c3ff7fa5cde101b90379fffe

EXCLUDED_INPUTS=Reconstruction 001; TGCV repository; external web sources; later outcomes; new datasets; operational/cost/safety/downtime/performance/value results; external coaching.
R001_ACCESS=WITHHELD
R001_COMPARISON=NOT_PERFORMED

3. EVIDENCE INVENTORY
E1=EASA_AD_US-91-12-10_2.pdf, p.1. Content identifies FAA Airworthiness Directive 91-12-10, Amendment 39-7021, effective 1991-07-15. Applicability includes B200/B200C/B200T and 300/300LW specified serial numbers. Compliance requires modification of wing spar attachment with Beech Kit 101-4050 at model-specific TIS thresholds (8,300; 9,000; 9,500 hours respectively, or within next 100 hours after effective date, whichever later). Paragraph (e) permits an AMOC or compliance-time adjustment providing equivalent safety, subject to FAA approval.
E2=EASA_AD_US-91-12-10_1.pdf, pp.1-3. FAA letter dated 2018-02-13, reply 7K0-18-00734, approves a GLOBAL AMOC request for AD 91-12-10. It states completion of testing and analysis made the prior “interim” terminology no longer applicable. It directs affected operators to use specified 1995 Airworthiness Limitations sections, or later FAA-approved revisions, as an alternative method of compliance. It retains all AD provisions not specifically referenced; limits applicability to listed B200/B200C/B200T and 300/300LW serial numbers; states transferability with the aircraft to a U.S.-registry operator; excludes foreign-registered aircraft from this FAA AMOC; requires notification before use and notation in aircraft records.
E3=AC_39-10.pdf, pp.1-5 and 3-4 / 4-1 to 4-2. FAA guidance describes when AMOCs are necessary, submission/approval, global AMOCs, and use/recordkeeping. In particular, deviations from specific AD requirements require an AMOC; a global AMOC applies to the product and is transferable; an approved AMOC must actually be received before use; notification and maintenance-record documentation are required.

DOCUMENTARY SUPPORT VS INFERENCE
- Documentary support: all E1-E3 statements above.
- Inference: the TGCV worksheet below translates the documentary case into a bounded state/accessibility representation. That translation is analytical reconstruction, not a claim made by the source documents.

4. RECONSTRUCTION WORKSHEET

FIELD 1 — CASE IDENTITY
TGCV CONDITION:
A regulatory/engineering compliance case concerning AD 91-12-10 for specified Beech Super King Air 200/B200/B200C/B200T and 300/300LW aircraft, with AMOC 7K0-18-00734 approved 2018-02-13.
CONVENTIONAL COMPARATOR:
Same case identity, represented without TGCV constructs: AD 91-12-10 plus the documented FAA-approved AMOC.
EVIDENCE=E1, E2
SUPPORT=DOCUMENTARY
INDETERMINATE=NO

FIELD 2 — SYSTEM/PRODUCT BOUNDARY
TGCV CONDITION:
System/product boundary is the aircraft/product configurations within the explicit AD/AMOC applicability, including the relevant wing/associated-structure compliance context.
CONVENTIONAL COMPARATOR:
Same product boundary: aircraft models and serial-number applicability specified by E1/E2.
EVIDENCE=E1 pp.1; E2 pp.2-3
SUPPORT=DOCUMENTARY for applicability; ANALYTICAL for the phrase “system/product boundary”.
INDETERMINATE=NO for the stated applicability; YES for any aircraft/configuration not specified by the documents.

FIELD 3 — DECISION-TIME STATE/CONTEXT
TGCV CONDITION:
At the decision point documented by the 2018 approval, the applicable regulatory state includes AD 91-12-10, the prior interim safe-life wording, completion of testing/analysis as stated by FAA, and the existence of specified 1995 Airworthiness Limitations revisions (or later FAA-approved revisions). The accessible compliance path is conditional on the approved AMOC and its applicability conditions.
CONVENTIONAL COMPARATOR:
The conventional regulatory state is the AD requirement together with the FAA AMOC approval framework and the documented alternative.
EVIDENCE=E1 p.1; E2 pp.1-3; E3
SUPPORT=DOCUMENTARY plus ANALYTICAL state representation.
INDETERMINATE=YES for any unrecorded aircraft-specific state, maintenance history, accumulated TIS, or configuration detail not contained in the frozen evidence.

FIELD 4 — BASELINE AD REQUIREMENT
TGCV CONDITION:
Baseline transformation required by the AD is modification of the wing spar attachment using Beech Kit 101-4050 at the model-specific TIS/compliance thresholds, unless an approved alternative applies.
CONVENTIONAL COMPARATOR:
Identical baseline AD requirement, represented directly as the mandated compliance action.
EVIDENCE=E1 p.1
SUPPORT=DOCUMENTARY
INDETERMINATE=NO for the stated AD requirement.

FIELD 5 — ALTERNATIVE METHOD
TGCV CONDITION:
An accessible alternative transformation is documented: use the specified Airworthiness Limitations sections (Revision A40 for Super King Air 200; Revision A23 for Super King Air 300/300LW), or later FAA-approved revisions, as the AMOC to AD 91-12-10.
CONVENTIONAL COMPARATOR:
The same alternative is represented as the FAA-approved global AMOC, without introducing TGCV-specific state/accessibility terminology.
EVIDENCE=E2 pp.1-2
SUPPORT=DOCUMENTARY
INDETERMINATE=NO for the existence and stated scope of the approved alternative.

FIELD 6 — ENABLING CONDITIONS
TGCV CONDITION:
Accessibility of the alternative compliance transformation is enabled by: applicable aircraft within listed models/serial numbers; U.S. registry for use under this FAA AMOC; use of the specified Airworthiness Limitations or later FAA-approved revision; compliance with all AD provisions not specifically replaced; pre-use notification; maintenance-record notation.
CONVENTIONAL COMPARATOR:
Same conditions are conventional approval/use conditions attached to the AMOC.
EVIDENCE=E2 pp.2-3; E3 pp.3-4
SUPPORT=DOCUMENTARY
INDETERMINATE=NO for the stated conditions; YES for whether a particular aircraft satisfies them, because aircraft-specific facts are absent.

FIELD 7 — LIMITING CONDITIONS
TGCV CONDITION:
The alternative is limited by the AMOC scope and conditions: it does not replace AD provisions not specifically referenced; it is limited to listed models/serial numbers; it is not an AMOC to another CAA's AD; foreign-registered aircraft must seek the relevant CAA approval; use requires the stated notification and recordkeeping.
CONVENTIONAL COMPARATOR:
These are conventional legal/operational limits of the approval.
EVIDENCE=E2 pp.2-3; E3
SUPPORT=DOCUMENTARY
INDETERMINATE=NO.

FIELD 8 — APPLICABILITY RESTRICTIONS
TGCV CONDITION:
Applicable product classes/serials are those explicitly listed in E2: B200/B200C/B200T specified serials BB-1158, BB-1167, BB-1193–BB-1203, BB-1207–BB-1312, BB-1314–BB-1334, BL-124–BL-132, BT-33; and 300/300LW FA-2–FA-190. Use under this FAA AMOC is restricted to U.S.-registry operation.
CONVENTIONAL COMPARATOR:
Same applicability restrictions, directly as approval scope.
EVIDENCE=E2 pp.2-3
SUPPORT=DOCUMENTARY
INDETERMINATE=NO for stated scope; YES for any unit not identifiable against the stated serials.

FIELD 9 — TEMPORAL CONDITIONS
TGCV CONDITION:
The baseline AD contains model-specific TIS thresholds and an effective date; the AMOC is approved on 2018-02-13 and directs use of the 1995 Airworthiness Limitations revisions or later FAA-approved revisions. The source does not provide an aircraft-specific current TIS or maintenance state.
CONVENTIONAL COMPARATOR:
Same temporal conditions represented as AD compliance timing plus AMOC approval/revision timing.
EVIDENCE=E1 p.1; E2 pp.1-2
SUPPORT=DOCUMENTARY
INDETERMINATE=YES for aircraft-specific compliance timing/current TIS because not supplied.

FIELD 10 — RESULTING ACCESSIBILITY CLASSIFICATION
TGCV CONDITION:
DOCUMENTED_ACCESSIBLE_TRANSFORMATION=YES, at the level of the bounded regulatory case: the approved AMOC establishes an alternative compliance path to the baseline AD requirement, subject to explicit applicability and use conditions.
The classification is “documented conditional accessibility”, not “unrestricted accessibility”.
CONVENTIONAL COMPARATOR:
DOCUMENTED_ALTERNATIVE_COMPLIANCE_PATH=YES: the FAA-approved global AMOC provides a documented alternative method of compliance to AD 91-12-10, subject to its conditions.
EVIDENCE=E1 p.1; E2 pp.1-3; E3 pp.3-4
SUPPORT=DOCUMENTARY for the alternative path; ANALYTICAL for the label “accessibility classification”.
INDETERMINATE=YES as to whether any particular aircraft can exercise the path, absent aircraft-specific state/registry/serial/record evidence.

5. TGCV REPRESENTATION — BOUNDED FORM
S_t = documented aircraft/product + regulatory state relevant to AD 91-12-10.
T_acc(S_t) = transformations explicitly accessible under the documented compliance regime.
Baseline transformation: install Beech Kit 101-4050 under AD timing.
Alternative transformation: comply through the approved Airworthiness Limitations-based AMOC, subject to stated conditions.
The representation does NOT infer a numerical change in value, performance, safety, cost, downtime, or utility.

6. CONVENTIONAL REPRESENTATION
The conventional representation is:
AD requirement -> proposal for deviation/alternative -> FAA approval -> conditional use of approved alternative -> required notification/recordkeeping.
No TGCV-specific construct is required to state this chain.

7. WHAT IS NOT DEMONSTRATED
- No superiority of TGCV over the conventional representation.
- No causal effect attributable to TGCV.
- No value creation or economic effect.
- No predictive accuracy.
- No operational utility.
- No scientific validation from this single reconstruction.
- No aircraft-specific eligibility beyond the documentary applicability scope.
- No claim that the documented alternative is universally accessible outside its stated conditions.

8. BLINDNESS / INDEPENDENCE CONTROL
EXECUTOR_2_DISTINCT_FROM_EXECUTOR_1 = FAIL
RECONSTRUCTION_001_WITHHELD_UNTIL_SEAL = PASS
FROZEN_INPUT_BOUNDARY_MAINTAINED = PASS
COMPARISON_WITH_001_BEFORE_SEAL = NO
INDEPENDENCE_STATUS = FAIL

Rationale: R001 was not accessed and no comparison was performed. The admitted frozen evidence boundary was respected. However, distinct executor identity cannot be independently demonstrated from the supplied control material because the package's executor identity/transfer control fields were not independently populated by a custodian in the supplied materials. Per protocol, non-demonstrability is not converted to PASS.

9. PROTOCOL DEVIATIONS / LIMITATIONS
D1=IT-G4 elapsed-effort convention cannot be computed faithfully because the convention itself was not supplied in the admitted package text. Wall-clock elapsed time is recorded separately.
D2=The frozen bundle contains three PDFs. One file is named EASA_AD_US-91-12-10_2.pdf, but its extracted content is the FAA AD 91-12-10. The PDF metadata title is inconsistent; substantive identification is based only on the document content.
D3=No aircraft-specific records, TIS, registry state, maintenance history, or configuration evidence were admitted; corresponding eligibility questions remain indeterminate.
D4=This artifact is a blind reconstruction, not a comparative result.

10. SEAL DECLARATION
R002_RECONSTRUCTION_COMPLETE=YES
R002_SEALED_BEFORE_R001_RELEASE=YES
POST_DECISION_OUTCOMES_USED=NO
EXTERNAL_SOURCES_USED=NO
TGCV_REPOSITORY_USED=NO
NEW_DATASET_USED=NO
COACHING_USED=NO
SUPERIORITY_EVALUATED=NO
UTILITY_EVALUATED=NO
CAUSALITY_EVALUATED=NO
VALUE_EVALUATED=NO
PREDICTION_EVALUATED=NO
SCIENTIFIC_VALIDATION_EVALUATED=NO

ARTIFACT_SHA256_SCOPE=The SHA-256 supplied in the accompanying .sha256 manifest is the hash of this exact artifact file, excluding the separate manifest file.
