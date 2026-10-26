import copy
import unittest

from trajectory_selector_001 import SelectorInputError, select_trajectories


SHA_MODEL = "a" * 64
SHA_RESULT = "b" * 64


def scenario(trajectories=None, truncated=False):
    return {
        "scenario_id": "baseline",
        "disabled_transitions": [],
        "enabled_transitions_at_initial_state": ["t_ab", "t_ac"],
        "reachable_states": ["A", "B", "C", "D"],
        "trajectories": trajectories if trajectories is not None else [
            [
                {"state": "A"},
                {"transition": "t_ab", "state": "B"},
                {"transition": "t_bd", "state": "D"},
            ],
            [
                {"state": "A"},
                {"transition": "t_ac", "state": "C"},
                {"transition": "t_cd", "state": "D"},
            ],
            [
                {"state": "A"},
                {"transition": "t_ab", "state": "B"},
            ],
        ],
        "truncated": truncated,
        "exploration_bounds": {"max_depth": 20, "max_trajectories": 100},
        "temporal_prerequisites": [],
    }


def config(criteria=None, restrictions=None):
    return {
        "config_id": "test-priority",
        "version": "1",
        "criteria": criteria if criteria is not None else [
            {"id": "steps", "direction": "minimize", "source": "step_count"}
        ],
        "restrictions": restrictions if restrictions is not None else [],
    }


def select(result=None, cfg=None):
    return select_trajectories(
        result if result is not None else scenario(),
        cfg if cfg is not None else config(),
        scenario_id="baseline",
        model_sha256=SHA_MODEL,
        result_sha256=SHA_RESULT,
    )


class TrajectorySelectorTests(unittest.TestCase):
    def test_lexicographic_ranking_is_deterministic_and_prefers_shorter_path_when_configured(self):
        result = select()
        self.assertEqual(result["status"], "RANKED")
        self.assertEqual(result["output_kind"], "HEURISTIC_RANKING_NOT_PREDICTION")
        self.assertEqual(
            [item["criteria"][0]["value"] for item in result["ranked_trajectories"]],
            [1, 2, 2],
        )
        self.assertEqual(result, select())

    def test_priority_and_direction_are_explicit_and_can_change_order(self):
        data = scenario()
        prefer_ab = config(
            criteria=[
                {"id": "uses_ab", "direction": "maximize", "source": "transition_present", "transition_id": "t_ab"},
                {"id": "steps", "direction": "minimize", "source": "step_count"},
            ]
        )
        result = select(data, prefer_ab)
        self.assertTrue(result["ranked_trajectories"][0]["criteria"][0]["value"])
        self.assertEqual(result["ranked_trajectories"][0]["criteria"][0]["id"], "uses_ab")

    def test_explicit_restriction_makes_trajectory_ineligible_without_compensation(self):
        cfg = config(restrictions=[
            {"id": "must_use_ab", "source": "transition_present", "transition_id": "t_ab", "must_be_present": True}
        ])
        result = select(cfg=cfg)
        eligible = [item for item in result["ranked_trajectories"] if item["eligible"]]
        ineligible = [item for item in result["ranked_trajectories"] if not item["eligible"]]
        self.assertTrue(eligible)
        self.assertTrue(ineligible)
        self.assertTrue(all(item["status"] == "INELIGIBLE" for item in ineligible))
        self.assertTrue(all(item["restrictions"][0]["satisfied"] is False for item in ineligible))

    def test_no_admissible_trajectory_abstains(self):
        cfg = config(restrictions=[
            {"id": "must_use_missing", "source": "transition_present", "transition_id": "never", "must_be_present": True}
        ])
        result = select(cfg=cfg)
        self.assertEqual(result["status"], "ABSTAINED")
        self.assertEqual(result["reason"], "NO_ADMISSIBLE_TRAJECTORIES")

    def test_truncation_returns_partial_ranking_and_warning(self):
        result = select(scenario(truncated=True))
        self.assertEqual(result["status"], "PARTIAL_TRUNCATED")
        self.assertEqual(result["reason"], "EXPLORATION_TRUNCATED")
        self.assertTrue(any("global optimality is not established" in warning for warning in result["warnings"]))

    def test_empty_trajectory_set_abstains(self):
        result = select(scenario(trajectories=[]))
        self.assertEqual(result["status"], "ABSTAINED")
        self.assertEqual(result["reason"], "NO_TRAJECTORIES")

    def test_invalid_provenance_hash_is_rejected(self):
        with self.assertRaises(SelectorInputError):
            select_trajectories(
                scenario(), config(), scenario_id="baseline",
                model_sha256="not-a-hash", result_sha256=SHA_RESULT,
            )

    def test_scenario_mismatch_is_rejected(self):
        data = scenario()
        data["scenario_id"] = "other"
        with self.assertRaises(SelectorInputError):
            select(data)

    def test_input_is_not_mutated_and_output_is_bound_to_snapshot_and_configuration(self):
        data = scenario()
        cfg = config()
        before_data = copy.deepcopy(data)
        before_cfg = copy.deepcopy(cfg)
        first = select(data, cfg)
        cfg["criteria"][0]["direction"] = "maximize"
        second = select(data, cfg)
        self.assertEqual(data, before_data)
        self.assertNotEqual(cfg, before_cfg)
        self.assertNotEqual(first["config_sha256"], second["config_sha256"])
        self.assertNotEqual(first["input_sha256"], second["input_sha256"])

    def test_unsupported_sources_and_unknown_configuration_fields_are_rejected(self):
        with self.assertRaises(SelectorInputError):
            select(cfg=config(criteria=[{"id": "cost", "direction": "minimize", "source": "invented_cost"}]))
        invalid = config()
        invalid["weights"] = {"steps": 1}
        with self.assertRaises(SelectorInputError):
            select(cfg=invalid)


if __name__ == "__main__":
    unittest.main()
