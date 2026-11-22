#!/usr/bin/env python3
"""Run a deterministic, disjoint selection of one unittest module.

The selection is explicit and auditable. This runner does not skip tests silently:
--only requires every requested test to exist, while --exclude removes only the
named tests and reports the exact selected test IDs and a selection digest.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib
import sys
import unittest


def _flatten(suite):
    for item in suite:
        if isinstance(item, unittest.TestSuite):
            yield from _flatten(item)
        else:
            yield item


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--module", required=True)
    parser.add_argument("--selection", choices=("all", "only", "exclude"), default="all")
    parser.add_argument("--test-names", default="")
    args = parser.parse_args()

    requested = tuple(name.strip() for name in args.test_names.split(",") if name.strip())
    if len(requested) != len(set(requested)):
        parser.error("duplicate test names are not allowed")
    module = importlib.import_module(args.module)
    discovered = sorted(_flatten(unittest.defaultTestLoader.loadTestsFromModule(module)), key=lambda t: t.id())
    if not discovered:
        raise SystemExit(f"NO_TESTS_DISCOVERED:{args.module}")
    by_name = {test._testMethodName: test for test in discovered}
    unknown = sorted(set(requested) - set(by_name))
    if unknown:
        raise SystemExit(f"UNKNOWN_TEST_NAMES:{','.join(unknown)}")
    if args.selection == "only":
        if not requested:
            raise SystemExit("ONLY_SELECTION_REQUIRES_TEST_NAMES")
        selected = [by_name[name] for name in requested]
    elif args.selection == "exclude":
        selected = [test for test in discovered if test._testMethodName not in set(requested)]
    else:
        if requested:
            raise SystemExit("ALL_SELECTION_DOES_NOT_ACCEPT_TEST_NAMES")
        selected = discovered
    if not selected:
        raise SystemExit("EMPTY_TEST_SELECTION")

    ids = [test.id() for test in selected]
    digest = hashlib.sha256("\n".join(ids).encode("utf-8")).hexdigest()
    print(f"MODULE={args.module}")
    print(f"SELECTION={args.selection}")
    print(f"TEST_COUNT={len(ids)}")
    print(f"TEST_IDS_SHA256={digest}")
    for test_id in ids:
        print(f"TEST_ID={test_id}")

    suite = unittest.TestSuite(selected)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    sys.exit(main())
