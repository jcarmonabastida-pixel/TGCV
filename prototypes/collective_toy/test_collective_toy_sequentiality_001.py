"""Test-first contract for temporal sequentiality in the Interactive Prototype.

These tests intentionally target a proposed, not-yet-implemented engine profile.
They must not be reported as passing until the production engine and this suite
run together on the sequentiality development branch.
"""
from __future__ import annotations

import copy
import unittest

import collective_toy_engine_001 as engine


PROFILE = {"type": "temporal_prerequisite_graph", "version": "1"}


def base_model() -> dict:
    return {
        "schema_version": "collective-toy-input-001",
        "model_id": "temporal-sequentiality-fixture-001",
        "initial_state": "A",
        "states": ["A", "B", "C", "D"],
        "transitions": [
            {"id": "t_prep", "source": "A", "target": "B"},
            {"id": "t_bypass", "source": "A", "target": "C"},
            {"id": "t_to_c", "source": "B", "target": "C"},
            {"id": "t_use", "source": "C", "target": "D"},
        ],
        "relations": [
            {
                "id": "r_use_requires_prep",
                "type": "requires_prior_execution",
                "transition_id": "t_use",
                "requires_transition_id": "t_prep",
            }
        ],
        "rule_profile": copy.deepcopy(PROFILE),
        "scenarios": [
            {"id": "baseline", "disabled_transitions": []},
            {"id": "disable_prep", "disabled_transitions": ["t_prep"]},
        ],
        "exploration": {"max_depth": 6, "max_trajectories": 100},
    }


def transition_ids(path: list[dict]) -> list[str]:
    return [step["transition"] for step in path if "transition" in step]


def path_state_ids(path: list[dict]) -> list[str]:
    return [step["state"] for step in path]


