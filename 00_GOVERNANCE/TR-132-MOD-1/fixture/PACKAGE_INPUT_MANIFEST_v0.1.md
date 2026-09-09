# TR-132-MOD-1 — Immutable Package Input Manifest v0.1

**Fixture:** `MOD1-FX-001`
**Package:** `TR132-MOD1-PKG-001`
**Status:** FROZEN PRE-EXECUTION
**Execution:** NOT AUTHORIZED
**Freeze commit:** `513fe333ee0b430da3e21e721c38f393d2c66fc6`

## Purpose

Canonical integrity inventory for the exact methodological inputs of MOD-1. Hashes are Git blob SHA-1 identities and are recorded externally to the files they identify; no self-hash is embedded in the fixture manifest.

## Immutable inputs

| object | canonical path | blob_sha |
|---|---|---|
| fixture_manifest | `00_GOVERNANCE/TR-132-MOD-1/fixture/FIXTURE_MANIFEST_v0.1.md` | `1012a2d974184b5c6e88df4e94afe9a1227ddf87` |
| evidence_manifest | `00_GOVERNANCE/TR-132-MOD-1/fixture/EVIDENCE_MANIFEST_v0.1.md` | `4740549cd73dd34cbff518b2e7defb39df92970d` |
| accessibility_adjudication | `00_GOVERNANCE/TR-132-MOD-1/fixture/ACCESSIBILITY_ADJUDICATION_v0.1.csv` | `a9c2dfbcb5c5baf2df61ef3d3de331e6e3d31a53` |
| control_cases | `00_GOVERNANCE/TR-132-MOD-1/fixture/CONTROL_CASES_v0.1.csv` | `63567783c74c35b0dfd3d08a6aa29a1541f62da5` |
| realization_schedule | `00_GOVERNANCE/TR-132-MOD-1/fixture/REALIZATION_SCHEDULE_v0.1.csv` | `fc7cc4a8ab2f6951cd5a388701e1eab23ef04ec8` |
| states | `00_GOVERNANCE/TR-132-MOD-1/fixture/STATES_v0.1.csv` | `b4b10c262b9eac53e039dad10ba1777b45b5d286` |
| transformations | `00_GOVERNANCE/TR-132-MOD-1/fixture/TRANSFORMATIONS_v0.1.csv` | `182cd12d5daede2b9646df5daa58f217410b53fb` |
| schema | `00_GOVERNANCE/TR-132-MOD-1_DESIGN_AUDIT_AND_FIXTURE_SCHEMA_v0.1.md` | `8f25cf0d4a620a2ef6ac98978c40b906147d623b` |
| package_specification | `00_GOVERNANCE/TR-132-MOD-1_CONCRETE_EXECUTION_PACKAGE_SPECIFICATION_v0.1.md` | `a558f13cc3899f03a0c998d0adf6f76673dd2d02` |
| executable_protocol | `00_GOVERNANCE/TR-132_EXECUTABLE_PROTOCOL_v0.1.md` | `b1da473d750d755acf282eabad82ef065ea449c9` |

## Freeze rule

Any mutation of an input above after this manifest is frozen invalidates this package instance and requires re-instantiation and a new authorization review.

## Authorization boundary

This manifest establishes package integrity only. It does not authorize empirical execution, dataset processing, result generation or interpretation.
