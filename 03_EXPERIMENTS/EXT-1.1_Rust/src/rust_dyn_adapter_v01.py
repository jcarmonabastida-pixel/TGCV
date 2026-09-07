"""RUST-DYN-EXEC-1A — real-data adapter skeleton.

This module is intentionally fail-closed with respect to real execution until
its structural loader and preflight are completed and separately authorized.
It preserves the frozen RUST-DYN-1 / DR-035 semantics:
- adjacent consecutive package-version origins within package;
- created_at ordering only;
- exact timestamp ties excluded;
- no arbitrary secondary ordering;
- H=1 downstream semantics;
- no outcome/predictive fields.

Synthetic conformance can be performed independently. Real dataset execution
must not occur merely by invoking this module.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from datetime import datetime
from typing import Iterable, Sequence


HORIZON_DEFAULT = 1
TEMPORAL_RULE_ID = "DR-035-v0.1-ADJACENT-CREATED-AT"
REAL_EXECUTION_AUTHORIZED = False


@dataclass(frozen=True)
class Origin:
    version_id: str
    package_id: str
    version_str: str
    created_at: str


def parse_created_at(value: str) -> datetime:
    """Parse an ISO timestamp; malformed timestamps fail closed."""
    if not isinstance(value, str) or not value.strip():
        raise ValueError("created_at must be a non-empty ISO timestamp")
    text = value.strip()
    try:
        return datetime.fromisoformat(text.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ValueError(f"invalid created_at: {value!r}") from exc


def build_adjacent_pairs(origins: Iterable[Origin]) -> tuple[list[tuple[Origin, Origin]], dict]:
    """Build the DR-035 primary temporal population.

    Origins are grouped by package_id and ordered only by created_at. Exact
    timestamp ties are excluded from temporal-pair construction. No secondary
    ordering is permitted.
    """
    groups: dict[str, list[Origin]] = {}
    for origin in origins:
        parse_created_at(origin.created_at)
        groups.setdefault(origin.package_id, []).append(origin)

    pairs: list[tuple[Origin, Origin]] = []
    tie_origin_count = 0
    excluded_origin_count = 0
    zero_pair_package_count = 0

    for package_id, package_origins in groups.items():
        ordered = sorted(package_origins, key=lambda o: parse_created_at(o.created_at))

        unique: list[Origin] = []
        i = 0
        while i < len(ordered):
            j = i + 1
            timestamp = parse_created_at(ordered[i].created_at)
            while j < len(ordered) and parse_created_at(ordered[j].created_at) == timestamp:
                j += 1
            block = ordered[i:j]
            if len(block) > 1:
                tie_origin_count += len(block)
                excluded_origin_count += len(block)
            else:
                unique.append(block[0])
            i = j

        package_pairs = list(zip(unique, unique[1:]))
        if not package_pairs:
            zero_pair_package_count += 1
        pairs.extend(package_pairs)

    manifest = {
        "temporal_rule_id": TEMPORAL_RULE_ID,
        "eligible_origin_count": len(origins),
        "timestamp_tie_origin_count": tie_origin_count,
        "excluded_origin_count_due_to_ties": excluded_origin_count,
        "temporal_pair_count": len(pairs),
        "pair_count_by_package": _pair_counts(pairs),
        "zero_pair_package_count": zero_pair_package_count,
        "real_execution_authorized": REAL_EXECUTION_AUTHORIZED,
    }
    return pairs, manifest


def _pair_counts(pairs: Sequence[tuple[Origin, Origin]]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for left, right in pairs:
        if left.package_id != right.package_id:
            raise RuntimeError("cross-package temporal pair detected")
        counts[left.package_id] = counts.get(left.package_id, 0) + 1
    return dict(sorted(counts.items()))


def synthetic_conformance() -> dict:
    """Minimal conformance tests for DR-035 pair construction."""
    a = Origin("1", "p", "0.1.0", "2020-01-01T00:00:00+00:00")
    b = Origin("2", "p", "0.2.0", "2020-02-01T00:00:00+00:00")
    c = Origin("3", "p", "0.3.0", "2020-03-01T00:00:00+00:00")
    tie1 = Origin("4", "q", "0.1.0", "2020-01-01T00:00:00+00:00")
    tie2 = Origin("5", "q", "0.2.0", "2020-01-01T00:00:00+00:00")

    pairs, manifest = build_adjacent_pairs([c, a, b, tie1, tie2])
    pair_ids = [(x.version_id, y.version_id) for x, y in pairs]

    tests = {
        "adjacent_only": pair_ids == [("1", "2"), ("2", "3")],
        "created_at_order_only": pair_ids == [("1", "2"), ("2", "3")],
        "timestamp_ties_excluded": manifest["timestamp_tie_origin_count"] == 2,
        "no_cross_package_pairs": all(x.package_id == y.package_id for x, y in pairs),
        "deterministic": pair_ids == [("1", "2"), ("2", "3")],
        "real_execution_blocked": REAL_EXECUTION_AUTHORIZED is False,
    }
    return {
        "MODE": "SYNTHETIC_CONFORMANCE_ONLY",
        "TEMPORAL_RULE_ID": TEMPORAL_RULE_ID,
        "HORIZON_DEFAULT": HORIZON_DEFAULT,
        "pass": all(tests.values()),
        "tests": tests,
        "manifest": manifest,
        "REAL_DATASET_EXECUTION": False,
        "EXECUTION_AUTHORIZATION": False,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--synthetic", action="store_true")
    parser.add_argument("--dataset", help="blocked until a later execution authorization")
    args = parser.parse_args(argv)

    if args.dataset:
        print(json.dumps({
            "MODE": "FAIL_CLOSED",
            "REAL_DATASET_EXECUTION": False,
            "EXECUTION_AUTHORIZATION": False,
            "reason": "Real dataset execution is not authorized by DR-035/DR-034.",
        }, indent=2))
        return 2

    if args.synthetic:
        print(json.dumps(synthetic_conformance(), indent=2))
        return 0 if synthetic_conformance()["pass"] else 1

    parser.error("Use --synthetic. Real dataset execution is blocked.")
    return 2


if __name__ == "__main__":
    sys.exit(main())
