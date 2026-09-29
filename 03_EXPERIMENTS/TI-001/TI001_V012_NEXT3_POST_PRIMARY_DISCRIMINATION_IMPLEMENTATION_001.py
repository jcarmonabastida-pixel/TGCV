#!/usr/bin/env python3
"""TI-001 V012 NEXT3 post-primary Q1-Q5 statistical implementation.

This file is a NEW implementation artifact. It does not modify, replace, or
import the closed NEXT3 primary-analysis implementation.

Statistical family:
    statsmodels.discrete.conditional_models.ConditionalLogit

Frozen execution parity target:
    NEXT3 primary implementation 001
    implementation SHA-256:
    1d29894b1ccb49c0dfce8b389fedb3a1f4d7d1bf83d5d38b5d24d5e3802ae22d

The implementation follows POST_PRIMARY_DISCRIMINATION_ANALYSIS_SPECIFICATION_002.
It is intended to be audited before scientific execution.
"""

import hashlib
from itertools import product

import numpy as np
import pandas as pd
from scipy.stats import chi2
from statsmodels.discrete.conditional_models import ConditionalLogit


SPECIFICATION_ID = (
    "TI001_V012_NEXT3_POST_PRIMARY_DISCRIMINATION_ANALYSIS_SPECIFICATION_002"
)
SPECIFICATION_SHA256 = (
    "f65737c3d24d2e4c973c0649632abf4247c9004452eed7c08225102b74a52f0f"
)
PRIMARY_IMPLEMENTATION_SHA256 = (
    "1d29894b1ccb49c0dfce8b389fedb3a1f4d7d1bf83d5d38b5d24d5e3802ae22d"
)
FIXTURE_SHA256 = (
    "0f16ebd02275ed32c481d34f92f704bb375dbe21e90d807483904ca73a9912d0"
)
EXECUTION_RESULT_SHA256 = (
    "b908abe936bbfd19232a1436f8a308ac5dd23ca7df418c55715520c80ec9f5de"
)

ACTIONS = ["A", "B", "C", "D"]
PROFILES = ["slot_1", "slot_2", "slot_3", "slot_4"]
CONDITIONS = [
    "UNINFORMATIVE_NULL",
    "INFORMATIVE",
    "SURFACE_PERMUTED",
    "CONTRADICTORY",
]
PRESENTATIONS = ["P1_order", "P2_position", "P3_orientation", "P4_format"]
DOMAINS = [
    "D1_spatial_planning", "D2_resource_planning",
    "D3_graph_reconfiguration", "D4_workflow_state_machine",
]
OPERATIONALISATIONS = [
    "O1_cardinality", "O2_topology", "O3_depth",
    "O4_constraints", "O5_composition",
]
# Canonical fixture encoding: replicate is stored as integer levels 1, 2, 3.\nREPLICATES = [1, 2, 3]
FIT_METHOD = "BFGS"
MAXITER = 500
Z95 = 1.959963984540054


def require(condition, message):
    if not condition:
        raise RuntimeError(message)



def make_dummy(values, levels, prefix):
    categorical = pd.Categorical(values, categories=levels, ordered=True)
    dummies = pd.get_dummies(
        categorical,
        prefix=prefix,
        drop_first=True,
        dtype=float,
    )
    return dummies


def interaction(left, right, left_levels, right_levels, left_prefix, right_prefix):
    cols = {}
    for l in left_levels[1:]:
        for r in right_levels[1:]:
            name = f"{left_prefix}_{l}:{right_prefix}_{r}"
            cols[name] = (
                (left == l).astype(float)
                * (right == r).astype(float)
            )
    return pd.DataFrame(cols, index=left.index)


def three_way_action_profile_condition(df):
    cols = {}
    for action in ACTIONS[1:]:
        for profile in PROFILES[1:]:
            for condition in CONDITIONS[1:]:
                name = (
                    f"action_{action}:profile_{profile}:condition_{condition}"
                )
                cols[name] = (
                    (df["action_identity"] == action).astype(float)
                    * (df["profile_id"] == profile).astype(float)
                    * (df["condition"] == condition).astype(float)
                )
    return pd.DataFrame(cols, index=df.index)


def prepare_dataframe(rows):
    df = pd.DataFrame(rows).copy()
    required = {
        "unit_id",
        "action_identity",
        "profile_id",
        "chosen",
        "condition",
        "domain",
        "operationalisation",
        "presentation",
        "replicate",
    }
    require(required.issubset(df.columns), "Missing required analysis fields")
    require(len(df) == 4 * df["unit_id"].nunique(), "Choice-set size is not four")
    require(
        df.groupby("unit_id")["chosen"].sum().eq(1).all(),
        "Each choice set must contain exactly one chosen alternative",
    )
    require(set(df["action_identity"]) == set(ACTIONS), "Unexpected action levels")
    require(set(df["profile_id"]) == set(PROFILES), "Unexpected profile levels")
    require(set(df["condition"]) == set(CONDITIONS), "Unexpected condition levels")
    return df


