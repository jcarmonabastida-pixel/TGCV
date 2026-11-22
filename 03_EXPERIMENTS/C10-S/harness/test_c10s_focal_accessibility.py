import unittest

from c10s_focal_accessibility import (
    FocalAccessibilityContractError, FocalAccessibilityInput,
    D2FocalAccessibilitySpecification, FocalDependencyRoute,
    FocalPredicateEvidence, SemanticTransformationMatch,
    adjudicate_d2_focal_potentials, adjudicate_focal_accessibility,
    derive_focal_opening,
)


class FocalAccessibilityTests(unittest.TestCase):
    def predicate(self, role, truth="1", observed="1", coverage="COMPLETE", snapshot_id="SNAP-1", transformation_id="TAU2-v3", transformation_version="TAU2-SEMVER-3"):
        return FocalPredicateEvidence(
            role, truth, observed, coverage, "UE-1", transformation_id, transformation_version, "BND-1",
            "CTX-1", snapshot_id, "SNAPVER-1", "PRED-v1", f"PROV-{role}",
        )

    def route(self, route_id, dep="1", local_block="0", components=None, coverage="COMPLETE", snapshot_id="SNAP-1", transformation_id="TAU2-v3", transformation_version="TAU2-SEMVER-3"):
        names = ("C_install", "C_integrity", "C_compat", "C_oper")
        values = tuple(components) if components is not None else (dep,) * 4
        observed = tuple((name, value) for name, value in zip(names, values))
        truth = tuple((name, value) for name, value in zip(names, values))
        return FocalDependencyRoute(
            route_id, "ROUTE-v1", "UE-1", transformation_id, transformation_version,
            "BND-1", "CTX-1", snapshot_id, "SNAPVER-1",
            truth, local_block, observed, local_block,
            coverage, f"PROV-{route_id}",
        )

    def source(self, *, predicates=None, routes=None, exhaustive=True, global_block="0", snapshot_id="SNAP-1", truth="1", transformation_id="TAU2-v3", transformation_version="TAU2-SEMVER-3"):
        return FocalAccessibilityInput(
            "UE-1", transformation_id, transformation_version, "BND-1", "CTX-1", snapshot_id, "SNAPVER-1",
            tuple(predicates or [self.predicate(x, truth=truth, snapshot_id=snapshot_id, transformation_id=transformation_id, transformation_version=transformation_version) for x in ("ID", "REL", "COND", "AUTH", "RES")]),
            tuple(routes if routes is not None else [self.route("R1", dep=truth, snapshot_id=snapshot_id, transformation_id=transformation_id, transformation_version=transformation_version)]),
            exhaustive, global_block, global_block, "COMPLETE", "BLOCK-v1", "BLOCK-PROV",
            True, "ROUTE-CATALOG-v1", "ROUTE-CATALOG-PROV", "ROUTE-CATALOG-OBS-PROV",
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
            "R1", "ROUTE-v1", "UE-OTHER", "TAU2-v3", "TAU2-SEMVER-3",
            "BND-1", "CTX-1", "SNAP-1", "SNAPVER-1",
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

    def test_focal_opening_requires_explicit_semantic_match(self):
        baseline = adjudicate_focal_accessibility(self.source(
            snapshot_id="SNAP-BASE", global_block="1"
        ))
        post = adjudicate_focal_accessibility(self.source(snapshot_id="SNAP-POST"))
        identity = SemanticTransformationMatch(
            "UE-1", "BND-1", "CTX-1", "TAU2-v3", "TAU2-SEMVER-3",
            "TAU2-v3", "TAU2-SEMVER-3", "SNAP-BASE", "SNAPVER-1", "SNAP-POST", "SNAPVER-1",
            "MATCHED", "TID-MATCH-v1", "ADJUDICATION-001",
        )
        result = derive_focal_opening(baseline, post, identity)
        self.assertEqual(result.d_f_truth, "1")
        self.assertEqual(result.d_f_observed, "1")

    def test_explicit_adjudication_can_match_semantic_identity_across_versions(self):
        baseline = adjudicate_focal_accessibility(self.source(snapshot_id="SNAP-BASE", global_block="1"))
        post = adjudicate_focal_accessibility(self.source(
            snapshot_id="SNAP-POST", transformation_id="TAU2-v4",
            transformation_version="TAU2-SEMVER-4",
        ))
        identity = SemanticTransformationMatch(
            "UE-1", "BND-1", "CTX-1", "TAU2-v3", "TAU2-SEMVER-3",
            "TAU2-v4", "TAU2-SEMVER-4", "SNAP-BASE", "SNAPVER-1", "SNAP-POST", "SNAPVER-1",
            "MATCHED", "TID-MATCH-v1", "ADJUDICATION-005",
        )
        result = derive_focal_opening(baseline, post, identity)
        self.assertEqual(result.d_f_truth, "1")

    def test_unmatched_semantic_identity_is_not_comparable(self):
        baseline = adjudicate_focal_accessibility(self.source(snapshot_id="SNAP-BASE", global_block="1"))
        post = adjudicate_focal_accessibility(self.source(snapshot_id="SNAP-POST", transformation_id="TAU2-v4", transformation_version="TAU2-SEMVER-4"))
        identity = SemanticTransformationMatch(
            "UE-1", "BND-1", "CTX-1", "TAU2-v3", "TAU2-SEMVER-3",
            "TAU2-v4", "TAU2-SEMVER-4", "SNAP-BASE", "SNAPVER-1", "SNAP-POST", "SNAPVER-1",
            "NOT_MATCHED", "TID-MATCH-v1", "ADJUDICATION-002",
        )
        result = derive_focal_opening(baseline, post, identity)
        self.assertEqual(result.d_f_truth, "NOT_COMPARABLE")

    def test_unresolved_semantic_identity_keeps_opening_unknown(self):
        baseline = adjudicate_focal_accessibility(self.source(snapshot_id="SNAP-BASE", global_block="1"))
        post = adjudicate_focal_accessibility(self.source(snapshot_id="SNAP-POST", transformation_id="TAU2-v4", transformation_version="TAU2-SEMVER-4"))
        identity = SemanticTransformationMatch(
            "UE-1", "BND-1", "CTX-1", "TAU2-v3", "TAU2-SEMVER-3",
            "TAU2-v4", "TAU2-SEMVER-4", "SNAP-BASE", "SNAPVER-1", "SNAP-POST", "SNAPVER-1",
            "UNRESOLVED", "TID-MATCH-v1", "ADJUDICATION-003",
        )
        result = derive_focal_opening(baseline, post, identity)
        self.assertEqual(result.d_f_truth, "?")

    def test_opening_truth_is_separate_from_observed_opening(self):
        baseline = adjudicate_focal_accessibility(self.source(snapshot_id="SNAP-BASE", global_block="1"))
        observed_incomplete = [self.predicate(x, observed="?", coverage="INCOMPLETE", snapshot_id="SNAP-POST")
                               if x == "AUTH" else self.predicate(x, snapshot_id="SNAP-POST")
                               for x in ("ID", "REL", "COND", "AUTH", "RES")]
        post = adjudicate_focal_accessibility(self.source(
            snapshot_id="SNAP-POST", predicates=observed_incomplete
        ))
        identity = SemanticTransformationMatch(
            "UE-1", "BND-1", "CTX-1", "TAU2-v3", "TAU2-SEMVER-3",
            "TAU2-v3", "TAU2-SEMVER-3", "SNAP-BASE", "SNAPVER-1", "SNAP-POST", "SNAPVER-1",
            "MATCHED", "TID-MATCH-v1", "ADJUDICATION-004",
        )
        result = derive_focal_opening(baseline, post, identity)
        self.assertEqual(result.d_f_truth, "1")
        self.assertEqual(result.d_f_observed, "?")


    def d2_spec(self, *, post_z1_components=None, post_z1_res="1",
                exhaustive=True, auth="1", post_z1_transformation=("TAU2-v3", "TAU2-SEMVER-3"),
                match_z1="MATCHED"):
        unit = "UE-1"
        baseline = self.source(
            snapshot_id="SNAP-BASE",
            routes=[self.route("R1", dep="0", snapshot_id="SNAP-BASE")],
            exhaustive=exhaustive,
            predicates=[self.predicate(
                role, truth=auth if role == "AUTH" else "1",
                snapshot_id="SNAP-BASE",
            ) for role in ("ID", "REL", "COND", "AUTH", "RES")],
        )
        post0 = self.source(
            snapshot_id="SNAP-Z0",
            routes=[self.route("R1", dep="0", snapshot_id="SNAP-Z0")],
        )
        post1_predicates = [
            self.predicate(
                role,
                truth=post_z1_res if role == "RES" else "1",
                snapshot_id="SNAP-Z1",
                transformation_id=post_z1_transformation[0],
                transformation_version=post_z1_transformation[1],
            ) for role in ("ID", "REL", "COND", "AUTH", "RES")
        ]
        post1_route = self.route(
            "R1", components=post_z1_components, snapshot_id="SNAP-Z1",
            transformation_id=post_z1_transformation[0],
            transformation_version=post_z1_transformation[1],
        )
        post1 = self.source(
            snapshot_id="SNAP-Z1", predicates=post1_predicates,
            routes=[post1_route], transformation_id=post_z1_transformation[0],
            transformation_version=post_z1_transformation[1],
        )
        matches = (
            (0, SemanticTransformationMatch(
                unit, "BND-1", "CTX-1", "TAU2-v3", "TAU2-SEMVER-3",
                "TAU2-v3", "TAU2-SEMVER-3", "SNAP-BASE", "SNAPVER-1",
                "SNAP-Z0", "SNAPVER-1", "MATCHED", "TID-MATCH-v1", "MATCH-Z0",
            )),
            (1, SemanticTransformationMatch(
                unit, "BND-1", "CTX-1", "TAU2-v3", "TAU2-SEMVER-3",
                post_z1_transformation[0], post_z1_transformation[1],
                "SNAP-BASE", "SNAPVER-1", "SNAP-Z1", "SNAPVER-1",
                match_z1, "TID-MATCH-v1", "MATCH-Z1",
            )),
        )
        return D2FocalAccessibilitySpecification(
            unit, baseline, ((0, post0), (1, post1)), matches,
            "D2-AF-SPEC-v1", "D2-AF-SPEC-PROV",
        )

    def test_d2_focal_potentials_are_derived_for_both_z_worlds(self):
        result = adjudicate_d2_focal_potentials(self.d2_spec())
        self.assertEqual(result.baseline.accessibility_truth, "0")
        self.assertEqual(result.baseline.dep_truth, "0")
        self.assertEqual(result.opening_by_z[0][1].d_f_truth, "0")
        self.assertEqual(result.opening_by_z[1][1].d_f_truth, "1")

    def test_d2_focal_unknown_post_dependency_propagates_to_opening(self):
        result = adjudicate_d2_focal_potentials(
            self.d2_spec(post_z1_components=("?", "1", "1", "1"))
        )
        self.assertEqual(result.post_by_z[1][1].accessibility_truth, "?")
        self.assertEqual(result.opening_by_z[1][1].d_f_truth, "?")

    def test_d2_focal_rejects_differential_nonfocal_resource_predicate(self):
        with self.assertRaisesRegex(FocalAccessibilityContractError, "isolation violation"):
            adjudicate_d2_focal_potentials(self.d2_spec(post_z1_res="0"))

    def test_d2_focal_requires_basal_authorization_one(self):
        with self.assertRaisesRegex(FocalAccessibilityContractError, "C_auth,base=1"):
            adjudicate_d2_focal_potentials(self.d2_spec(auth="0"))

    def test_d2_focal_requires_exhaustive_baseline_route_catalogue(self):
        with self.assertRaisesRegex(FocalAccessibilityContractError, "baseline A_f\*=0"):
            adjudicate_d2_focal_potentials(self.d2_spec(exhaustive=False))

    def test_d2_focal_nonmatching_tau2_is_not_comparable(self):
        result = adjudicate_d2_focal_potentials(self.d2_spec(
            post_z1_transformation=("TAU2-v4", "TAU2-SEMVER-4"),
            match_z1="NOT_MATCHED",
        ))
        self.assertEqual(result.opening_by_z[1][1].d_f_truth, "NOT_COMPARABLE")

    def test_block_scope_must_be_universal(self):
        source = FocalAccessibilityInput(
            "UE-1", "TAU2-v3", "TAU2-SEMVER-3", "BND-1", "CTX-1", "SNAP-1", "SNAPVER-1",
            tuple(self.predicate(x) for x in ("ID", "REL", "COND", "AUTH", "RES")),
            (self.route("R1"),), True, "0", "0", "COMPLETE", "BLOCK-v1", "BLOCK-PROV",
            True, "ROUTE-CATALOG-v1", "ROUTE-CATALOG-PROV", "ROUTE-CATALOG-OBS-PROV",
            "LOCAL_ROUTE_ONLY", "C10S-AF-v0.1",
        )
        with self.assertRaises(FocalAccessibilityContractError):
            adjudicate_focal_accessibility(source)


if __name__ == "__main__":
    unittest.main()
