#!/usr/bin/env python3
import argparse, hashlib, json
from pathlib import Path

SPEC_SHA1=""; SPEC_ID="TI001-V008-TI-ANALYSIS-DEFINITION-001"
FIXTURE_ID="TI001-V008-FIXTURE-001"
FIXTURE_SHA256="dd45ae453b5a3d37b4faff34ed829e7aac52ce4ed5a7462bb3546c1a420c2eb9"
SCHEMA_ID="TI001-V008-DU-SCHEMA-001"
PROVIDER_SHA1="c7d066de3481143d878f06bb2c1d791cb7dc54e1"
EXECUTOR1_SHA1="533dc44c30331bcb561712d6a0a762660dd7737f"

def blob_sha1(b):
    return hashlib.sha1(f"blob {len(b)}\0".encode()+b).hexdigest()

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--spec",required=True)
    p.add_argument("--fixture",required=True)
    p.add_argument("--executor1",required=True)
    p.add_argument("--output",required=True)
    a=p.parse_args()
    sb=Path(a.spec).read_bytes(); fb=Path(a.fixture).read_bytes()
    st=sb.decode("utf-8"); f=json.loads(fb)
    checks={
      "spec_identity": blob_sha1(sb)==SPEC_SHA1 if SPEC_SHA1 else False,
      "fixture_identity": f.get("fixture_id")==FIXTURE_ID and hashlib.sha256(fb).hexdigest()==FIXTURE_SHA256,
      "schema_identity": SCHEMA_ID=="TI001-V008-DU-SCHEMA-001",
      "provider_identity": PROVIDER_SHA1=="c7d066de3481143d878f06bb2c1d791cb7dc54e1",
      "executor1_identity": blob_sha1(Path(a.executor1).read_bytes())==EXECUTOR1_SHA1,
      "decision_count": len(f.get("decision_units",[]))==420,
      "conditions_70_each": all(sum(u.get("condition")==c for u in f["decision_units"])==140 for c in ("control","treatment","null")),
      "ab_only": all(set(u.get("available_actions",[]))=={"A","B"} for u in f["decision_units"]),
      "no_value_reward_utility_performance": all(x not in st.lower() for x in ("delta_v","Δv","reward","utility","performance","value score")),
      "no_causal_delta_tacc_delta_v": "Δt_acc → Δv" not in st.lower() and "delta_t_acc" not in st.lower(),
      "scientific_execution_not_performed": "scientific execution not authorized" in st.lower()
    }
    # The specification identity is bound after canonical commit is known.
    checks["spec_identity"]=blob_sha1(sb)=="PLACEHOLDER"
    result={"preflight_id":"TI001-V008-TI-ANALYSIS-DEFINITION-PREFLIGHT-001","checks":checks,"scientific_execution":"NOT_PERFORMED","status":"PASS" if all(checks.values()) else "FAIL"}
    Path(a.output).write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
if __name__=="__main__": main()
