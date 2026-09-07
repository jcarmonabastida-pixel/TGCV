# TGCV — Technical Execution Workflow v0.1

**Status:** ACCEPTED WORKING GOVERNANCE PATTERN
**Date:** 2026-09-07
**Purpose:** Preserve the canonical workflow used for technical/empirical executions so that execution continuity does not depend on chat context.

## 1. Source-of-truth separation

- **GitHub is the canonical continuity layer:** specifications, governance decisions, frozen definitions, executable code, execution protocols, manifests, hashes, and audit records.
- **Local environment is the execution layer:** dataset files, runtime, stdout/stderr captures, generated raw outputs, and local verification.
- Chat context is operationally useful but is **not** a source of truth.

## 2. Mandatory execution sequence

For every governed technical execution, follow this order unless a specific decision explicitly changes it:

1. **Recover canonical design from GitHub**
   - governing test/specification;
   - applicable Decision Record(s);
   - frozen definitions and information firewall;
   - authorized executable and exact version/commit;
   - frozen input/dataset and provenance requirements;
   - canonical command/protocol.

2. **Integrity preflight**
   - verify executable identity/version against the governing decision;
   - verify frozen inputs and dataset path/provenance;
   - verify configuration and runtime prerequisites;
   - identify any mismatch before execution.

3. **Execute exactly once under authorization**
   - use the authorized command;
   - do not substitute code, dataset, resolver, configuration, or analytical definition;
   - capture stdout and stderr in full;
   - do not manually edit raw execution output.

4. **Primary execution audit**
   - parse and validate the raw result;
   - verify declared counts against observed structures;
   - verify integrity/fail-closed conditions;
   - verify information-firewall flags;
   - independently check hashes where the canonicalization procedure is available;
   - distinguish evidence integrity from scientific interpretation.

5. **Replay gate**
   - replay is permitted only after the primary execution passes its integrity gate;
   - use the same frozen executable, dataset, configuration, and analytical definitions;
   - compare deterministic summary and canonical evidence hashes exactly;
   - any unexplained divergence blocks scientific closure.

6. **Final execution-result audit**
   - classify primary + replay as PASS / FAIL / INDETERMINATE;
   - record any residual provenance or verification limitation;
   - only after this gate derive the scientific consequence authorized by the governing test.

7. **Scientific closure**
   - separate computational integrity, empirical result, and ontological/theoretical interpretation;
   - do not retroactively alter the test criterion to fit the observed result;
   - record the consequence in the Decision Log and/or governing test record.

## 3. Non-negotiable rules

- Never infer execution provenance solely from chat memory.
- Never run replay before the primary integrity gate passes.
- Never treat a raw output as self-authenticating evidence of its executable, dataset, or command.
- Never silently replace a frozen input or executable.
- Never mix execution audit with scientific interpretation.
- When GitHub and local state disagree, stop and resolve the discrepancy before proceeding.
- Any substantive deviation from a frozen execution requires a new or amended governance decision.

## 4. Recovery procedure after context loss

A new chat/session must be able to recover the workflow from GitHub alone:

`governing test → Decision Record → frozen definitions → executable/version → input/dataset → exact command → primary capture → primary audit → replay → replay audit → scientific closure`

The chat is therefore a coordination surface, not a continuity dependency.

## 5. Current reference implementation

The current TR-131 real-dataset execution is the reference application of this workflow. DR-031 v0.2 authorizes one deterministic exhaustive run using `tr131_executor_v02.py`, followed by an exact deterministic replay if the primary capture passes integrity audit.
