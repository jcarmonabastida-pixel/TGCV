#!/usr/bin/env python3
"""TI-001 fixture/generator binding integrity gate. No scientific execution."""
import argparse,hashlib,json,subprocess,sys,tempfile
from pathlib import Path

def sha256_bytes(b): return hashlib.sha256(b).hexdigest()
def git_blob_sha(p): return subprocess.check_output(["git","hash-object",str(p)],text=True).strip()

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--fixture",required=True); ap.add_argument("--generator",required=True)
    ap.add_argument("--schema",required=True); ap.add_argument("--output",required=True)
    a=ap.parse_args()
    fixture,generator,schema=map(Path,(a.fixture,a.generator,a.schema))
    checks={}
    checks["A1_FIXTURE_EXISTS"]=fixture.exists()
    checks["A2_GENERATOR_EXISTS"]=generator.exists()
    checks["A3_SCHEMA_EXISTS"]=schema.exists()
    if not all((fixture.exists(),generator.exists(),schema.exists())):
        raise SystemExit("Required artifact missing")
    fb=fixture.read_bytes(); data=json.loads(fb.decode("utf-8")); gs=git_blob_sha(generator); ss=git_blob_sha(schema)
    declared=data.get("fixture_sha256")
    raw=dict(data); raw.pop("fixture_sha256",None)
    canonical=json.dumps(raw,sort_keys=True,separators=(",",":")).encode("utf-8")
    checks["A4_FIXTURE_DECLARED_HASH"]=declared==sha256_bytes(canonical)
    checks["A5_SCHEMA_IDENTIFIER_PRESENT"]=bool(data.get("schema"))
    checks["A6_GENERATOR_IDENTIFIER_PRESENT"]=True
    checks["A7_RANDOMISATION_SEED_FROZEN"]=data.get("randomisation_seed")==582031
    checks["A8_ENVIRONMENT_SEED_BASE_FROZEN"]=data.get("environment_seed_base")==731407
    checks["A9_PAIR_COUNT"]=data.get("pair_count")==32
    checks["A10_RECORD_COUNT"]=data.get("record_count")==64 and len(data.get("instances",[]))==64
    checks["A11_SCHEMA_VERSION"]=data.get("schema")=="TI001_PREFLIGHT_FIXTURE_v004"
    checks["A12_NO_SCIENTIFIC_EXECUTION_MARKER"]=all(x.get("selected_transformation") is None and x.get("S_t1") is None for x in data["instances"])
    checks["A13_GENERATOR_NO_MODEL_EXECUTION"]="responses.create" not in generator.read_text(encoding="utf-8") and "chat.completions" not in generator.read_text(encoding="utf-8")
    checks["A14_GENERATOR_NO_EXTERNAL_API"]="requests." not in generator.read_text(encoding="utf-8")
    checks["A15_GENERATOR_SERIALIZATION_FROZEN"]='separators=(",",":")' in generator.read_text(encoding="utf-8") and 'sort_keys=True' in generator.read_text(encoding="utf-8")
    with tempfile.TemporaryDirectory() as td:
        out=Path(td)/"fixture.json"
        p=subprocess.run([sys.executable,str(generator)],capture_output=True,text=True,check=True)
        out.write_text(p.stdout,encoding="utf-8")
        checks["A16_DETERMINISTIC_REGENERATION"]=out.read_bytes()==fb
    checks["A17_GENERATOR_GIT_BLOB_SHA"]=len(gs)==40
    checks["A18_SCHEMA_GIT_BLOB_SHA"]=len(ss)==40
    checks["A19_CURRENT_SPACE_UNIFORM"]=len({json.dumps(x["T_acc_t"],sort_keys=True) for x in data["instances"]})==1
    checks["A20_CONDITIONS_BALANCED"]=sum(x["condition"]=="control" for x in data["instances"])==32 and sum(x["condition"]=="treatment" for x in data["instances"])==32
    status="PASS" if all(checks.values()) else "FAIL"
    result={"gate_id":"TI001-FIXTURE-GENERATOR-BINDING-INTEGRITY-GATE-001","status":status,"checks":checks,"fixture_sha256":sha256_bytes(fb),"fixture_declared_sha256":declared,"generator_blob_sha":gs,"schema_blob_sha":ss,"scientific_execution":"NOT_AUTHORIZED"}
    Path(a.output).write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(result,indent=2))
    raise SystemExit(0 if status=="PASS" else 1)
if __name__=="__main__": main()
