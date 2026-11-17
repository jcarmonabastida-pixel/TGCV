"""Focused regressions for explicit D2/g_A functional-history rules."""
from __future__ import annotations

import unittest
from types import SimpleNamespace
from decimal import Decimal

from c10s_synthetic_components import ContractError, D2PotentialStage, FunctionalState
from c10s_functional_history import FunctionalHistoryRule, _apply_rules


class FunctionalHistoryRuleTests(unittest.TestCase):
    def stage(self, *, a_f_post=True, d_f_opening=True):
        return D2PotentialStage(
            unit_id="U1", z=1, policy_id="P1", policy_version="1",
            policy_artifact_ref="ART1", actor_id="ACT1",
            w_programmed=True, w_attempt=True, receipt=True, s_install=True,
            c_install=True, c_integrity=True, c_compat=True, c_oper=True,
            c_dep_star=True, a_f_post=a_f_post, d_f_opening=d_f_opening,
            provenance_sha256="a" * 64,
        )

    def test_accessibility_stage_does_not_change_admission_without_explicit_rule(self):
        initial = FunctionalState(False, "NO_ADMISSION")
        changes = _apply_rules(
            source="D2", initial=initial, rules=(), mechanism=self.stage(),
        )
        self.assertEqual(changes, ())

    def test_explicit_d2_rule_changes_only_declared_functional_dimension(self):
        initial = FunctionalState(False, "NO_ADMISSION")
        rule = FunctionalHistoryRule(
            rule_id="D2-ADMIT-01", source="D2", event_time=Decimal("1"),
            causal_family="DGP_FUNCTIONAL_ADMISSION",
            provenance_ref="DGP-CONFIG#D2-ADMIT-01",
            set_admission="ADMIT", d2_field="d_f_opening", d2_value=True,
        )
        changes = _apply_rules(
            source="D2", initial=initial, rules=(rule,), mechanism=self.stage(),
        )
        self.assertEqual(len(changes), 1)
        self.assertFalse(changes[0].state_after.enabled)
        self.assertEqual(changes[0].state_after.admission_behavior, "ADMIT")

    def test_direct_g_a_rule_uses_exact_joint_vector_component(self):
        initial = FunctionalState(False, "NO_ADMISSION")
        rule = FunctionalHistoryRule(
            rule_id="GA-ENABLED-01", source="G_A", event_time=Decimal("2"),
            causal_family="DIRECT_GA_FUNCTIONAL_ENABLED",
            provenance_ref="DGP-CONFIG#GA-ENABLED-01",
            set_enabled=True, vector_index=2, vector_value=1,
        )
        changes = _apply_rules(
            source="G_A", initial=initial, rules=(rule,),
            mechanism=(0, 0, 1, 0),
        )
        self.assertEqual(len(changes), 1)
        self.assertTrue(changes[0].state_after.enabled)
        self.assertEqual(changes[0].state_after.admission_behavior, "NO_ADMISSION")


    def test_explicit_alternative_path_uses_its_own_joint_vector_component(self):
        initial = FunctionalState(True, "ADMIT")
        rule = FunctionalHistoryRule(
            rule_id="GA-ALTERNATIVE-01", source="G_A",
            event_time=Decimal("1"),
            causal_family="ALTERNATIVE_FUNCTIONAL_PATH",
            provenance_ref="DGP-CONFIG#GA-ALTERNATIVE-01",
            set_enabled=False,
            vector_predicates=((1, 1),),
        )
        changes = _apply_rules(
            source="G_A", initial=initial, rules=(rule,),
            mechanism=(0, 1, 0, 0),
        )
        self.assertEqual(len(changes), 1)
        self.assertFalse(changes[0].state_after.enabled)
        self.assertEqual(changes[0].state_after.admission_behavior, "ADMIT")

    def test_d2_trajectory_rule_changes_functional_state_only_on_exact_target_potential(self):
        initial = FunctionalState(False, "NO_ADMISSION")
        rule = FunctionalHistoryRule(
            rule_id="TRAJ-D2-01", source="TRAJECTORY",
            event_time=Decimal("3"),
            causal_family="EXECUTED_TRAJECTORY_CONSEQUENCE",
            provenance_ref="DGP-CONFIG#TRAJ-D2-01",
            set_enabled=True, trajectory_target_state="TARGET-A",
            trajectory_field="trajectory_status", trajectory_value="COMPLETED",
        )
        completed = SimpleNamespace(trajectory_status="COMPLETED", execution_state=1)
        partial = SimpleNamespace(trajectory_status="PARTIAL", execution_state=0)
        matched = _apply_rules(
            source="D2", initial=initial, rules=(rule,),
            mechanism=self.stage(),
            trajectories_by_target={"TARGET-A": completed},
        )
        unmatched = _apply_rules(
            source="D2", initial=initial, rules=(rule,),
            mechanism=self.stage(),
            trajectories_by_target={"TARGET-A": partial},
        )
        self.assertEqual(len(matched), 1)
        self.assertTrue(matched[0].state_after.enabled)
        self.assertEqual(unmatched, ())

    def test_g_a_trajectory_rule_uses_exact_factorial_potential_and_target(self):
        initial = FunctionalState(True, "ADMIT")
        rule = FunctionalHistoryRule(
            rule_id="TRAJ-GA-01", source="TRAJECTORY",
            event_time=Decimal("4"),
            causal_family="GA_EXECUTED_TRAJECTORY_CONSEQUENCE",
            provenance_ref="DGP-CONFIG#TRAJ-GA-01",
            set_admission="NO_ADMISSION", trajectory_target_state="TARGET-B",
            trajectory_field="execution_state", trajectory_value=1,
        )
        completed = SimpleNamespace(
            history_ref="HX1", vector_sha256="a" * 64,
            r_common_fingerprint="b" * 64, target_state="TARGET-B",
            trajectory_status="COMPLETED", execution_state=1,
        )
        not_executed = SimpleNamespace(
            history_ref="HX1", vector_sha256="a" * 64,
            r_common_fingerprint="b" * 64, target_state="TARGET-B",
            trajectory_status="NOT_SELECTED", execution_state=0,
        )
        matched = _apply_rules(
            source="G_A", initial=initial, rules=(rule,),
            mechanism=(1, 0, 0, 1),
            trajectories_by_target={"TARGET-B": completed},
        )
        unmatched = _apply_rules(
            source="G_A", initial=initial, rules=(rule,),
            mechanism=(1, 0, 0, 1),
            trajectories_by_target={"TARGET-B": not_executed},
        )
        self.assertEqual(len(matched), 1)
        self.assertEqual(matched[0].state_after.admission_behavior, "NO_ADMISSION")
        self.assertEqual(unmatched, ())

    def test_trajectory_rule_fails_closed_when_exact_target_is_missing(self):
        rule = FunctionalHistoryRule(
            rule_id="TRAJ-MISSING-01", source="TRAJECTORY",
            event_time=Decimal("5"),
            causal_family="TRAJECTORY_MISSING_TARGET",
            provenance_ref="DGP-CONFIG#TRAJ-MISSING-01",
            set_enabled=True, trajectory_target_state="TARGET-C",
            trajectory_field="execution_state", trajectory_value=1,
        )
        with self.assertRaises(ContractError):
            _apply_rules(
                source="D2", initial=FunctionalState(False, "NO_ADMISSION"),
                rules=(rule,), mechanism=self.stage(),
                trajectories_by_target={},
            )

    def test_interaction_rule_requires_all_declared_vector_components(self):
        initial = FunctionalState(True, "ADMIT")
        rule = FunctionalHistoryRule(
            rule_id="GA-FOCAL-X-ALTERNATIVE-01", source="G_A",
            event_time=Decimal("1"),
            causal_family="FOCAL_BY_ALTERNATIVE_INTERACTION",
            provenance_ref="DGP-CONFIG#GA-FOCAL-X-ALTERNATIVE-01",
            set_admission="NO_ADMISSION",
            vector_predicates=((0, 0.0), (1, 0.0)),
        )
        active = _apply_rules(
            source="G_A", initial=initial, rules=(rule,),
            mechanism=(0.0, 0.0, 0.0, 0.0),
        )
        inactive = _apply_rules(
            source="G_A", initial=initial, rules=(rule,),
            mechanism=(0.0, 1.0, 0.0, 0.0),
        )
        self.assertEqual(len(active), 1)
        self.assertEqual(active[0].state_after.admission_behavior, "NO_ADMISSION")
        self.assertEqual(inactive, ())


if __name__ == "__main__":
    unittest.main()
