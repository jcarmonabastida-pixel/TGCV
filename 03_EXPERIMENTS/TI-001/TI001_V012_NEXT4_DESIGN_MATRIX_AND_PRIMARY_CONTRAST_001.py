"""NEXT4 frozen design matrix and primary contrast.

Design-stage implementation. The contrast is a response-independent
linear functional over action×profile×mapping cells.
"""

from __future__ import annotations
import hashlib, json
from itertools import permutations

ACTIONS=(0,1,2,3)
PERMUTATIONS=tuple(permutations(ACTIONS))
CONDITIONS=("STATIC_CONTROL","FUTURE_REASSIGNED","SURFACE_CONTROL","UNINFORMATIVE_NULL")
DOMAINS=(0,1,2)
OPS=(0,1)
PRESENTATIONS=(0,1,2,3)

def latent_mapping(condition, permutation):
    if condition in ("STATIC_CONTROL","SURFACE_CONTROL"):
        return (0,1,2,3)
    if condition=="FUTURE_REASSIGNED":
        return permutation
    if condition=="UNINFORMATIVE_NULL":
        return None
    raise ValueError(condition)

def row_features(row):
    """Frozen action-specific feature representation."""
    action=row["action"]; profile=row["profile"]
    mapping=row["latent_mapping"]
    future=None if mapping is None else mapping[profile]
    aligned=int(future is not None and action==future)
    return {
        "intercept":1,
        "action":action,
        "profile":profile,
        "mapping_signal":int(mapping is not None),
        "action_profile":(action,profile),
        "mapping_aligned":aligned,
        "domain":row["domain"],
        "operationalisation":row["operationalisation"],
        "presentation":row["presentation"],
        "condition":row["condition"],
    }

def primary_contrast_definition():
    return {
        "name":"mapping_alignment_reorganisation",
        "estimand":"difference in mapping-aligned action×profile association between STATIC_CONTROL and FUTURE_REASSIGNED",
        "direction":"positive mapping-aligned reorganisation",
        "alpha":0.05,
        "response_independent":True,
        "not_generic_condition_effect":True
    }

def build_rows(choice_sets):
    rows=[]
    for cs in choice_sets:
        for a in ACTIONS:
            row=dict(cs)
            row["action"]=a
            row["chosen"]=int(a==cs["chosen_action"])
            rows.append(row)
    return rows

def feature_schema():
    return [
        "intercept","action","profile","mapping_signal","action_profile",
        "mapping_aligned","domain","operationalisation","presentation","condition"
    ]

def manifest():
    p={"implementation":"NEXT4_DESIGN_MATRIX_AND_PRIMARY_CONTRAST_001",
       "actions":4,"permutations":24,
       "feature_schema":feature_schema(),
       "contrast":primary_contrast_definition()}
    raw=json.dumps(p,sort_keys=True,separators=(",",":")).encode()
    p["sha256"]=hashlib.sha256(raw).hexdigest()
    return p

if __name__=="__main__":
    print(json.dumps(manifest(),sort_keys=True))
