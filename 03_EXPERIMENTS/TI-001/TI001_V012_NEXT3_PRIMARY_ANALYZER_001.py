#!/usr/bin/env python3
"""TI-001 V012 NEXT3 primary statistical analyzer.

This analyzer is specific to TI001_V012_NEXT3_PRIMARY_ANALYSIS_SPECIFICATION_002.
It does not reuse NEXT2 analysis logic, results, estimands, or model terms.

Scientific analysis is disabled unless --execute-analysis is explicitly supplied.
"""

import argparse
import hashlib
import json
import math
from pathlib import Path

SPEC_ARTIFACT = "TI001_V012_NEXT3_PRIMARY_ANALYSIS_SPECIFICATION_002"
SPEC_SHA256 = "f65737c3d24d2e4c973c0649632abf4247c9004452eed7c08225102b74a52f0f"
FIXTURE_ID = "TI001_V012_NEXT3_CANDIDATE_FIXTURE_003"
FIXTURE_VERSION = "NEXT3_v003"
UNIT_COUNT = 23040
ACTIONS = ("A", "B", "C", "D")
PROFILES = ("slot_1", "slot_2", "slot_3", "slot_4")
VALIDITY = "VALID"


def canonical(obj):
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def sha256_bytes(data):
    return hashlib.sha256(data).hexdigest()


def load_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def verify_spec(path):
    data = Path(path).read_bytes()
    observed = sha256_bytes(data)
    if observed != SPEC_SHA256:
        raise ValueError(
            f"Primary specification SHA-256 mismatch: {observed} != {SPEC_SHA256}"
        )
    spec = json.loads(data)
    if spec.get("artifact_id") != SPEC_ARTIFACT:
        raise ValueError("Unexpected primary specification artifact_id.")
    if spec.get("exploratory_only") is not True or spec.get("confirmatory") is not False:
        raise ValueError("NEXT3 analysis must remain exploratory/non-confirmatory.")
    if spec.get("no_pooling_with_NEXT2") is not True:
        raise ValueError("NEXT3 specification does not permit pooling with NEXT2.")
    return spec


def load_fixture(path):
    fixture = load_json(path)
    if fixture.get("fixture_id") != FIXTURE_ID:
        raise ValueError("Unexpected NEXT3 fixture_id.")
    if fixture.get("version") != FIXTURE_VERSION:
        raise ValueError("Unexpected NEXT3 fixture version.")
    rows = fixture.get("rows")
    if not isinstance(rows, list):
        raise ValueError("Fixture rows are missing or not a list.")
    if len(rows) != UNIT_COUNT:
        raise ValueError(f"Fixture unit count {len(rows)} != {UNIT_COUNT}.")
    by_unit = {}
    for row in rows:
        uid = row.get("unit_id")
        if not uid or uid in by_unit:
            raise ValueError("Fixture contains missing or duplicate unit_id.")
        f = row.get("f")
        if not isinstance(f, dict) or tuple(sorted(f)) != tuple(sorted(ACTIONS)):
            raise ValueError(f"Invalid f mapping for {uid}.")
        if tuple(sorted(f.values())) != tuple(sorted(PROFILES)):
            raise ValueError(f"Non-bijective f mapping for {uid}.")
        by_unit[uid] = row
    return fixture, by_unit


def extract_decisions(result):
    if not isinstance(result, dict):
        raise ValueError("Scientific execution result must be a JSON object.")
    decisions = result.get("decisions")
    if not isinstance(decisions, list):
        raise ValueError("Scientific execution result has no decisions list.")
    return decisions


def build_choice_rows(decisions, fixture_by_unit):
    rows = []
    invalid = 0
    seen_units = set()

    for decision in decisions:
        uid = decision.get("unit_id")
        validity = decision.get("validity")
        if not uid:
            raise ValueError("Decision without unit_id.")
        if uid not in fixture_by_unit:
            raise ValueError(f"Decision unit_id not found in frozen fixture: {uid}")

        if validity != VALIDITY:
            invalid += 1
            continue

        chosen_action = decision.get("parsed_action")
        if chosen_action not in ACTIONS:
            raise ValueError(
                f"VALID decision has invalid parsed_action for {uid}: {chosen_action}"
            )

        if uid in seen_units:
            raise ValueError(f"Duplicate valid decision for unit_id: {uid}")
        seen_units.add(uid)

        fixture_row = fixture_by_unit[uid]
        f = fixture_row["f"]

        for action in ACTIONS:
            rows.append(
                {
                    "unit_id": uid,
                    "action_identity": action,
                    "profile_id": f[action],
                    "chosen": int(action == chosen_action),
                    "presentation": fixture_row["presentation"],
                    "operationalisation": fixture_row["operationalisation"],
                    "domain": fixture_row["domain"],
                    "permutation_index": fixture_row["permutation_index"],
                    "replicate": fixture_row["replicate"],
                }
            )

    if rows:
        group_sizes = {}
        for row in rows:
            group_sizes[row["unit_id"]] = group_sizes.get(row["unit_id"], 0) + 1
        bad = [uid for uid, n in group_sizes.items() if n != 4]
        if bad:
            raise ValueError(f"Choice sets without exactly four alternatives: {bad[:5]}")
        for uid, n in group_sizes.items():
            chosen = sum(r["chosen"] for r in rows if r["unit_id"] == uid)
            if chosen != 1:
                raise ValueError(f"Choice set {uid} does not contain exactly one choice.")

    return rows, invalid


