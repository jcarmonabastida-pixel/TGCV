#!/usr/bin/env python3
"""Deterministic generator for TI-001 V012 NEXT2 fixture.

Inputs are cryptographically bound to the frozen requirements and canonical
mapping-semantics artifacts. This generator writes a fresh candidate package;
it never mutates an existing fixture package.
"""
import hashlib, json, itertools
from pathlib import Path

REQUIREMENTS_SHA256 = "c9e55982188e4242124adbe196a6d98211bec2fe"
SEMANTICS_BLOB_SHA256 = "b0801bfc7e7614f5fc7ca6304fb305c0d77d9252"
VERSION = "NEXT2_v001"
DOMAINS = range(1,5)
OPS = range(1,6)
CONDS = ("INFORMATIVE","SURFACE_PERMUTED","UNINFORMATIVE_NULL","CONTRADICTORY")
PRESENTATIONS = range(1,5)
ACTIONS = ("A","B","C","D")
SLOTS = ("slot_1","slot_2","slot_3","slot_4")
REPLICATES = range(1,4)

def sha256_text(s): return hashlib.sha256(s.encode("utf-8")).hexdigest()

def perm_key(p): return tuple(p)

def prp(seed_material, d, o, m, p, r):
    seed = hashlib.sha256((seed_material + f"|{d}|{o}|{m}|{p}|{r}").encode()).digest()
    # Deterministic Fisher-Yates permutation of slots; independent of f and k.
    a=list(SLOTS)
    for i in range(len(a)-1,0,-1):
        j=int.from_bytes(seed[(len(a)-1-i)*2:(len(a)-1-i)*2+2],"big") % (i+1)
        a[i],a[j]=a[j],a[i]
    return dict(zip(ACTIONS,a))

def shift(f,n):
    return {a:SLOTS[(SLOTS.index(f[a])+n)%4] for a in ACTIONS}

def generate(out):
    seed_material=REQUIREMENTS_SHA256
    perms=list(itertools.permutations(SLOTS))
    rows=[]
    ordinal=1
    for d in DOMAINS:
      for o in OPS:
       for m in CONDS:
        for p in PRESENTATIONS:
         for k,perm in enumerate(perms,1):
          f=dict(zip(ACTIONS,perm))
          for r in REPLICATES:
            if m=="INFORMATIVE": z=dict(f)
            elif m=="SURFACE_PERMUTED": z=shift(f,1)
            elif m=="CONTRADICTORY": z=shift(f,2)
            else: z=prp(seed_material,d,o,m,p,r)
            rows.append({"id":f"N2-{ordinal:05d}","d":d,"o":o,"m":m,"p":p,"k":k,"r":r,
                         "f":f,"z":z,"s":f"S{d}-{ordinal:05d}"})
            ordinal+=1
    assert len(rows)==23040
    out=Path(out); out.mkdir(parents=True,exist_ok=False)
    for i in range(24):
      chunk=rows[i*960:(i+1)*960]
      (out/f"SHARD_{i+1:03d}.json").write_text(json.dumps(chunk,separators=(",",":"),ensure_ascii=False)+"\n",encoding="utf-8")
    manifest={"artifact_id":"TI001_V012_NEXT2_FIXTURE_REGENERATED_CANDIDATE_001",
              "status":"GENERATED_NOT_FROZEN","immutable_version":VERSION,
              "requirements_blob_sha256":REQUIREMENTS_SHA256,
              "semantics_blob_sha256":SEMANTICS_BLOB_SHA256,
              "unit_count":23040,"shard_count":24,"units_per_shard":960}
    (out/"MANIFEST.json").write_text(json.dumps(manifest,indent=2)+"\n",encoding="utf-8")

if __name__=="__main__":
    import sys
    if len(sys.argv)!=2: raise SystemExit("usage: generator.py OUTPUT_DIR")
    generate(sys.argv[1])