def fit_model(df, X, label):
    require(X.shape[0] == len(df), f"{label}: design-row mismatch")
    rank = int(np.linalg.matrix_rank(X.to_numpy(dtype=float)))
    require(rank == X.shape[1], f"{label}: rank deficient ({rank}/{X.shape[1]})")

    # Preserve the pandas DataFrame so statsmodels retains coefficient names
    # in result.params/result.bse/result.pvalues. These names are required by
    # coefficient_report() and joint_wald() for the frozen Q1-Q5 restrictions.
    result = ConditionalLogit(
        df["chosen"].to_numpy(dtype=float),
        X,
        groups=df["unit_id"].to_numpy(),
    ).fit(method=FIT_METHOD, maxiter=MAXITER, disp=False)

    return result, rank


def coefficient_report(result):
    ci = np.asarray(result.conf_int(alpha=0.05), dtype=float)
    names = list(result.params.index)
    return {
        name: {
            "estimate": float(result.params.loc[name]),
            "standard_error": float(result.bse.loc[name]),
            "ci95_low": float(ci[i, 0]),
            "ci95_high": float(ci[i, 1]),
            "raw_p_value": float(result.pvalues.loc[name]),
        }
        for i, name in enumerate(names)
    }


def joint_likelihood_ratio(reduced_result, full_result, df_difference, label):
    statistic = float(2.0 * (full_result.llf - reduced_result.llf))
    p = float(chi2.sf(statistic, df_difference))
    return {
        "test": "likelihood_ratio_chi_square",
        "label": label,
        "statistic": statistic,
        "degrees_of_freedom": int(df_difference),
        "p_value": p,
    }


def joint_wald(result, names):
    names = list(names)
    require(names, "Empty Wald restriction")
    param_names = list(result.params.index)
    R = np.zeros((len(names), len(param_names)), dtype=float)
    for i, name in enumerate(names):
        require(name in param_names, f"Missing coefficient for restriction: {name}")
        R[i, param_names.index(name)] = 1.0

    beta = np.asarray(result.params, dtype=float)
    cov = np.asarray(result.cov_params(), dtype=float)
    rb = R @ beta
    rcov = R @ cov @ R.T
    stat = float(rb.T @ np.linalg.pinv(rcov) @ rb)
    df = len(names)
    p = float(chi2.sf(stat, df))
    return {
        "test": "joint_wald_chi_square",
        "coefficients": names,
        "statistic": stat,
        "degrees_of_freedom": df,
        "p_value": p,
    }


def add_holm(results):
    ordered = sorted(range(len(results)), key=lambda i: results[i]["p_value"])
    m = len(results)
    adjusted = [None] * m
    running = 0.0
    for rank, idx in enumerate(ordered, start=1):
        value = min(1.0, (m - rank + 1) * results[idx]["p_value"])
        running = max(running, value)
        adjusted[idx] = running
    for i, item in enumerate(results):
        item["holm_adjusted_p_value"] = float(adjusted[i])
    return results


def build_common(df):
    action = make_dummy(df["action_identity"], ACTIONS, "action")
    profile = make_dummy(df["profile_id"], PROFILES, "profile")
    return action, profile


def fit_q1(df):
    action, profile = build_common(df)
    pc = interaction(
        df["profile_id"], df["condition"],
        PROFILES, CONDITIONS, "profile", "condition",
    )
    X = pd.concat([action, profile, pc], axis=1)
    result, rank = fit_model(df, X, "Q1")
    informative = [
        f"profile_{p}:condition_INFORMATIVE" for p in PROFILES[1:]
    ]
    return {
        "model": "chosen ~ action_identity + profile_id + profile_id:condition",
        "rank": rank,
        "columns": list(X.columns),
        "coefficients": coefficient_report(result),
        "primary_contrast": joint_wald(result, informative),
    }


def fit_q2(df):
    action, profile = build_common(df)
    levels = PRESENTATIONS
    require(len(levels) >= 2, "Q2 requires at least two presentation levels")
    pp = interaction(
        df["profile_id"], df["presentation"],
        PROFILES, levels, "profile", "presentation",
    )
    X = pd.concat([action, profile, pp], axis=1)
    reduced_X = pd.concat([action, profile], axis=1)
    reduced_result, reduced_rank = fit_model(df, reduced_X, "Q2_reduced")
    result, rank = fit_model(df, X, "Q2")
    return {
        "model": "chosen ~ action_identity + profile_id + profile_id:presentation_factor",
        "presentation_levels": levels,
        "rank": rank,
        "reduced_rank": reduced_rank,
        "columns": list(X.columns),
        "coefficients": coefficient_report(result),
        "primary_contrast": joint_likelihood_ratio(
            reduced_result, result, len(pp.columns),
            "profile_id:presentation interaction",
        ),
    }


