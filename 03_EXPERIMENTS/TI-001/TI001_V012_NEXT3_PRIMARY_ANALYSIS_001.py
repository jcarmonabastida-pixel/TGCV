#!/usr/bin/env python3

import json
import hashlib
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import chi2
from statsmodels.discrete.conditional_models import ConditionalLogit


RESULT = Path(
    "03_EXPERIMENTS/TI-001/"
    "TI001_V012_NEXT3_EXPLORATORY_SCIENTIFIC_EXECUTION_RESULT_001.json"
)

POPULATION = Path(
    "03_EXPERIMENTS/TI-001/"
    "TI001_V012_NEXT3_ANALYSIS_POPULATION_SPECIFICATION_001.json"
)

SPECIFICATION = Path(
    "03_EXPERIMENTS/TI-001/"
    "TI001_V012_NEXT3_PRIMARY_ANALYSIS_SPECIFICATION_002.json"
)

EXPECTED_RESULT_SHA256 = (
    "b908abe936bbfd19232a1436f8a308ac5dd23ca7df418c55715520c80ec9f5de"
)

EXPECTED_POPULATION_SHA256 = (
    "dceb6065a723a37db235b3ea496e087e711f3e8bdb9d7d6731b949d2a22c04f8"
)

EXPECTED_SPECIFICATION_SHA256 = (
    "f65737c3d24d2e4c973c0649632abf4247c9004452eed7c08225102b74a52f0f"
)

FIXTURE = Path("/tmp/TI001_V012_NEXT3_CANDIDATE_FIXTURE_003.json")

EXPECTED_FIXTURE_SHA256 = (
    "0f16ebd02275ed32c481d34f92f704bb375dbe21e90d807483904ca73a9912d0"
)


