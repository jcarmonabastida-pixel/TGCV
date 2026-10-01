import copy

def expansion(f):
    x=copy.deepcopy(f); x["transformations"].append({"id":"tau_extra","parameters":[["r","robot"],["where","location"]],"preconditions":[["at","r","where"]],"add_effects":[],"delete_effects":[]}); return x

def contraction(f):
    x=copy.deepcopy(f); x["transformations"]=[t for t in x["transformations"] if t["id"]!="tau_scan"]; return x

def reconfiguration_r3(r3):
    x=copy.deepcopy(r3); edges=[e for e in x["edges"] if e!=["tau_move","tau_wait"]]; edges.append(["tau_wait","tau_scan"]); x["edges"]=edges; return x

def mixed_identity(f):
    x=contraction(f); return expansion(x)
