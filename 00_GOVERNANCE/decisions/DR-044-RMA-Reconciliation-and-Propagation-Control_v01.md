# DR-044 — RMA Reconciliation and Propagation Control v0.1

**Date:** 2026-09-08  
**Status:** ACCEPTED — GOVERNANCE CONTROL ESTABLISHED

## Decision

Establish the current RMA as the operative master state for TGCV and require explicit impact propagation after every accepted substantive change.

## Basis

The governance reconciliation audit confirmed that the previous current RMA and STATUS had become stale relative to accepted scientific, experimental and governance state. Historical RMA versions remain immutable.

## Required propagation

For each accepted substantive change:

`Decision/Gate/Closure → Impact analysis → RMA current master → dependent current assets → STATUS → Evidence-to-Claim Matrix → consistency audit → next gate`

The propagation workflow, RMA traceability map, structural validator and conformance test are the enforcement controls.

## Boundary

This decision governs state consistency and provenance. It does not upgrade scientific evidence, prove causality, establish universality, or establish originality.

## Acceptance

The control is accepted as operative. Its conformance is separately closed by DR-045 after successful execution of the governance conformance test.
