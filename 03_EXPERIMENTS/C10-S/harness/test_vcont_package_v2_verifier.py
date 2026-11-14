"""Pure tests for the independent package-v2 verifier primitives."""
import unittest

import rfc8785
from vcont_package_v2_verify import (
    PACKAGE_PATHS,
    PackageVerificationError,
    _check_registered_uint64,
    _check_report,
    _safe_archive_path,
    _strict_json,
    _uint64,
    _historical_fingerprint,
)


class IndependentVerifierPrimitiveTests(unittest.TestCase):
    def test_exact_fourteen_path_inventory_is_unique(self):
        self.assertEqual(len(PACKAGE_PATHS), 14)
        self.assertEqual(len(set(PACKAGE_PATHS)), 14)

    def test_strict_json_accepts_canonical_payload_with_one_lf(self):
        raw = rfc8785.dumps({"a": 1, "b": [True, None]}) + b"\n"
        value, canonical = _strict_json(raw, "fixture.json")
        self.assertEqual(value, {"a": 1, "b": [True, None]})
        self.assertEqual(canonical, raw[:-1])

    def test_strict_json_rejects_duplicate_keys(self):
        with self.assertRaises(PackageVerificationError):
            _strict_json(b'{"a":1,"a":2}\n', "duplicate.json")

    def test_strict_json_rejects_noncanonical_whitespace_and_missing_lf(self):
        for raw in (b'{ "a":1}\n', b'{"a":1}'):
            with self.subTest(raw=raw), self.assertRaises(PackageVerificationError):
                _strict_json(raw, "noncanonical.json")

    def test_strict_json_rejects_bom_and_nonfinite_constants(self):
        for raw in (b"\xef\xbb\xbf{}\n", b'{"x":NaN}\n'):
            with self.subTest(raw=raw), self.assertRaises(PackageVerificationError):
                _strict_json(raw, "invalid.json")

    def test_uint64_exact_boundary_roundtrips(self):
        for value in (0, (1 << 53) - 1, 1 << 53, (1 << 64) - 1):
            wrapper = {"$type": "uint64", "decimal": str(value)}
            self.assertEqual(_uint64(wrapper, "boundary"), value)

    def test_uint64_rejects_bool_float_and_noncanonical_decimal(self):
        invalid = (
            True, 1.0, -1, (1 << 64),
            {"$type": "uint64", "decimal": "00"},
            {"$type": "uint64", "decimal": "+1"},
            {"$type": "uint64", "decimal": "١"},
            {"$type": "uint64", "decimal": "1e2"},
            {"$type": "uint64", "decimal": "1", "extra": 0},
        )
        for value in invalid:
            with self.subTest(value=value), self.assertRaises(PackageVerificationError):
                _uint64(value, "invalid")

    def test_archive_path_rejects_parent_absolute_and_backslash(self):
        for path in ("../escape", "/absolute", "a/../b", "a\\b", "a//b"):
            with self.subTest(path=path), self.assertRaises(PackageVerificationError):
                _safe_archive_path(path)

    def test_report_accepts_complete_legacy_fingerprint_and_duplicate_views(self):
        manifest = {"temporal_manifest": [], "pair_ledger": []}
        fingerprint = _historical_fingerprint(manifest)
        report = {
            "manifest": manifest,
            "report_fingerprint": fingerprint,
            "temporal_manifest": [],
            "pair_ledger": [],
            "coverage": {"required_pairs": 52, "observed_pairs": 52, "scenario_count": 13},
            "scenario_reports": {
                f"S{i:02d}": {
                    "per_outer_replicate": [
                        {"outer_replicate_id": "outer-000000", "run": [{}, {}, {}, {}]}
                    ]
                }
                for i in range(13)
            },
        }
        _check_report({
            "schema_id": "TGCV-C10S-VCONT-REPORT-SNAPSHOT",
            "schema_version": "2.1.0",
            "payload_type": "TGCV-C10S-VCONT-BENCHMARK-REPORT",
            "legacy_report_fingerprint": fingerprint,
            "legacy_fingerprint_algorithm": "TGCV-C10S-VCONT-LEGACY-REPORT-FINGERPRINT-PYJSON-SORTKEYS-COMPACT-SHA256-1",
            "report": report,
        })

    def test_report_rejects_root_nested_manifest_divergence(self):
        fingerprint = _historical_fingerprint({"temporal_manifest": [], "pair_ledger": []})
        report = {
            "manifest": {"temporal_manifest": [], "pair_ledger": []},
            "report_fingerprint": fingerprint,
            "temporal_manifest": [{"run_id": "different"}],
            "pair_ledger": [],
            "coverage": {"required_pairs": 52, "observed_pairs": 52, "scenario_count": 13},
            "scenario_reports": {},
        }
        with self.assertRaises(PackageVerificationError):
            _check_report({
                "schema_id": "TGCV-C10S-VCONT-REPORT-SNAPSHOT",
                "schema_version": "2.1.0",
                "payload_type": "TGCV-C10S-VCONT-BENCHMARK-REPORT",
                "legacy_report_fingerprint": fingerprint,
                "legacy_fingerprint_algorithm": "legacy",
                "report": report,
            })

    def test_registered_seed_pointers_require_typed_wrappers(self):
        wrapper = {"$type": "uint64", "decimal": "0"}
        files = {
            "seeds/evaluation_seed_assignments.json": {"row_count": 1, "rows": [{
                "world_seed": wrapper, "z_assignment_seed": wrapper, "g_assignment_seed": wrapper,
            }]},
            "seeds/calibration_seed_manifest.json": {"row_count": 1, "rows": [{
                "world_seed": wrapper, "z_assignment_seed": wrapper, "g_assignment_seed": wrapper,
            }]},
            "runs/temporal_manifest.json": {"row_count": 1, "rows": [{
                "world_seed": wrapper, "z_assignment_seed": wrapper, "g_assignment_seed": wrapper,
            }]},
            "report/report.json": {"report": {
                "temporal_manifest": [{"world_seed": wrapper, "z_assignment_seed": wrapper, "g_assignment_seed": wrapper}],
                "manifest": {
                    "temporal_manifest": [{"world_seed": wrapper, "z_assignment_seed": wrapper, "g_assignment_seed": wrapper}],
                    "pair_ledger": [{"contributions": [{"world_seed": wrapper}]}],
                },
                "pair_ledger": [{"contributions": [{"world_seed": wrapper}]}],
                "scenario_reports": {
                    "S": {"per_outer_replicate": [{"run": [
                        {"seed": wrapper}, {}, {}, {
                            "world_seed": wrapper, "z_assignment_seed": wrapper, "g_assignment_seed": wrapper,
                        }
                    ]}]}
                },
            }},
            "runs/run_records.json": {"outer_world_evidence_records": [{"key": {"world_seed": wrapper}}]},
        }
        counts = _check_registered_uint64(files)
        self.assertEqual(len(counts), 5)
        self.assertTrue(all(count > 0 for count in counts))

    def test_unregistered_uint64_wrapper_is_rejected(self):
        files = {
            "seeds/evaluation_seed_assignments.json": {"row_count": 1, "rows": [{
                "world_seed": {"$type": "uint64", "decimal": "0"},
                "z_assignment_seed": {"$type": "uint64", "decimal": "1"},
                "g_assignment_seed": {"$type": "uint64", "decimal": "2"},
            }]},
            "seeds/calibration_seed_manifest.json": {"row_count": 1, "rows": [{
                "world_seed": {"$type": "uint64", "decimal": "0"},
                "z_assignment_seed": {"$type": "uint64", "decimal": "1"},
                "g_assignment_seed": {"$type": "uint64", "decimal": "2"},
            }]},
            "runs/temporal_manifest.json": {"row_count": 1, "rows": [{
                "world_seed": {"$type": "uint64", "decimal": "0"},
                "z_assignment_seed": {"$type": "uint64", "decimal": "1"},
                "g_assignment_seed": {"$type": "uint64", "decimal": "2"},
            }]},
            "report/report.json": {"report": {
                "temporal_manifest": [{"world_seed": {"$type": "uint64", "decimal": "0"},
                                       "z_assignment_seed": {"$type": "uint64", "decimal": "1"},
                                       "g_assignment_seed": {"$type": "uint64", "decimal": "2"}}],
                "manifest": {
                    "temporal_manifest": [{"world_seed": {"$type": "uint64", "decimal": "0"},
                                           "z_assignment_seed": {"$type": "uint64", "decimal": "1"},
                                           "g_assignment_seed": {"$type": "uint64", "decimal": "2"}}],
                    "pair_ledger": [{"contributions": [{"world_seed": {"$type": "uint64", "decimal": "0"}}]}],
                },
                "pair_ledger": [{"contributions": [{"world_seed": {"$type": "uint64", "decimal": "0"}}]}],
                "scenario_reports": {"S": {"per_outer_replicate": [{"run": [
                    {"seed": {"$type": "uint64", "decimal": "0"}}, {}, {},
                    {"world_seed": {"$type": "uint64", "decimal": "0"},
                     "z_assignment_seed": {"$type": "uint64", "decimal": "1"},
                     "g_assignment_seed": {"$type": "uint64", "decimal": "2"}}
                ]}]}},
                "unexpected": {"seed": {"$type": "uint64", "decimal": "7"}},
            }},
            "runs/run_records.json": {"outer_world_evidence_records": [{"key": {"world_seed": {"$type": "uint64", "decimal": "0"}}}]},
        }
        with self.assertRaises(PackageVerificationError):
            _check_registered_uint64(files)


if __name__ == "__main__":
    unittest.main()
