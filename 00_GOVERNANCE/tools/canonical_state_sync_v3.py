#!/usr/bin/env python3
"""TGCV Canonical State Sync v3.5.

Controlled canonical-state reconciliation. CURRENT matrix is derived only from
its versioned matrix. All other governed artifacts are byte-exact source-commit
references. apply/publish are enabled only after manifest validation.
"""
from __future__ import annotations
import argparse, hashlib, json, subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
GOV = ROOT / "00_GOVERNANCE"
VERSIONED_MATRIX = GOV / "EVIDENCE_TO_CLAIM_MATRIX_v1.5.md"
CURRENT_MATRIX = GOV / "EVIDENCE_TO_CLAIM_MATRIX_CURRENT.md"
CURRENT_POINTER = GOV / "EVIDENCE_TO_CLAIM_MATRIX_CURRENT_POINTER.md"
CANONICAL = GOV / "CANONICAL_STATE.json"
RMA = GOV / "rma" / "TGCV_RMA_current.md"
TRACE = GOV / "rma" / "TGCV_RMA_traceability_current.csv"
STATUS = ROOT / "STATUS.md"
FILES = [CANONICAL, CURRENT_MATRIX, CURRENT_POINTER, VERSIONED_MATRIX, RMA, TRACE, STATUS]
TARGET_MATRIX_VERSION = "v1.5"
TARGET_RMA_VERSION = "v3.34"
TARGET_TRACE_VERSION = "v3.34"

def rel(p: Path) -> str: return p.relative_to(ROOT).as_posix()
def sha_bytes(b: bytes) -> str: return hashlib.sha256(b).hexdigest()
def sha(p: Path) -> str: return sha_bytes(p.read_bytes())

def git(*args: str, check: bool = True) -> str:
    r = subprocess.run(["git", *args], cwd=ROOT, text=True, capture_output=True, encoding="utf-8", errors="replace")
    if check and r.returncode: raise RuntimeError(r.stderr.strip() or r.stdout.strip())
    return r.stdout.strip()

def git_bytes(*args: str) -> bytes:
    r = subprocess.run(["git", *args], cwd=ROOT, capture_output=True)
    if r.returncode: raise RuntimeError(r.stderr.decode("utf-8", "replace").strip())
    return r.stdout

def source_bytes(commit: str, p: Path) -> bytes: return git_bytes("show", f"{commit}:{rel(p)}")
def heads(t: str) -> list[str]: return [x.lstrip("#").strip() for x in t.splitlines() if x.startswith("#")]
def columns(t: str) -> list[str]:
    for x in t.splitlines():
        if x.startswith("| ID") or x.startswith("|ID"): return [y.strip() for y in x.strip("|").split("|")]
    return []
def claims(t: str) -> list[str]: return [x.split("|")[1].strip() for x in t.splitlines() if x.startswith("| C") and "|" in x]
def evidence_sections(t: str) -> set[str]: return {h for h in heads(t) if h.lower().startswith("material ") and "evidence" in h.lower()}

def validate_pointer(t: str) -> list[str]:
    e=[]
    if "**Current version:** v1.5" not in t: e.append("POINTER_TARGET_VERSION_INVALID")
    if "EVIDENCE_TO_CLAIM_MATRIX_v1.5.md" not in t: e.append("POINTER_TARGET_ARTIFACT_INVALID")
    return e

def validate_canonical(t: str) -> list[str]:
    try: s=json.loads(t)
    except json.JSONDecodeError: return ["CANONICAL_STATE_INVALID_JSON"]
    v=s.get("current_versions",{}); e=[]
    if v.get("rma") != TARGET_RMA_VERSION: e.append("CANONICAL_RMA_VERSION_INVALID")
    if v.get("claim_matrix") != TARGET_MATRIX_VERSION: e.append("CANONICAL_MATRIX_VERSION_INVALID")
    if v.get("rma_traceability") != TARGET_TRACE_VERSION: e.append("CANONICAL_TRACE_VERSION_INVALID")
    return e

