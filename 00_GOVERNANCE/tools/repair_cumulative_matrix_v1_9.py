#!/usr/bin/env python3
"""Repair the cumulative v1.9 matrix header and historical closure summaries.

This preserves all material evidence and only restores cumulative references
that the first v1.9 migration accidentally replaced with the latest update.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
V19 = ROOT / "EVIDENCE_TO_CLAIM_MATRIX_v1.9.md"
CURRENT = ROOT / "EVIDENCE_TO_CLAIM_MATRIX_CURRENT.md"

C10C002 = (
    "Propagation of the closed C10C-002 bounded causal experiment, "
    "*The Neighborhood Impacts of Local Infrastructure Investment: Evidence from Urban Mexico*, "
    "using the frozen bounded structural reconstruction and the completed T10–T17 audit chain. "
    "The result is `CLOSED — NEGATIVE BOUNDED CAUSAL RESULT`: the frozen ITT estimate for net "
    "accessible-transformation change is −0.0314211391; wild-cluster bootstrap p=0.8354 with "
    "95% CI [−0.3086899032, 0.2458476249]. The result is not evidence of a positive TGCV causal "
    "effect and is not a refutation of TGCV. The value pathway was not executed and municipal "
    "interference/saturation remains unresolved. No Core/RMA-wide scientific upgrade is implied."
)

C10C001 = (
    "C10C-001 Egypt structural reconstruction. The controlled reconstruction establishes `S0`, `S1` "
    "and observed `ΔS` for the identified sample, but no independently defined accessibility predicate "
    "`Pτ` is identified; therefore `Uτ`, `T_acc,0`, `T_acc,1` and `ΔT_acc` are not reconstructible "
    "from the frozen evidence. This is a material non-software empirical boundary qualification, not "
    "positive accessibility or trajectory/value causal evidence. No claim-level status is upgraded."
)


def replace_once(text: str, old: str, new: str) -> str:
    if old not in text:
        raise SystemExit(f"ERROR: expected text not found: {old[:80]}")
    return text.replace(old, new, 1)


def main() -> int:
    if not V19.exists():
        raise SystemExit("ERROR: v1.9 matrix missing")
    text = V19.read_text(encoding="utf-8")

    old_current = "**Current update:** " + C10C001
    new_current = "**Current update:** " + C10C002 + "\n\n**C10C-001 update:** " + C10C001
    text = replace_once(text, old_current, new_current)

    old_boundary = "The v1.8 update preserves the full evidence/claim structure of v1.7 and adds the C10C-002 empirical evidence record plus bounded propagation to C02, C07, C11 and C16. No C01–C16 status is upgraded. C08, C09 and C10 are explicitly not upgraded or positively supported by C10C-002. The TGCV Core remains unchanged."
    new_boundary = "The v1.9 update preserves the full evidence/claim structure of v1.8 and adds the C10C-001 empirical evidence record plus bounded propagation to C02, C07, C08, C11 and C16. The complete C10C-002 evidence record and its prior bounded propagation remain preserved. No C01–C16 status is upgraded by C10C-001. C08, C09 and C10 are not upgraded or positively supported by C10C-001. The TGCV Core remains unchanged."
    text = replace_once(text, old_boundary, new_boundary)

    old_position = "The only claim-level change in v1.7 remains C09; v1.8 adds evidence propagation only and makes no claim-level status upgrade. The scientific Core remains unchanged."
    new_position = "The only claim-level change in the cumulative matrix remains the prior C09 consolidation; v1.8 added C10C-002 evidence propagation only, and v1.9 adds C10C-001 evidence propagation only. Neither v1.8 nor v1.9 changes any claim status. The scientific Core remains unchanged."
    text = replace_once(text, old_position, new_position)

    V19.write_text(text, encoding="utf-8", newline="\n")
    CURRENT.write_text(text, encoding="utf-8", newline="\n")
    print("REPAIRED: cumulative v1.9 matrix summaries")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
