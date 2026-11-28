"""Pure package-v2 writer boundary tests; no synthetic producer is invoked."""
import io
import tarfile
import unittest
from types import SimpleNamespace

from vcont_package_v2 import (
    PACKAGE_PATHS,
    PackageBuildError,
    VContPackageCompanionsV2,
    build_deterministic_tar_v2,
    serialize_package_files_v2,
)


class PackageV2SerializationTests(unittest.TestCase):
    def test_tar_is_byte_deterministic_for_identical_inputs(self):
        files = {"report/report.json": b"{}\n", "manifest.json": b"{}\n"}
        self.assertEqual(build_deterministic_tar_v2(files), build_deterministic_tar_v2(files))

    def test_tar_entries_have_normalized_metadata_and_lexical_order(self):
        files = {"z/file.json": b"z", "a/file.json": b"a"}
        archive_bytes = build_deterministic_tar_v2(files)
        with tarfile.open(fileobj=io.BytesIO(archive_bytes), mode="r:") as archive:
            members = archive.getmembers()
        self.assertEqual([item.name for item in members], ["a/file.json", "z/file.json"])
        for item in members:
            self.assertEqual(item.mtime, 0)
            self.assertEqual((item.uid, item.gid), (0, 0))
            self.assertEqual((item.uname, item.gname), ("", ""))
            self.assertEqual(item.mode, 0o644)
            self.assertEqual(item.type, tarfile.REGTYPE)

    def test_tar_rejects_parent_traversal_and_absolute_paths(self):
        for path in ("../escape", "/absolute", "a/../b", "a\\b"):
            with self.subTest(path=path), self.assertRaises(PackageBuildError):
                build_deterministic_tar_v2({path: b"x"})

    def test_tar_rejects_casefold_collisions_and_non_bytes(self):
        with self.assertRaises(PackageBuildError):
            build_deterministic_tar_v2({"A.json": b"a", "a.json": b"b"})
        with self.assertRaises(PackageBuildError):
            build_deterministic_tar_v2({"a.json": bytearray(b"a")})

    def test_writer_rejects_unknown_profile_before_serialization(self):
        with self.assertRaises(PackageBuildError):
            serialize_package_files_v2(None, None, None, profile="DIAGNOSTIC")

    def test_writer_requires_complete_capture_and_companions(self):
        captured = SimpleNamespace(
            capture_id="a" * 64,
            benchmark_export_id="a" * 64,
            matrix_capture=None,
            report_snapshot=None,
        )
        with self.assertRaises(PackageBuildError):
            serialize_package_files_v2(
                captured, object(), VContPackageCompanionsV2({}),
                profile="CONFIRMATORY",
            )

    def test_frozen_inventory_contains_fourteen_unique_paths(self):
        self.assertEqual(len(PACKAGE_PATHS), 14)
        self.assertEqual(len(set(PACKAGE_PATHS)), 14)
        self.assertIn("report/report.json", PACKAGE_PATHS)
        self.assertIn("manifest.json", PACKAGE_PATHS)


if __name__ == "__main__":
    unittest.main()
