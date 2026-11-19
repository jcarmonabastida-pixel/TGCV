from __future__ import annotations

from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import validate_c10s_post_holdout_f5_b2_b3_development_calibration_authorization as validator


class F5DevelopmentAuthorizationTests(unittest.TestCase):
    def _authorization(self, root: Path, branch: str, code_commit: str) -> dict:
        now = datetime.now(timezone.utc)
        auth = {
            "schema": validator.AUTH_SCHEMA,
            "status": "APPROVED",
            "authorization_id": "C10S-F5-B2B3-20261119",
            "authorization_branch": branch,
            "scope": "C10S_F5_B2_B3_DEVELOPMENT_CALIBRATION_ONLY",
            "f5_b2_b3_authorized": True,
            "f1_a2_a3_authorized": False,
            "tier_b_authorized": False,
            "comparative_holdout_authorized": False,
            "c10_scientific_execution_authorized": False,
            "mcse_interval_construction_authorized": False,
            "approved_by": "USER_EXPLICIT_APPROVAL",
            "approved_at_utc": now.isoformat(),
            "expires_utc": (now + timedelta(hours=24)).isoformat(),
            "spec_id": validator.SPEC_ID,
            "spec_version": "1.0",
            "seed_schedule_id": validator.SEED_SCHEDULE_ID,
            "cells": validator.EXPECTED_CELLS,
            "k_calibration_per_cell": 5000,
            "k_validation_per_cell": 5000,
            "c0_bootstrap_replicates": 1000,
            "c5_bootstrap_replicates": 1000,
            "b3_selected_per_cell": 250,
            "b3_bootstrap_b1000": 1000,
            "b3_bootstrap_b4000": 4000,
            "b3_selection_rule": "SHA256(schedule_id|B3_SELECTION|cell_id|dataset_id), ascending, first 250",
            "approved_code_commit": code_commit,
        }
        for key, relative in {
            "spec_sha256": validator.SPEC_PATH,
            "runner_sha256": validator.RUNNER_PATH,
            "holdout_generator_sha256": validator.HOLDOUT_GENERATOR_PATH,
            "fixtures_sha256": validator.FIXTURES_PATH,
            "engine_sha256": validator.ENGINE_PATH,
            "bootstrap_sha256": validator.BOOTSTRAP_PATH,
            "diagnostics_sha256": validator.DIAGNOSTICS_PATH,
            "interface_sha256": validator.INTERFACE_PATH,
            "oracle_sha256": validator.ORACLE_PATH,
            "dependency_lock_sha256": validator.LOCK_PATH,
            "workflow_sha256": validator.WORKFLOW_PATH,
            "validator_sha256": validator.VALIDATOR_PATH,
        }.items():
            target = root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(relative, encoding="utf-8")
            auth[key] = validator.sha256(target)
        return auth

    def test_draft_or_missing_approval_fails_closed(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "authorization.json"
            path.write_text(json.dumps({"schema": validator.AUTH_SCHEMA, "status": "DRAFT"}), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "not APPROVED"):
                validator.validate(
                    path, Path(tmp), "a" * 40,
                    validator.BRANCH_PREFIX + "C10S-F5-B2B3-20261119",
                )

    def test_scope_cannot_expand_to_f1_or_causal_execution(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            branch = validator.BRANCH_PREFIX + "C10S-F5-B2B3-20261119"
            auth = self._authorization(root, branch, "b" * 40)
            auth["f1_a2_a3_authorized"] = True
            path = root / "auth.json"
            path.write_text(json.dumps(auth), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "f1_a2_a3_authorized"):
                validator.validate(path, root, "a" * 40, branch)

    def test_wrong_frozen_k_or_b_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            branch = validator.BRANCH_PREFIX + "C10S-F5-B2B3-20261119"
            auth = self._authorization(root, branch, "b" * 40)
            auth["b3_selected_per_cell"] = 249
            path = root / "auth.json"
            path.write_text(json.dumps(auth), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "b3_selected_per_cell"):
                validator.validate(path, root, "a" * 40, branch)

    def test_exact_parent_and_hash_bound_authorization_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            branch = validator.BRANCH_PREFIX + "C10S-F5-B2B3-20261119"
            auth = self._authorization(root, branch, "b" * 40)
            path = root / "auth.json"
            path.write_text(json.dumps(auth), encoding="utf-8")
            def fake_git(*args):
                if args == ("rev-parse", "HEAD"):
                    return "a" * 40
                if args == ("rev-list", "--parents", "-n", "1", "a" * 40):
                    return "a" * 40 + " " + "b" * 40
                if args == ("diff-tree", "--no-commit-id", "--name-only", "-r", "a" * 40):
                    return validator.AUTH_PATH
                raise AssertionError(args)
            with patch.object(validator, "git", side_effect=fake_git):
                result = validator.validate(path, root, "a" * 40, branch)
            self.assertEqual(result["authorization_id"], auth["authorization_id"])
            self.assertEqual(result["approved_code_commit"], "b" * 40)
            self.assertTrue(result["f5_b2_b3_authorized"])
            self.assertFalse(result["c10_scientific_execution_authorized"])

    def test_wrong_authorization_parent_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            branch = validator.BRANCH_PREFIX + "C10S-F5-B2B3-20261119"
            auth = self._authorization(root, branch, "b" * 40)
            path = root / "auth.json"
            path.write_text(json.dumps(auth), encoding="utf-8")
            def fake_git(*args):
                if args == ("rev-parse", "HEAD"):
                    return "a" * 40
                if args == ("rev-list", "--parents", "-n", "1", "a" * 40):
                    return "a" * 40 + " " + "c" * 40
                raise AssertionError(args)
            with patch.object(validator, "git", side_effect=fake_git):
                with self.assertRaisesRegex(ValueError, "sole parent"):
                    validator.validate(path, root, "a" * 40, branch)


if __name__ == "__main__":
    unittest.main()
