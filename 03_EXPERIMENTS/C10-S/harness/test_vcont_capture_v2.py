"""Pure fixture tests for Gate 185 capture primitives; never invoke producers."""
from dataclasses import replace
import copy
import json
import hashlib
import math
import unittest
from types import SimpleNamespace

import rfc8785

from vcont_benchmark_protocol import (
    SCENARIO_IDS, build_scenario_estimand_matrix, scenario_matrix_fingerprint,
)
from vcont_evidence_export import (
    CapturedBenchmark, ContractError, capture_matrix, freeze_report_snapshot,
)


class CaptureV2Tests(unittest.TestCase):
    def setUp(self):
        self.versions = tuple((sid, "VCONT-SYNTH-001") for sid in SCENARIO_IDS)
        self.matrix = build_scenario_estimand_matrix(dict(self.versions))
        self.design = SimpleNamespace(
            scenario_versions=self.versions,
            n_units=32,
            outer_replicates=2,
            repeated_assignments=2,
            matrix_fingerprint=scenario_matrix_fingerprint(self.matrix),
        )

    def report_fixture(self):
        temporal = []
        for scenario_id, scenario_version in self.versions:
            for m in range(self.design.outer_replicates):
                outer_id = f"outer-{m:06d}"
                for role, assignment_index in (
                    [("RUN", -1)] + [
                        ("REPEATED_ASSIGNMENT", r)
                        for r in range(self.design.repeated_assignments)
                    ]
                ):
                    temporal.append({
                        "scenario_id": scenario_id,
                        "scenario_version": scenario_version,
                        "N": self.design.n_units,
                        "outer_replicate_id": outer_id,
                        "assignment_role": role,
                        "assignment_index": assignment_index,
                        "run_id": f"run-{scenario_id}-{m}-{assignment_index}",
                        "world_id": f"world-{scenario_id}-{m}",
                        "world_seed": 17,
                        "z_assignment_seed": 19 + max(0, assignment_index),
                        "g_assignment_seed": 23 + max(0, assignment_index),
                    })

        binary = {
            "n": 2, "successes": 1, "rate": 0.5, "mcse": 0.35,
            "wilson_95_low": 0.1, "wilson_95_high": 0.9,
        }
        metric = {
            "outer_replicates": 2, "metric_mean": 0.1, "metric_sd": 0.2,
            "mcse": 0.14, "target_mcse": 0.2, "precision_status": "PASS",
        }
        rmse_metric = {
            "outer_replicates": 2, "rmse": 0.2, "mean_squared_error": 0.04,
            "mcse_rmse_delta": 0.1, "target_mcse": 0.2, "precision_status": "PASS",
        }
        pair_ledger = []
        scenario_reports = {}

        truth_fields = (
            "run_id potential_v potential_interval_truth potential_enabled_truth "
            "potential_profile_truth potential_delta_t_acc itt_z_truth itt_g_z0_truth "
            "theta_a_truth seed itt_z_run_truth itt_z_mechanism_truth itt_z_reference_truth "
            "transportability_invariant_truth transportability_scope_truth "
            "g_reference_regime_id g_reference_regime_version g_assignment_mechanism_hash "
            "z_assignment_mechanism_hash outer_replicate_id assignment_role assignment_index"
        ).split()
        analyzer_fields = (
            "run_id estimand_id package_status g_assignment_status package_itt "
            "g_assignment_effect first_stage_delta_t_acc package_se g_assignment_se "
            "abstention_reasons input_sha256 output_sha256 target_regime_id "
            "target_regime_version outcome_id outcome_version reference_regime_status "
            "reference_regime_id reference_regime_version g_assignment_mechanism_hash "
            "z_assignment_mechanism_hash transportability_id transportability_version "
            "transportability_scope transportability_evidence_status estimand_version "
            "g_assignment_mechanism_id g_assignment_mechanism_version "
            "z_assignment_mechanism_id z_assignment_mechanism_version provenance_sha256 "
            "transportability_outcome_id transportability_basis reference_regime_itt "
            "run_conditional_estimand_id run_conditional_estimand_version "
            "reference_regime_estimand_id reference_regime_estimand_version "
            "g_assignment_estimand_id g_assignment_estimand_version outer_replicate_id "
            "assignment_role assignment_index"
        ).split()
        contract_fields = (
            "estimand_id estimand_version randomized_z randomized_g positivity "
            "no_interference measurement_identified version_consistency "
            "focal_direct_path_absent common_nonfocal_regime target_regime_id "
            "target_regime_version outcome_id outcome_version z_effect_invariant_across_g "
            "transportability_id transportability_version transportability_scope "
            "transportability_evidence_status g_assignment_mechanism_hash "
            "z_assignment_mechanism_hash g_assignment_mechanism_id "
            "g_assignment_mechanism_version z_assignment_mechanism_id "
            "z_assignment_mechanism_version reference_regime_id reference_regime_version "
            "transportability_outcome_id transportability_basis run_conditional_estimand_id "
            "run_conditional_estimand_version mechanism_marginal_estimand_id "
            "mechanism_marginal_estimand_version reference_regime_estimand_id "
            "reference_regime_estimand_version g_assignment_estimand_id "
            "g_assignment_estimand_version"
        ).split()
        run_manifest_fields = (
            "run_id scenario_id version n_units n_intervals window_start window_end "
            "interval_width generator_version world_id world_version replicate_id "
            "g_assignment_mechanism_id g_assignment_mechanism_version "
            "g_assignment_mechanism_hash z_assignment_mechanism_id "
            "z_assignment_mechanism_version z_assignment_mechanism_hash "
            "g_reference_regime_id g_reference_regime_version z_assignment_vector_hash "
            "g_assignment_vector_hash g_assignment_probability_by_stratum world_seed "
            "z_assignment_seed g_assignment_seed outer_replicate_id assignment_role "
            "assignment_index"
        ).split()
        evaluation_fields = (
            "run_id package_abs_error g_assignment_abs_error package_recovered "
            "g_assignment_recovered expected_abstention_respected notes "
            "reference_regime_status_correct reference_regime_estimate_present"
        ).split()
        repeated_fields = (
            "world_id replicate_count mean_run_estimate mechanism_truth marginal_abs_error "
            "marginal_recovered per_run_reports reference_truth reference_estimate_mean "
            "reference_abs_error reference_recovered reference_identification_status "
            "mechanism_marginal_estimand_id mechanism_marginal_estimand_version "
            "reference_regime_estimand_id reference_regime_estimand_version"
        ).split()

        for scenario_id, scenario_version in self.versions:
            selected = [spec for spec in self.matrix if spec.key.scenario_id == scenario_id]
            for spec in selected:
                contributions = []
                for m in range(self.design.outer_replicates):
                    contributions.append({
                        "outer_replicate_id": f"outer-{m:06d}",
                        "world_id": f"world-{scenario_id}-{m}",
                        "world_seed": 17,
                        "run_id": f"run-{scenario_id}-{m}",
                        "temporal_source": "RUN",
                        "evaluation_class": "EVALUABLE",
                        "run_status": "IDENTIFIED",
                        "identification_status": "IDENTIFIED",
                        "identification_expected": "IDENTIFIED",
                        "abstention_expected": False,
                        "adjudicated_status": "IDENTIFIED",
                        "identification_correct": True,
                        "abstention_correct": True,
                        "abstained": False,
                        "abstention_reasons": [],
                        "estimate": 0.1,
                        "truth": 0.1,
                        "signed_error": 0.0,
                        "absolute_error": 0.0,
                        "squared_error": 0.0,
                        "contribution_state": "NUMERIC",
                    })
                pair_ledger.append({
                    "key": [scenario_id, scenario_version, spec.key.estimand_id,
                            spec.key.estimand_version, "MONTE_CARLO"],
                    "evaluation_class": "EVALUABLE",
                    "truth_status": "DEFINED",
                    "expected_M": 2, "observed_M": 2,
                    "numeric_denominator": 2, "status_denominator": 2,
                    "missing_contribution_count": 0, "truth_missing_count": 0,
                    "invalid_output_count": 0, "abstention_count": 0,
                    "identification_correct_count": 2, "abstention_correct_count": 2,
                    "identification_rates": {
                        "identified": binary, "not_identified": binary,
                        "indeterminate": binary, "abstained": binary,
                    },
                    "run_identification_rates": {
                        "identified": binary, "not_identified": binary,
                        "indeterminate": binary,
                    },
                    "metrics": {"bias": metric, "mae": metric, "rmse": rmse_metric},
                    "precision_status": "PASS_PRECISION",
                    "contributions": contributions,
                })

            per_outer = []
            for m in range(self.design.outer_replicates):
                outer_id = f"outer-{m:06d}"
                run = [
                    dict.fromkeys(truth_fields),
                    dict.fromkeys(analyzer_fields),
                    dict.fromkeys(contract_fields),
                    dict.fromkeys(run_manifest_fields),
                ]
                run[0].update({"run_id": f"run-{scenario_id}-{m}", "seed": 17})
                run[1].update({"run_id": f"run-{scenario_id}-{m}"})
                run[3].update({
                    "run_id": f"run-{scenario_id}-{m}", "scenario_id": scenario_id,
                    "version": scenario_version, "n_units": self.design.n_units,
                    "world_seed": 17, "z_assignment_seed": 19, "g_assignment_seed": 23,
                    "outer_replicate_id": outer_id,
                })
                evaluation = dict.fromkeys(evaluation_fields)
                evaluation["run_id"] = f"run-{scenario_id}-{m}"
                repeated = dict.fromkeys(repeated_fields)
                repeated["world_id"] = f"world-{scenario_id}-{m}"
                repeated["replicate_count"] = self.design.repeated_assignments
                repeated["per_run_reports"] = [dict(evaluation) for _ in range(2)]
                per_outer.append({
                    "outer_replicate_id": outer_id,
                    "run": run,
                    "run_report": evaluation,
                    "repeated_report": repeated,
                })
            scenario_reports[scenario_id] = {
                "scenario_id": scenario_id, "scenario_version": scenario_version,
                "n_units": self.design.n_units, "outer_replicate_count": 2,
                "coverage": {
                    "required_pairs": 4, "run_conditional_numeric": 2,
                    "g_assignment_numeric": 2, "mechanism_marginal_numeric": 2,
                    "reference_regime_numeric": 2,
                    "reference_regime_identification_status": 2,
                },
                "run_conditional": {
                    "bias": metric, "mae": metric, "rmse": rmse_metric,
                    "recovery_rate": binary, "identification_rate": binary,
                },
                "g_assignment_z0": {
                    "bias": metric, "mae": metric, "rmse": rmse_metric,
                    "recovery_rate": binary, "identification_rate": binary,
                },
                "mechanism_marginal": {
                    "bias": metric, "mae": metric, "rmse": rmse_metric,
                    "recovery_rate": binary,
                },
                "reference_regime": {
                    "bias": metric, "mae": metric, "rmse": rmse_metric,
                    "identification_rate": binary, "recovery_rate": binary,
                },
                "per_outer_replicate": per_outer,
            }

        manifest = {
            "scenario_versions": self.versions,
            "N": 32, "M": 2, "R": 2,
            "matrix_fingerprint": self.design.matrix_fingerprint,
            "seed_bank_label": "evaluation",
            "seed_bank_fingerprint": "a" * 64,
            "executable_commit": "c" * 40,
            "configuration_fingerprint": "b" * 64,
            "metric_targets": (),
            "temporal_manifest": copy.deepcopy(temporal),
            "pair_ledger": copy.deepcopy(pair_ledger),
        }
        return {
            "design": {
                "scenario_versions": self.versions, "n_units": 32,
                "outer_replicates": 2, "repeated_assignments": 2,
                "matrix_fingerprint": self.design.matrix_fingerprint,
                "metric_targets": (), "seed_bank_label": "evaluation",
                "seed_bank_fingerprint": "a" * 64, "executable_commit": "c" * 40,
                "configuration_fingerprint": "b" * 64,
            },
            "temporal_manifest": temporal,
            "pair_ledger": pair_ledger,
            "manifest": manifest,
            "scenario_reports": scenario_reports,
            "coverage": {"required_pairs": 52, "observed_pairs": 52, "scenario_count": 13},
            "report_fingerprint": hashlib.sha256(
                json.dumps(manifest, sort_keys=True, separators=(",", ":"), allow_nan=False)
                .encode("utf-8")
            ).hexdigest(),
        }

    def test_matrix_capture_has_exact_52_rows_and_recomputable_digest(self):
        capture = capture_matrix(self.matrix, self.design)
        payload = capture.to_payload()
        self.assertEqual(capture.row_count, 52)
        self.assertEqual(len(payload["rows"]), 52)
        digest_input = {
            "schema_id": "TGCV-C10S-VCONT-MATRIX-CAPTURE",
            "schema_version": "1.0.0",
            "row_count": 52,
            "rows": payload["rows"],
        }
        self.assertEqual(
            capture.full_matrix_sha256,
            __import__("hashlib").sha256(rfc8785.dumps(digest_input)).hexdigest(),
        )
        self.assertEqual(capture.full_matrix_digest_algorithm,
                         "TGCV-C10S-VCONT-MATRIX-FULL-JCS-SHA256-1")

    def test_matrix_capture_rejects_permutation_even_when_pair_set_is_unchanged(self):
        with self.assertRaises(ContractError):
            capture_matrix((self.matrix[1], self.matrix[0]) + self.matrix[2:], self.design)

    def test_tolerance_id_changes_full_digest_but_not_legacy_fingerprint(self):
        changed = (replace(self.matrix[0], tolerance_id="TOLERANCE-REVISION-2"),) + self.matrix[1:]
        self.assertEqual(scenario_matrix_fingerprint(changed), self.design.matrix_fingerprint)
        changed_capture = capture_matrix(changed, self.design)
        baseline = capture_matrix(self.matrix, self.design)
        self.assertNotEqual(changed_capture.full_matrix_sha256, baseline.full_matrix_sha256)

    def test_report_snapshot_wraps_uint64_and_is_immutable_from_compatibility_dict(self):
        report = self.report_fixture()
        snapshot = freeze_report_snapshot(report)
        original_bytes = snapshot.canonical_bytes
        report["coverage"]["observed_pairs"] = 0
        self.assertEqual(snapshot.canonical_bytes, original_bytes)
        envelope = json.loads(snapshot.canonical_bytes.decode("utf-8"))
        self.assertEqual(envelope["schema_version"], "2.1.0")
        self.assertEqual(envelope["payload_type"], "TGCV-C10S-VCONT-BENCHMARK-REPORT")
        self.assertEqual(envelope["schema_id"], "TGCV-C10S-VCONT-REPORT-SNAPSHOT")
        self.assertEqual(
            envelope["legacy_fingerprint_algorithm"],
            "TGCV-C10S-VCONT-LEGACY-REPORT-FINGERPRINT-PYJSON-SORTKEYS-COMPACT-SHA256-1",
        )
        temporal = envelope["report"]["temporal_manifest"][0]
        self.assertEqual(temporal["world_seed"],
                         {"$type": "uint64", "decimal": "18446744073709551615"})
        self.assertEqual(temporal["z_assignment_seed"],
                         {"$type": "uint64", "decimal": "9007199254740993"})
        nested = envelope["report"]["manifest"]["temporal_manifest"][0]
        self.assertEqual(temporal, nested)
        self.assertEqual(snapshot.sha256,
                         __import__("hashlib").sha256(snapshot.canonical_bytes).hexdigest())

    def test_report_snapshot_rejects_root_nested_manifest_disagreement(self):
        report = self.report_fixture()
        report["manifest"]["temporal_manifest"][0]["world_seed"] = 1
        normalized = json.loads(json.dumps(
            report["manifest"], default=lambda value: value.__dict__, sort_keys=True
        ))
        report["report_fingerprint"] = hashlib.sha256(json.dumps(
            normalized, sort_keys=True, separators=(",", ":"), allow_nan=False
        ).encode("utf-8")).hexdigest()
        with self.assertRaises(ContractError):
            freeze_report_snapshot(report)


    def test_report_snapshot_rejects_tampered_legacy_fingerprint(self):
        report = self.report_fixture()
        report["report_fingerprint"] = "e" * 64
        with self.assertRaises(ContractError):
            freeze_report_snapshot(report)

    def test_report_snapshot_rejects_non_uint64_seed_and_unknown_top_level_field(self):
        report = self.report_fixture()
        report["temporal_manifest"][0]["world_seed"] = -1
        with self.assertRaises(ContractError):
            freeze_report_snapshot(report)
        report = self.report_fixture()
        report["temporal_manifest"][0]["z_assignment_seed"] = 1 << 64
        with self.assertRaises(ContractError):
            freeze_report_snapshot(report)
        report = self.report_fixture()
        report["temporal_manifest"][0]["g_assignment_seed"] = True
        with self.assertRaises(ContractError):
            freeze_report_snapshot(report)
        report = self.report_fixture()
        report["unexpected"] = True
        with self.assertRaises(ContractError):
            freeze_report_snapshot(report)


    def test_report_snapshot_rejects_unknown_nested_scenario_field(self):
        report = self.report_fixture()
        report["scenario_reports"]["R0_FOCAL_POSITIVE"]["per_outer_replicate"][0]["run"][0]["unexpected"] = 1
        with self.assertRaises(ContractError):
            freeze_report_snapshot(report)

    def test_report_snapshot_rejects_temporal_and_pair_cardinality_drift(self):
        report = self.report_fixture()
        report["temporal_manifest"].pop()
        with self.assertRaises(ContractError):
            freeze_report_snapshot(report)
        report = self.report_fixture()
        report["pair_ledger"].pop()
        with self.assertRaises(ContractError):
            freeze_report_snapshot(report)

    def test_report_snapshot_rejects_unknown_pair_contribution_field(self):
        report = self.report_fixture()
        report["pair_ledger"][0]["contributions"][0]["unexpected"] = "drift"
        with self.assertRaises(ContractError):
            freeze_report_snapshot(report)


    def test_report_snapshot_v2_1_wraps_all_four_scenario_run_uint64_paths(self):
        report = self.report_fixture()
        run = report["scenario_reports"]["R0_FOCAL_POSITIVE"]["per_outer_replicate"][0]["run"]
        run[0]["seed"] = 9007199254740992
        run[3]["world_seed"] = 9007199254740991
        run[3]["z_assignment_seed"] = 18446744073709551615
        run[3]["g_assignment_seed"] = 0
        snapshot = freeze_report_snapshot(report)
        envelope = json.loads(snapshot.canonical_bytes.decode("utf-8"))
        projected = envelope["report"]["scenario_reports"]["R0_FOCAL_POSITIVE"]["per_outer_replicate"][0]["run"]
        self.assertEqual(projected[0]["seed"], {"$type": "uint64", "decimal": "9007199254740992"})
        self.assertEqual(projected[3]["world_seed"], {"$type": "uint64", "decimal": "9007199254740991"})
        self.assertEqual(projected[3]["z_assignment_seed"], {"$type": "uint64", "decimal": "18446744073709551615"})
        self.assertEqual(projected[3]["g_assignment_seed"], {"$type": "uint64", "decimal": "0"})
        self.assertEqual(snapshot.schema_version, "2.1.0")

    def test_report_snapshot_v2_1_rejects_invalid_nested_uint64_sources(self):
        mutations = (
            (0, "seed", -1),
            (0, "seed", True),
            (0, "seed", 1 << 64),
            (3, "world_seed", -1),
            (3, "world_seed", True),
            (3, "world_seed", 1 << 64),
            (3, "z_assignment_seed", 1.5),
            (3, "g_assignment_seed", "23"),
        )
        for tuple_index, field, invalid in mutations:
            report = self.report_fixture()
            report["scenario_reports"]["R0_FOCAL_POSITIVE"]["per_outer_replicate"][0]["run"][tuple_index][field] = invalid
            with self.subTest(tuple_index=tuple_index, field=field, invalid=invalid):
                with self.assertRaises(ContractError):
                    freeze_report_snapshot(report)

    def test_rfc8785_known_canonicalization_vectors(self):
        self.assertEqual(rfc8785.dumps({"b": 2, "a": 1}), b'{"a":1,"b":2}')
        self.assertEqual(
            rfc8785.dumps({"numbers": [333333333.33333329, 1e30, 4.50, 2e-3, 1e-27]}),
            b'{"numbers":[333333333.3333333,1e+30,4.5,0.002,1e-27]}',
        )
        self.assertEqual(rfc8785.dumps({"a": None, "b": []}), b'{"a":null,"b":[]}')

    def test_rfc8785_rejects_non_finite_numbers_and_unsafe_integers(self):
        with self.assertRaises(Exception):
            rfc8785.dumps({"x": math.nan})
        with self.assertRaises(Exception):
            rfc8785.dumps({"x": 9007199254740992})

    def test_three_argument_legacy_constructor_remains_compatible(self):
        captured = CapturedBenchmark({}, (), ())
        self.assertIsNone(captured.matrix_capture)
        self.assertIsNone(captured.report_snapshot)
        self.assertIsNone(captured.capture_id)
        self.assertIsNone(captured.benchmark_export_id)


if __name__ == "__main__":
    unittest.main()