def audit_matrix(pre: str, suc: str) -> list[str]:
    e=[]
    if len(suc.splitlines()) < len(pre.splitlines()): e.append("SUCCESSOR_MATRIX_SHRINKS_IN_LINES")
    if not set(claims(pre)) <= set(claims(suc)): e.append("SUCCESSOR_LOSES_CLAIMS")
    if columns(pre) != columns(suc): e.append("SUCCESSOR_COLUMNS_CHANGED")
    if not evidence_sections(pre) <= evidence_sections(suc): e.append("SUCCESSOR_LOSES_EVIDENCE_SECTIONS")
    req={"Claim boundary","Current methodological routing","Current scientific position","Gate state","Interpretation boundary"}
    if not req <= set(heads(suc)): e.append("SUCCESSOR_LOSES_GOVERNANCE_BOUNDARIES")
    if "**Predecessor:** v1.4" not in suc: e.append("SUCCESSOR_PREDECESSOR_METADATA_INVALID")
    if "FOS C09" not in suc: e.append("FOS_C09_MISSING")
    return e

def build_target(source: str) -> dict[str,bytes]:
    versioned=source_bytes(source,VERSIONED_MATRIX)
    if source_bytes(source,CURRENT_MATRIX) != versioned: raise RuntimeError("SOURCE_CURRENT_DIFFERS_FROM_DERIVED_MATRIX")
    return {rel(CANONICAL):source_bytes(source,CANONICAL),rel(CURRENT_MATRIX):versioned,rel(CURRENT_POINTER):source_bytes(source,CURRENT_POINTER),rel(VERSIONED_MATRIX):versioned,rel(RMA):source_bytes(source,RMA),rel(TRACE):source_bytes(source,TRACE),rel(STATUS):source_bytes(source,STATUS)}

def snapshot(): return {rel(p):(sha(p) if p.exists() else None) for p in FILES}

def resolve_manifest(matrix_version: str, source_commit: str) -> dict:
    if matrix_version != TARGET_MATRIX_VERSION: return {"status":"BLOCKED_VALIDATION","validation_result":{"ok":False,"errors":["UNSUPPORTED_TARGET_VERSION"]}}
    head=git("rev-parse","HEAD"); source=git("rev-parse",f"{source_commit}^{{commit}}")
    e=[]
    if head != source: e.append("SOURCE_COMMIT_NOT_HEAD")
    target=build_target(source)
    pre=source_bytes(source,GOV/"EVIDENCE_TO_CLAIM_MATRIX_v1.4.md").decode(); ver=target[rel(VERSIONED_MATRIX)].decode(); cur=target[rel(CURRENT_MATRIX)].decode()
    e += audit_matrix(pre,ver)+validate_pointer(target[rel(CURRENT_POINTER)].decode())+validate_canonical(target[rel(CANONICAL)].decode())
    if cur != ver: e.append("CURRENT_MATRIX_DIFFERS_FROM_TARGET")
    if not target[rel(STATUS)].strip(): e.append("STATUS_EMPTY")
    fs=[]
    for p in FILES:
        n=rel(p); cb=p.read_bytes() if p.exists() else None; tb=target[n]
        if n != rel(CURRENT_MATRIX) and cb != tb: e.append(f"CANONICAL_SOURCE_MISMATCH:{n}")
        fs.append({"path":n,"predecessor_sha256":sha_bytes(cb) if cb is not None else None,"source_commit_sha256":sha_bytes(source_bytes(source,p)),"target_sha256":sha_bytes(tb),"target_source":"derived_from_versioned_matrix" if n==rel(CURRENT_MATRIX) else "source_commit_canonical","changed":cb!=tb,"authorized":True})
    return {"manifest_version":"1.4","engine_version":"v3.5","status":"PREPARED_NOT_APPLIED" if not e else "BLOCKED_VALIDATION","transition":"RECONCILE_MATRIX_CURRENT_TO_VERSIONED_CANONICAL","target_matrix_version":matrix_version,"source_commit":source,"source_commit_verified":source==head,"source_of_truth":"source_commit","projections":["CURRENT_MATRIX"],"validation":["SOURCE_COMMIT_EXACTNESS","MONOTONIC_EVIDENCE","CROSS_REFERENCE","VERSION_POINTER","STATUS","CURRENT_EQUALS_VERSIONED_TARGET","NO_UNAUTHORIZED_CANONICAL_REWRITE"],"write_order":["BUILD","VALIDATE","WRITE","RE_READ","VERIFY"],"remote_policy":"COMMIT_PUSH_REMOTE_VERIFY","allowed_paths":[rel(p) for p in FILES],"files":fs,"validation_result":{"ok":not e,"errors":e}}

