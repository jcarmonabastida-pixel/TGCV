#!/usr/bin/env python3
import argparse, hashlib, json
from pathlib import Path

EXPECTED_SPEC_SHA1="5cb84ecb96dc08664fc507d5b681d1e3c935437a"
FIXTURE_ID="TI001-V008-FIXTURE-001"
FIXTURE_SHA256="dd45ae453b5a3d37b4faff34ed829e7aac52ce4ed5a7462bb3546c1a420c2eb9"

def blob_sha1(b):
    return hashlib.sha1(f"blob {len(b)}\0".encode()+b).hexdigest()

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--spec",required=True)
    p.add_argument("--fixture",required=True)
    p.add_argument("--output",required=True)
    a=p.parse_args()
    sb=Path(a.spec).read_bytes()
    st=sb.decode("utf-8")
    fb=Path(a.fixture).read_bytes()
    f=json.loads(fb)
    units=f.get("decision_units",[])
    pairs={}
    for u in units:
        pairs.setdefault(u.get("pair_id"),[]).append(u)
    checks={
      "spec_identity": blob_sha1(sb)==EXPECTED_SPEC_SHA1,
      "fixture_identity": f.get("fixture_id")==FIXTURE_ID and hashlib.sha256(fb).hexdigest()==FIXTURE_SHA256,
      "decision_count": len(units)==420,
      "pair_count": len(pairs)==210 and all(len(v)==2 for v in pairs.values()),
      "ab_only": all(set(u.get("available_actions",[]))=={"A","B"} for u in units),
      "three_conditions": all(sum(u.get("condition")==c for u in units)==140 for c in ("control","treatment","null")),
      "paired_presentation": all(len({u.get("presentation") for u in v})==2 for v in pairs.values()),
      "indicator_treatment_control": "TI_DC = q_treatment(A) - q_control(A)" in st,
      "null_reference": "TI_NULL = q_null(A) - q_control(A)" in st,
      "pair_agreement_switch": "I_agree(p)" in st and "I_switch(p)" in st,
      "no_value_reward_utility_performance": all(x in st.lower() for x in ("value","reward","utility","performance")),
      "no_scientific_authorization": "scientific_execution: not_authorized" in st.lower(),
    }
    result={"preflight_id":"TI001-V008-TI-INDICATOR-DEFINITION-PREFLIGHT-001","checks":checks,"spec_blob_sha1":blob_sha1(sb),"scientific_execution":"NOT_PERFORMED","status":"PASS" if all(checks.values()) else "FAIL"}
    Path(a.output).write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")

if __name__=="__main__":
    main()
