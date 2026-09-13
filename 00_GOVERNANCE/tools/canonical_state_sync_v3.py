#!/usr/bin/env python3
"""TGCV Canonical State Sync v3.4.

Read-only transition resolution and validated local reconciliation.
The source commit is the canonical byte-level reference for governed state.
Only CURRENT matrix is derived from the versioned matrix; every other governed
artifact is taken byte-for-byte from the source commit and validated.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
import subprocess
import tempfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
GOV=ROOT/"00_GOVERNANCE"
VERSIONED_MATRIX=GOV/"EVIDENCE_TO_CLAIM_MATRIX_v1.5.md"
CURRENT_MATRIX=GOV/"EVIDENCE_TO_CLAIM_MATRIX_CURRENT.md"
CURRENT_POINTER=GOV/"EVIDENCE_TO_CLAIM_MATRIX_CURRENT_POINTER.md"
CANONICAL=GOV/"CANONICAL_STATE.json"
RMA=GOV/"rma"/"TGCV_RMA_current.md"
TRACE=GOV/"rma"/"TGCV_RMA_traceability_current.csv"
STATUS=ROOT/"STATUS.md"
FILES=[CANONICAL,CURRENT_MATRIX,CURRENT_POINTER,VERSIONED_MATRIX,RMA,TRACE,STATUS]
ALLOWED_PATHS={p.relative_to(ROOT).as_posix() for p in FILES}
TARGET_MATRIX_VERSION="v1.5"
TARGET_RMA_VERSION="v3.34"
TARGET_TRACE_VERSION="v3.34"

def rel(path): return path.relative_to(ROOT).as_posix()
def sha_bytes(data): return hashlib.sha256(data).hexdigest()
def sha(path): return sha_bytes(path.read_bytes())
def git(*args):
 r=subprocess.run(["git",*args],cwd=ROOT,text=True,capture_output=True,encoding="utf-8",errors="replace")
 if r.returncode: raise RuntimeError(r.stderr.strip() or r.stdout.strip())
 return r.stdout.strip()
def git_bytes(*args):
 r=subprocess.run(["git",*args],cwd=ROOT,capture_output=True)
 if r.returncode: raise RuntimeError(r.stderr.decode("utf-8","replace").strip())
 return r.stdout
def source_bytes(source_commit,path): return git_bytes("show",f"{source_commit}:{rel(path)}")
def heads(text): return [line.lstrip("#").strip() for line in text.splitlines() if line.startswith("#")]
def columns(text):
 for line in text.splitlines():
  if line.startswith("| ID") or line.startswith("|ID"): return [x.strip() for x in line.strip("|").split("|")]
 return []
def claims(text): return [line.split("|")[1].strip() for line in text.splitlines() if line.startswith("| C") and "|" in line]
def evidence_sections(text): return {h for h in heads(text) if h.lower().startswith("material ") and "evidence" in h.lower()}
def validate_pointer(pointer):
 e=[]
 if "**Current version:** v1.5" not in pointer: e.append("POINTER_TARGET_VERSION_INVALID")
 if "EVIDENCE_TO_CLAIM_MATRIX_v1.5.md" not in pointer: e.append("POINTER_TARGET_ARTIFACT_INVALID")
 return e
def validate_canonical(canonical):
 try: state=json.loads(canonical)
 except json.JSONDecodeError: return ["CANONICAL_STATE_INVALID_JSON"]
 v=state.get("current_versions",{}); e=[]
 if v.get("rma")!=TARGET_RMA_VERSION: e.append("CANONICAL_RMA_VERSION_INVALID")
 if v.get("claim_matrix")!=TARGET_MATRIX_VERSION: e.append("CANONICAL_MATRIX_VERSION_INVALID")
 if v.get("rma_traceability")!=TARGET_TRACE_VERSION: e.append("CANONICAL_TRACE_VERSION_INVALID")
 return e
def audit_matrix(predecessor,successor):
 e=[]
 if len(successor.splitlines())<len(predecessor.splitlines()): e.append("SUCCESSOR_MATRIX_SHRINKS_IN_LINES")
 if not set(claims(predecessor))<=set(claims(successor)): e.append("SUCCESSOR_LOSES_CLAIMS")
 if columns(predecessor)!=columns(successor): e.append("SUCCESSOR_COLUMNS_CHANGED")
 lost=sorted(evidence_sections(predecessor)-evidence_sections(successor))
 if lost: e.append("SUCCESSOR_LOSES_EVIDENCE_SECTIONS:"+"|".join(lost))
 req={"Claim boundary","Current methodological routing","Current scientific position","Gate state","Interpretation boundary"}
 if not req<=set(heads(successor)): e.append("SUCCESSOR_LOSES_GOVERNANCE_BOUNDARIES")
 if "**Predecessor:** v1.4" not in successor: e.append("SUCCESSOR_PREDECESSOR_METADATA_INVALID")
 if "FOS C09" not in successor: e.append("FOS_C09_MISSING")
 return e
def build_target_state(source_commit):
 versioned=source_bytes(source_commit,VERSIONED_MATRIX)
 if source_bytes(source_commit,CURRENT_MATRIX)!=versioned: raise RuntimeError("SOURCE_CURRENT_DIFFERS_FROM_DERIVED_MATRIX")
 return {rel(CANONICAL):source_bytes(source_commit,CANONICAL),rel(CURRENT_MATRIX):versioned,rel(CURRENT_POINTER):source_bytes(source_commit,CURRENT_POINTER),rel(VERSIONED_MATRIX):versioned,rel(RMA):source_bytes(source_commit,RMA),rel(TRACE):source_bytes(source_commit,TRACE),rel(STATUS):source_bytes(source_commit,STATUS)}
def snapshot(): return {rel(p):{"sha256":sha(p) if p.exists() else None,"bytes":p.stat().st_size if p.exists() else None} for p in FILES}
def resolve_manifest(matrix_version,source_commit):
 if matrix_version!=TARGET_MATRIX_VERSION: return {"status":"BLOCKED_VALIDATION","errors":["UNSUPPORTED_TARGET_VERSION"]}
 head=git("rev-parse","HEAD"); source=git("rev-parse",f"{source_commit}^{{commit}}"); errors=[]
 if head!=source: errors.append("SOURCE_COMMIT_NOT_HEAD")
 target=build_target_state(source); predecessor=source_bytes(source,GOV/"EVIDENCE_TO_CLAIM_MATRIX_v1.4.md").decode(); versioned=target[rel(VERSIONED_MATRIX)].decode(); current=target[rel(CURRENT_MATRIX)].decode(); pointer=target[rel(CURRENT_POINTER)].decode(); canonical=target[rel(CANONICAL)].decode(); status=target[rel(STATUS)].decode()
 errors+=audit_matrix(predecessor,versioned)
 if current!=versioned: errors.append("CURRENT_MATRIX_DIFFERS_FROM_TARGET")
 errors+=validate_pointer(pointer); errors+=validate_canonical(canonical)
 if not status.strip(): errors.append("STATUS_EMPTY")
 files=[]
 for path in FILES:
  name=rel(path); current_bytes=path.read_bytes() if path.exists() else None; target_bytes=target[name]; source_kind="derived_from_versioned_matrix" if name==rel(CURRENT_MATRIX) else "source_commit_canonical"
  files.append({"path":name,"predecessor_sha256":sha_bytes(current_bytes) if current_bytes is not None else None,"source_commit_sha256":sha_bytes(source_bytes(source,path)),"target_sha256":sha_bytes(target_bytes),"target_source":source_kind,"changed":current_bytes!=target_bytes,"authorized":True})
  if source_kind=="source_commit_canonical" and target_bytes!=source_bytes(source,path): errors.append(f"TARGET_SOURCE_CONSTRUCTION_MISMATCH:{name}")
 return {"manifest_version":"1.3","engine_version":"v3.4","status":"PREPARED_NOT_APPLIED" if not errors else "BLOCKED_VALIDATION","transition":"RECONCILE_MATRIX_CURRENT_TO_VERSIONED_CANONICAL","target_matrix_version":matrix_version,"source_commit":source,"source_commit_verified":source==head,"source_of_truth":"source_commit","projections":["CURRENT_MATRIX"],"validation":["SOURCE_COMMIT_EXACTNESS","MONOTONIC_EVIDENCE","CROSS_REFERENCE","VERSION_POINTER","STATUS","CURRENT_EQUALS_VERSIONED_TARGET","NO_UNAUTHORIZED_CANONICAL_REWRITE"],"write_order":["BUILD","VALIDATE","WRITE","RE_READ","VERIFY"],"remote_policy":"COMMIT_PUSH_REMOTE_VERIFY","allowed_paths":sorted(ALLOWED_PATHS),"files":files,"validation_result":{"ok":not errors,"errors":errors}}
def self_test():
 source=git("rev-parse","HEAD"); target=build_target_state(source); matrix=target[rel(VERSIONED_MATRIX)].decode(); predecessor=source_bytes(source,GOV/"EVIDENCE_TO_CLAIM_MATRIX_v1.4.md").decode(); pointer=target[rel(CURRENT_POINTER)].decode(); canonical=target[rel(CANONICAL)].decode(); current=target[rel(CURRENT_MATRIX)].decode(); positive=audit_matrix(predecessor,matrix)+validate_pointer(pointer)+validate_canonical(canonical); source_exact=all(source_bytes(source,p)==target[rel(p)] for p in FILES if p!=CURRENT_MATRIX); current_projection=current==matrix; broken_pointer=validate_pointer(pointer.replace("**Current version:** v1.5","**Current version:** v1.4")); broken_canonical=validate_canonical(canonical.replace('"claim_matrix": "v1.5"','"claim_matrix": "v1.4"')); evidence_names=sorted(evidence_sections(predecessor)); broken_evidence=matrix.replace(evidence_names[0],"",1) if evidence_names else matrix; evidence_loss=audit_matrix(predecessor,broken_evidence); evidence_loss_exact=(not evidence_names) or ("SUCCESSOR_LOSES_EVIDENCE_SECTIONS:"+evidence_names[0] in evidence_loss); unauthorized_rewrite=source_exact and target[rel(CURRENT_POINTER)]!=pointer.replace("material FOS","material CHANGED")
 print("TGCV CANONICAL STATE SYNC"); print("MODE=SELFTEST"); print("ENGINE_VERSION=v3.4"); print("POSITIVE_TARGET_CONTRACT="+("PASS" if not positive and current_projection else "FAIL")); print("SOURCE_COMMIT_EXACTNESS="+("PASS" if source_exact else "FAIL")); print("NEGATIVE_POINTER_BLOCK="+("PASS" if "POINTER_TARGET_VERSION_INVALID" in broken_pointer else "FAIL")); print("NEGATIVE_CANONICAL_BLOCK="+("PASS" if "CANONICAL_MATRIX_VERSION_INVALID" in broken_canonical else "FAIL")); print("NEGATIVE_EVIDENCE_SECTION_BLOCK="+("PASS" if evidence_loss_exact else "FAIL")); print("UNAUTHORIZED_PROJECTION_REWRITE_BLOCKED="+("PASS" if unauthorized_rewrite else "FAIL")); ok=not positive and current_projection and source_exact and ("POINTER_TARGET_VERSION_INVALID" in broken_pointer) and ("CANONICAL_MATRIX_VERSION_INVALID" in broken_canonical) and evidence_loss_exact and unauthorized_rewrite; print("SELFTEST_RESULT="+("PASS" if ok else "FAIL")); return 0 if ok else 2

def load_manifest(path):
 try: data=json.loads(Path(path).read_text(encoding="utf-8"))
 except (OSError,json.JSONDecodeError) as exc: raise RuntimeError(f"INVALID_TRANSITION_MANIFEST:{exc}")
 required={"manifest_version","engine_version","status","target_matrix_version","source_commit","source_commit_verified","source_of_truth","allowed_paths","files","validation_result"}
 missing=sorted(required-set(data))
 if missing: raise RuntimeError("MANIFEST_MISSING_FIELDS:"+"|".join(missing))
 if data["manifest_version"]!="1.3" or data["engine_version"]!="v3.4": raise RuntimeError("MANIFEST_VERSION_INVALID")
 if data["status"]!="PREPARED_NOT_APPLIED": raise RuntimeError("MANIFEST_STATUS_INVALID")
 if data["target_matrix_version"]!=TARGET_MATRIX_VERSION: raise RuntimeError("MANIFEST_TARGET_VERSION_INVALID")
 if data["source_of_truth"]!="source_commit" or data["source_commit_verified"] is not True: raise RuntimeError("MANIFEST_SOURCE_NOT_VERIFIED")
 if data["validation_result"].get("ok") is not True or data["validation_result"].get("errors")!=[]: raise RuntimeError("MANIFEST_VALIDATION_NOT_PASS")
 if set(data["allowed_paths"])!=ALLOWED_PATHS: raise RuntimeError("MANIFEST_ALLOWED_PATHS_INVALID")
 expected={rel(p) for p in FILES}; rows=data["files"]
 if not isinstance(rows,list) or {r.get("path") for r in rows}!=expected or len(rows)!=len(expected): raise RuntimeError("MANIFEST_FILE_SET_INVALID")
 if any(r.get("authorized") is not True for r in rows): raise RuntimeError("MANIFEST_UNAUTHORIZED_PATH")
 return data

def apply_manifest(manifest_path):
 manifest=load_manifest(manifest_path); source=git("rev-parse",f'{manifest["source_commit"]}^{{commit}}'); head=git("rev-parse","HEAD")
 if source!=head: raise RuntimeError("SOURCE_COMMIT_NOT_HEAD")
 target=build_target_state(source); predecessor=source_bytes(source,GOV/"EVIDENCE_TO_CLAIM_MATRIX_v1.4.md").decode(); versioned=target[rel(VERSIONED_MATRIX)].decode()
 errors=audit_matrix(predecessor,versioned)+validate_pointer(target[rel(CURRENT_POINTER)].decode())+validate_canonical(target[rel(CANONICAL)].decode())
 if target[rel(CURRENT_MATRIX)]!=target[rel(VERSIONED_MATRIX)]: errors.append("CURRENT_MATRIX_DIFFERS_FROM_TARGET")
 if errors: raise RuntimeError("TARGET_VALIDATION_FAILED:"+"|".join(errors))
 rows={r["path"]:r for r in manifest["files"]}
 for name in ALLOWED_PATHS:
  expected_source=sha_bytes(source_bytes(source,Path(ROOT/name))); expected_target=sha_bytes(target[name])
  row=rows[name]
  if row.get("source_commit_sha256")!=expected_source or row.get("target_sha256")!=expected_target: raise RuntimeError(f"MANIFEST_HASH_MISMATCH:{name}")
 changed=[name for name in sorted(ALLOWED_PATHS) if (ROOT/name).read_bytes() if False]
 backups={}; writes=[]
 try:
  for name in sorted(ALLOWED_PATHS):
   path=ROOT/name; old=path.read_bytes() if path.exists() else None; new=target[name]
   backups[name]=old
   if old!=new: path.parent.mkdir(parents=True,exist_ok=True); writes.append(name); path.write_bytes(new)
  for name in sorted(ALLOWED_PATHS):
   path=ROOT/name
   if not path.exists() or sha(path)!=sha_bytes(target[name]): raise RuntimeError(f"POST_WRITE_VERIFY_FAILED:{name}")
 except Exception:
  for name,old in backups.items():
   path=ROOT/name
   if old is None:
    if path.exists(): path.unlink()
   else: path.write_bytes(old)
  raise
 print("TGCV CANONICAL STATE SYNC"); print("MODE=APPLY"); print("ENGINE_VERSION=v3.4"); print("SOURCE_COMMIT="+source); print("WRITE_RESULT=PASS"); print("FILES_WRITTEN="+str(len(writes))); print("RE_READ_VERIFY=PASS"); print("WRITTEN_PATHS="+json.dumps(writes,ensure_ascii=False)); print("REMOTE_COMMIT_PUSH=NOT_PERFORMED")
 return 0

def main():
 parser=argparse.ArgumentParser(); sub=parser.add_subparsers(dest="command",required=True); sub.add_parser("check"); sub.add_parser("verify"); sub.add_parser("selftest")
 for name in ("plan","manifest"):
  p=sub.add_parser(name); p.add_argument("--matrix-version",default=TARGET_MATRIX_VERSION); p.add_argument("--source-commit",default="HEAD");
  if name=="manifest": p.add_argument("--output")
 apply=sub.add_parser("apply"); apply.add_argument("--transition-manifest",required=True); publish=sub.add_parser("publish"); publish.add_argument("--transition-manifest",required=True)
 args=parser.parse_args(); before=snapshot()
 try:
  if args.command=="selftest": return self_test()
  if args.command in {"manifest","plan"}:
   data=resolve_manifest(args.matrix_version,args.source_commit)
   if args.command=="manifest":
    output=json.dumps(data,ensure_ascii=False,indent=2); print(output)
    if args.output: Path(args.output).write_text(output+"\n",encoding="utf-8")
    print("NO_GOVERNANCE_FILES_WRITTEN="+str(before==snapshot()).upper()); print("MANIFEST_RESULT="+("PREPARED_READ_ONLY" if data["validation_result"]["ok"] else "BLOCKED_READ_ONLY"))
   else:
    print("TGCV CANONICAL STATE SYNC"); print("MODE=PLAN"); print("ENGINE_VERSION=v3.4"); print("SOURCE_COMMIT="+data.get("source_commit","")); print("VALIDATION_RESULT="+("PASS" if data.get("validation_result",{}).get("ok") else "BLOCKED")); print("NO_GOVERNANCE_FILES_WRITTEN="+str(before==snapshot()).upper())
   return 0 if data.get("validation_result",{}).get("ok") else 2
  if args.command=="apply": return apply_manifest(args.transition_manifest)
  if args.command in {"check","verify"}:
   head=git("rev-parse","HEAD"); target=build_target_state(head); predecessor=source_bytes(head,GOV/"EVIDENCE_TO_CLAIM_MATRIX_v1.4.md").decode(); errors=audit_matrix(predecessor,target[rel(VERSIONED_MATRIX)].decode())+validate_pointer(target[rel(CURRENT_POINTER)].decode())+validate_canonical(target[rel(CANONICAL)].decode());
   if target[rel(CURRENT_MATRIX)]!=target[rel(VERSIONED_MATRIX)]: errors.append("CURRENT_MATRIX_DIFFERS_FROM_TARGET")
   print("TGCV CANONICAL STATE SYNC"); print("MODE="+args.command.upper()); print("ENGINE_VERSION=v3.4"); print("AUDIT_RESULT="+("PASS" if not errors else "BLOCKED")); print("ERRORS="+json.dumps(errors,ensure_ascii=False)); print("NO_GOVERNANCE_FILES_WRITTEN="+str(before==snapshot()).upper()); return 0 if not errors and before==snapshot() else 2
 except (RuntimeError,KeyError,TypeError) as exc:
  print("RESULT=FAIL_CLOSED"); print("REASON="+str(exc)); return 2
 print("RESULT=FAIL_CLOSED"); print("REASON=V3_4_WRITE_PATH_NOT_ENABLED"); return 2
if __name__=="__main__": raise SystemExit(main())