def selftest() -> int:
    source=git("rev-parse","HEAD"); target=build_target(source); pre=source_bytes(source,GOV/"EVIDENCE_TO_CLAIM_MATRIX_v1.4.md").decode(); matrix=target[rel(VERSIONED_MATRIX)].decode(); pointer=target[rel(CURRENT_POINTER)].decode(); canonical=target[rel(CANONICAL)].decode(); current=target[rel(CURRENT_MATRIX)].decode()
    positive=audit_matrix(pre,matrix)+validate_pointer(pointer)+validate_canonical(canonical); exact=all(source_bytes(source,p)==target[rel(p)] for p in FILES if p!=CURRENT_MATRIX); projection=current==matrix
    bp=validate_pointer(pointer.replace("**Current version:** v1.5","**Current version:** v1.4")); bc=validate_canonical(canonical.replace('"claim_matrix": "v1.5"','"claim_matrix": "v1.4"'))
    print("TGCV CANONICAL STATE SYNC\nMODE=SELFTEST\nENGINE_VERSION=v3.5")
    print("POSITIVE_TARGET_CONTRACT="+('PASS' if not positive and projection else 'FAIL')); print("SOURCE_COMMIT_EXACTNESS="+('PASS' if exact else 'FAIL')); print("NEGATIVE_POINTER_BLOCK="+('PASS' if "POINTER_TARGET_VERSION_INVALID" in bp else 'FAIL')); print("NEGATIVE_CANONICAL_BLOCK="+('PASS' if "CANONICAL_MATRIX_VERSION_INVALID" in bc else 'FAIL')); print("SELFTEST_RESULT="+('PASS' if not positive and exact and projection and bp and bc else 'FAIL'))
    return 0 if not positive and exact and projection and bp and bc else 2

def write_target(target: dict[str,bytes], manifest: dict):
    if not manifest.get("validation_result",{}).get("ok"): raise RuntimeError("TRANSITION_MANIFEST_BLOCKED")
    if git("rev-parse","HEAD") != manifest["source_commit"]: raise RuntimeError("SOURCE_COMMIT_NOT_HEAD")
    for n in manifest["allowed_paths"]:
        p=ROOT/n; p.parent.mkdir(parents=True,exist_ok=True); p.write_bytes(target[n])
    return snapshot()

def load_manifest(path: str) -> dict: return json.loads(Path(path).read_text(encoding="utf-8"))

def apply_manifest(path: str) -> int:
    before=snapshot(); m=load_manifest(path); source=m.get("source_commit"); target=build_target(source)
    if git("rev-parse","HEAD") != source: raise RuntimeError("SOURCE_COMMIT_NOT_HEAD")
    after=write_target(target,m); print("TGCV CANONICAL STATE SYNC\nMODE=APPLY\nENGINE_VERSION=v3.5"); print("FILES_CHANGED="+str(sum(before[k]!=after[k] for k in before))); print("APPLY_RESULT=PASS"); return 0