def fit_models(rows):
    try:
        import pandas as pd
        import statsmodels.api as sm
        from statsmodels.discrete.conditional_models import ConditionalLogit
    except ImportError as exc:
        raise RuntimeError(
            "NEXT3 primary analysis requires pandas and statsmodels."
        ) from exc

    df = pd.DataFrame(rows)

    # Reference coding is required because each categorical predictor is
    # constant-sum within a conditional-choice stratum.
    action_dummies = pd.get_dummies(
        df["action_identity"], prefix="action", dtype=float
    )
    profile_dummies = pd.get_dummies(
        df["profile_id"], prefix="profile", dtype=float
    )

    action_cols = [f"action_{x}" for x in ACTIONS[1:]]
    profile_cols = [f"profile_{x}" for x in PROFILES[1:]]

    X_restricted = action_dummies[action_cols].copy()
    X_primary = pd.concat(
        [action_dummies[action_cols], profile_dummies[profile_cols]], axis=1
    )

    restricted = ConditionalLogit(
        df["chosen"], X_restricted, groups=df["unit_id"]
    ).fit(disp=False)
    primary = ConditionalLogit(
        df["chosen"], X_primary, groups=df["unit_id"]
    ).fit(disp=False)

    llr = 2.0 * (primary.llf - restricted.llf)
    df_diff = len(primary.params) - len(restricted.params)

    try:
        from scipy.stats import chi2
        lr_p = float(chi2.sf(llr, df_diff))
    except ImportError:
        lr_p = None

    return {
        "restricted_action_identity_only": {
            "log_likelihood": float(restricted.llf),
            "aic": float(restricted.aic),
            "parameters": {k: float(v) for k, v in restricted.params.items()},
        },
        "primary_action_identity_plus_profile_id": {
            "log_likelihood": float(primary.llf),
            "aic": float(primary.aic),
            "parameters": {k: float(v) for k, v in primary.params.items()},
        },
        "profile_id_joint_likelihood_ratio_test": {
            "log_likelihood_difference": float(primary.llf - restricted.llf),
            "lr_statistic": float(llr),
            "df": int(df_diff),
            "p_value": lr_p,
        },
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--spec", required=True, type=Path)
    parser.add_argument("--fixture", required=True, type=Path)
    parser.add_argument("--result", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--execute-analysis", action="store_true")
    args = parser.parse_args()

    spec = verify_spec(args.spec)
    fixture, fixture_by_unit = load_fixture(args.fixture)
    result = load_json(args.result)

    if result.get("scientific_execution") is not True:
        raise ValueError("Input result is not marked scientific_execution=true.")

    decisions = extract_decisions(result)

    if not args.execute_analysis:
        print(json.dumps({
            "status": "ANALYZER_INPUT_VALIDATION_PASS",
            "analysis_executed": False,
            "spec_artifact": SPEC_ARTIFACT,
            "spec_sha256": SPEC_SHA256,
            "fixture_id": fixture["fixture_id"],
            "fixture_version": fixture["version"],
            "fixture_sha256": fixture.get("sha256"),
            "fixture_units": len(fixture["rows"]),
            "result_decisions": len(decisions),
            "next_action": "Re-run with --execute-analysis only after scientific analysis authorization.",
        }, sort_keys=True, indent=2))
        return

    choice_rows, invalid_count = build_choice_rows(decisions, fixture_by_unit)
    if not choice_rows:
        raise ValueError("No VALID decisions available for analysis.")

    model_result = fit_models(choice_rows)

    output = {
        "artifact_id": "TI001_V012_NEXT3_PRIMARY_ANALYSIS_RESULT_001",
        "record_type": "TGCV_TI001_V012_NEXT3_PRIMARY_ANALYSIS_RESULT",
        "analysis_specification": SPEC_ARTIFACT,
        "analysis_specification_sha256": SPEC_SHA256,
        "fixture_id": fixture["fixture_id"],
        "fixture_version": fixture["version"],
        "fixture_sha256": fixture.get("sha256"),
        "source_result_artifact": result.get("artifact_id"),
        "scientific_execution": True,
        "analysis_executed": True,
        "exploratory_only": True,
        "confirmatory": False,
        "no_pooling_with_NEXT2": True,
        "analysis_population": "validity == VALID",
        "decision_count": len(decisions),
        "invalid_decisions_excluded": invalid_count,
        "valid_choice_sets": len(choice_rows) // 4,
        "alternative_rows": len(choice_rows),
        "primary_model": (
            "Conditional choice model stratified by unit_id, with "
            "action_identity and profile_id as alternative-level predictors."
        ),
        "mapping_condition_in_primary_model": False,
        "design_factors_retained": [
            "presentation", "operationalisation", "domain",
            "permutation_index", "replicate"
        ],
        "composite_score": False,
        "value_signal": False,
        "utility_signal": False,
        "reward_signal": False,
        "performance_signal": False,
        "post_hoc_recoding": False,
        "model_result": model_result,
    }

    args.output.write_text(
        json.dumps(output, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({
        "status": "PRIMARY_ANALYSIS_COMPLETE",
        "output": str(args.output),
        "valid_choice_sets": len(choice_rows) // 4,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
