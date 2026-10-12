import copy
import unittest

from collective_toy_engine_001 import (
    ModelValidationError,
    assess_exported_package,
    assess_exported_package_integrity,
    demo_model,
    export_run,
    run_model,
    canonical_json,
    sha256_json,
    verify_exported_package,
    verify_exported_package_integrity,
)


class CollectiveToyEngineTests(unittest.TestCase):
    def setUp(self):
        self.model = demo_model()

    def test_diamond_fixture_matches_expected_reachability_and_paths(self):
        result = run_model(self.model)
        base = result["scenario_results"]["baseline"]
        intervention = result["scenario_results"]["block_ac"]
        self.assertEqual(base["reachable_states"], ["A", "B", "C", "D"])
        self.assertEqual(intervention["reachable_states"], ["A", "B", "D"])
        base_paths = {
            tuple(item.get("state") for item in path)
            for path in base["trajectories"]
            if path[-1].get("state") == "D"
        }
        intervention_paths = {
            tuple(item.get("state") for item in path)
            for path in intervention["trajectories"]
            if path[-1].get("state") == "D"
        }
        self.assertEqual(base_paths, {("A", "B", "D"), ("A", "C", "D")})
        self.assertEqual(intervention_paths, {("A", "B", "D")})
        self.assertFalse(base["truncated"])
        self.assertFalse(intervention["truncated"])

    def test_initial_state_must_be_a_string_id_and_malformed_containers_raise_validation_error(self):
        for invalid_initial_state in ([], {}, None, 1):
            with self.subTest(initial_state=invalid_initial_state):
                model = copy.deepcopy(self.model)
                model["initial_state"] = invalid_initial_state
                with self.assertRaises(ModelValidationError):
                    run_model(model)

    def test_unknown_state_reference_fails(self):
        model = copy.deepcopy(self.model)
        model["transitions"][0]["target"] = "UNKNOWN"
        with self.assertRaisesRegex(ModelValidationError, "transition t_ab references an unknown state"):
            run_model(model)

    def test_duplicate_semantic_relation_is_operationally_idempotent(self):
        model = copy.deepcopy(self.model)
        model["rule_profile"] = {"type": "relation_guarded_graph", "version": "1"}
        relation = {
            "id": "r_guard_bd_by_ab",
            "type": "requires_transition_enabled",
            "transition_id": "t_bd",
            "requires_transition_id": "t_ab",
        }
        model["relations"] = [relation]
        duplicate = copy.deepcopy(model)
        duplicate["relations"].append({
            **relation,
            "id": "r_guard_bd_by_ab_duplicate",
        })

        original = run_model(model)
        repeated = run_model(duplicate)
        for scenario_id in original["scenario_results"]:
            for key in ("reachable_states", "trajectories", "effective_disabled_transitions"):
                self.assertEqual(
                    original["scenario_results"][scenario_id][key],
                    repeated["scenario_results"][scenario_id][key],
                    f"duplicate semantic relation changed {key} in {scenario_id}",
                )
        self.assertNotEqual(original["input_sha256"], repeated["input_sha256"])

    def test_duplicate_transition_id_fails(self):
        model = copy.deepcopy(self.model)
        model["transitions"].append(dict(model["transitions"][0]))
        with self.assertRaises(ModelValidationError):
            run_model(model)

    def test_disabling_transitions_cannot_expand_reachability_or_trajectories(self):
        result = run_model(self.model)
        baseline = result["scenario_results"]["baseline"]
        intervention = result["scenario_results"]["block_ac"]

        self.assertLessEqual(
            set(intervention["reachable_states"]),
            set(baseline["reachable_states"]),
        )
        baseline_trajectories = {canonical_json(path) for path in baseline["trajectories"]}
        intervention_trajectories = {canonical_json(path) for path in intervention["trajectories"]}
        self.assertLessEqual(intervention_trajectories, baseline_trajectories)

    def test_disabling_unreachable_transition_does_not_change_intervened_scenario(self):
        model = copy.deepcopy(self.model)
        model["scenarios"].append({
            "id": "block_ac_and_cd",
            "disabled_transitions": ["t_ac", "t_cd"],
        })
        result = run_model(model)
        self.assertEqual(
            result["scenario_results"]["block_ac"]["reachable_states"],
            result["scenario_results"]["block_ac_and_cd"]["reachable_states"],
        )
        self.assertEqual(
            result["scenario_results"]["block_ac"]["trajectories"],
            result["scenario_results"]["block_ac_and_cd"]["trajectories"],
        )
        self.assertEqual(
            result["scenario_results"]["block_ac"]["enabled_transitions_at_initial_state"],
            result["scenario_results"]["block_ac_and_cd"]["enabled_transitions_at_initial_state"],
        )

    def test_intervention_does_not_change_unrelated_transition(self):
        result = run_model(self.model)
        base = result["scenario_results"]["baseline"]
        intervention = result["scenario_results"]["block_ac"]
        self.assertIn("t_ab", base["enabled_transitions_at_initial_state"])
        self.assertIn("t_ab", intervention["enabled_transitions_at_initial_state"])
        self.assertNotIn("t_ac", intervention["enabled_transitions_at_initial_state"])
        self.assertEqual(
            result["comparisons_to_baseline"]["block_ac"]["enabled_at_initial_removed"],
            ["t_ac"],
        )

    def test_cycle_terminates_and_marks_depth_truncation(self):
        model = copy.deepcopy(self.model)
        model["transitions"].append({"id": "t_ba", "source": "B", "target": "A"})
        model["exploration"]["max_depth"] = 3
        result = run_model(model)
        self.assertEqual(set(result["scenario_results"]["baseline"]["reachable_states"]), {"A", "B", "C", "D"})
        self.assertTrue(result["scenario_results"]["baseline"]["truncated"])

    def test_trajectory_limit_is_explicit(self):
        model = copy.deepcopy(self.model)
        model["exploration"]["max_trajectories"] = 1
        result = run_model(model)
        self.assertTrue(result["scenario_results"]["baseline"]["truncated"])

    def test_depth_boundary_distinguishes_pending_transition_from_terminal_path(self):
        model = copy.deepcopy(self.model)
        model["states"] = ["A", "B", "C"]
        model["initial_state"] = "A"
        model["transitions"] = [
            {"id": "t_ab", "source": "A", "target": "B"},
            {"id": "t_bc", "source": "B", "target": "C"},
        ]
        model["scenarios"] = [{"id": "baseline", "disabled_transitions": []}]
        model["exploration"] = {"max_depth": 1, "max_trajectories": 10}
        at_one = run_model(model)["scenario_results"]["baseline"]
        self.assertTrue(at_one["truncated"])
        self.assertEqual(at_one["reachable_states"], ["A", "B", "C"])
        model["exploration"]["max_depth"] = 2
        at_two = run_model(model)["scenario_results"]["baseline"]
        self.assertFalse(at_two["truncated"])
        self.assertEqual(at_two["reachable_states"], ["A", "B", "C"])
        self.assertEqual(len(at_two["trajectories"]), 1)

    def test_exact_trajectory_cap_does_not_mark_complete_enumeration_truncated(self):
        model = copy.deepcopy(self.model)
        model["states"] = ["A", "B"]
        model["initial_state"] = "A"
        model["transitions"] = [{"id": "t_ab", "source": "A", "target": "B"}]
        model["scenarios"] = [{"id": "baseline", "disabled_transitions": []}]
        model["exploration"] = {"max_depth": 4, "max_trajectories": 1}
        result = run_model(model)
        baseline = result["scenario_results"]["baseline"]
        self.assertEqual(baseline["trajectories"], [[{"state": "A"}, {"transition": "t_ab", "state": "B"}]])
        self.assertFalse(baseline["truncated"])

    def test_terminal_path_at_depth_boundary_is_not_truncated(self):
        model = copy.deepcopy(self.model)
        model["states"] = ["A", "B"]
        model["initial_state"] = "A"
        model["transitions"] = [{"id": "t_ab", "source": "A", "target": "B"}]
        model["scenarios"] = [{"id": "baseline", "disabled_transitions": []}]
        model["exploration"] = {"max_depth": 1, "max_trajectories": 10}
        result = run_model(model)
        baseline = result["scenario_results"]["baseline"]
        self.assertEqual(len(baseline["trajectories"]), 1)
        self.assertFalse(baseline["truncated"])

    def test_depth_and_trajectory_caps_interact_without_false_complete_result(self):
        model = copy.deepcopy(self.model)
        model["states"] = ["A", "B", "C", "D", "E"]
        model["initial_state"] = "A"
        model["transitions"] = [
            {"id": "t_ab", "source": "A", "target": "B"},
            {"id": "t_bd", "source": "B", "target": "D"},
            {"id": "t_ac", "source": "A", "target": "C"},
            {"id": "t_ce", "source": "C", "target": "E"},
        ]
        model["scenarios"] = [{"id": "baseline", "disabled_transitions": []}]
        model["exploration"] = {"max_depth": 1, "max_trajectories": 1}
        both_caps = run_model(model)["scenario_results"]["baseline"]
        self.assertTrue(both_caps["truncated"])
        self.assertEqual(len(both_caps["trajectories"]), 1)

        model["exploration"] = {"max_depth": 2, "max_trajectories": 1}
        trajectory_cap_only = run_model(model)["scenario_results"]["baseline"]
        self.assertTrue(trajectory_cap_only["truncated"])
        self.assertEqual(len(trajectory_cap_only["trajectories"]), 1)

        model["exploration"] = {"max_depth": 2, "max_trajectories": 2}
        neither_cap = run_model(model)["scenario_results"]["baseline"]
        self.assertFalse(neither_cap["truncated"])
        self.assertEqual(len(neither_cap["trajectories"]), 2)

    def test_current_baseline_package_fixture_is_canonical_and_replay_verified(self):
        from pathlib import Path
        import hashlib
        import json

        fixture_path = Path(__file__).with_name("fixtures") / "current_baseline_package_001.json"
        raw = fixture_path.read_bytes()
        package = json.loads(raw.decode("utf-8"))
        self.assertEqual(raw.decode("utf-8"), canonical_json(package))
        self.assertEqual(package["package_version"], "collective-toy-run-package-001")
        self.assertEqual(package["engine_version"], "collective-toy-engine-001")
        self.assertEqual(sha256_json(package["input"]), package["result"]["input_sha256"])
        self.assertEqual(package["package_sha256"], "4f56aa1618d9a9aadbb68ee5f456950dfaf4898c94bbf7672be3d9d0bba9c9b8")
        self.assertEqual(package["result"]["result_sha256"], "bb937763a3e8bd3e5aa9ae4b461f10ae2d6b655f17a9f735f5ae8f930ad93a84")
        self.assertEqual(hashlib.sha256(raw).hexdigest(), "cda406ad711caef3e0d6fb87a429bf329ae99ca35254747166c5b6c61056ab19")
        self.assertEqual(assess_exported_package(package)["status"], "replay-verified")
        self.assertEqual(package["result"]["scenario_results"]["baseline"]["reachable_states"], ["A", "B", "C", "D"])
        self.assertEqual(package["result"]["scenario_results"]["block_ac"]["reachable_states"], ["A", "B", "D"])

    def test_deterministic_result_hash(self):
        first = run_model(self.model)
        second = run_model(self.model)
        self.assertEqual(first["result_sha256"], second["result_sha256"])
        self.assertEqual(first["input_sha256"], second["input_sha256"])

    def test_object_key_insertion_order_does_not_change_hashes_or_semantics(self):
        model = copy.deepcopy(self.model)

        def reverse_object_key_order(value):
            if isinstance(value, dict):
                return {
                    key: reverse_object_key_order(value[key])
                    for key in reversed(list(value.keys()))
                }
            if isinstance(value, list):
                return [reverse_object_key_order(item) for item in value]
            return value

        permuted = reverse_object_key_order(model)
        self.assertEqual(canonical_json(model), canonical_json(permuted))
        original = run_model(model)
        reordered = run_model(permuted)
        self.assertEqual(original["input_sha256"], reordered["input_sha256"])
        self.assertEqual(original["result_sha256"], reordered["result_sha256"])
        self.assertEqual(original["scenario_results"], reordered["scenario_results"])
        self.assertEqual(original["comparisons_to_baseline"], reordered["comparisons_to_baseline"])

    def test_canonical_json_normalizes_integral_floats_and_codepoint_sorts_unicode_keys(self):
        value = {"n": 1.0, "negative_zero": -0.0, "\U00010000": "supplementary", "\uE000": "bmp"}
        self.assertEqual(
            canonical_json(value),
            '{"n":1,"negative_zero":0,"\uE000":"bmp","𐀀":"supplementary"}',
        )
        self.assertEqual(sha256_json({"n": 1.0}), sha256_json({"n": 1}))

    def test_canonical_json_rejects_non_integer_and_unsafe_numbers(self):
        for value in ({"n": 1.5}, {"n": float("nan")}, {"n": 9_007_199_254_740_992}):
            with self.subTest(value=value):
                with self.assertRaises(ModelValidationError):
                    canonical_json(value)

    def test_canonical_json_rejects_unpaired_surrogates(self):
        with self.assertRaises(ModelValidationError):
            canonical_json({"label": "\ud800"})

    def test_export_package_detects_tampering_of_input_result_and_package(self):
        package = export_run(self.model)

        altered_input = copy.deepcopy(package)
        altered_input["input"]["transitions"][0]["target"] = "__tampered_target__"
        self.assertNotEqual(
            sha256_json(altered_input["input"]),
            altered_input["result"]["input_sha256"],
        )
        altered_input_payload = copy.deepcopy(altered_input)
        del altered_input_payload["package_sha256"]
        self.assertNotEqual(
            sha256_json(altered_input_payload),
            altered_input["package_sha256"],
        )

        altered_result = copy.deepcopy(package)
        altered_result["result"]["scenario_results"] = {}
        altered_result_payload = copy.deepcopy(altered_result["result"])
        del altered_result_payload["input_sha256"]
        del altered_result_payload["result_sha256"]
        self.assertNotEqual(
            sha256_json(altered_result_payload),
            altered_result["result"]["result_sha256"],
        )

        altered_package_metadata = copy.deepcopy(package)
        altered_package_metadata["package_version"] = "tampered-version"
        altered_package_payload = copy.deepcopy(altered_package_metadata)
        del altered_package_payload["package_sha256"]
        self.assertNotEqual(
            sha256_json(altered_package_payload),
            altered_package_metadata["package_sha256"],
        )

    def test_exported_package_rejects_truncated_or_incomplete_documents(self):
        package = export_run(self.model)
        self.assertTrue(verify_exported_package(package))

        for field in ("package_version", "engine_version", "input", "result", "package_sha256"):
            with self.subTest(missing_top_level=field):
                incomplete = copy.deepcopy(package)
                del incomplete[field]
                with self.assertRaises(ModelValidationError):
                    verify_exported_package(incomplete)

        incomplete_result = copy.deepcopy(package)
        del incomplete_result["result"]["result_sha256"]
        incomplete_result_payload = copy.deepcopy(incomplete_result)
        del incomplete_result_payload["package_sha256"]
        incomplete_result["package_sha256"] = sha256_json(incomplete_result_payload)
        with self.assertRaises(ModelValidationError):
            verify_exported_package(incomplete_result)

        incomplete_input = copy.deepcopy(package)
        del incomplete_input["input"]["transitions"]
        incomplete_input_payload = copy.deepcopy(incomplete_input)
        del incomplete_input_payload["package_sha256"]
        incomplete_input["package_sha256"] = sha256_json(incomplete_input_payload)
        with self.assertRaises(ModelValidationError):
            verify_exported_package(incomplete_input)

    def test_exported_package_rejects_unsupported_package_version_even_with_recomputed_hash(self):
        package = export_run(self.model)
        package["package_version"] = "collective-toy-run-package-999"
        package_payload = copy.deepcopy(package)
        del package_payload["package_sha256"]
        package["package_sha256"] = sha256_json(package_payload)
        with self.assertRaises(ModelValidationError):
            verify_exported_package(package)

        wrong_engine = export_run(self.model)
        wrong_engine["engine_version"] = "collective-toy-engine-999"
        engine_payload = copy.deepcopy(wrong_engine)
        del engine_payload["package_sha256"]
        wrong_engine["package_sha256"] = sha256_json(engine_payload)
        with self.assertRaises(ModelValidationError):
            verify_exported_package(wrong_engine)

    def test_unknown_engine_can_be_integrity_verified_but_not_replayed(self):
        package = export_run(self.model)
        package["engine_version"] = "collective-toy-engine-999"
        payload = copy.deepcopy(package)
        del payload["package_sha256"]
        package["package_sha256"] = sha256_json(payload)

        # Known package format and all hashes are valid; this says nothing about replay.
        self.assertTrue(verify_exported_package_integrity(package))
        with self.assertRaisesRegex(ModelValidationError, "Unsupported exported package engine version"):
            verify_exported_package(package)

    def test_integrity_only_assessment_does_not_claim_replay(self):
        package = export_run(self.model)
        self.assertEqual(
            assess_exported_package_integrity(package),
            {
                "status": "integrity-verified",
                "integrity_verified": True,
                "replay_verified": False,
                "reason": None,
            },
        )

    def test_package_assessment_reports_inspect_only_when_engine_is_unavailable(self):
        package = export_run(self.model)
        package["engine_version"] = "collective-toy-engine-999"
        payload = copy.deepcopy(package)
        del payload["package_sha256"]
        package["package_sha256"] = sha256_json(payload)

        self.assertEqual(
            assess_exported_package(package),
            {
                "status": "inspect-only/replay-unavailable",
                "integrity_verified": True,
                "replay_verified": False,
                "reason": "Unsupported exported package engine version",
            },
        )

    def test_package_assessment_reports_replay_verified_for_current_engine(self):
        package = export_run(self.model)
        self.assertEqual(
            assess_exported_package(package),
            {
                "status": "replay-verified",
                "integrity_verified": True,
                "replay_verified": True,
                "reason": None,
            },
        )

    def test_integrity_verification_rejects_tampering_even_for_unknown_engine(self):
        package = export_run(self.model)
        package["engine_version"] = "collective-toy-engine-999"
        package["result"]["model_id"] = "tampered-result"
        payload = copy.deepcopy(package)
        del payload["package_sha256"]
        package["package_sha256"] = sha256_json(payload)

        with self.assertRaisesRegex(ModelValidationError, "Exported result SHA-256 does not verify"):
            verify_exported_package_integrity(package)

    def test_integrity_verification_rejects_unknown_package_format_even_with_recomputed_hash(self):
        package = export_run(self.model)
        package["package_version"] = "collective-toy-run-package-999"
        payload = copy.deepcopy(package)
        del payload["package_sha256"]
        package["package_sha256"] = sha256_json(payload)

        with self.assertRaisesRegex(ModelValidationError, "Unsupported exported package version"):
            verify_exported_package_integrity(package)

    def test_integrity_rejects_missing_or_malformed_engine_version_even_with_recomputed_package_hash(self):
        for invalid_version in ("missing", None, "", 17):
            with self.subTest(engine_version=invalid_version):
                package = export_run(self.model)
                if invalid_version == "missing":
                    del package["engine_version"]
                else:
                    package["engine_version"] = invalid_version
                payload = copy.deepcopy(package)
                del payload["package_sha256"]
                package["package_sha256"] = sha256_json(payload)
                with self.assertRaises(ModelValidationError):
                    verify_exported_package_integrity(package)

    def test_valid_hashes_do_not_make_divergent_result_replay_verified(self):
        package = export_run(self.model)
        package["result"]["scenario_results"]["baseline"]["reachable_states"].append(
            "FORGED_STATE_NOT_IN_MODEL"
        )
        result_payload = copy.deepcopy(package["result"])
        del result_payload["input_sha256"]
        del result_payload["result_sha256"]
        package["result"]["result_sha256"] = sha256_json(result_payload)
        package_payload = copy.deepcopy(package)
        del package_payload["package_sha256"]
        package["package_sha256"] = sha256_json(package_payload)

        # The package, input, and result hashes are internally consistent.
        self.assertTrue(verify_exported_package_integrity(package))
        with self.assertRaisesRegex(ModelValidationError, "does not match independent replay"):
            assess_exported_package(package)

    def test_export_contains_reproduction_inputs_and_hashes(self):
        package = export_run(self.model)
        self.assertEqual(package["input"], self.model)
        self.assertIn("result_sha256", package["result"])
        self.assertIn("package_sha256", package)

    def test_export_package_hashes_verify_and_export_replays_independently(self):
        package = export_run(self.model)

        package_payload = copy.deepcopy(package)
        del package_payload["package_sha256"]
        self.assertEqual(sha256_json(package_payload), package["package_sha256"])

        self.assertEqual(sha256_json(package["input"]), package["result"]["input_sha256"])
        result_payload = copy.deepcopy(package["result"])
        del result_payload["input_sha256"]
        del result_payload["result_sha256"]
        self.assertEqual(sha256_json(result_payload), package["result"]["result_sha256"])

        replayed = run_model(package["input"])
        self.assertEqual(replayed, package["result"])

        tampered = copy.deepcopy(package)
        tampered["input"]["transitions"][0]["target"] = "D"
        tampered_payload = copy.deepcopy(tampered)
        del tampered_payload["package_sha256"]
        self.assertNotEqual(sha256_json(tampered_payload), tampered["package_sha256"])
        self.assertNotEqual(sha256_json(tampered["input"]), tampered["result"]["input_sha256"])

    def test_schema_type_and_required_field_validation_matrix(self):
        cases = []

        model = copy.deepcopy(self.model)
        model["schema_version"] = "unsupported"
        cases.append(("schema-version", model))

        model = copy.deepcopy(self.model)
        model["model_id"] = "   "
        cases.append(("blank-model-id", model))

        model = copy.deepcopy(self.model)
        model.pop("initial_state")
        cases.append(("missing-initial-state", model))

        model = copy.deepcopy(self.model)
        model["transitions"] = [None]
        cases.append(("non-object-transition", model))

        model = copy.deepcopy(self.model)
        model["scenarios"] = [None]
        cases.append(("non-object-scenario", model))

        model = copy.deepcopy(self.model)
        model["scenarios"].append({"id": "baseline", "disabled_transitions": []})
        cases.append(("duplicate-scenario-id", model))

        model = copy.deepcopy(self.model)
        model["scenarios"][1]["disabled_transitions"] = "t_ac"
        cases.append(("disabled-transitions-not-list", model))

        model = copy.deepcopy(self.model)
        model["exploration"] = []
        cases.append(("exploration-not-object", model))

        model = copy.deepcopy(self.model)
        model["exploration"]["max_depth"] = True
        cases.append(("boolean-depth", model))

        model = copy.deepcopy(self.model)
        model["exploration"]["max_trajectories"] = 0
        cases.append(("zero-trajectory-cap", model))

        model = copy.deepcopy(self.model)
        model["exploration"]["max_depth"] = 101
        cases.append(("depth-over-resource-cap", model))

        model = copy.deepcopy(self.model)
        model["exploration"]["max_trajectories"] = 10001
        cases.append(("trajectory-cap-over-resource-limit", model))

        model = copy.deepcopy(self.model)
        model["states"] = ["S" + str(i) for i in range(501)]
        model["initial_state"] = "S0"
        model["transitions"] = []
        cases.append(("state-count-over-resource-cap", model))

        model = copy.deepcopy(self.model)
        model["transitions"] = [
            {"id": "t" + str(i), "source": "A", "target": "A"} for i in range(2001)
        ]
        cases.append(("transition-count-over-resource-cap", model))

        model = copy.deepcopy(self.model)
        model["unexpected_top_level"] = True
        cases.append(("unknown-top-level-field", model))

        model = copy.deepcopy(self.model)
        model["transitions"][0]["unexpected"] = True
        cases.append(("unknown-transition-field", model))

        model = copy.deepcopy(self.model)
        model["scenarios"][0]["unexpected"] = True
        cases.append(("unknown-scenario-field", model))

        model = copy.deepcopy(self.model)
        model["exploration"]["unexpected"] = True
        cases.append(("unknown-exploration-field", model))

        model = copy.deepcopy(self.model)
        model["rule_profile"]["unexpected"] = True
        cases.append(("unknown-rule-profile-field", model))

        # Systematic missing-required-field and wrong-container-type cases.
        for field in ("schema_version", "model_id", "states", "transitions",
                      "rule_profile", "scenarios", "exploration"):
            model = copy.deepcopy(self.model)
            model.pop(field)
            cases.append(("missing-required-" + field, model))

        model = copy.deepcopy(self.model)
        model["states"] = "A"
        cases.append(("states-not-list", model))

        model = copy.deepcopy(self.model)
        model["transitions"] = {}
        cases.append(("transitions-not-list", model))

        model = copy.deepcopy(self.model)
        model["rule_profile"] = None
        cases.append(("rule-profile-not-object", model))

        model = copy.deepcopy(self.model)
        model["relations"] = {}
        cases.append(("relations-not-list", model))

        model = copy.deepcopy(self.model)
        model["scenarios"][0]["disabled_transitions"] = ["t_ab", "t_ab"]
        cases.append(("duplicate-disabled-transition", model))

        # Nested-field presence, non-empty identifiers, and numeric type boundaries.
        for field in ("id", "source", "target"):
            model = copy.deepcopy(self.model)
            model["transitions"][0].pop(field)
            cases.append(("missing-transition-" + field, model))

        for field in ("id", "source", "target"):
            model = copy.deepcopy(self.model)
            model["transitions"][0][field] = ""
            cases.append(("empty-transition-" + field, model))

        model = copy.deepcopy(self.model)
        model["exploration"]["max_depth"] = 1.5
        cases.append(("fractional-max-depth", model))

        model = copy.deepcopy(self.model)
        model["exploration"]["max_trajectories"] = True
        cases.append(("boolean-max-trajectories", model))

        model = copy.deepcopy(self.model)
        model["rule_profile"] = {"type": "unknown_graph", "version": "1"}
        cases.append(("unknown-rule-profile-type", model))

        model = copy.deepcopy(self.model)
        model["scenarios"][0]["disabled_transitions"] = [""]
        cases.append(("empty-disabled-transition-id", model))

        # Nested relation/scenario/exploration field coverage (profile 2 where applicable).
        valid_relation = {
            "id": "r_schema", "type": "requires_transition_enabled",
            "transition_id": "t_bd", "requires_transition_id": "t_ab"
        }
        for field in ("id", "type", "transition_id", "requires_transition_id"):
            model = copy.deepcopy(self.model)
            model["rule_profile"] = {"type": "relation_guarded_graph", "version": "1"}
            relation = copy.deepcopy(valid_relation)
            relation.pop(field)
            model["relations"] = [relation]
            cases.append(("missing-relation-" + field, model))

        for field in ("id", "transition_id", "requires_transition_id"):
            model = copy.deepcopy(self.model)
            model["rule_profile"] = {"type": "relation_guarded_graph", "version": "1"}
            relation = copy.deepcopy(valid_relation)
            relation[field] = ""
            model["relations"] = [relation]
            cases.append(("empty-relation-" + field, model))

        model = copy.deepcopy(self.model)
        model["rule_profile"] = {"type": "relation_guarded_graph", "version": "1"}
        model["relations"] = [None]
        cases.append(("non-object-relation", model))

        model = copy.deepcopy(self.model)
        model["rule_profile"] = {"type": "relation_guarded_graph", "version": "1"}
        relation = copy.deepcopy(valid_relation)
        relation["unexpected"] = True
        model["relations"] = [relation]
        cases.append(("unknown-relation-field", model))

        model = copy.deepcopy(self.model)
        model["scenarios"][0].pop("id")
        cases.append(("missing-scenario-id", model))

        model = copy.deepcopy(self.model)
        model["scenarios"][0]["id"] = ""
        cases.append(("empty-scenario-id", model))

        model = copy.deepcopy(self.model)
        model["scenarios"][0]["disabled_transitions"] = [1]
        cases.append(("non-string-disabled-transition-id", model))

        for field in ("max_depth", "max_trajectories"):
            model = copy.deepcopy(self.model)
            model["exploration"].pop(field)
            cases.append(("missing-exploration-" + field, model))

        for name, candidate in cases:
            with self.subTest(name=name):
                with self.assertRaises(ModelValidationError):
                    run_model(candidate)

    def test_relation_guard_cannot_reference_itself(self):
        model = copy.deepcopy(self.model)
        model["rule_profile"] = {"type": "relation_guarded_graph", "version": "1"}
        model["relations"] = [{
            "id": "r_self",
            "type": "requires_transition_enabled",
            "transition_id": "t_ab",
            "requires_transition_id": "t_ab",
        }]
        with self.assertRaises(ModelValidationError):
            run_model(model)

    def test_duplicate_state_id_fails(self):
        model = copy.deepcopy(self.model)
        model["states"].append("A")
        with self.assertRaisesRegex(ModelValidationError, "duplicate state IDs"):
            run_model(model)

    def test_unknown_disabled_transition_fails(self):
        model = copy.deepcopy(self.model)
        model["scenarios"][1]["disabled_transitions"] = ["no_such_transition"]
        with self.assertRaisesRegex(ModelValidationError, "references unknown transitions"):
            run_model(model)

    def test_disabled_transition_ids_must_be_strings(self):
        for invalid_ids in ([{}], [None], [1], [""]):
            with self.subTest(invalid_ids=invalid_ids):
                model = copy.deepcopy(self.model)
                model["scenarios"][1]["disabled_transitions"] = invalid_ids
                with self.assertRaises(ModelValidationError):
                    run_model(model)

    def test_reachability_invariants_across_deterministic_generated_graphs(self):
        # Fixed-seed graph generation keeps this property suite reproducible.
        import random

        rng = random.Random(20261011)
        states = [f"S{i}" for i in range(5)]
        for case_index in range(30):
            transitions = []
            for source in states:
                for target in states:
                    if rng.random() < 0.24:
                        transitions.append({
                            "id": f"c{case_index}_t{len(transitions)}",
                            "source": source,
                            "target": target,
                        })
            disabled = [t["id"] for t in transitions if rng.random() < 0.18]
            model = {
                "schema_version": "collective-toy-input-001",
                "model_id": f"property-graph-{case_index:02d}",
                "initial_state": "S0",
                "states": states,
                "transitions": transitions,
                "relations": [],
                "rule_profile": {"type": "finite_deterministic_graph", "version": "1"},
                "scenarios": [
                    {"id": "baseline", "disabled_transitions": []},
                    {"id": "intervention", "disabled_transitions": disabled},
                ],
                "exploration": {"max_depth": 5, "max_trajectories": 500},
            }
            with self.subTest(case=case_index):
                result = run_model(model)
                base = result["scenario_results"]["baseline"]
                altered = result["scenario_results"]["intervention"]

                # Initial state is always reachable, and reachability never
                # includes an undeclared state.
                self.assertIn(model["initial_state"], base["reachable_states"])
                self.assertIn(model["initial_state"], altered["reachable_states"])
                self.assertLessEqual(set(base["reachable_states"]), set(states))
                self.assertLessEqual(set(altered["reachable_states"]), set(states))

                # Removing transitions cannot add reachable states in this
                # graph semantics, regardless of bounded trajectory output.
                self.assertLessEqual(
                    set(altered["reachable_states"]), set(base["reachable_states"])
                )

                # Every emitted path starts at the initial state and every
                # transition/state pair is a declared edge in that scenario.
                enabled = {
                    t["id"]: t for t in transitions if t["id"] not in set(disabled)
                }
                for path in altered["trajectories"]:
                    self.assertEqual(path[0], {"state": model["initial_state"]})
                    for previous, current in zip(path, path[1:]):
                        tid = current.get("transition")
                        self.assertIn(tid, enabled)
                        self.assertEqual(enabled[tid]["source"], previous["state"])
                        self.assertEqual(enabled[tid]["target"], current["state"])

    def test_relation_metadata_does_not_change_hashes_or_execution_in_profile_one(self):
        model_without = copy.deepcopy(self.model)
        model_with = copy.deepcopy(self.model)
        model_with["relations"] = [
            {"id": "r1", "type": "descriptive-only", "from": "A", "to": "D"}
        ]
        without_result = run_model(model_without)
        with_result = run_model(model_with)
        self.assertEqual(
            without_result["scenario_results"], with_result["scenario_results"]
        )
        self.assertNotEqual(without_result["input_sha256"], with_result["input_sha256"])
        self.assertEqual(without_result["result_sha256"], with_result["result_sha256"])

    def test_two_relations_guarding_same_transition_form_conjunctive_requirements(self):
        model = copy.deepcopy(self.model)
        model["rule_profile"] = {"type": "relation_guarded_graph", "version": "1"}
        model["relations"] = [
            {"id": "r_bd_requires_ab", "type": "requires_transition_enabled",
             "transition_id": "t_bd", "requires_transition_id": "t_ab"},
            {"id": "r_bd_requires_ac", "type": "requires_transition_enabled",
             "transition_id": "t_bd", "requires_transition_id": "t_ac"},
        ]
        model["scenarios"] = [
            {"id": "baseline", "disabled_transitions": []},
            {"id": "disable_ab", "disabled_transitions": ["t_ab"]},
            {"id": "disable_ac", "disabled_transitions": ["t_ac"]},
            {"id": "disable_both", "disabled_transitions": ["t_ab", "t_ac"]},
        ]
        result = run_model(model)["scenario_results"]
        self.assertNotIn("t_bd", result["baseline"]["effective_disabled_transitions"])
        for scenario_id in ("disable_ab", "disable_ac", "disable_both"):
            with self.subTest(scenario=scenario_id):
                self.assertIn("t_bd", result[scenario_id]["effective_disabled_transitions"])

    def test_conjunctive_guard_relation_order_does_not_change_operational_semantics(self):
        model = copy.deepcopy(self.model)
        model["rule_profile"] = {"type": "relation_guarded_graph", "version": "1"}
        model["relations"] = [
            {"id": "r_bd_requires_ab", "type": "requires_transition_enabled",
             "transition_id": "t_bd", "requires_transition_id": "t_ab"},
            {"id": "r_bd_requires_ac", "type": "requires_transition_enabled",
             "transition_id": "t_bd", "requires_transition_id": "t_ac"},
        ]
        model["scenarios"] = [
            {"id": "baseline", "disabled_transitions": []},
            {"id": "disable_ab", "disabled_transitions": ["t_ab"]},
            {"id": "disable_ac", "disabled_transitions": ["t_ac"]},
            {"id": "disable_both", "disabled_transitions": ["t_ab", "t_ac"]},
        ]
        reversed_model = copy.deepcopy(model)
        reversed_model["relations"].reverse()
        original = run_model(model)
        reversed_result = run_model(reversed_model)
        for scenario_id in original["scenario_results"]:
            for key in ("reachable_states", "trajectories", "effective_disabled_transitions"):
                self.assertEqual(
                    original["scenario_results"][scenario_id][key],
                    reversed_result["scenario_results"][scenario_id][key],
                    f"relation order changed {key} in {scenario_id}",
                )
        self.assertNotEqual(original["input_sha256"], reversed_result["input_sha256"])

    def test_relation_guarded_intervention_preserves_reachability_monotonicity(self):
        model = copy.deepcopy(self.model)
        model["rule_profile"] = {"type": "relation_guarded_graph", "version": "1"}
        model["relations"] = [
            {
                "id": "r_guard_bd_by_ab",
                "type": "requires_transition_enabled",
                "transition_id": "t_bd",
                "requires_transition_id": "t_ab",
            },
            {
                "id": "r_guard_cd_by_ac",
                "type": "requires_transition_enabled",
                "transition_id": "t_cd",
                "requires_transition_id": "t_ac",
            },
        ]
        model["scenarios"] = [
            {"id": "baseline", "disabled_transitions": []},
            {"id": "disable_ab", "disabled_transitions": ["t_ab"]},
        ]
        result = run_model(model)
        baseline = result["scenario_results"]["baseline"]
        intervention = result["scenario_results"]["disable_ab"]
        self.assertLessEqual(set(intervention["reachable_states"]), set(baseline["reachable_states"]))
        baseline_paths = {canonical_json(path) for path in baseline["trajectories"]}
        intervention_paths = {canonical_json(path) for path in intervention["trajectories"]}
        self.assertLessEqual(intervention_paths, baseline_paths)

    def test_direct_intervention_and_guard_chain_do_not_propagate_recursively(self):
        model = copy.deepcopy(self.model)
        model["states"] = ["A", "B", "C", "D"]
        model["initial_state"] = "A"
        model["transitions"] = [
            {"id": "t_ab", "source": "A", "target": "B"},
            {"id": "t_bc", "source": "B", "target": "C"},
            {"id": "t_cd", "source": "C", "target": "D"},
        ]
        model["rule_profile"] = {"type": "relation_guarded_graph", "version": "1"}
        model["relations"] = [
            {"id": "r_bc_requires_ab", "type": "requires_transition_enabled",
             "transition_id": "t_bc", "requires_transition_id": "t_ab"},
            {"id": "r_cd_requires_bc", "type": "requires_transition_enabled",
             "transition_id": "t_cd", "requires_transition_id": "t_bc"},
        ]
        model["scenarios"] = [
            {"id": "baseline", "disabled_transitions": []},
            {"id": "disable_ab", "disabled_transitions": ["t_ab"]},
            {"id": "disable_bc", "disabled_transitions": ["t_bc"]},
            {"id": "disable_cd", "disabled_transitions": ["t_cd"]},
        ]

        result = run_model(model)["scenario_results"]
        self.assertEqual(result["baseline"]["effective_disabled_transitions"], [])
        self.assertEqual(result["disable_ab"]["effective_disabled_transitions"], ["t_ab", "t_bc"])
        self.assertEqual(
            [(effect["relation_id"], effect["status"])
             for effect in result["disable_ab"]["relation_effects"]],
            [("r_bc_requires_ab", "BLOCKED"), ("r_cd_requires_bc", "APPLIED")],
            "a relation-derived disablement must not be treated as an explicit prerequisite disablement",
        )
        self.assertEqual(result["disable_bc"]["effective_disabled_transitions"], ["t_bc", "t_cd"])
        self.assertEqual(
            [(effect["relation_id"], effect["status"])
             for effect in result["disable_bc"]["relation_effects"]],
            [("r_bc_requires_ab", "APPLIED"), ("r_cd_requires_bc", "BLOCKED")],
        )
        self.assertEqual(result["disable_cd"]["effective_disabled_transitions"], ["t_cd"])
        self.assertEqual(
            [effect["status"] for effect in result["disable_cd"]["relation_effects"]],
            ["APPLIED", "APPLIED"],
            "a directly disabled target does not change whether its guards' prerequisites are explicitly disabled",
        )

    def test_relation_guarded_profile_blocks_transition_when_prerequisite_disabled(self):
        model = copy.deepcopy(self.model)
        model["rule_profile"] = {"type": "relation_guarded_graph", "version": "1"}
        model["relations"] = [{
            "id": "r_guard_bd",
            "type": "requires_transition_enabled",
            "transition_id": "t_bd",
            "requires_transition_id": "t_ab",
        }]
        model["scenarios"] = [
            {"id": "baseline", "disabled_transitions": []},
            {"id": "disable_prerequisite", "disabled_transitions": ["t_ab"]},
        ]
        result = run_model(model)
        baseline = result["scenario_results"]["baseline"]
        intervention = result["scenario_results"]["disable_prerequisite"]
        self.assertNotIn("t_bd", baseline["effective_disabled_transitions"])
        self.assertIn("t_bd", intervention["effective_disabled_transitions"])
        self.assertIn("D", intervention["reachable_states"])  # alternate route A -> C -> D remains available
        self.assertFalse(any(step.get("transition") == "t_bd" for path in intervention["trajectories"] for step in path))
        self.assertEqual(intervention["relation_effects"], [{
            "relation_id": "r_guard_bd",
            "type": "requires_transition_enabled",
            "transition_id": "t_bd",
            "requires_transition_id": "t_ab",
            "status": "BLOCKED",
            "reason": "prerequisite_transition_disabled",
        }])
        self.assertEqual(baseline["relation_effects"][0]["status"], "APPLIED")

    def test_relation_guarded_profile_applies_multiple_guards_deterministically(self):
        model = copy.deepcopy(self.model)
        model["rule_profile"] = {"type": "relation_guarded_graph", "version": "1"}
        model["relations"] = [
            {
                "id": "r_guard_bd",
                "type": "requires_transition_enabled",
                "transition_id": "t_bd",
                "requires_transition_id": "t_ab",
            },
            {
                "id": "r_guard_cd",
                "type": "requires_transition_enabled",
                "transition_id": "t_cd",
                "requires_transition_id": "t_ac",
            },
        ]
        model["scenarios"] = [
            {"id": "baseline", "disabled_transitions": []},
            {"id": "disable_both_prerequisites", "disabled_transitions": ["t_ab", "t_ac"]},
        ]
        first = run_model(model)
        second = run_model(model)
        baseline = first["scenario_results"]["baseline"]
        altered = first["scenario_results"]["disable_both_prerequisites"]
        self.assertEqual(first["result_sha256"], second["result_sha256"])
        self.assertEqual(
            [effect["relation_id"] for effect in altered["relation_effects"]],
            ["r_guard_bd", "r_guard_cd"],
        )
        self.assertEqual(
            [effect["status"] for effect in altered["relation_effects"]],
            ["BLOCKED", "BLOCKED"],
        )
        self.assertEqual(altered["effective_disabled_transitions"], ["t_ab", "t_ac", "t_bd", "t_cd"])
        self.assertEqual(altered["reachable_states"], ["A"])
        self.assertIn("D", baseline["reachable_states"])

    def test_multiple_guards_for_same_transition_use_explicit_interventions(self):
        model = copy.deepcopy(self.model)
        model["rule_profile"] = {"type": "relation_guarded_graph", "version": "1"}
        model["relations"] = [
            {"id": "r_guard_bd_by_ab", "type": "requires_transition_enabled",
             "transition_id": "t_bd", "requires_transition_id": "t_ab"},
            {"id": "r_guard_bd_by_ac", "type": "requires_transition_enabled",
             "transition_id": "t_bd", "requires_transition_id": "t_ac"},
        ]
        model["scenarios"] = [
            {"id": "baseline", "disabled_transitions": []},
            {"id": "disable_ab_only", "disabled_transitions": ["t_ab"]},
        ]
        result = run_model(model)
        altered = result["scenario_results"]["disable_ab_only"]
        self.assertEqual(
            [(effect["relation_id"], effect["status"]) for effect in altered["relation_effects"]],
            [("r_guard_bd_by_ab", "BLOCKED"), ("r_guard_bd_by_ac", "APPLIED")],
        )
        self.assertEqual(altered["effective_disabled_transitions"], ["t_ab", "t_bd"])
        self.assertNotIn("t_cd", altered["effective_disabled_transitions"])

    def test_disabling_interventions_compose_independently_of_declaration_order(self):
        model = copy.deepcopy(self.model)
        model["rule_profile"] = {"type": "relation_guarded_graph", "version": "1"}
        model["relations"] = [
            {"id": "r_guard_bd_by_ab", "type": "requires_transition_enabled",
             "transition_id": "t_bd", "requires_transition_id": "t_ab"},
            {"id": "r_guard_cd_by_ac", "type": "requires_transition_enabled",
             "transition_id": "t_cd", "requires_transition_id": "t_ac"},
        ]
        model["scenarios"] = [
            {"id": "baseline", "disabled_transitions": []},
            {"id": "disable_ab", "disabled_transitions": ["t_ab"]},
            {"id": "disable_ac", "disabled_transitions": ["t_ac"]},
            {"id": "disable_both", "disabled_transitions": ["t_ab", "t_ac"]},
            {"id": "disable_both_reversed", "disabled_transitions": ["t_ac", "t_ab"]},
        ]
        result = run_model(model)["scenario_results"]
        ab = set(result["disable_ab"]["effective_disabled_transitions"])
        ac = set(result["disable_ac"]["effective_disabled_transitions"])
        both = set(result["disable_both"]["effective_disabled_transitions"])
        reversed_both = set(result["disable_both_reversed"]["effective_disabled_transitions"])
        self.assertEqual(both, ab | ac)
        self.assertEqual(both, reversed_both)
        semantic_keys = set(result["disable_both"]) - {"scenario_id", "disabled_transitions"}
        self.assertEqual(
            {key: result["disable_both"][key] for key in semantic_keys},
            {key: result["disable_both_reversed"][key] for key in semantic_keys},
        )

    def test_duplicate_disabled_transition_ids_are_rejected(self):
        model = copy.deepcopy(self.model)
        model["scenarios"][0]["disabled_transitions"] = ["t_ab", "t_ab"]
        with self.assertRaises(ModelValidationError):
            run_model(model)

    def test_disabled_transition_order_does_not_change_semantics(self):
        model = copy.deepcopy(self.model)
        model["rule_profile"] = {"type": "relation_guarded_graph", "version": "1"}
        model["relations"] = [
            {"id": "r_guard_bd_by_ab", "type": "requires_transition_enabled",
             "transition_id": "t_bd", "requires_transition_id": "t_ab"},
            {"id": "r_guard_cd_by_ac", "type": "requires_transition_enabled",
             "transition_id": "t_cd", "requires_transition_id": "t_ac"},
        ]
        model["scenarios"] = [
            {"id": "baseline", "disabled_transitions": []},
            {"id": "disable_both", "disabled_transitions": ["t_ab", "t_ac"]},
        ]
        permuted = copy.deepcopy(model)
        # Keep semantic identity fixed; only serialized list order changes.
        permuted["scenarios"][1]["disabled_transitions"].reverse()

        original_result = run_model(model)
        permuted_result = run_model(permuted)
        self.assertEqual(original_result["scenario_results"], permuted_result["scenario_results"])
        self.assertEqual(original_result["comparisons_to_baseline"], permuted_result["comparisons_to_baseline"])
        self.assertEqual(original_result["result_sha256"], permuted_result["result_sha256"])
        self.assertNotEqual(original_result["input_sha256"], permuted_result["input_sha256"])

    def test_state_declaration_order_does_not_change_semantics(self):
        model = copy.deepcopy(self.model)
        permuted = copy.deepcopy(model)
        permuted["states"].reverse()

        original_result = run_model(model)
        permuted_result = run_model(permuted)
        self.assertEqual(original_result["scenario_results"], permuted_result["scenario_results"])
        self.assertEqual(original_result["comparisons_to_baseline"], permuted_result["comparisons_to_baseline"])
        self.assertEqual(original_result["result_sha256"], permuted_result["result_sha256"])
        self.assertNotEqual(original_result["input_sha256"], permuted_result["input_sha256"])

    def test_transition_declaration_order_does_not_change_semantics(self):
        model = copy.deepcopy(self.model)
        permuted = copy.deepcopy(model)
        permuted["transitions"].reverse()

        original_result = run_model(model)
        permuted_result = run_model(permuted)
        self.assertEqual(original_result["scenario_results"], permuted_result["scenario_results"])
        self.assertEqual(original_result["comparisons_to_baseline"], permuted_result["comparisons_to_baseline"])
        self.assertEqual(original_result["result_sha256"], permuted_result["result_sha256"])
        self.assertNotEqual(original_result["input_sha256"], permuted_result["input_sha256"])

    def test_scenario_declaration_order_does_not_change_semantics(self):
        model = copy.deepcopy(self.model)
        permuted = copy.deepcopy(model)
        permuted["scenarios"].reverse()

        original_result = run_model(model)
        permuted_result = run_model(permuted)
        self.assertEqual(original_result["scenario_results"], permuted_result["scenario_results"])
        self.assertEqual(original_result["comparisons_to_baseline"], permuted_result["comparisons_to_baseline"])
        self.assertEqual(original_result["result_sha256"], permuted_result["result_sha256"])
        self.assertNotEqual(original_result["input_sha256"], permuted_result["input_sha256"])

    def test_relation_guarded_scenario_declaration_order_does_not_change_semantics(self):
        model = copy.deepcopy(self.model)
        model["rule_profile"] = {"type": "relation_guarded_graph", "version": "1"}
        model["relations"] = [
            {"id": "r_guard_bd_by_ab", "type": "requires_transition_enabled",
             "transition_id": "t_bd", "requires_transition_id": "t_ab"},
            {"id": "r_guard_cd_by_ac", "type": "requires_transition_enabled",
             "transition_id": "t_cd", "requires_transition_id": "t_ac"},
        ]
        model["scenarios"] = [
            {"id": "baseline", "disabled_transitions": []},
            {"id": "disable_ab", "disabled_transitions": ["t_ab"]},
            {"id": "disable_ac", "disabled_transitions": ["t_ac"]},
        ]
        permuted = copy.deepcopy(model)
        permuted["scenarios"].reverse()
        original_result = run_model(model)
        permuted_result = run_model(permuted)
        self.assertEqual(original_result["scenario_results"], permuted_result["scenario_results"])
        self.assertEqual(original_result["comparisons_to_baseline"], permuted_result["comparisons_to_baseline"])
        self.assertEqual(original_result["result_sha256"], permuted_result["result_sha256"])
        self.assertNotEqual(original_result["input_sha256"], permuted_result["input_sha256"])

    def test_disabled_transition_declaration_order_does_not_change_semantics(self):
        model = copy.deepcopy(self.model)
        model["rule_profile"] = {"type": "relation_guarded_graph", "version": "1"}
        model["relations"] = [
            {"id": "r_guard_bd_by_ab", "type": "requires_transition_enabled",
             "transition_id": "t_bd", "requires_transition_id": "t_ab"},
            {"id": "r_guard_cd_by_ac", "type": "requires_transition_enabled",
             "transition_id": "t_cd", "requires_transition_id": "t_ac"},
        ]
        model["scenarios"] = [
            {"id": "baseline", "disabled_transitions": []},
            {"id": "disable_both", "disabled_transitions": ["t_ab", "t_ac"]},
        ]
        permuted = copy.deepcopy(model)
        permuted["scenarios"][1]["disabled_transitions"].reverse()
        original = run_model(model)
        reordered = run_model(permuted)
        self.assertEqual(original["scenario_results"], reordered["scenario_results"])
        self.assertEqual(original["comparisons_to_baseline"], reordered["comparisons_to_baseline"])
        self.assertEqual(original["result_sha256"], reordered["result_sha256"])
        self.assertNotEqual(original["input_sha256"], reordered["input_sha256"])

    def test_combined_disabling_interventions_are_monotone(self):
        model = copy.deepcopy(self.model)
        model["rule_profile"] = {"type": "relation_guarded_graph", "version": "1"}
        model["relations"] = [
            {"id": "r_guard_bd_by_ab", "type": "requires_transition_enabled",
             "transition_id": "t_bd", "requires_transition_id": "t_ab"},
            {"id": "r_guard_cd_by_ac", "type": "requires_transition_enabled",
             "transition_id": "t_cd", "requires_transition_id": "t_ac"},
        ]
        model["scenarios"] = [
            {"id": "baseline", "disabled_transitions": []},
            {"id": "disable_ab", "disabled_transitions": ["t_ab"]},
            {"id": "disable_ac", "disabled_transitions": ["t_ac"]},
            {"id": "disable_both", "disabled_transitions": ["t_ab", "t_ac"]},
        ]
        result = run_model(model)["scenario_results"]
        combined = result["disable_both"]
        for single_id in ("disable_ab", "disable_ac"):
            single = result[single_id]
            self.assertLessEqual(set(combined["reachable_states"]), set(single["reachable_states"]))
            # Removing edges can create new terminal paths, so complete trajectory
            # lists are not subsets. Every edge in a combined-case path must,
            # however, remain available in either single-intervention graph.
            single_enabled = {
                transition["id"] for transition in model["transitions"]
                if transition["id"] not in set(model["scenarios"][1 if single_id == "disable_ab" else 2]["disabled_transitions"])
                and all(
                    relation["transition_id"] == transition["id"]
                    or relation["requires_transition_id"] not in set(model["scenarios"][1 if single_id == "disable_ab" else 2]["disabled_transitions"])
                    for relation in model["relations"]
                )
            }
            for path in combined["trajectories"]:
                path_transitions = {step["transition"] for step in path if "transition" in step}
                self.assertTrue(path_transitions <= single_enabled)

    def test_disconnected_component_preserves_truncation_under_trajectory_cap(self):
        model = copy.deepcopy(self.model)
        model["transitions"].append({"id": "t_ba", "source": "B", "target": "A"})
        model["exploration"]["max_depth"] = 3
        augmented = copy.deepcopy(model)
        augmented["model_id"] = "toy-diamond-with-disconnected-component-capped"
        augmented["states"].extend(["X", "Y"])
        augmented["transitions"].append({"id": "t_xy", "source": "X", "target": "Y"})
        original_result = run_model(model)
        augmented_result = run_model(augmented)
        for scenario_id, original in original_result["scenario_results"].items():
            actual = augmented_result["scenario_results"][scenario_id]
            self.assertTrue(original["truncated"])
            self.assertTrue(actual["truncated"])
            self.assertEqual(original["reachable_states"], actual["reachable_states"])
            self.assertEqual(original["trajectories"], actual["trajectories"])
            self.assertEqual(original["truncated"], actual["truncated"])
        self.assertNotEqual(original_result["input_sha256"], augmented_result["input_sha256"])

    def test_disconnected_component_does_not_change_existing_scenario_outcomes(self):
        model = copy.deepcopy(self.model)
        augmented = copy.deepcopy(model)
        augmented["model_id"] = "toy-diamond-with-disconnected-component"
        augmented["states"].extend(["X", "Y"])
        augmented["transitions"].append({"id": "t_xy", "source": "X", "target": "Y"})
        original_result = run_model(model)
        augmented_result = run_model(augmented)
        for scenario_id in original_result["scenario_results"]:
            original = original_result["scenario_results"][scenario_id]
            actual = augmented_result["scenario_results"][scenario_id]
            self.assertEqual(original["reachable_states"], actual["reachable_states"])
            self.assertEqual(original["trajectories"], actual["trajectories"])
            self.assertEqual(original["truncated"], actual["truncated"])
        self.assertNotEqual(original_result["input_sha256"], augmented_result["input_sha256"])

    def test_scenario_declaration_order_does_not_couple_scenarios(self):
        model = copy.deepcopy(self.model)
        model["rule_profile"] = {"type": "relation_guarded_graph", "version": "1"}
        model["relations"] = [
            {"id": "r_guard_bd_by_ab", "type": "requires_transition_enabled",
             "transition_id": "t_bd", "requires_transition_id": "t_ab"}
        ]
        model["scenarios"] = [
            {"id": "baseline", "disabled_transitions": []},
            {"id": "disable_ab", "disabled_transitions": ["t_ab"]},
            {"id": "disable_ac", "disabled_transitions": ["t_ac"]},
        ]
        reversed_model = copy.deepcopy(model)
        reversed_model["scenarios"].reverse()
        original = run_model(model)
        reversed_result = run_model(reversed_model)
        self.assertEqual(original["scenario_results"], reversed_result["scenario_results"])
        self.assertEqual(original["comparisons_to_baseline"], reversed_result["comparisons_to_baseline"])
        self.assertNotEqual(original["input_sha256"], reversed_result["input_sha256"])

    def test_guard_is_inert_when_prerequisite_is_enabled(self):
        unguarded = copy.deepcopy(self.model)
        unguarded["scenarios"] = [{"id": "baseline", "disabled_transitions": []}]
        guarded = copy.deepcopy(unguarded)
        guarded["rule_profile"] = {"type": "relation_guarded_graph", "version": "1"}
        guarded["relations"] = [
            {"id": "r_guard_bd_by_ab", "type": "requires_transition_enabled",
             "transition_id": "t_bd", "requires_transition_id": "t_ab"}
        ]
        plain_result = run_model(unguarded)["scenario_results"]["baseline"]
        guarded_result = run_model(guarded)["scenario_results"]["baseline"]
        for key in ("reachable_states", "trajectories", "effective_disabled_transitions"):
            self.assertEqual(plain_result.get(key, []), guarded_result.get(key, []), f"{key} changed while prerequisite remained enabled")

    def test_duplicate_semantic_guard_does_not_change_graph_outcomes(self):
        model = copy.deepcopy(self.model)
        model["rule_profile"] = {"type": "relation_guarded_graph", "version": "1"}
        guard = {
            "id": "r_guard_bd_by_ab",
            "type": "requires_transition_enabled",
            "transition_id": "t_bd",
            "requires_transition_id": "t_ab",
        }
        model["relations"] = [guard]
        duplicate = copy.deepcopy(guard)
        duplicate["id"] = "r_guard_bd_by_ab_duplicate"
        duplicated_model = copy.deepcopy(model)
        duplicated_model["relations"].append(duplicate)
        original = run_model(model)
        duplicated = run_model(duplicated_model)
        for scenario_id in original["scenario_results"]:
            left = original["scenario_results"][scenario_id]
            right = duplicated["scenario_results"][scenario_id]
            for key in ("reachable_states", "trajectories", "effective_disabled_transitions"):
                self.assertEqual(left[key], right[key], f"{key} changed in {scenario_id}")

    def test_relation_guard_effect_is_local_to_guarded_transition(self):
        model = copy.deepcopy(self.model)
        model["rule_profile"] = {"type": "relation_guarded_graph", "version": "1"}
        model["relations"] = [
            {"id": "r_guard_bd_by_ab", "type": "requires_transition_enabled",
             "transition_id": "t_bd", "requires_transition_id": "t_ab"}
        ]
        model["scenarios"] = [
            {"id": "baseline", "disabled_transitions": []},
            {"id": "disable_ab", "disabled_transitions": ["t_ab"]},
        ]
        result = run_model(model)
        baseline = result["scenario_results"]["baseline"]
        intervention = result["scenario_results"]["disable_ab"]
        self.assertIn("D", baseline["reachable_states"])
        self.assertIn("D", intervention["reachable_states"])
        self.assertIn("t_bd", intervention["effective_disabled_transitions"])
        self.assertIn("t_cd", {transition["id"] for transition in model["transitions"]})
        baseline_paths = {tuple(item.get("state") for item in path) for path in baseline["trajectories"]}
        intervention_paths = {tuple(item.get("state") for item in path) for path in intervention["trajectories"]}
        self.assertIn(("A", "C", "D"), baseline_paths)
        self.assertIn(("A", "C", "D"), intervention_paths)
        self.assertNotIn(("A", "B", "D"), intervention_paths)

    def test_adding_guard_cannot_expand_reachability_or_trajectories(self):
        single = copy.deepcopy(self.model)
        single["rule_profile"] = {"type": "relation_guarded_graph", "version": "1"}
        single["relations"] = [
            {"id": "r_guard_bd_by_ab", "type": "requires_transition_enabled",
             "transition_id": "t_bd", "requires_transition_id": "t_ab"},
        ]
        single["scenarios"] = [
            {"id": "baseline", "disabled_transitions": []},
            {"id": "disable_ab", "disabled_transitions": ["t_ab"]},
            {"id": "disable_ac", "disabled_transitions": ["t_ac"]},
            {"id": "disable_both", "disabled_transitions": ["t_ab", "t_ac"]},
        ]
        extended = copy.deepcopy(single)
        extended["relations"].append(
            {"id": "r_guard_cd_by_ac", "type": "requires_transition_enabled",
             "transition_id": "t_cd", "requires_transition_id": "t_ac"}
        )
        single_result = run_model(single)
        extended_result = run_model(extended)
        for scenario_id in single_result["scenario_results"]:
            before = single_result["scenario_results"][scenario_id]
            after = extended_result["scenario_results"][scenario_id]
            self.assertLessEqual(set(after["reachable_states"]), set(before["reachable_states"]))
            before_paths = {canonical_json(path) for path in before["trajectories"]}
            after_paths = {canonical_json(path) for path in after["trajectories"]}
            self.assertLessEqual(after_paths, before_paths)

    def test_transition_declaration_order_does_not_change_semantics(self):
        model = copy.deepcopy(self.model)
        model["rule_profile"] = {"type": "relation_guarded_graph", "version": "1"}
        model["relations"] = [
            {"id": "r_guard_bd_by_ab", "type": "requires_transition_enabled",
             "transition_id": "t_bd", "requires_transition_id": "t_ab"},
            {"id": "r_guard_cd_by_ac", "type": "requires_transition_enabled",
             "transition_id": "t_cd", "requires_transition_id": "t_ac"},
        ]
        model["scenarios"] = [
            {"id": "baseline", "disabled_transitions": []},
            {"id": "disable_ab", "disabled_transitions": ["t_ab"]},
            {"id": "disable_ac", "disabled_transitions": ["t_ac"]},
        ]
        permuted = copy.deepcopy(model)
        permuted["transitions"].reverse()
        original_result = run_model(model)
        permuted_result = run_model(permuted)
        self.assertEqual(original_result["scenario_results"], permuted_result["scenario_results"])
        self.assertEqual(original_result["comparisons_to_baseline"], permuted_result["comparisons_to_baseline"])
        self.assertEqual(original_result["result_sha256"], permuted_result["result_sha256"])
        self.assertNotEqual(original_result["input_sha256"], permuted_result["input_sha256"])

    def test_relation_declaration_order_does_not_change_semantics(self):
        model = copy.deepcopy(self.model)
        model["rule_profile"] = {"type": "relation_guarded_graph", "version": "1"}
        model["relations"] = [
            {"id": "r_guard_bd_by_ab", "type": "requires_transition_enabled",
             "transition_id": "t_bd", "requires_transition_id": "t_ab"},
            {"id": "r_guard_bd_by_ac", "type": "requires_transition_enabled",
             "transition_id": "t_bd", "requires_transition_id": "t_ac"},
        ]
        model["scenarios"] = [
            {"id": "baseline", "disabled_transitions": []},
            {"id": "disable_ab", "disabled_transitions": ["t_ab"]},
            {"id": "disable_both", "disabled_transitions": ["t_ab", "t_ac"]},
        ]
        permuted = copy.deepcopy(model)
        permuted["relations"].reverse()

        original_result = run_model(model)
        permuted_result = run_model(permuted)
        self.assertEqual(original_result["scenario_results"], permuted_result["scenario_results"])
        self.assertEqual(original_result["comparisons_to_baseline"], permuted_result["comparisons_to_baseline"])
        self.assertEqual(original_result["result_sha256"], permuted_result["result_sha256"])
        self.assertNotEqual(original_result["input_sha256"], permuted_result["input_sha256"])

    def test_cyclic_guard_relations_are_not_recursively_evaluated(self):
        model = copy.deepcopy(self.model)
        model["rule_profile"] = {"type": "relation_guarded_graph", "version": "1"}
        model["relations"] = [
            {"id": "r_ab_requires_bd", "type": "requires_transition_enabled",
             "transition_id": "t_ab", "requires_transition_id": "t_bd"},
            {"id": "r_bd_requires_ab", "type": "requires_transition_enabled",
             "transition_id": "t_bd", "requires_transition_id": "t_ab"},
        ]
        model["scenarios"] = [
            {"id": "baseline", "disabled_transitions": []},
            {"id": "disable_ab_only", "disabled_transitions": ["t_ab"]},
        ]
        result = run_model(model)
        baseline = result["scenario_results"]["baseline"]
        altered = result["scenario_results"]["disable_ab_only"]
        self.assertEqual(
            [(effect["relation_id"], effect["status"]) for effect in baseline["relation_effects"]],
            [("r_ab_requires_bd", "APPLIED"), ("r_bd_requires_ab", "APPLIED")],
        )
        self.assertEqual(
            [(effect["relation_id"], effect["status"]) for effect in altered["relation_effects"]],
            [("r_ab_requires_bd", "APPLIED"), ("r_bd_requires_ab", "BLOCKED")],
        )
        self.assertEqual(altered["effective_disabled_transitions"], ["t_ab", "t_bd"])
        self.assertNotIn("t_ac", altered["effective_disabled_transitions"])

    def test_relation_guarded_profile_cycle_and_exploration_caps_are_explicit(self):
        model = copy.deepcopy(self.model)
        model["rule_profile"] = {"type": "relation_guarded_graph", "version": "1"}
        model["transitions"].append({"id": "t_ba", "source": "B", "target": "A"})
        model["relations"] = [{
            "id": "r_guard_bd",
            "type": "requires_transition_enabled",
            "transition_id": "t_bd",
            "requires_transition_id": "t_ab",
        }]
        model["exploration"] = {"max_depth": 3, "max_trajectories": 2}
        result = run_model(model)
        baseline = result["scenario_results"]["baseline"]
        self.assertEqual(set(baseline["reachable_states"]), {"A", "B", "C", "D"})
        self.assertTrue(baseline["truncated"])
        self.assertLessEqual(len(baseline["trajectories"]), 2)
        self.assertEqual(baseline["exploration_bounds"], {"max_depth": 3, "max_trajectories": 2})

    def test_relation_guarded_profile_rejects_unknown_relation_references(self):
        model = copy.deepcopy(self.model)
        model["rule_profile"] = {"type": "relation_guarded_graph", "version": "1"}
        model["relations"] = [{
            "id": "r_bad",
            "type": "requires_transition_enabled",
            "transition_id": "t_bd",
            "requires_transition_id": "missing",
        }]
        with self.assertRaises(ModelValidationError):
            run_model(model)

    def test_relation_guarded_profile_rejects_unknown_relation_types(self):
        model = copy.deepcopy(self.model)
        model["rule_profile"] = {"type": "relation_guarded_graph", "version": "1"}
        model["relations"] = [{
            "id": "r_bad",
            "type": "mystery",
            "transition_id": "t_bd",
            "requires_transition_id": "t_ab",
        }]
        with self.assertRaises(ModelValidationError):
            run_model(model)

    def test_relation_guarded_profile_rejects_duplicate_relation_ids(self):
        model = copy.deepcopy(self.model)
        model["rule_profile"] = {"type": "relation_guarded_graph", "version": "1"}
        relation = {
            "id": "r_duplicate",
            "type": "requires_transition_enabled",
            "transition_id": "t_bd",
            "requires_transition_id": "t_ab",
        }
        model["relations"] = [relation, copy.deepcopy(relation)]
        with self.assertRaises(ModelValidationError):
            run_model(model)

    def test_relations_are_inert_metadata_in_profile_one(self):
        baseline = run_model(self.model)["scenario_results"]
        model = copy.deepcopy(self.model)
        model["relations"] = [{"id": "r1", "type": "descriptive-only", "from": "A", "to": "D"}]
        with_relations = run_model(model)["scenario_results"]
        self.assertEqual(baseline, with_relations)

    def test_deterministic_malformed_input_mutation_matrix(self):
        # Fixed mutation catalogue: reproducible malformed-input property battery.
        cases = []
        def add(name, mutate):
            model = copy.deepcopy(self.model)
            mutate(model)
            cases.append((name, model))

        add("mutated-states-container", lambda m: m.__setitem__("states", {}))
        add("mutated-transitions-container", lambda m: m.__setitem__("transitions", None))
        add("mutated-transition-item", lambda m: m.__setitem__("transitions", [None]))
        add("mutated-transition-id-type", lambda m: m["transitions"][0].__setitem__("id", 7))
        add("mutated-transition-source-type", lambda m: m["transitions"][0].__setitem__("source", None))
        add("mutated-transition-target-type", lambda m: m["transitions"][0].__setitem__("target", []))
        add("mutated-scenarios-container", lambda m: m.__setitem__("scenarios", {}))
        add("mutated-scenario-item", lambda m: m.__setitem__("scenarios", [None]))
        add("mutated-scenario-id-empty", lambda m: m["scenarios"][0].__setitem__("id", ""))
        add("mutated-disabled-transition-item", lambda m: m["scenarios"][0].__setitem__("disabled_transitions", [None]))
        add("mutated-exploration-container", lambda m: m.__setitem__("exploration", None))
        add("mutated-depth-type", lambda m: m["exploration"].__setitem__("max_depth", "2"))
        add("mutated-trajectory-cap-negative", lambda m: m["exploration"].__setitem__("max_trajectories", -1))
        add("mutated-relations-container", lambda m: m.__setitem__("relations", {}))
        def relation_item(m):
            m["rule_profile"] = {"type": "relation_guarded_graph", "version": "1"}
            m["relations"] = [None]
        add("mutated-relation-item", relation_item)
        def relation_type(m):
            m["rule_profile"] = {"type": "relation_guarded_graph", "version": "1"}
            m["relations"] = [{"id": "r_mut", "type": "unknown", "transition_id": "t_ab", "requires_transition_id": "t_ac"}]
        add("mutated-relation-type", relation_type)
        def relation_reference(m):
            m["rule_profile"] = {"type": "relation_guarded_graph", "version": "1"}
            m["relations"] = [{"id": "r_mut", "type": "requires_transition_enabled", "transition_id": "missing", "requires_transition_id": "t_ab"}]
        add("mutated-relation-reference", relation_reference)
        add("mutated-duplicate-scenario-id", lambda m: m["scenarios"].append(copy.deepcopy(m["scenarios"][0])))
        add("mutated-initial-state-boolean", lambda m: m.__setitem__("initial_state", False))

        self.assertEqual(len(cases), 19)
        for name, candidate in cases:
            with self.subTest(name=name):
                with self.assertRaises(ModelValidationError):
                    run_model(candidate)


    def test_schema_resource_limits_accept_exact_upper_bounds(self):
        # Boundary checks call validation only; they do not alter the frozen fixture.
        model = copy.deepcopy(self.model)
        model["states"] = ["S" + str(i) for i in range(500)]
        model["initial_state"] = "S0"
        model["transitions"] = [
            {"id": "t" + str(i), "source": "S0", "target": "S0"}
            for i in range(2000)
        ]
        model["scenarios"] = [{"id": "baseline", "disabled_transitions": []}]
        model["exploration"] = {"max_depth": 100, "max_trajectories": 10000}
        from collective_toy_engine_001 import validate_model
        validate_model(model)

    def test_schema_resource_limits_reject_values_above_upper_bounds(self):
        from collective_toy_engine_001 import validate_model

        cases = []
        too_many_states = copy.deepcopy(self.model)
        too_many_states["states"] = ["S" + str(i) for i in range(501)]
        too_many_states["initial_state"] = "S0"
        cases.append(("states-501", too_many_states))

        too_many_transitions = copy.deepcopy(self.model)
        too_many_transitions["transitions"] = [
            {"id": "t" + str(i), "source": "A", "target": "A"}
            for i in range(2001)
        ]
        cases.append(("transitions-2001", too_many_transitions))

        excessive_depth = copy.deepcopy(self.model)
        excessive_depth["exploration"]["max_depth"] = 101
        cases.append(("max-depth-101", excessive_depth))

        excessive_trajectories = copy.deepcopy(self.model)
        excessive_trajectories["exploration"]["max_trajectories"] = 10001
        cases.append(("max-trajectories-10001", excessive_trajectories))

        for name, candidate in cases:
            with self.subTest(name=name):
                with self.assertRaises(ModelValidationError):
                    validate_model(candidate)


    def test_schema_rejects_boolean_and_negative_exploration_bounds(self):
        from collective_toy_engine_001 import validate_model

        cases = [
            ("depth-boolean", lambda m: m["exploration"].__setitem__("max_depth", True)),
            ("depth-negative", lambda m: m["exploration"].__setitem__("max_depth", -1)),
            ("trajectory-boolean", lambda m: m["exploration"].__setitem__("max_trajectories", False)),
            ("trajectory-zero", lambda m: m["exploration"].__setitem__("max_trajectories", 0)),
        ]
        for name, mutate in cases:
            with self.subTest(name=name):
                candidate = copy.deepcopy(self.model)
                mutate(candidate)
                with self.assertRaises(ModelValidationError):
                    validate_model(candidate)

    def test_schema_rejects_unknown_nested_fields(self):
        from collective_toy_engine_001 import validate_model

        cases = []
        candidate = copy.deepcopy(self.model)
        candidate["rule_profile"]["unexpected"] = "x"
        cases.append(("rule-profile", candidate))

        candidate = copy.deepcopy(self.model)
        candidate["transitions"][0]["unexpected"] = "x"
        cases.append(("transition", candidate))

        candidate = copy.deepcopy(self.model)
        candidate["scenarios"][0]["unexpected"] = "x"
        cases.append(("scenario", candidate))

        candidate = copy.deepcopy(self.model)
        candidate["exploration"]["unexpected"] = 1
        cases.append(("exploration", candidate))

        candidate = copy.deepcopy(self.model)
        candidate["rule_profile"] = {"type": "relation_guarded_graph", "version": "1"}
        candidate["relations"] = [{
            "id": "r1", "type": "requires_transition_enabled",
            "transition_id": "t_bd", "requires_transition_id": "t_ab",
            "unexpected": True,
        }]
        cases.append(("relation", candidate))

        for name, candidate in cases:
            with self.subTest(name=name):
                with self.assertRaises(ModelValidationError):
                    validate_model(candidate)

    def test_schema_rejects_duplicate_disabled_transition_ids(self):
        from collective_toy_engine_001 import validate_model

        candidate = copy.deepcopy(self.model)
        candidate["scenarios"][1]["disabled_transitions"] = ["t_ac", "t_ac"]
        with self.assertRaises(ModelValidationError):
            validate_model(candidate)

    def test_schema_rejects_missing_baseline_and_empty_state_ids(self):
        from collective_toy_engine_001 import validate_model

        no_baseline = copy.deepcopy(self.model)
        no_baseline["scenarios"] = [{"id": "other", "disabled_transitions": []}]
        with self.assertRaises(ModelValidationError):
            validate_model(no_baseline)

        empty_state = copy.deepcopy(self.model)
        empty_state["states"][0] = ""
        with self.assertRaises(ModelValidationError):
            validate_model(empty_state)

    def test_canonical_json_rejects_unsafe_and_non_finite_numbers(self):
        from collective_toy_engine_001 import canonical_json, MAX_SAFE_JSON_INTEGER

        for value in (
            MAX_SAFE_JSON_INTEGER + 1,
            -(MAX_SAFE_JSON_INTEGER + 1),
            float("nan"),
            float("inf"),
            float("-inf"),
            1.5,
        ):
            with self.subTest(value=repr(value)):
                with self.assertRaises(ModelValidationError):
                    canonical_json({"value": value})

    def test_canonical_json_rejects_unpaired_surrogates_and_non_json_values(self):
        from collective_toy_engine_001 import canonical_json

        for value in (chr(0xD800), {"key": object()}, {1: "non-string key"}):
            with self.subTest(value=repr(value)):
                with self.assertRaises(ModelValidationError):
                    canonical_json(value)

    def test_schema_rejects_empty_states_and_scenarios(self):
        # Empty containers exercise distinct non-empty-list invariants.
        empty_states = copy.deepcopy(self.model)
        empty_states["states"] = []
        with self.subTest(case="empty-states"):
            with self.assertRaisesRegex(ModelValidationError, "states must be a non-empty list"):
                run_model(empty_states)

        empty_scenarios = copy.deepcopy(self.model)
        empty_scenarios["scenarios"] = []
        with self.subTest(case="empty-scenarios"):
            with self.assertRaisesRegex(ModelValidationError, "scenarios must be a non-empty list"):
                run_model(empty_scenarios)

    def test_schema_accepts_minimum_valid_graph_and_zero_depth(self):
        from collective_toy_engine_001 import run_model

        model = copy.deepcopy(self.model)
        model["states"] = ["A"]
        model["initial_state"] = "A"
        model["transitions"] = []
        model["relations"] = []
        model["scenarios"] = [{"id": "baseline", "disabled_transitions": []}]
        model["exploration"] = {"max_depth": 0, "max_trajectories": 1}

        result = run_model(model)
        baseline = result["scenario_results"]["baseline"]
        self.assertEqual(baseline["reachable_states"], ["A"])
        self.assertEqual(baseline["trajectories"], [[{"state": "A"}]])
        self.assertFalse(baseline["truncated"])

    def test_optional_relations_and_disabled_transitions_default_empty(self):
        model = copy.deepcopy(self.model)
        model["states"] = ["A"]
        model["initial_state"] = "A"
        model["transitions"] = []
        model.pop("relations", None)
        model["scenarios"] = [{"id": "baseline"}]
        model["exploration"] = {"max_depth": 0, "max_trajectories": 1}

        result = run_model(model)
        baseline = result["scenario_results"]["baseline"]
        self.assertEqual(baseline["reachable_states"], ["A"])
        self.assertEqual(baseline["trajectories"], [[{"state": "A"}]])
        self.assertEqual(baseline["disabled_transitions"], [])
        self.assertFalse(baseline["truncated"])

    def test_omitted_relations_default_empty_in_relation_guarded_profile(self):
        model = copy.deepcopy(self.model)
        model["rule_profile"] = {"type": "relation_guarded_graph", "version": "1"}
        model["states"] = ["A"]
        model["initial_state"] = "A"
        model["transitions"] = []
        model.pop("relations", None)
        model["scenarios"] = [{"id": "baseline"}]
        model["exploration"] = {"max_depth": 0, "max_trajectories": 1}

        result = run_model(model)
        baseline = result["scenario_results"]["baseline"]
        self.assertEqual(baseline["relation_effects"], [])
        self.assertEqual(baseline["effective_disabled_transitions"], [])
        self.assertEqual(baseline["reachable_states"], ["A"])
        self.assertEqual(baseline["trajectories"], [[{"state": "A"}]])
        self.assertFalse(baseline["truncated"])

    def test_zero_depth_with_enabled_outgoing_transition_is_explicitly_truncated(self):
        from collective_toy_engine_001 import run_model

        model = copy.deepcopy(self.model)
        model["scenarios"] = [{"id": "baseline", "disabled_transitions": []}]
        model["exploration"] = {"max_depth": 0, "max_trajectories": 1}

        result = run_model(model)
        baseline = result["scenario_results"]["baseline"]
        self.assertEqual(baseline["reachable_states"], ["A", "B", "C", "D"])
        self.assertEqual(baseline["trajectories"], [[{"state": "A"}]])
        self.assertTrue(baseline["truncated"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
