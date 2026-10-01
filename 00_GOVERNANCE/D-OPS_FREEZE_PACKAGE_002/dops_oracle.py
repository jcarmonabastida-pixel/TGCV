from dops_canonical import canonical_omega

def classify(old, new):
    if old is None or new is None: return "NON_COMPARABLE"
    au=set(new["U"])-set(old["U"]); ru=set(old["U"])-set(new["U"])
    if au and not ru: return "EXPANSION"
    if ru and not au: return "CONTRACTION"
    if au and ru: return "OTHER_STRUCTURAL_CHANGE"
    if all(old[k]==new[k] for k in ("equivalence","R1","R2","R3")): return "PERSISTENCE"
    dr3_old=set(map(tuple,old["R3"])); dr3_new=set(map(tuple,new["R3"]))
    if old["equivalence"]==new["equivalence"] and old["R1"]==new["R1"] and old["R2"]==new["R2"] and len(dr3_old-dr3_new)==1 and len(dr3_new-dr3_old)==1:
        return "RECONFIGURATION_ONLY"
    return "OTHER_STRUCTURAL_CHANGE"

def expected():
    return {"persistence":"PERSISTENCE","expansion":"EXPANSION","contraction":"CONTRACTION","reconfiguration":"RECONFIGURATION_ONLY","mixed_identity_change":"OTHER_STRUCTURAL_CHANGE","representation":"INVARIANT","state_only_variation":"NO_OMEGA_CHANGE","incomparable":"NON_COMPARABLE"}
