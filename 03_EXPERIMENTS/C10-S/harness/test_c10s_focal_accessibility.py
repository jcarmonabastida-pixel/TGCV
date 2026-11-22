import unittest

from c10s_focal_accessibility import (
    FocalAccessibilityContractError, FocalAccessibilityInput,
    FocalDependencyRoute, FocalPredicateEvidence, adjudicate_focal_accessibility,
)


class FocalAccessibilityTests(unittest.TestCase):
    def predicate(self, role, truth="1", observed="1", coverage="COMPLETE"):
        return FocalPredicateEvidence(
            role, truth, observed, coverage, "UE-1", "TAU2-v3", "TAU2-SEMVER-3", "BND-1",
            "CTX-1", "SNAP-1", "SNAPVER-1", "PRED-v1", f"PROV-{role}",
        )

    def route(self, route_id, dep="1", local_block="0", components=None, coverage="COMPLETE"):
        names = ("C_install", "C_integrity", "C_compat", "C_oper")
        values = tuple(components) if components is not None else (dep,) * 4
        observed = tuple((name, value) for name, value in zip(names, values))
        truth = tuple((name, value) for name, value in zip(names, values))
        return FocalDependencyRoute(
            route_id, "ROUTE-v1", "UE-1", "TAU2-v3", "BND-1",
            "TAU2-SEMVER-3", "BND-1", "CTX-1", "SNAP-1", "SNAPVER-1",
            truth, local_block, observed, local_block,
            coverage, f"PROV-{route_id}",
        )

    def source(self, *, predicates=None, routes=None, exhaustive=True, global_block="0"):
        return FocalAccessibilityInput(
            "UE-1", "TAU2-v3", "TAU2-SEMVER-3", "BND-1", "CTX-1", "SNAP-1", "SNAPVER-1",
            tuple(predicates or [self.predicate(x) for x in ("ID", "REL", "COND", "AUTH", "RES")]),
            tuple(routes if routes is not None else [self.route("R1")]),
            exhaustive, global_block, global_block, "COMPLETE", True,
            "ALL_ADMISSIBLE_ROUTES", "C10S-AF-v0.1",
        )

    def test_all_constitutive_predicates_and_route_true(self):
        result = adjudicate_focal_accessibility(self.source())
        self.assertEqual(result.accessibility_truth, "1")
        self.assertEqual(result.dep_truth, "1")

    def test_local_block_does_not_block_valid_alternative_route(self):
        result = adjudicate_focal_accessibility(self.source(
            routes=[self.route("R1", "1", "1"), self.route("R2", "1", "0")]
        ))
        self.assertEqual(dict(result.route_truth), {"R1": "0", "R2": "1"})
        self.assertEqual(result.dep_truth, "1")
        self.assertEqual(result.accessibility_truth, "1")

    def test_global_block_requires_all_routes_and_blocks_accessibility(self):
        result = adjudicate_focal_accessibility(self.source(global_block="1"))
        self.assertEqual(result.accessibility_truth, "0")

    def test_incomplete_route_catalog_never_proves_no_dependency(self):
        result = adjudicate_focal_accessibility(self.source(
            routes=[self.route("R1", "0", "0")], exhaustive=False
        ))
        self.assertEqual(result.dep_truth, "?")
        self.assertEqual(result.accessibility_truth, "?")

    def test_exhaustive_all_failed_routes_prove_no_dependency(self):
        result = adjudicate_focal_accessibility(self.source(
            routes=[self.route("R1", "0", "0")], exhaustive=True
        ))
        self.assertEqual(result.dep_truth, "0")
        self.assertEqual(result.accessibility_truth, "0")

    def test_unknown_predicate_propagates_without_compensating_score(self):
        predicates = [self.predicate(x, truth="?" if x == "AUTH" else "1")
                      for x in ("ID", "REL", "COND", "AUTH", "RES")]
        result = adjudicate_focal_accessibility(self.source(predicates=predicates))
        self.assertEqual(result.accessibility_truth, "?")

    def test_information_and_residual_are_not_accepted_as_extra_predicates(self):
        predicates = [self.predicate(x) for x in ("ID", "REL", "COND", "AUTH", "RES")]
        predicates.extend([self.predicate("C_INFO"), self.predicate("C_OTHER")])
        with self.assertRaises(FocalAccessibilityContractError):
            adjudicate_focal_accessibility(self.source(predicates=predicates))

    def test_observed_coverage_does_not_rewrite_dgp_truth(self):
        predicates = [self.predicate(x, truth="1", observed="?", coverage="INCOMPLETE")
                      if x == "AUTH" else self.predicate(x)
                      for x in ("ID", "REL", "COND", "AUTH", "RES")]
        result = adjudicate_focal_accessibility(self.source(predicates=predicates))
        self.assertEqual(result.accessibility_truth, "1")
        self.assertEqual(result.observed_accessibility, "?")
        self.assertFalse(result.observed_coverage_complete)

    def test_route_identity_mismatch_fails_closed(self):
        bad = FocalDependencyRoute(
            "R1", "ROUTE-v1", "UE-OTHER", "TAU2-v3", "BND-1",
            "TAU2-SEMVER-3", "BND-1", "CTX-1", "SNAP-1", "SNAPVER-1",
            (("C_install", "1"),), "0",
            (("C_install", "1"),), "0", "COMPLETE", "PROV-R1",
        )
        with self.assertRaises(FocalAccessibilityContractError):
            adjudicate_focal_accessibility(self.source(routes=[bad]))

    def test_route_keeps_named_technical_dependencies_separate(self):
        result = adjudicate_focal_accessibility(self.source(
            routes=[self.route("R1", components=("1", "1", "0", "1"))]
        ))
        self.assertEqual(result.route_truth, (("R1", "0"),))
        self.assertEqual(result.dep_truth, "0")

    def test_empty_exhaustive_route_catalog_proves_no_dependency(self):
        result = adjudicate_focal_accessibility(self.source(routes=[], exhaustive=True))
        self.assertEqual(result.dep_truth, "0")
        self.assertEqual(result.accessibility_truth, "0")

    def test_incomplete_observed_route_coverage_does_not_change_truth(self):
        result = adjudicate_focal_accessibility(self.source(
            routes=[self.route("R1", coverage="INCOMPLETE")]
        ))
        self.assertEqual(result.accessibility_truth, "1")
        self.assertEqual(result.observed_accessibility, "?")
        self.assertFalse(result.observed_coverage_complete)

    def test_block_scope_must_be_universal(self):
        source = FocalAccessibilityInput(
            "UE-1", "TAU2-v3", "TAU2-SEMVER-3", "BND-1", "CTX-1", "SNAP-1", "SNAPVER-1",
            tuple(self.predicate(x) for x in ("ID", "REL", "COND", "AUTH", "RES")),
            (self.route("R1"),), True, "0", "0", "COMPLETE", True,
            "LOCAL_ROUTE_ONLY", "C10S-AF-v0.1",
        )
        with self.assertRaises(FocalAccessibilityContractError):
            adjudicate_focal_accessibility(source)


if __name__ == "__main__":
    unittest.main()