class TemporalSequentialityContractTests(unittest.TestCase):
    def test_01_valid_sequence_preserves_exact_order(self) -> None:
        result = engine.run_model(base_model())
        paths = result["scenario_results"]["baseline"]["trajectories"]
        expected = ["t_prep", "t_to_c", "t_use"]
        self.assertIn(expected, [transition_ids(path) for path in paths])
        matching = next(path for path in paths if transition_ids(path) == expected)
        self.assertEqual(["A", "B", "C", "D"], path_state_ids(matching))

    def test_02_declared_transition_does_not_satisfy_temporal_prerequisite(self) -> None:
        result = engine.run_model(base_model())
        paths = result["scenario_results"]["baseline"]["trajectories"]
        for path in paths:
            ids = transition_ids(path)
            if "t_use" in ids:
                self.assertLess(ids.index("t_prep"), ids.index("t_use"))

    def test_03_concrete_execution_rejects_unmet_prerequisite(self) -> None:
        execution = engine.execute_sequence(
            base_model(), scenario_id="baseline",
            transition_ids=["t_bypass", "t_use"],
        )
        self.assertEqual("BLOCKED", execution["status"])
        self.assertEqual(2, execution["blocked_step"]["index"])
        self.assertEqual("t_use", execution["blocked_step"]["transition_id"])
        self.assertEqual("t_prep", execution["blocked_step"]["required_transition_id"])
        self.assertEqual("temporal_prerequisite_not_satisfied", execution["blocked_step"]["reason"])

    def test_04_wrong_current_state_is_blocked_without_skipping_a_step(self) -> None:
        execution = engine.execute_sequence(
            base_model(), scenario_id="baseline",
            transition_ids=["t_prep", "t_use"],
        )
        self.assertEqual("BLOCKED", execution["status"])
        self.assertEqual(2, execution["blocked_step"]["index"])
        self.assertEqual("transition_source_mismatch", execution["blocked_step"]["reason"])
        self.assertEqual(["t_prep"], [s["transition_id"] for s in execution["steps"]])

    def test_05_intervention_does_not_mutate_baseline_configuration(self) -> None:
        model = base_model()
        before = copy.deepcopy(model)
        base_result = engine.run_model(model)
        intervention = engine.execute_sequence(
            model, scenario_id="disable_prep",
            transition_ids=["t_prep", "t_to_c", "t_use"],
        )
        self.assertEqual(before, model)
        self.assertEqual("PASS", base_result["validation"])
        self.assertEqual("BLOCKED", intervention["status"])
        self.assertEqual("transition_disabled_by_scenario", intervention["blocked_step"]["reason"])

    def test_06_possible_paths_are_not_execution_traces(self) -> None:
        model = base_model()
        exploration = engine.run_model(model)
        self.assertNotIn("execution_trace", exploration)
        execution = engine.execute_sequence(
            model, scenario_id="baseline",
            transition_ids=["t_prep", "t_to_c", "t_use"],
        )
        self.assertEqual("PASS", execution["status"])
        self.assertEqual(
            ["t_prep", "t_to_c", "t_use"],
            [step["transition_id"] for step in execution["steps"]],
        )
        self.assertEqual(["B", "C", "D"], [step["state_after"] for step in execution["steps"]])

    def test_07_execution_record_retains_configuration_snapshot(self) -> None:
        model = base_model()
        execution = engine.execute_sequence(
            model, scenario_id="baseline",
            transition_ids=["t_prep", "t_to_c", "t_use"],
        )
        snapshot = copy.deepcopy(execution["configuration"])
        model["scenarios"][0]["disabled_transitions"].append("t_prep")
        self.assertEqual(snapshot, execution["configuration"])
        self.assertEqual(PROFILE, execution["configuration"]["rule_profile"])
        self.assertEqual("baseline", execution["configuration"]["scenario_id"])

    def test_08_same_semantic_execution_is_reproducible_but_run_ids_are_distinct(self) -> None:
        model = base_model()
        first = engine.execute_sequence(
            model, scenario_id="baseline",
            transition_ids=["t_prep", "t_to_c", "t_use"],
        )
        second = engine.execute_sequence(
            model, scenario_id="baseline",
            transition_ids=["t_prep", "t_to_c", "t_use"],
        )
        self.assertNotEqual(first["execution_id"], second["execution_id"])
        self.assertEqual(first["trace_sha256"], second["trace_sha256"])
        self.assertEqual(first["configuration_sha256"], second["configuration_sha256"])

    def test_09_truncated_exploration_is_explicit(self) -> None:
        model = base_model()
        model["exploration"]["max_depth"] = 1
        result = engine.run_model(model)
        self.assertTrue(result["scenario_results"]["baseline"]["truncated"])

    def test_10_historical_profile_two_guard_semantics_remain_distinct(self) -> None:
        model = base_model()
        model["rule_profile"] = {"type": "relation_guarded_graph", "version": "1"}
        model["relations"] = [{
            "id": "r_legacy_guard",
            "type": "requires_transition_enabled",
            "transition_id": "t_use",
            "requires_transition_id": "t_prep",
        }]
        result = engine.run_model(model)
        baseline = result["scenario_results"]["baseline"]
        intervention = result["scenario_results"]["disable_prep"]
        self.assertNotIn("t_use", baseline["effective_disabled_transitions"])
        self.assertIn("t_use", intervention["effective_disabled_transitions"])

    def test_12_multiple_temporal_prerequisites_must_all_have_occurred(self) -> None:
        model = base_model()
        model["transitions"].append({"id": "t_return", "source": "B", "target": "A"})
        model["relations"].append({
            "id": "r_use_requires_bypass",
            "type": "requires_prior_execution",
            "transition_id": "t_use",
            "requires_transition_id": "t_bypass",
        })
        execution = engine.execute_sequence(
            model, scenario_id="baseline",
            transition_ids=["t_prep", "t_return", "t_to_c", "t_use"],
        )
        self.assertEqual("BLOCKED", execution["status"])
        self.assertEqual("temporal_prerequisite_not_satisfied", execution["blocked_step"]["reason"])
        self.assertEqual("t_bypass", execution["blocked_step"]["required_transition_id"])

        valid = engine.execute_sequence(
            model, scenario_id="baseline",
            transition_ids=["t_prep", "t_return", "t_bypass", "t_use"],
        )
        self.assertEqual("PASS", valid["status"])

    def test_13_prerequisite_history_survives_a_cycle_in_the_same_sequence(self) -> None:
        model = base_model()
        model["transitions"].append({"id": "t_return", "source": "B", "target": "A"})
        execution = engine.execute_sequence(
            model, scenario_id="baseline",
            transition_ids=["t_prep", "t_return", "t_prep", "t_to_c", "t_use"],
        )
        self.assertEqual("PASS", execution["status"])
        self.assertEqual("D", execution["final_state"])
        self.assertEqual(
            ["t_prep", "t_return", "t_prep", "t_to_c", "t_use"],
            [step["transition_id"] for step in execution["steps"]],
        )

    def test_14_unknown_transition_blocks_at_exact_position(self) -> None:
        execution = engine.execute_sequence(
            base_model(), scenario_id="baseline",
            transition_ids=["t_prep", "t_missing", "t_to_c"],
        )
        self.assertEqual("BLOCKED", execution["status"])
        self.assertEqual(2, execution["blocked_step"]["index"])
        self.assertEqual("t_missing", execution["blocked_step"]["transition_id"])
        self.assertEqual("unknown_transition", execution["blocked_step"]["reason"])
        self.assertEqual(["t_prep"], [step["transition_id"] for step in execution["steps"]])
        self.assertEqual("B", execution["final_state"])

    def test_11_unknown_rule_profile_fails_closed(self) -> None:
        model = base_model()
        model["rule_profile"] = {"type": "temporal_prerequisite_graph", "version": "999"}
        with self.assertRaises(engine.ModelValidationError):
            engine.run_model(model)


if __name__ == "__main__":
    unittest.main()
