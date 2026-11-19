# C10-S calibration research branch — scope audit

**Status:** OPERATIONAL AUDIT NOTE — NON-CANONICAL  
**Date:** 2026-11-19  
**Research branch:** `research/c10s-nested-mr-calibration-design-20261119`

## Intended scope

All calibration design, comparator implementation, tests and workflow changes belong on the research branch. No production Analyzer, frozen protocol v002, Tier B authorization, C10 scientific execution, RMA or Evidence→Claim Matrix change is in scope.

## Corrective record

During creation of `c10s_gaussian_variance_oracles.py`, the initial GitHub file-creation call omitted the explicit research-branch parameter and briefly created that file on `main`.

The discrepancy was detected when the research-branch static workflow checked out its commit and could not find the module. The file was immediately copied to the intended research branch and deleted from `main`.

- Accidental add commit on main: `8d86f440622e99594fc6e9cff0ea3fb9516694a9`
- Corrective deletion commit on main: `a79e1939ea0e48064d3751d2d77c421b4dfdf59a`
- Research-branch copy commit: `cf9a327057aa5db4b82a01f41eb88b8f2413b082`
- Research-branch static validation run: `44451657996`
- Validated research code commit: `cf9a327057aa5db4b82a01f41eb88b8f2413b082`

A direct GitHub contents lookup for the module on `main` returned 404 after the corrective deletion. Thus the module is absent from the current main tree. The two main commits remain in Git history; history was not rewritten.

## Workflow debugging

The first isolated static workflow push failed before job creation because the pip command contained an unquoted YAML colon. The command was quoted. A subsequent run then failed at compile because the module had not yet been copied to the research branch. After the copy, the static workflow completed successfully:
- dependency installation: PASS;
- Python compilation: PASS;
- 7/7 oracle unit tests: PASS.

These failures were infrastructure/scope-detection failures, not numerical-method outcomes. The final successful run is the only positive validation result for the comparator code.

## Current scope conclusion

- Current `main` tree: no comparator module; no scientific or governance content changed by the final state.
- Main commit history: contains the temporary add/delete sequence above and is transparently retained.
- Research branch: contains the calibration design, F1 oracle, tests and isolated static workflow.
- No Tier B or C10 scientific execution was triggered.
