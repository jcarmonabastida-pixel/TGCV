# Collective Toy — Audit-Branch CI Enablement 001

**Date:** 2026-10-13
**Branch:** `prototype/collective-toy-branch-audit-002-20261013`
**Scope:** workflow trigger configuration only; no engine/test semantics changed in this record.

## Change made

Added `prototype/collective-toy-branch-audit-002-20261013` to the existing `push.branches` list in both:

- `.github/workflows/collective-toy-engine-tests.yml`
- `.github/workflows/collective-toy-browser-tests.yml`

This is a minimal additive trigger change. It leaves the existing `pull_request` target `main` and its path filters unchanged. It does not modify `main`, change the base of PR #56, or enable scientific execution.

Workflow commits:
- Engine workflow: `c4728939f687227e7d8c7696c55c17d462019ab6`
- Browser workflow: `3c48f789bee6db0747d7989f86e180221ce9455f`

Verified workflow blob SHAs at the audit branch:
- Engine: `1767b65a828c6b9ada33d79c7f386140edfc39e0`
- Browser: `5ffee41b4e8eec96844da2a27b01f5736b407852`

## Intended validation

The engine workflow compiles the engine/tests, runs the Python unit suite, then repeats it from a clean source archive. The browser workflow runs the browser/Python concordance suite and repeats it from a clean source archive.

## Status / limitation

The files were fetched back from GitHub and the branch trigger was verified. The available commit-run lookup returns pull-request-triggered runs only, so an empty response cannot establish whether push-triggered runs started. No PASS is claimed. Next step is to inspect the actual GitHub Actions runs by branch/workflow and verify that their head SHA equals the final audit branch head; if they did not start, diagnose the trigger/permissions before any further code changes.

Scientific execution remains disabled. No merge, promotion, or changes to `main` are authorized by this change.