def fit_q3(df):
    action, profile = build_common(df)
    pc = interaction(
        df["profile_id"], df["condition"],
        PROFILES, CONDITIONS, "profile", "condition",
    )
    X = pd.concat([action, profile, pc], axis=1)
    result, rank = fit_model(df, X, "Q3")
    contrasts = []
    for condition in CONDITIONS[1:]:
        names = [f"profile_{p}:condition_{condition}" for p in PROFILES[1:]]
        test = joint_wald(result, names)
        test["contrast"] = f"{condition} - UNINFORMATIVE_NULL"
        contrasts.append(test)
    return {
        "model": "chosen ~ action_identity + profile_id + profile_id:condition",
        "rank": rank,
        "columns": list(X.columns),
        "coefficients": coefficient_report(result),
        "primary_contrasts": contrasts,
    }


def fit_factor(df, factor, label):
    action, profile = build_common(df)
    levels = {"domain": DOMAINS, "operationalisation": OPERATIONALISATIONS, "presentation": PRESENTATIONS, "replicate": REPLICATES}[factor]
    require(len(levels) >= 2, f"{label} requires at least two factor levels")
    inter = interaction(
        df["profile_id"], df[factor],
        PROFILES, levels, "profile", factor,
    )
    X = pd.concat([action, profile, inter], axis=1)
    result, rank = fit_model(df, X, label)
    return {
        "model": f"chosen ~ action_identity + profile_id + profile_id:{factor}",
        "factor_levels": levels,
        "rank": rank,
        "columns": list(X.columns),
        "coefficients": coefficient_report(result),
        "primary_contrast": joint_wald(result, list(inter.columns)),
    }


def fit_q4(df):
    return {
        "domain": fit_factor(df, "domain", "Q4_domain"),
        "operationalisation": fit_factor(
            df, "operationalisation", "Q4_operationalisation"
        ),
        "secondary_presentation": fit_factor(
            df, "presentation", "Q4_presentation"
        ),
        "secondary_replicate": fit_factor(
            df, "replicate", "Q4_replicate"
        ),
    }


def fit_q5(df):
    action, profile = build_common(df)
    ap = pd.DataFrame({
        f"action_{a}:profile_{p}":
            ((df["action_identity"] == a).astype(float)
             * (df["profile_id"] == p).astype(float))
        for a, p in product(ACTIONS[1:], PROFILES[1:])
    }, index=df.index)
    condition = make_dummy(df["condition"], CONDITIONS, "condition")
    apc = three_way_action_profile_condition(df)
    X = pd.concat([action, profile, ap, condition, apc], axis=1)
    result, rank = fit_model(df, X, "Q5")

    informative = [
        f"action_{a}:profile_{p}:condition_INFORMATIVE"
        for a, p in product(ACTIONS[1:], PROFILES[1:])
    ]
    return {
        "model": (
            "chosen ~ action_identity + profile_id + "
            "action_identity:profile_id + condition + "
            "action_identity:profile_id:condition"
        ),
        "rank": rank,
        "columns": list(X.columns),
        "coefficients": coefficient_report(result),
        "primary_contrast": joint_wald(result, informative),
    }


def run_post_primary(rows):
    df = prepare_dataframe(rows)

    q1 = fit_q1(df)
    q2 = fit_q2(df)
    q3 = fit_q3(df)
    q4 = fit_q4(df)
    q5 = fit_q5(df)

    tests = [
        q1["primary_contrast"],
        q2["primary_contrast"],
        *q3["primary_contrasts"],
        q4["domain"]["primary_contrast"],
        q4["operationalisation"]["primary_contrast"],
        q5["primary_contrast"],
    ]
    require(len(tests) == 8, "Expected exactly eight primary inferential tests")
    add_holm(tests)

    return {
        "implementation": {
            "model_family": "conditional_logit",
            "library": "statsmodels.discrete.conditional_models.ConditionalLogit",
            "fit_method": FIT_METHOD,
            "maxiter": MAXITER,
            "primary_implementation_sha256": PRIMARY_IMPLEMENTATION_SHA256,
            "specification_id": SPECIFICATION_ID,
            "specification_sha256": SPECIFICATION_SHA256,
        },
        "Q1": q1,
        "Q2": q2,
        "Q3": q3,
        "Q4": q4,
        "Q5": q5,
        "primary_inferential_test_count": 8,
        "multiple_comparison_adjustment": "Holm",
    }


if __name__ == "__main__":
    raise SystemExit(
        "This module is an analysis implementation, not an execution command."
    )
