"""Deterministic contract tests for the comparative holdout runner."""
from __future__ import annotations

import unittest
import tempfile
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

import run_c10s_nested_mr_comparative_holdout as runner
from c10s_nested_mr_fixtures import tier_a_specs


def spec_for(cell_id):
    return next(item for item in tier_a_specs() if item.cell_id == cell_id)


class ComparativeHoldoutRunnerTests(unittest.TestCase):
    def test_seed_schedule_is_stable_and_namespace_separated(self):
        cell = "F1_balanced_M10_R5"
        seeds = {
            runner.derive_holdout_seed(namespace, cell, 0)
            for namespace in ("dataset", "C0_bootstrap", "C5_bootstrap")
        }
        self.assertEqual(len(seeds), 3)
        self.assertTrue(all(0 <= seed < 2**64 for seed in seeds))

    def test_generators_are_deterministic_and_match_frozen_shapes(self):
        for cell_id in (
            "F1_balanced_M10_R5", "F1_low_between_M10_R5",
            "F1_high_between_M10_R5", "F5_beta22_M10_R5",
        ):
            with self.subTest(cell_id=cell_id):
                spec = spec_for(cell_id)
                first = runner.generate_holdout_dataset(spec, 7)
                self.assertEqual(first, runner.generate_holdout_dataset(spec, 7))
                self.assertEqual(len(first), spec.m)
                self.assertTrue(all(len(row) == spec.r for row in first))
                if spec.family == "F5":
                    self.assertTrue(set(x for row in first for x in row) <= {0.0, 1.0})

    def test_generator_rejects_cell_outside_frozen_roster(self):
        spec = spec_for("F1_balanced_M10_R5")
        invalid = spec.__class__(**{**spec.__dict__, "cell_id": "F1_UNREGISTERED"})
        with self.assertRaisesRegex(runner.HoldoutRunnerError, "CELL_NOT_IN_FROZEN"):
            runner.generate_holdout_dataset(invalid, 0)

    def test_generator_rejects_parameter_or_tier_drift(self):
        f5 = next(item for item in tier_a_specs() if item.cell_id == "F5_beta22_M10_R5")
        wrong_parameters = f5.__class__(**{
            **f5.__dict__, "parameters": (("alpha", 3), ("beta", 2))
        })
        with self.assertRaisesRegex(runner.HoldoutRunnerError, "F5_DGP_PARAMETERS"):
            runner.generate_holdout_dataset(wrong_parameters, 0)
        wrong_tier = f5.__class__(**{**f5.__dict__, "tier": "B"})
        with self.assertRaisesRegex(runner.HoldoutRunnerError, "TIER_A_K_B"):
            runner.generate_holdout_dataset(wrong_tier, 0)

    def test_dataset_generated_once_and_exact_f1_roster_passed_to_engine(self):
        spec = spec_for("F1_balanced_M10_R5")
        comparison = SimpleNamespace(
            dataset_id="1.0:F1_balanced_M10_R5:000000",
            input_m=spec.m, input_r=spec.r, target_m=spec.m, target_r=spec.r,
            baseline=SimpleNamespace(method_id=runner.IMPLEMENTED_METHODS["F1"][0]),
            candidates=(SimpleNamespace(method_id=runner.IMPLEMENTED_METHODS["F1"][1]),),
        )
        with (
            patch.object(runner, "generate_holdout_dataset", wraps=runner.generate_holdout_dataset) as gen,
            patch.object(runner, "compare_dataset", return_value=comparison) as compare,
            patch.object(runner, "adjudicate_matched_datasets", return_value=()) as adjudicate,
        ):
            result = runner.run_comparative_cell(spec, k=1, c0_b=100)
        self.assertEqual(gen.call_count, 1)
        self.assertEqual(compare.call_count, 1)
        kwargs = compare.call_args.kwargs
        self.assertFalse(kwargs["include_profile_diagnostics"])
        self.assertEqual(kwargs["baseline_bootstrap_replicates"], 100)
        self.assertIsNone(kwargs["bootstrap_replicates"])
        self.assertIsNone(kwargs["bootstrap_seed"])
        self.assertEqual(kwargs["baseline_bootstrap_seed"], runner.derive_holdout_seed(
            "C0_bootstrap", spec.cell_id, 0
        ))
        self.assertEqual(adjudicate.call_count, 1)
        self.assertEqual(result["datasets_completed"], 1)
        self.assertEqual(result["records"][0]["truth"]["within"], spec.true_within)
        self.assertEqual(result["records"][0]["truth"]["between"], spec.true_between)

    def test_f5_candidate_gets_separate_seed_and_frozen_bootstrap_count(self):
        spec = spec_for("F5_beta22_M10_R5")
        comparison = SimpleNamespace(
            dataset_id="1.0:F5_beta22_M10_R5:000000",
            input_m=spec.m, input_r=spec.r, target_m=spec.m, target_r=spec.r,
            baseline=SimpleNamespace(method_id=runner.IMPLEMENTED_METHODS["F5"][0]),
            candidates=(SimpleNamespace(method_id=runner.IMPLEMENTED_METHODS["F5"][1]),),
        )
        with (
            patch.object(runner, "compare_dataset", return_value=comparison) as compare,
            patch.object(runner, "adjudicate_matched_datasets", return_value=()),
        ):
            result = runner.run_comparative_cell(spec, k=1, c0_b=100, c5_b=100)
        kwargs = compare.call_args.kwargs
        self.assertEqual(kwargs["bootstrap_replicates"], 100)
        self.assertEqual(kwargs["bootstrap_seed"], runner.derive_holdout_seed(
            "C5_bootstrap", spec.cell_id, 0
        ))
        self.assertNotEqual(kwargs["baseline_bootstrap_seed"], kwargs["bootstrap_seed"])
        self.assertEqual(result["records"][0]["C5_bootstrap_seed"], kwargs["bootstrap_seed"])

    def test_holdout_reorders_specs_to_frozen_protocol_order(self):
        with patch.object(
            runner, "run_comparative_cell",
            side_effect=lambda spec, **kwargs: {
                "cell": spec.cell_id, "datasets_completed": kwargs["k"]
            },
        ):
            result = runner.run_holdout(specs=tuple(reversed(tier_a_specs())), k=2)
        self.assertEqual(
            [cell["cell"] for cell in result["cells"]],
            list(runner.EXPECTED_CELLS),
        )
        self.assertEqual(result["total_datasets"], 16)

    def test_holdout_rejects_duplicate_and_missing_cells(self):
        specs = tier_a_specs()
        with self.assertRaisesRegex(runner.HoldoutRunnerError, "DUPLICATE_CELL_SPEC"):
            runner.run_holdout(specs=specs + (specs[0],), k=1)
        with self.assertRaisesRegex(runner.HoldoutRunnerError, "EXACT_ORDERED_EIGHT"):
            runner.run_holdout(specs=specs[:-1], k=1)

    def test_replay_digest_is_deterministic_and_mismatch_fails_closed(self):
        result = {"protocol": "v1", "records": [{"id": "a", "truth": 1.0}]}
        digest = runner.verify_replay_identity(result, dict(result))
        self.assertEqual(digest, runner.deterministic_result_digest(result))
        with self.assertRaisesRegex(runner.HoldoutRunnerError, "REPLAY_HASH_MISMATCH"):
            runner.verify_replay_identity(result, {"protocol": "v1", "records": []})

    def test_checkpoint_resume_reuses_verified_completed_cells(self):
        specs = tier_a_specs()
        with tempfile.TemporaryDirectory() as directory:
            calls = []
            def fake_cell(spec, **kwargs):
                calls.append(spec.cell_id)
                return {
                    "protocol_id": runner.PROTOCOL_ID,
                    "protocol_version": runner.PROTOCOL_VERSION,
                    "cell": {"cell_id": spec.cell_id},
                    "datasets_completed": kwargs["k"],
                    "method_roster": [], "metrics": [], "mcse_adjudication": "NOT_SCORED",
                    "records": [{"dataset_id": f"{spec.cell_id}:{i}"} for i in range(kwargs["k"])],
                }
            with patch.object(runner, "run_comparative_cell", side_effect=fake_cell):
                first = runner.run_holdout_checkpointed(
                    Path(directory), code_commit="a" * 40,
                    protocol_sha256="b" * 64, source_inventory={"runner.py": "c" * 64},
                    specs=specs, k=1, c0_b=100, c5_b=100,
                )
                self.assertEqual(len(calls), 8)
                second = runner.run_holdout_checkpointed(
                    Path(directory), code_commit="a" * 40,
                    protocol_sha256="b" * 64, source_inventory={"runner.py": "c" * 64},
                    specs=specs, k=1, c0_b=100, c5_b=100,
                )
            self.assertEqual(len(calls), 8)
            self.assertEqual(first["total_datasets"], 8)
            self.assertEqual(second["total_datasets"], 8)
            self.assertNotIn("records", first["cells"][0])
            self.assertEqual(first["cells"][0]["records_count"], 1)
            self.assertTrue((Path(directory) / first["cells"][0]["records_file"]).is_file())
            self.assertEqual(first["checkpoint_index_sha256"], second["checkpoint_index_sha256"])

    def test_checkpoint_rejects_code_or_protocol_mismatch(self):
        specs = tier_a_specs()
        with tempfile.TemporaryDirectory() as directory:
            with patch.object(
                runner, "run_comparative_cell",
                side_effect=lambda spec, **kwargs: {
                    "protocol_id": runner.PROTOCOL_ID,
                    "protocol_version": runner.PROTOCOL_VERSION,
                    "cell": {"cell_id": spec.cell_id},
                    "datasets_completed": kwargs["k"],
                    "method_roster": [], "metrics": [], "mcse_adjudication": "NOT_SCORED",
                    "records": [{"dataset_id": f"{spec.cell_id}:0"}],
                },
            ):
                runner.run_holdout_checkpointed(
                    Path(directory), code_commit="a" * 40,
                    protocol_sha256="b" * 64, source_inventory={"runner.py": "c" * 64},
                    specs=specs, k=1, c0_b=100, c5_b=100,
                )
                with self.assertRaisesRegex(runner.HoldoutRunnerError, "CONFIGURATION_MISMATCH"):
                    runner.run_holdout_checkpointed(
                        Path(directory), code_commit="d" * 40,
                        protocol_sha256="b" * 64, source_inventory={"runner.py": "c" * 64},
                        specs=specs, k=1, c0_b=100, c5_b=100,
                    )

    def test_checkpoint_rejects_tampered_cell_file(self):
        specs = tier_a_specs()
        with tempfile.TemporaryDirectory() as directory:
            with patch.object(
                runner, "run_comparative_cell",
                side_effect=lambda spec, **kwargs: {
                    "protocol_id": runner.PROTOCOL_ID,
                    "protocol_version": runner.PROTOCOL_VERSION,
                    "cell": {"cell_id": spec.cell_id},
                    "datasets_completed": kwargs["k"],
                    "method_roster": [], "metrics": [], "mcse_adjudication": "NOT_SCORED",
                    "records": [{"dataset_id": f"{spec.cell_id}:0"}],
                },
            ):
                runner.run_holdout_checkpointed(
                    Path(directory), code_commit="a" * 40,
                    protocol_sha256="b" * 64, source_inventory={"runner.py": "c" * 64},
                    specs=specs, k=1, c0_b=100, c5_b=100,
                )
            cell_path = Path(directory) / "F1_balanced_M10_R5.cell.json"
            cell_path.write_text("{}\\n", encoding="utf-8")
            with self.assertRaisesRegex(runner.HoldoutRunnerError, "CELL_HASH_MISMATCH"):
                runner.run_holdout_checkpointed(
                    Path(directory), code_commit="a" * 40,
                    protocol_sha256="b" * 64, source_inventory={"runner.py": "c" * 64},
                    specs=specs, k=1, c0_b=100, c5_b=100,
                )

    def test_cli_fails_closed_without_authorization_wrapper(self):
        with patch("sys.argv", ["runner", "--output-dir", "/tmp/unused"]):
            with self.assertRaisesRegex(SystemExit, "FAIL_CLOSED"):
                runner.main()


if __name__ == "__main__":
    unittest.main()
