from __future__ import annotations

import argparse
import json
import sys

from igt_core import start_session


def main() -> int:
    parser = argparse.ArgumentParser(description="TGCV Integrated Governance Runtime — session start")
    parser.add_argument("--work-item", default=None, help="Optional active work-item identifier")
    args = parser.parse_args()

    try:
        state = start_session(args.work_item)
    except Exception as exc:
        print("IGRT_SESSION_START=FAIL")
        print(f"ERROR={exc}")
        return 1

    print(f"IGRT_SESSION_START={'PASS' if state.governance_current_state == 'PASS' else 'FAIL'}")
    print(f"GOVERNANCE_CURRENT_STATE={state.governance_current_state}")
    print(f"RMA={state.rma_version or 'UNRESOLVED'}")
    print(f"MATRIX={state.matrix_version or 'UNRESOLVED'}")
    print(f"TRACEABILITY={state.traceability_version or 'UNRESOLVED'}")
    print(f"SESSION_STATE={state.phase}")
    print(json.dumps({"active_work_item": state.active_work_item, "next_action": state.next_action}, ensure_ascii=False))
    return 0 if state.governance_current_state == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
