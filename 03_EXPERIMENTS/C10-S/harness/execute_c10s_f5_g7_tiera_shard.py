"""CLI entry point for one immutable F5 G7 primary or replay shard."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from c10s_nested_mr_fixtures import tier_a_specs
from c10s_f5_g7_shard_execution import run_cell_shard
import run_c10s_f5_g7_tiera_calibration as g7


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--phase", choices=("primary", "replay"), required=True)
    parser.add_argument("--cell-id", required=True)
    parser.add_argument("--replicate-start", type=int, required=True)
    parser.add_argument("--replicate-count", type=int, required=True)
    parser.add_argument("--source-commit", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    spec = next((item for item in g7.f5_specs() if item.cell_id == args.cell_id), None)
    if spec is None:
        raise SystemExit("G7_SHARD_CELL_NOT_IN_FROZEN_ROSTER")
    result = run_cell_shard(
        spec,
        phase=args.phase,
        replicate_start=args.replicate_start,
        replicate_count=args.replicate_count,
        c0_b=g7.C0_B,
        c5_b=g7.C5_B,
        source_commit=args.source_commit,
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, sort_keys=True, indent=2, allow_nan=False) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({
        "phase": args.phase,
        "cell_id": args.cell_id,
        "replicate_start": args.replicate_start,
        "replicate_count": args.replicate_count,
        "records_digest": result["records_digest"],
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
