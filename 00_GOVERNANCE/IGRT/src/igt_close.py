from __future__ import annotations

import argparse
import json
import sys

from igt_core import close_session


def main() -> int:
    parser = argparse.ArgumentParser(description="TGCV Integrated Governance Runtime — session close")
    parser.add_argument("--material-change", action="store_true", help="Re-run canonical validator at close")
    parser.add_argument("--work-item", default=None, help="Optional active work-item identifier")
    parser.add_argument("--note", default="", help="Compact continuation note")
    args = parser.parse_args()

    try:
        result = close_session(
            material_change=args.material_change,
            active_work_item=args.work_item,
            continuation_note=args.note,
        )
    except Exception as exc:
        print("IGRT_SESSION_CLOSE=FAIL")
        print(f"ERROR={exc}")
        return 1

    state = result.get("governance_current_state")
    if args.material_change:
        passed = state == "PASS"
        print(f"IGRT_SESSION_CLOSE={'PASS' if passed else 'FAIL'}")
        print(f"GOVERNANCE_CURRENT_STATE={state}")
        if "validator_output" in result:
            first_line = result["validator_output"].splitlines()[0] if result["validator_output"] else ""
            print(f"VALIDATOR={first_line}")
        print(json.dumps(result, ensure_ascii=False))
        return 0 if passed else 1

    print("IGRT_SESSION_CLOSE=PASS")
    print("MATERIAL_CHANGE=NO")
    print("CONTINUATION_STATE=RECORDED")
    print(json.dumps(result, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
