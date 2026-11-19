"""Contract tests: resource preflight measures workload and never adjudicates coverage."""
from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

import run_c10s_nested_mr_comparative_resource_preflight as preflight
import validate_c10s_nested_mr_resource_preflight_authorization as resource_auth
import validate_c10s_nested_mr_comparative_holdout_authorization as holdout_auth
from c10s_nested_mr_comparative_inference_engine import IMPLEMENTED_METHODS


class ResourcePreflightTests(unittest.TestCase):
    def test_resource_authorization_validator_rejects_draft(self):
        with tempfile.TemporaryDirectory() as directory:
            auth_path = Path(directory) / "authorization.json"
            auth_path.write_text(json.dumps({
                "schema": resource_auth.AUTH_SCHEMA,
                "status": "DRAFT",
            }), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "not APPROVED"):
                resource_auth.validate(
                    auth_path, Path(directory), "a" * 40,
                    resource_auth.BRANCH_PREFIX + "draft-authorization-001",
                )

    def test_holdout_authorization_validator_rejects_draft(self):
        with tempfile.TemporaryDirectory() as directory:
            auth_path = Path(directory) / "authorization.json"
            auth_path.write_text(json.dumps({
                "schema": holdout_auth.AUTH_SCHEMA,
                "status": "DRAFT",
            }), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "not APPROVED"):
                holdout_auth.validate(
                    auth_path, Path(directory), "a" * 40,
                    holdout_auth.BRANCH_PREFIX + "draft-authorization-001",
                )

    def test_preflight_uses_separate_seed_namespace(self):
        self.assertNotEqual(
            preflight.seed("dataset", "F1_balanced_M30_R20", 0),
            preflight.seed("C0", "F1_balanced_M30_R20", 0),
        )
        self.assertEqual(
            preflight.seed("dataset", "F1_balanced_M30_R20", 0),
            preflight.seed("dataset", "F1_balanced_M30_R20", 0),
        )

    def test_preflight_never_calls_coverage_adjudicator_or_emits_coverage(self):
        preflight.K_PER_CELL = 1
        def fake_compare(rows, **kwargs):
            family = kwargs["family"]
            return SimpleNamespace(
                baseline=SimpleNamespace(method_id=IMPLEMENTED_METHODS[family][0]),
                candidates=(SimpleNamespace(method_id=IMPLEMENTED_METHODS[family][1]),),
            )
        with tempfile.TemporaryDirectory() as directory:
            with patch.object(preflight, "compare_dataset", side_effect=fake_compare) as compare, patch.object(
                preflight, "generate_holdout_dataset", return_value=((0.0, 1.0), (1.0, 0.0))
            ):
                result = preflight.run_preflight(Path(directory))
                self.assertEqual(compare.call_count, 2)
                self.assertEqual(result["total_datasets"], 2)
                self.assertEqual(result["coverage_adjudication"], "NOT_RUN")
                self.assertFalse(result["scientific_holdout_executed"])
                self.assertTrue(all(
                    cell["adjudicate_matched_datasets_called"] is False
                    and cell["coverage_adjudication"] == "NOT_RUN"
                    for cell in result["cells"]
                ))
                persisted = json.loads((Path(directory) / "resource_preflight.json").read_text())
                self.assertEqual(persisted["total_datasets"], 2)
                self.assertNotIn("metrics", persisted)
                self.assertNotIn("coverage_results", persisted)
                self.assertNotIn("coverage_rate", json.dumps(persisted).lower())


if __name__ == "__main__":
    unittest.main()
