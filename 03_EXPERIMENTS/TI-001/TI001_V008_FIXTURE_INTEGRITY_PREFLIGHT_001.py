#!/usr/bin/env python3
"""TI-001 V008 Fixture Integrity Preflight 001."""

from pathlib import Path
import hashlib, json

FIXTURE=Path("03_EXPERIMENTS/TI-001/generated/V008/TI001_V008_FIXTURE_001.json")
MANIFEST=Path("03_EXPERIMENTS/TI-001/generated/V008/TI001_V008_FIXTURE_001_INTEGRITY_MANIFEST.json")
EXPECTED_SHA="dd45ae453b5a3d37b4faff34ed829e7aac52ce4ed5a7462bb3546c1a420c2eb9"
EXPECTED_GENERATOR="f345c41371a189c43b69b707b49b7eb17d140f55"
EXPECTED_SCHEMA="d9539790452b047bc845a19bdcf50b8713a42b2a"

def main():
    checks={}
    def c(n,v): checks[n]=bool(v)
    c("fixture_exists",FIXTURE.exists()); c("manifest_exists",MANIFEST.exists())
    data=FIXTURE.read_bytes() if FIXTURE.exists() else b""
    c("utf8", bool(data))
    obj=json.loads(data.decode("utf-8")) if data else {}
    c("fixture_id",obj.get("fixture_id")=="TI001-V008-FIXTURE-001")
    c("schema_id",obj.get("schema_id")=="TI001-V008-DU-SCHEMA-001")
    c("generator_id",obj.get("generator_id")=="TI001-V008-FIXTURE-GENERATOR-001")
    c("seed",obj.get("seed")==20260925)
    units=obj.get("decision_units",[])
    c("decision_count_420",len(units)==420)
    c("decision_ids", [u.get("decision_id") for u in units]==[f"D{i:03d}" for i in range(1,421)])
    c("pair_count_210",len({u.get("pair_id") for u in units})==210)
    c("two_per_pair",all(sum(u.get("pair_id")==p for u in units)==2 for p in [f"P{i:03d}" for i in range(1,211)]))
    conditions={k:0 for k in ("control","treatment","null")}
    presentations={k:0 for k in ("I1_FIRST","I2_FIRST")}
    pairs={}
    structure=True; actions=True; context=True; fields=True
    for u in units:
        if u.get("condition") in conditions: conditions[u["condition"]]+=1
        if u.get("presentation") in presentations: presentations[u["presentation"]]+=1
        fields &= list(u.keys())==["decision_id","pair_id","condition","presentation","context","available_actions","future_structure"]
        actions &= u.get("available_actions")==["A","B"]
        context &= list(u.get("context",{}).keys())==["items","item_count"] and u["context"].get("item_count")==2
        fs=u.get("future_structure",{})
        structure &= list(fs.keys())==["successor_realized","future_structure_available"] and fs.get("successor_realized") is False and fs.get("future_structure_available")==(u.get("condition")=="treatment")
        pairs.setdefault(u.get("pair_id"),[]).append(u.get("presentation"))
    c("condition_balance",conditions=={"control":140,"treatment":140,"null":140})
    c("presentation_balance",presentations=={"I1_FIRST":210,"I2_FIRST":210})
    c("seven_fields",fields); c("actions_ab",actions); c("context_schema",context); c("future_structure",structure)
    c("pair_presentation_complementary",all(sorted(v)==["I1_FIRST","I2_FIRST"] for v in pairs.values()))
    c("pair_order", [u["pair_id"] for u in units[::2]]==[f"P{i:03d}" for i in range(1,211)])
    c("fixture_sha256",hashlib.sha256(data).hexdigest()==EXPECTED_SHA)
    m=json.loads(MANIFEST.read_text(encoding="utf-8")) if MANIFEST.exists() else {}
    c("manifest_sha256",m.get("fixture_sha256")==EXPECTED_SHA)
    c("manifest_generator_sha",m.get("generator_blob_sha1")==EXPECTED_GENERATOR)
    c("manifest_schema_sha",m.get("schema_blob_sha1")==EXPECTED_SCHEMA)
    c("scientific_not_performed",m.get("scientific_execution")=="NOT_PERFORMED")
    status="PASS" if all(checks.values()) else "FAIL"
    result={"preflight_id":"TI001-V008-FIXTURE-INTEGRITY-PREFLIGHT-001","checks":checks,"fixture_id":obj.get("fixture_id"),"fixture_sha256":hashlib.sha256(data).hexdigest(),"generator_blob_sha1":EXPECTED_GENERATOR,"schema_blob_sha1":EXPECTED_SCHEMA,"scientific_execution":"NOT_PERFORMED","status":status}
    print(json.dumps(result,indent=2,sort_keys=True))
    return 0 if status=="PASS" else 1
if __name__=="__main__":
    raise SystemExit(main())
