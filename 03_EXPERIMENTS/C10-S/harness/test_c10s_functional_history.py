"""Focused regressions for explicit D2/g_A functional-history rules."""
from __future__ import annotations

import unittest
from decimal import Decimal

from c10s_synthetic_components import D2PotentialStage, FunctionalState
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


if __name__ == "__main__":
    unittest.main()
