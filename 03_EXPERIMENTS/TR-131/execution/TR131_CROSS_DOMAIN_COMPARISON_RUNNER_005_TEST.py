#!/usr/bin/env python3
import unittest
import TR131_CROSS_DOMAIN_COMPARISON_RUNNER_005 as R
def rec(rid="r",domain="TEST",t0=("a",),t1=("a",),real="a",tid=None,step=None,s=None,s1=None):
 d={"domain":domain,"record_id":rid,"S_t":s if s is not None else {"x":0},"T_acc_t":list(t0),"T_real_t":real,"S_t1":s1 if s1 is not None else {"x":1},"T_acc_t1":list(t1)}
 if tid is not None:d["trajectory_id"]=tid
 if step is not None:d["step"]=step
 return d
class T(unittest.TestCase):
 def test_unchanged(self): self.assertEqual(R.derive(rec(t0=("a","b"),t1=("a","b")))["Delta_T_acc_t"],{"Added":[],"Removed":[]})
 def test_addition(self): self.assertEqual(R.derive(rec(t1=("a","b")))["Delta_T_acc_t"],{"Added":["b"],"Removed":[]})
 def test_loss(self): self.assertEqual(R.derive(rec(t0=("a","b")))["Delta_T_acc_t"],{"Added":[],"Removed":["b"]})
 def test_turnover(self): self.assertEqual(R.derive(rec(t0=("a","b"),t1=("b","c")))["R"],2)
 def test_duplicate_rejected(self):
  with self.assertRaisesRegex(ValueError,"DUPLICATE"): R.derive(rec(t0=("a","a")))
 def test_missing_visible(self):
  x=rec(); del x["T_acc_t1"]; self.assertEqual(R.analyze({"protocol":R.PROTOCOL,"records":[x]})["invalid_count"],1)
 def test_forbidden_rejected(self):
  x=rec(); x["value"]=3
  with self.assertRaisesRegex(ValueError,"FORBIDDEN"): R.derive(x)
 def test_unknown_rejected(self):
  x=rec(); x["foo"]="bar"
  with self.assertRaisesRegex(ValueError,"UNAUTHORIZED"): R.derive(x)
 def test_H_explicit(self):
  x=R.derive(rec(real="pick",s={"q":0},s1={"q":1})); self.assertEqual(x["H"],[{"q":0},"pick",{"q":1}])
 def test_trajectory_insufficient(self):
  self.assertEqual(R.trajectory_analysis([R.derive(rec(tid="one",step=0))])["TEST"]["divergence"],"NOT TESTABLE")
 def test_trajectory_divergence(self):
  a=R.derive(rec("a","D",("x",),("x","y"),tid="b1",step=0,s={"root":0})); b=R.derive(rec("b","D",("x",),("x","y","z"),tid="b1",step=1,s={"root":1}))
  c=R.derive(rec("c","D",("x",),("x","z"),tid="b2",step=0,s={"root":0})); d=R.derive(rec("d","D",("x",),("x",),tid="b2",step=1,s={"root":2}))
  self.assertEqual(R.trajectory_analysis([a,b,c,d])["D"]["divergence"],"OBSERVED")
 def test_domain_separation(self):
  y=R.analyze({"protocol":R.PROTOCOL,"records":[rec("v","VisitAll"),rec("p","PRISM",("pick",),("read",),"pick")]}); self.assertEqual(y["domains"],["PRISM","VisitAll"])
 def test_utility_probe(self):
  p={"protocol":R.PROTOCOL,"records":[rec(t0=("a",),t1=("a","b"),real="x")]}
  u=R.analyze(p)["utility_probe"]
  self.assertEqual(u["accessibility_expansion_contraction"],"OBSERVABLE"); self.assertEqual(u["transformation_space_turnover"],"OBSERVABLE")
  self.assertEqual(u["persistence"],"OBSERVABLE"); self.assertEqual(u["transformation_followed_by_future_accessibility_reconfiguration"],"OBSERVABLE")
 def test_deterministic_hash(self):
  p={"protocol":R.PROTOCOL,"records":[rec(t1=("a","b"))]}; self.assertEqual(R.analyze(p)["output_sha256"],R.analyze(p)["output_sha256"])
if __name__=="__main__": unittest.main(verbosity=2)
