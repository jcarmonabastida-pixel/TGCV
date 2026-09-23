import unittest
import TR131_CROSS_DOMAIN_COMPARISON_RUNNER_006 as R
def rec(rid="r",domain="VisitAll",t0=("a",),t1=("a",),real="a",tid=None,step=None,s=None,s1=None):
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
 def test_forbidden_rejected(self):
  x=rec(); x["value"]=3
  with self.assertRaisesRegex(ValueError,"FORBIDDEN"): R.derive(x)
 def test_unknown_rejected(self):
  x=rec(); x["foo"]="bar"
  with self.assertRaisesRegex(ValueError,"UNAUTHORIZED"): R.derive(x)
 def test_H_full(self):
  a=R.derive(rec("a","VisitAll",real="m",tid="t",step=0,s={"q":0},s1={"q":1}))
  b=R.derive(rec("b","VisitAll",real="n",tid="t",step=1,s={"q":1},s1={"q":2}))
  _,h=R.trajectory_analysis([a,b]); self.assertEqual(h[("VisitAll","t")],[{"q":0},"m",{"q":1},"n",{"q":2}])
 def test_trajectory_insufficient(self):
  a=R.derive(rec(tid="one",step=0)); self.assertEqual(R.trajectory_analysis([a])[0]["VisitAll"]["divergence"],"NOT TESTABLE")
 def test_trajectory_divergence(self):
  a=R.derive(rec("a","VisitAll",("x",),("x","y"),tid="b1",step=0,s={"root":0})); b=R.derive(rec("b","VisitAll",("x",),("x","y","z"),tid="b1",step=1,s={"root":1}))
  c=R.derive(rec("c","VisitAll",("x",),("x","z"),tid="b2",step=0,s={"root":0})); d=R.derive(rec("d","VisitAll",("x",),("x",),tid="b2",step=1,s={"root":2}))
  self.assertEqual(R.trajectory_analysis([a,b,c,d])[0]["VisitAll"]["divergence"],"OBSERVED")
 def test_domain_scope_rejected(self):
  with self.assertRaisesRegex(ValueError,"FROZEN_TWO_DOMAIN_SCOPE_MISMATCH"): R.analyze({"protocol":R.PROTOCOL,"records":[rec()]})
 def test_domain_separation(self):
  p={"protocol":R.PROTOCOL,"records":[rec("v","VisitAll"),rec("p","PRISM",("pick",),("read",),"pick")]}
  self.assertEqual(R.analyze(p)["domains"],["PRISM","VisitAll"])
 def test_utility_probe(self):
  rows=[rec("a","VisitAll",("a",),("a","b"),"x","t",0,{"q":0},{"q":1}),rec("b","VisitAll",("a","b"),("a","b","c"),"y","t",1,{"q":1},{"q":2}),rec("c","PRISM",("p",),("p","q"),"pick","u",0,{"q":0},{"q":1}),rec("d","PRISM",("p","q"),("p","q"),"read","u",1,{"q":1},{"q":2})]
  u=R.analyze({"protocol":R.PROTOCOL,"records":rows})["utility_probe"]
  for k in ["accessibility_expansion_contraction","transformation_space_turnover","persistence","trajectory_divergence","transformation_followed_by_future_accessibility_reconfiguration"]: self.assertIn(u[k],{"OBSERVABLE","NOT OBSERVABLE","NOT TESTABLE"})
  self.assertEqual(u["transformation_followed_by_future_accessibility_reconfiguration"],"OBSERVABLE")
 def test_utility_probe_temporal_control(self):
  rows=[rec("a","VisitAll",("a",),("a",),"x","t",0,{"q":0},{"q":1}),rec("b","VisitAll",("a",),("a",),"y","t",1,{"q":1},{"q":2}),rec("c","PRISM",("p",),("p",),"pick","u",0,{"q":0},{"q":1}),rec("d","PRISM",("p",),("p",),"read","u",1,{"q":1},{"q":2})]
  self.assertEqual(R.analyze({"protocol":R.PROTOCOL,"records":rows})["utility_probe"]["transformation_followed_by_future_accessibility_reconfiguration"],"NOT OBSERVABLE")
 def test_deterministic_hash(self):
  p={"protocol":R.PROTOCOL,"records":[rec("v","VisitAll"),rec("p","PRISM",("pick",),("read",),"pick")]}
  self.assertEqual(R.analyze(p)["output_sha256"],R.analyze(p)["output_sha256"])
if __name__=="__main__": unittest.main(verbosity=2)