def sha256_file(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def fit_primary_analysis(alternatives):
    """
    Frozen NEXT3 specification 002 statistical implementation.

    Restricted model:
        action_identity

    Primary model:
        action_identity + profile_id

    Choice set:
        unit_id

    Primary test:
        joint contribution of profile_id using a likelihood-ratio test.

    This function is defined here but is NOT called by the preflight
    execution path.
    """

    df = pd.DataFrame(alternatives)

    require(
        len(df) == 4 * df["unit_id"].nunique(),
        "Analysis table is not four-alternatives-per-choice-set",
    )

    require(
        df.groupby("unit_id")["chosen"].sum().eq(1).all(),
        "Each choice set must contain exactly one chosen alternative",
    )

    action_dummies = pd.get_dummies(
        df["action_identity"],
        prefix="action",
        drop_first=True,
        dtype=float,
    )

    profile_dummies = pd.get_dummies(
        df["profile_id"],
        prefix="profile",
        drop_first=True,
        dtype=float,
    )

    expected_action_columns = [
        "action_B",
        "action_C",
        "action_D",
    ]

    expected_profile_columns = [
        "profile_slot_2",
        "profile_slot_3",
        "profile_slot_4",
    ]

    require(
        list(action_dummies.columns) == expected_action_columns,
        "Unexpected action dummy encoding",
    )

    require(
        list(profile_dummies.columns) == expected_profile_columns,
        "Unexpected profile dummy encoding",
    )

    X_restricted = action_dummies

    X_primary = pd.concat(
        [action_dummies, profile_dummies],
        axis=1,
    )

    y = df["chosen"]
    groups = df["unit_id"]

    restricted_result = ConditionalLogit(
        y,
        X_restricted,
        groups=groups,
    ).fit(
        method="BFGS",
        maxiter=500,
        disp=False,
    )

    primary_result = ConditionalLogit(
        y,
        X_primary,
        groups=groups,
    ).fit(
        method="BFGS",
        maxiter=500,
        disp=False,
    )

    ll_restricted = float(restricted_result.llf)
    ll_primary = float(primary_result.llf)

    lr_statistic = 2.0 * (
        ll_primary - ll_restricted
    )

    degrees_of_freedom = (
        len(primary_result.params)
        - len(restricted_result.params)
    )

    require(
        degrees_of_freedom == 3,
        "Unexpected profile_id degrees of freedom",
    )

    p_value = float(
        chi2.sf(
            lr_statistic,
            degrees_of_freedom,
        )
    )

    return {
        "model_family": "conditional_logit",
        "choice_set": "unit_id",
        "restricted_model": {
            "predictors": ["action_identity"],
            "parameter_names": list(
                restricted_result.params.index
            ),
            "parameters": {
                str(k): float(v)
                for k, v in restricted_result.params.items()
            },
            "standard_errors": {
                str(k): float(v)
                for k, v in restricted_result.bse.items()
            },
            "log_likelihood": ll_restricted,
            "parameter_count": int(
                len(restricted_result.params)
            ),
        },
        "primary_model": {
            "predictors": [
                "action_identity",
                "profile_id",
            ],
            "parameter_names": list(
                primary_result.params.index
            ),
            "parameters": {
                str(k): float(v)
                for k, v in primary_result.params.items()
            },
            "standard_errors": {
                str(k): float(v)
                for k, v in primary_result.bse.items()
            },
            "log_likelihood": ll_primary,
            "parameter_count": int(
                len(primary_result.params)
            ),
        },
        "primary_test": {
            "test": "likelihood_ratio",
            "null_model": "action_identity_only",
            "alternative_model": (
                "action_identity_plus_profile_id"
            ),
            "tested_term": "profile_id",
            "lr_statistic": lr_statistic,
            "degrees_of_freedom": int(
                degrees_of_freedom
            ),
            "p_value": p_value,
        },
    }


def main():
    for path in (RESULT, POPULATION, SPECIFICATION, FIXTURE):
        require(
            path.exists(),
            f"Missing required artifact: {path}",
        )

    hashes = {
        "result": sha256_file(RESULT),
        "population": sha256_file(POPULATION),
        "specification": sha256_file(SPECIFICATION),
        "fixture": sha256_file(FIXTURE),
    }

    expected = {
        "result": EXPECTED_RESULT_SHA256,
        "population": EXPECTED_POPULATION_SHA256,
        "specification": EXPECTED_SPECIFICATION_SHA256,
        "fixture": EXPECTED_FIXTURE_SHA256,
    }

    for key in expected:
        require(
            hashes[key] == expected[key],
            f"{key} SHA-256 mismatch: "
            f"expected {expected[key]}, got {hashes[key]}",
        )

    result = json.loads(
        RESULT.read_text(encoding="utf-8")
    )

    population = json.loads(
        POPULATION.read_text(encoding="utf-8")
    )

    specification = json.loads(
        SPECIFICATION.read_text(encoding="utf-8")
    )

    fixture = json.loads(
        FIXTURE.read_text(encoding="utf-8")
    )

    require(
        result["decision_count"]
        == population["total_decisions"],
        "Decision-count mismatch",
    )

    valid = [
        d for d in result["decisions"]
        if d["validity"] == "VALID"
    ]

    invalid = [
        d for d in result["decisions"]
        if d["validity"] != "VALID"
    ]

    require(
        len(valid) == population["valid_decisions"],
        "Valid-decision count mismatch",
    )

    require(
        len(invalid)
        == (
            population["total_decisions"]
            - population["valid_decisions"]
        ),
        "Invalid-decision count mismatch",
    )

    # Frozen specification contract.
    require(
        specification["artifact_id"]
        == "TI001_V012_NEXT3_PRIMARY_ANALYSIS_SPECIFICATION_002",
        "Unexpected specification artifact",
    )

    require(
        specification["analysis_population"]
        == "validity == VALID",
        "Unexpected analysis population rule",
    )

    require(
        specification["unit_of_analysis"]
        == "alternative within decision choice set",
        "Unexpected unit of analysis",
    )

    require(
        specification["choice_set"] == "unit_id",
        "Unexpected choice-set definition",
    )

    require(
        specification["observed_outcome"] == "chosen",
        "Unexpected observed outcome",
    )

    require(
        specification["alternative_predictors"]
        == ["action_identity", "profile_id"],
        "Unexpected alternative predictors",
    )

    require(
        specification["mapping_condition"]
        ["primary_model_inclusion"]
        is False,
        "mapping_condition must not enter primary model",
    )

    require(
        specification["profile_dimension_modeling"]
        ["primary_representation"]
        == "categorical profile_id",
        "Unexpected profile representation",
    )

    require(
        specification["profile_dimension_modeling"]
        ["joint_linear_entry_of_four_dimensions"]
        is False,
        "Four profile dimensions must not enter jointly as linear predictors",
    )

    require(
        specification["exploratory_only"] is True,
        "NEXT3 primary analysis must remain exploratory",
    )

    require(
        specification["confirmatory"] is False,
        "NEXT3 primary analysis must not be confirmatory",
    )

    require(
        specification["composite_score"] is False,
        "Composite score is prohibited",
    )

    require(
        specification["value_signal"] is False,
        "Value signal is prohibited",
    )

    require(
        specification["utility_signal"] is False,
        "Utility signal is prohibited",
    )

    require(
        specification["reward_signal"] is False,
        "Reward signal is prohibited",
    )

    require(
        specification["performance_signal"] is False,
        "Performance signal is prohibited",
    )

    require(
        specification["no_pooling_with_NEXT2"] is True,
        "NEXT2 pooling is prohibited",
    )

    fixture_index = {
        row["unit_id"]: row
        for row in fixture["rows"]
    }

    require(
        fixture["fixture_id"]
        == "TI001_V012_NEXT3_CANDIDATE_FIXTURE_003",
        "Unexpected fixture artifact",
    )

    require(
        fixture["version"] == "NEXT3_v003",
        "Unexpected fixture version",
    )

    require(
        fixture["unit_count"] == 23040,
        "Unexpected fixture unit count",
    )

    require(
        len(fixture_index) == 23040,
        "Fixture unit_id uniqueness/cardinality mismatch",
    )

    # Construct the analysis-ready alternative table in memory only.
    alternatives = []

    for decision in valid:
        unit_id = decision["unit_id"]
        parsed_action = decision["parsed_action"]

        fixture_row = fixture_index.get(unit_id)

        require(
            fixture_row is not None,
            f"Missing fixture row for unit {unit_id}",
        )

        f = fixture_row["f"]

        require(
            list(f.keys()) == ["A", "B", "C", "D"],
            f"Unexpected action keys in fixture for unit {unit_id}",
        )

        require(
            sorted(f.values())
            == [
                "slot_1",
                "slot_2",
                "slot_3",
                "slot_4",
            ],
            f"Fixture f is not bijective for unit {unit_id}",
        )

        for action_identity in ["A", "B", "C", "D"]:
            alternatives.append({
                "unit_id": unit_id,
                "action_identity": action_identity,
                "profile_id": f[action_identity],
                "chosen": int(
                    parsed_action == action_identity
                ),
                "domain": decision["domain"],
                "operationalisation": (
                    decision["operationalisation"]
                ),
                "presentation": decision["presentation"],
                "permutation_index": (
                    decision["permutation_index"]
                ),
                "replicate": decision["replicate"],
            })

    require(
        len(alternatives) == 4 * len(valid),
        "Alternative cardinality mismatch",
    )

    by_unit = {}

    for row in alternatives:
        by_unit.setdefault(
            row["unit_id"],
            [],
        ).append(row)

    require(
        len(by_unit) == len(valid),
        "Choice-set cardinality mismatch",
    )

    for unit_id, rows in by_unit.items():
        require(
            len(rows) == 4,
            f"Choice set {unit_id} does not contain four alternatives",
        )

        require(
            sum(r["chosen"] for r in rows) == 1,
            f"Choice set {unit_id} does not contain exactly one chosen alternative",
        )

    print(json.dumps({
        "status": "ANALYSIS_INPUT_ADAPTER_PASS",
        "result_sha256": hashes["result"],
        "population_sha256": hashes["population"],
        "specification_sha256": hashes["specification"],
        "total_decisions": len(result["decisions"]),
        "valid_decisions": len(valid),
        "invalid_decisions": len(invalid),
        "analysis_alternatives": len(alternatives),
        "choice_sets": len(by_unit),
        "alternatives_per_choice_set": 4,
        "analysis_executed": False,
        "statistical_model_executed": False,
    }, indent=2))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
