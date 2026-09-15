#!/usr/bin/env python3
"""One-time governed construction of Evidence-to-Claim Matrix v1.9.

This migration is deliberately narrow: it starts from the complete v1.8
matrix, changes only the explicitly approved C10C-001 rows, and adds the
complete material evidence record. It is a no-op once v1.9 exists.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
V18 = ROOT / "EVIDENCE_TO_CLAIM_MATRIX_v1.8.md"
V19 = ROOT / "EVIDENCE_TO_CLAIM_MATRIX_v1.9.md"
CURRENT = ROOT / "EVIDENCE_TO_CLAIM_MATRIX_CURRENT.md"

SECTION = r'''## Material empirical evidence — C10C-001 Structural Reconstruction

**Case:** `C10C-001 — Egypt`  
**Status:** `PARTIAL — STRUCTURAL STATE RECONSTRUCTIBLE, ACCESSIBILITY PREDICATE NOT IDENTIFIED`  
**Result artifact:** `00_GOVERNANCE/SIP/TGCV_C10C001_STRUCTURAL_RECONSTRUCTION_RESULT_001.md`  
**Protocol:** `00_GOVERNANCE/SIP/TGCV_C10C001_STRUCTURAL_RECONSTRUCTION_PROTOCOL_001.md`  
**Source freeze:** `00_GOVERNANCE/SIP/TGCV_C10C001_SOURCE_VERSION_FREEZE_001.md`  
**Propagation record:** `00_GOVERNANCE/SIP/TGCV_C10C001_EVIDENCE_TO_CLAIM_PROPAGATION_001.md`

The controlled reconstruction was conducted on the frozen C10C-001 Egypt source. The baseline and identified longitudinal subset permit reconstruction of structural state and observed state changes, but the source does not expose an independently defined accessibility predicate `Pτ(S,C,τ)`. The audited variables identified as treatment/assignment, realized take-up/adoption, observed configuration identity, orders/production, or implementation detail cannot be promoted to an accessibility predicate without an additional admissibility rule.

The reconstruction therefore establishes a bounded non-software empirical boundary: `S0`, `S1` and observed `ΔS` are reconstructible for the identified sample, while `Uτ` cannot be defined as a cross-temporal union, `Pτ` is not identified, and consequently `T_acc,0`, `T_acc,1` and `ΔT_acc` are not reconstructible from the frozen evidence. Observed realization is not treated as accessibility; treatment assignment is not treated as availability; take-up/adoption is not treated as availability; observed configuration identity is not treated as the accessible transformation universe; and later-observed configurations are not used to define earlier accessibility because of temporal leakage.

This is material empirical evidence because it independently qualifies the boundary between structural-state reconstruction and accessibility-space reconstruction in a non-software domain. It does **not** establish positive evidence of `ΔT_acc`, a trajectory effect, a value pathway, causal effect on subsequent trajectories, transversal validity, or a Core modification. No claim-level upgrade follows from this propagation.

### Evidence-to-claim propagation

- **C02:** Material qualification. Structural reconstruction and observed configuration changes do not identify `Pτ`/`T_acc`; an explicit admissibility predicate remains required. No upgrade.
- **C07:** Bounded negative/limiting qualification. The case does not identify `ΔT_acc`; observed structural changes are not substituted for accessible transformation-space changes. No upgrade.
- **C08:** Material boundary qualification. Structural change/realized transformation cannot substitute for reachable trajectory evidence, and no trajectory causal estimand is established. No upgrade.
- **C11:** Material methodological qualification. The case is a distinct non-software empirical reconstruction boundary, strengthening the documented cross-domain evidence base only by showing where accessibility reconstruction fails. No transversal-validity upgrade.
- **C16:** Material methodological evidence. The case reinforces preservation of the distinctions among state, candidate transformations, accessibility, realized transformations and temporal leakage controls. No upgrade.

No positive propagation is made to C01, C03, C04, C05, C06, C09, C10, C12, C13, C14 or C15. The Core/RMA status is unchanged.

'''

ROWS = {
"C02": "| C02 | Accessibility is represented by transformations satisfying an independently defined admissibility predicate | E0 | Formalization + Rust + C-01 A-C + I-01 Gate C + IT-NOSD-010 G0/G1/G2 + EXT-UPD-4.8 + SWIM Reactive-0 + SWIM Reactive2 + IT-G1 + C10C-002 + C10C-001 | SWIM provides bounded accessibility operationalization; IT-G1 adds bounded evidence that end-to-end accessibility/function can depend on conditions external to the internal remediation target; C10C-002 adds an independent real-world bounded reconstruction of `T_acc*` from six structural infrastructure dimensions using pre-outcome structural predicates across 342 polygons and two observed rounds. C10C-001 independently demonstrates in a distinct non-software case that structural state reconstruction and observed configuration changes do not identify `Pτ`/`T_acc` without an explicit admissibility predicate. General `T_acc` remains unclosed and no claim-level upgrade is implied. | Independent operationalization across a distinct exemplar |",
"C07": "| C07 | Accessible transformation spaces change over time in Rust | E1 | Rust non-persistent pairs + bounded SWIM operationalization + C10C-002 + C10C-001 | SWIM provides bounded non-Rust evidence that accessible transformation spaces can change across observed state transitions; IT-G1 adds a bounded industrial state-transformation sequence; C10C-002 adds independent real-world longitudinal evidence from 342 polygons in which a bounded universe of 12 elementary structural transformations yields non-empty `ΔT_acc*` in 238 polygons, including 104 openings and 171 closures. C10C-001 adds a distinct non-software boundary case in which observed structural changes are reconstructible but `T_acc` and `ΔT_acc` are not identified; it therefore qualifies the distinction between observed structural change and accessible transformation-space change and is not evidence of `ΔT_acc`. This does not upgrade the Rust-specific claim level. | Independent closed operationalization / replication |",
"C08": "| C08 | Accessibility changes modify reachable future trajectories | H | Formal chain + bounded Rust H=1 + SWIM trajectory-linkage reconstruction + IT-G1 bounded state/trajectory observation + C10C-001 | SWIM adds bounded reconstructability of ordered subsequent transformations and state transitions; IT-G1 provides a bounded industrial state/trajectory observation. KGFS supplies the causal layer now reflected in C09. C10C-002 does not add a trajectory outcome and therefore does not establish modification of reachable future trajectories. C10C-001 adds a material empirical boundary qualification: structural change and realized transformation cannot substitute for reachable-trajectory evidence because accessibility was not identified and no trajectory causal estimand was estimated. No claim-level upgrade is implied. | Independent valid trajectory test with explicit trajectory criterion beyond bounded exemplars |",
"C11": "| C11 | TGCV is domain-independent / transversal | H | C-01 A-C + I-01 Gate C + bounded cross-domain evidence + C10C-002 + C10C-001 | SWIM is a bounded self-adaptive software exemplar, IT-G1 a bounded industrial AWS exemplar, KGFS a bounded real-world rural-finance intervention, and C10C-002 a bounded urban-infrastructure/real-estate empirical case. C10C-001 adds a distinct non-software empirical reconstruction boundary, showing that structural state/change can be recovered while accessibility remains unidentified unless an explicit admissibility predicate is available. This strengthens the documented heterogeneity and boundary evidence only; it does not establish transversal validity or justify a claim upgrade. | Independent operationalization across broader domains |",
"C16": "| C16 | TGCV provides a transversal analytical translation protocol preserving distinctions among state, candidate transformations, accessibility, Reach, Trajectory, Outcome and Value | H | D-OPS-22/23 + C-01 A-C + I-01 Gate C + IT-NOSD-010 G0/G1/G2 + EXT-UPD-4.8 + SWIM Reactive-0 + SWIM Reactive2 + SWIM trajectory-linkage reconstruction + IT-G1 + C09 Bundle 003 + C10C-002 + C10C-001 | SWIM supports bounded state/context → accessibility → `T_acc` → `ΔT_acc` and bounded trajectory linkage. IT-G1 adds bounded industrial evidence preserving distinctions among internal state transformation, external enabling condition and end-to-end outcome. C09 Bundle 003 adds bounded executable causal-operationalization evidence while preserving the distinction between intervention/accessibility and downstream outcome. C10C-002 adds a reproducible real-world bounded chain `Z → ΔS → T_acc* → ΔT_acc* → frozen causal estimand`, with structural-only predicates, explicit treatment/state separation, endpoint separation, and a negative result retained without post-hoc rescue. C10C-001 adds a complementary non-software boundary case preserving the distinction among structural state, candidate transformations, accessibility and realized transformations, while explicitly preventing temporal leakage. It does not close downstream value boundaries or establish transversal validity. | Closed independent-domain operationalization / downstream test |",
}


def replace_row(text: str, claim_id: str, replacement: str) -> str:
    pattern = re.compile(rf"^\| {re.escape(claim_id)} \|.*$", re.MULTILINE)
    text2, n = pattern.subn(replacement, text)
    if n != 1:
        raise RuntimeError(f"Expected exactly one matrix row for {claim_id}; found {n}")
    return text2


def main() -> int:
    if V19.exists():
        print("NOOP: v1.9 already exists")
        return 0
    if not V18.exists():
        raise SystemExit("ERROR: v1.8 source matrix missing")
    text = V18.read_text(encoding="utf-8")
    if "# TGCV — Evidence-to-Claim Matrix — Current v1.8" not in text:
        raise SystemExit("ERROR: source is not the expected v1.8 matrix")
    for cid, row in ROWS.items():
        text = replace_row(text, cid, row)
    text = text.replace("# TGCV — Evidence-to-Claim Matrix — Current v1.8", "# TGCV — Evidence-to-Claim Matrix — Current v1.9", 1)
    text = text.replace("**Date:** 2026-09-15  \n**Predecessor:** v1.7", "**Date:** 2026-09-15  \n**Predecessor:** v1.8", 1)
    text = text.replace("**Incremental governance update:** v1.8 preserves the complete material evidentiary content and schema of v1.7; no evidence is deleted, collapsed, or downgraded. C10C-002 is propagated as material bounded empirical evidence to C02, C07, C11 and C16. No claim-level status is upgraded by this propagation.", "**Incremental governance update:** v1.9 preserves the complete material evidentiary content and schema of v1.8; no evidence is deleted, collapsed, or downgraded. C10C-001 is propagated as material bounded empirical evidence to C02, C07, C08, C11 and C16. No claim-level status is upgraded by this propagation.", 1)
    current_update = "**Current update:** C10C-001 Egypt structural reconstruction. The controlled reconstruction establishes `S0`, `S1` and observed `ΔS` for the identified sample, but no independently defined accessibility predicate `Pτ` is identified; therefore `Uτ`, `T_acc,0`, `T_acc,1` and `ΔT_acc` are not reconstructible from the frozen evidence. This is a material non-software empirical boundary qualification, not positive accessibility or trajectory/value causal evidence. No claim-level status is upgraded."
    old_prefix = "**Current update:** Propagation of the closed C10C-002 bounded causal experiment, *The Neighborhood Impacts of Local Infrastructure Investment: Evidence from Urban Mexico*, using the frozen bounded structural reconstruction and the completed T10–T17 audit chain."
    start = text.find(old_prefix)
    if start == -1:
        raise SystemExit("ERROR: v1.8 current-update block not found")
    end = text.find("\n\n## Matrix preservation rule", start)
    if end == -1:
        raise SystemExit("ERROR: matrix preservation boundary not found")
    text = text[:start] + current_update + text[end:]
    marker = "## Material methodological evidence — IUT-A-01 U2 FULL_PILOT 001"
    if marker not in text:
        raise SystemExit("ERROR: insertion marker not found")
    text = text.replace(marker, SECTION + marker, 1)
    V19.write_text(text, encoding="utf-8", newline="\n")
    CURRENT.write_text(text, encoding="utf-8", newline="\n")
    print("CREATED: EVIDENCE_TO_CLAIM_MATRIX_v1.9.md")
    print("SYNCED: EVIDENCE_TO_CLAIM_MATRIX_CURRENT.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