def publish_manifest(path: str) -> int:
    m=load_manifest(path)
    if not m.get("validation_result",{}).get("ok"): raise RuntimeError("TRANSITION_MANIFEST_BLOCKED")
    branch=git("symbolic-ref","--short","-q","HEAD")
    if not branch: raise RuntimeError("PUBLISH_REQUIRES_BRANCH_HEAD")
    before=snapshot(); target=build_target(m["source_commit"]); write_target(target,m); after=snapshot()
    changed=[n for n in m["allowed_paths"] if before[n]!=after[n]]
    if not changed:
        print("TGCV CANONICAL STATE SYNC\nMODE=PUBLISH\nENGINE_VERSION=v3.5\nPUBLISH_RESULT=NO_CHANGES"); return 0
    git("add","--",*changed); git("commit","-m","GOVERNANCE: publish canonical state transition")
    git("push","origin",branch)
    pushed=git("rev-parse","HEAD"); remote=git("ls-remote","origin",f"refs/heads/{branch}").split()[0]
    if pushed != remote: raise RuntimeError("REMOTE_HEAD_VERIFICATION_FAILED")
    print("TGCV CANONICAL STATE SYNC\nMODE=PUBLISH\nENGINE_VERSION=v3.5\nPUBLISHED_BRANCH="+branch+"\nPUBLISHED_COMMIT="+pushed+"\nPUBLISH_RESULT=PASS"); return 0

def main() -> int:
    ap=argparse.ArgumentParser(); sub=ap.add_subparsers(dest="command",required=True); sub.add_parser("check"); sub.add_parser("verify"); sub.add_parser("selftest")
    for n in ("plan","manifest"):
        p=sub.add_parser(n); p.add_argument("--matrix-version",default=TARGET_MATRIX_VERSION); p.add_argument("--source-commit",default="HEAD"); p.add_argument("--output") if n=="manifest" else None
    for n in ("apply","publish"): sub.add_parser(n).add_argument("--transition-manifest",required=True)
    a=ap.parse_args(); before=snapshot()
    if a.command=="selftest": return selftest()
    if a.command in {"plan","manifest"}:
        d=resolve_manifest(a.matrix_version,a.source_commit)
        if a.command=="manifest":
            out=json.dumps(d,ensure_ascii=False,indent=2); print(out)
            if a.output: Path(a.output).write_text(out+"\n",encoding="utf-8")
            print("NO_GOVERNANCE_FILES_WRITTEN="+str(before==snapshot()).upper()); print("MANIFEST_RESULT="+("PREPARED_READ_ONLY" if d["validation_result"]["ok"] else "BLOCKED_READ_ONLY"))
        else:
            print("TGCV CANONICAL STATE SYNC\nMODE=PLAN\nENGINE_VERSION=v3.5\nSOURCE_COMMIT="+d.get("source_commit","") ); print("VALIDATION_RESULT="+("PASS" if d.get("validation_result",{}).get("ok") else "BLOCKED")); print("NO_GOVERNANCE_FILES_WRITTEN="+str(before==snapshot()).upper())
        return 0 if d.get("validation_result",{}).get("ok") else 2
    if a.command in {"check","verify"}:
        d=resolve_manifest(TARGET_MATRIX_VERSION,"HEAD"); print("TGCV CANONICAL STATE SYNC\nMODE="+a.command.upper()+"\nENGINE_VERSION=v3.5\nAUDIT_RESULT="+("PASS" if d["validation_result"]["ok"] and before==snapshot() else "BLOCKED")+"\nERRORS="+json.dumps(d["validation_result"]["errors"])); return 0 if d["validation_result"]["ok"] and before==snapshot() else 2
    try: return apply_manifest(a.transition_manifest) if a.command=="apply" else publish_manifest(a.transition_manifest)
    except Exception as ex: print("RESULT=FAIL_CLOSED\nREASON="+str(ex)); return 2

if __name__ == "__main__": raise SystemExit(main())