#!/usr/bin/env python3
"""Minimum deterministic unit tests for TR131_CROSS_DOMAIN_COMPARISON_RUNNER_001."""
from __future__ import annotations
import json, tempfile, unittest
from pathlib import Path
import TR131_CROSS_DOMAIN_COMPARISON_RUNNER_001 as R

P=R.PROTOCOL
def rec(domain="TEST",rid="r",t0=("a",),t1=("a",),real="a"):
    return {"domain":domain,"record_id":rid,"S_t":{"x":0},"T_acc_t":list(t0),
            "T_real_t":real,"S_t1":{"x":1},"T_acc_t1":list(t1)}

class TestMinimum(unittest.TestCase):
    def test_unchanged_accessibility(self):
        d=R.derive(rec(t0=("a","b"),t1=("a","b")))
        self.assertEqual((d["G"],d["L"],d["P"],d["R"],d["D"]),(0,0,2,0,0))
        self.assertIn("STABILITY",d["FPE"])

    def test_pure_addition(self):
        d=R.derive(rec(t0=("a",),t1=("a","b")))
        self.assertEqual((d["G"],d["L"],d["P"],d["R"],d["D"]),(1,0,1,1,1))
        self.assertIn("EXPANSION",d["FPE"])

    def test_pure_loss(self):
        d=R.derive(rec(t0=("a","b"),t1=("a",)))
        self.assertEqual((d["G"],d["L"],d["P"],d["R"],d["D"]),(0,1,1,1,-1))
        self.assertIn("CONTRACTION",d["FPE"])

    def test_simultaneous_addition_and_loss(self):
        d=R.derive(rec(t0=("a","b"),t1=("b","c")))
        self.assertEqual((d["G"],d["L"],d["P"],d["R"],d["D"]),(1,1,1,2,0))
        self.assertIn("TURNOVER",d["FPE"])

    def test_duplicate_identity_rejected(self):
        with self.assertRaisesRegex(ValueError,"duplicate"):
            R.derive(rec(t0=("a","a"),t1=("a",)))

    def test_missing_required_field_rejected(self):
        x=rec(); del x["T_acc_t1"]
        with self.assertRaisesRegex(ValueError,"MISSING_REQUIRED_FIELDS"):
            R.derive(x)

    def test_trajectory_insufficient_is_not_testable_by_deriver(self):
        # A single transition has no basis for trajectory divergence.
        d=R.derive(rec())
        self.assertEqual(d["record_id"],"r")
        self.assertNotIn("trajectory_divergence",d)

    def test_protocol_and_domain_comparison(self):
        package={"protocol":P,"records":[rec("VisitAll","v"),rec("PRISM","p",("pick",),("read",),"pick")]}
        out=R.analyze(package)
        self.assertEqual(out["domains"],["PRISM","VisitAll"])
        self.assertEqual(out["record_count"],2)

    def test_deterministic_output_hash(self):
        package={"protocol":P,"records":[rec("VisitAll","v",("a",),("a","b"))]}
        self.assertEqual(R.analyze(package)["output_sha256"],R.analyze(package)["output_sha256"])

if __name__=="__main__":
    unittest.main(verbosity=2)
