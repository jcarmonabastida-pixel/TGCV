"""Deterministic contract tests for the comparative holdout runner."""
from __future__ import annotations

from types import SimpleNamespace
from unittest.mock import patch

import pytest

import run_c10s_nested_mr_comparative_holdout as runner
from c10s_nested_mr_fixtures import tier_a_specs


def _spec(cell_id: str):
    return next(item for item in tier_a_specs() if item.cell_id == cell_id)


def test_seed_schedule_is_stable_and_namespace_separated():
    cell = "F1_balanced_M10_R5"
    dataset = runner.derive_holdout_seed("dataset", cell, 0)
    c0 = runner.derive_holdout_seed("C0_bootstrap", cell, 0)
    c5 = runner.derive_holdout_seed("C5_bootstrap", cell, 0)
    assert dataset == runner.derive_holdout_seed("dataset", cell, 0)
    assert len({dataset, c0, c5}) == 3
    assert all(0 <= seed < 2**64 for seed in (dataset, c0, c5))


@pytest.mark.parametrize("cell_id", [
    "F1_balanced_M10_R5", "F1_low_between_M10_R5",
    "F1_high_between_M10_R5", "F5_beta22_M10_R5",
])
def test_holdout_generator_is_deterministic_and_has_frozen_shape(cell_id):
    spec = _spec(cell_id)
    first = runner.generate_holdout_dataset(spec, 7)
    second = runner.generate_holdout_dataset(spec, 7)
    assert first == second
    assert len(first) == spec.m
    assert all(len(row) == spec.r for row in first)
    if spec.family == "F5":
        assert set(value for row in first for value in row) <= {0.0, 1.0}


def test_holdout_generator_rejects_non_roster_cell():
    spec = _spec("F1_balanced_M10_R5")
    invalid = spec.__class__(
        **{**spec.__dict__, "cell_id": "F1_UNREGISTERED"}
    )
    with pytest.raises(runner.HoldoutRunnerError, match="CELL_NOT_IN_FROZEN"):
        runner.generate_holdout_dataset(invalid, 0)


def test_one_dataset_generated_once_and_compared_with_exact_roster():
    spec = _spec("F1_balanced_M10_R5")
    baseline = SimpleNamespace(method_id=runner.IMPLEMENTED_METHODS["F1"][0])
    candidate = SimpleNamespace(method_id=runner.IMPLEMENTED_METHODS["F1"][1])
    comparison = SimpleNamespace(
        dataset_id="1.0:F1_balanced_M10_R5:000000",
        input_m=spec.m, input_r=spec.r, target_m=spec.m, target_r=spec.r,
        baseline=baseline, candidates=(candidate,),
    )
    with (
        patch.object(runner, "generate_holdout_dataset", wraps=runner.generate_holdout_dataset) as gen,
        patch.object(runner, "compare_dataset", return_value=comparison) as compare,
        patch.object(runner, "adjudicate_matched_datasets", return_value=()) as adjudicate,
    ):
        result = runner.run_comparative_cell(spec, k=1, c0_b=100)
    assert gen.call_count == 1
    assert compare.call_count == 1
    kwargs = compare.call_args.kwargs
    assert kwargs["include_profile_diagnostics"] is False
    assert kwargs["baseline_bootstrap_replicates"] == 100
    assert kwargs["bootstrap_replicates"] is None
    assert kwargs["bootstrap_seed"] is None
    assert kwargs["baseline_bootstrap_seed"] == runner.derive_holdout_seed(
        "C0_bootstrap", spec.cell_id, 0
    )
    assert adjudicate.call_count == 1
    assert result["datasets_completed"] == 1
    assert result["records"][0]["truth"]["within"] == spec.true_within
    assert result["records"][0]["truth"]["between"] == spec.true_between


def test_f5_candidate_receives_separate_c5_seed_and_bootstrap_count():
    spec = _spec("F5_beta22_M10_R5")
    baseline = SimpleNamespace(method_id=runner.IMPLEMENTED_METHODS["F5"][0])
    candidate = SimpleNamespace(method_id=runner.IMPLEMENTED_METHODS["F5"][1])
    comparison = SimpleNamespace(
        dataset_id="1.0:F5_beta22_M10_R5:000000",
        input_m=spec.m, input_r=spec.r, target_m=spec.m, target_r=spec.r,
        baseline=baseline, candidates=(candidate,),
    )
    with (
        patch.object(runner, "compare_dataset", return_value=comparison) as compare,
        patch.object(runner, "adjudicate_matched_datasets", return_value=()),
    ):
        result = runner.run_comparative_cell(spec, k=1, c0_b=100, c5_b=100)
    kwargs = compare.call_args.kwargs
    assert kwargs["bootstrap_replicates"] == 100
    assert kwargs["bootstrap_seed"] == runner.derive_holdout_seed(
        "C5_bootstrap", spec.cell_id, 0
    )
    assert kwargs["baseline_bootstrap_seed"] != kwargs["bootstrap_seed"]
    assert result["records"][0]["C5_bootstrap_seed"] == kwargs["bootstrap_seed"]


def test_run_holdout_reorders_fixture_specs_to_frozen_protocol_order():
    specs = tuple(reversed(tier_a_specs()))
    with patch.object(
        runner, "run_comparative_cell",
        side_effect=lambda spec, **kwargs: {"cell": spec.cell_id, "datasets_completed": kwargs["k"]},
    ):
        result = runner.run_holdout(specs=specs, k=2)
    assert [cell["cell"] for cell in result["cells"]] == list(runner.EXPECTED_CELLS)
    assert result["total_datasets"] == 16


def test_run_holdout_rejects_missing_or_duplicate_cells():
    specs = tier_a_specs()
    with pytest.raises(runner.HoldoutRunnerError, match="DUPLICATE_CELL_SPEC"):
        runner.run_holdout(specs=specs + (specs[0],), k=1)
    with pytest.raises(runner.HoldoutRunnerError, match="EXACT_ORDERED_EIGHT"):
        runner.run_holdout(specs=specs[:-1], k=1)


def test_cli_is_fail_closed_without_authorization_wrapper():
    with patch("sys.argv", ["runner", "--output-dir", "/tmp/unused"]):
        with pytest.raises(SystemExit, match="FAIL_CLOSED"):
            runner.main()
