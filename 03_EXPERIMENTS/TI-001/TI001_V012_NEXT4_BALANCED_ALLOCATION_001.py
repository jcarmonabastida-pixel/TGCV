"""NEXT4 frozen balanced allocation for all candidate sample sizes."""

from __future__ import annotations
import hashlib, json
from itertools import permutations

CANDIDATE_N=(1728,2304,3456,5184,6912)
CONDITIONS=("STATIC_CONTROL","FUTURE_REASSIGNED","SURFACE_CONTROL","UNINFORMATIVE_NULL")
DOMAINS=(0,1,2)
OPS=(0,1)
PRESENTATIONS=(0,1,2,3)
PERMUTATIONS=tuple(permutations(range(4)))

def allocate(n:int):
    if n not in CANDIDATE_N: raise ValueError("N is not a frozen candidate.")
    # 96 factorial cells. Every candidate N is divisible by 96.
    per_cell=n//96
    rows=[]
    i=0
    for c in CONDITIONS:
        for d in DOMAINS:
            for o in OPS:
                for p in PRESENTATIONS:
                    for k in range(per_cell):
                        perm=PERMUTATIONS[(i+k)%24]
                        rows.append({
                            "choice_set_id":i,
                            "condition":c,"domain":d,"operationalisation":o,
                            "presentation":p,"permutation":perm
                        })
                        i+=1
    return rows

def audit(n:int):
    rows=allocate(n)
    cell_counts={}
    perm_counts={}
    cond_counts={c:0 for c in CONDITIONS}
    for r in rows:
        key=(r["condition"],r["domain"],r["operationalisation"],r["presentation"])
        cell_counts[key]=cell_counts.get(key,0)+1
        pkey=(r["condition"],r["permutation"])
        perm_counts[pkey]=perm_counts.get(pkey,0)+1
        cond_counts[r["condition"]]+=1
    return {
        "n":n,
        "rows":len(rows),
        "cell_min":min(cell_counts.values()),
        "cell_max":max(cell_counts.values()),
        "condition_counts":cond_counts,
        "all_cells_equal":len(set(cell_counts.values()))==1,
        "permutation_counts_by_condition_min":min(perm_counts.values()),
        "permutation_counts_by_condition_max":max(perm_counts.values()),
        "all_permutations_each_condition":all(
            (c,p) in perm_counts for c in CONDITIONS for p in PERMUTATIONS
        ),
        "sha256":hashlib.sha256(json.dumps(rows,sort_keys=True,separators=(",",":")).encode()).hexdigest()
    }

if __name__=="__main__":
    print(json.dumps({"status":"BALANCED_ALLOCATION_READY","audits":[audit(n) for n in CANDIDATE_N]},sort_keys=True))
