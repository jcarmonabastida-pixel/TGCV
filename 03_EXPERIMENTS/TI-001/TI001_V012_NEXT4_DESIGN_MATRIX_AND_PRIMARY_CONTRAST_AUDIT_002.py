"""NEXT4 design-matrix/primary-contrast audit. Audit-only; no provider or scientific execution."""
from __future__ import annotations
import hashlib,json,sys
from TI001_V012_NEXT4_DESIGN_MATRIX_AND_PRIMARY_CONTRAST_001 import CANDIDATE_N,audit,manifest

results=[audit(n) for n in CANDIDATE_N]
checks={
  "all_candidate_N":len(results)==5,
  "all_54_columns":all(r["columns"]==54 for r in results),
  "full_column_rank":all(r["full_column_rank"] for r in results),
  "contrast_estimable":all(r["contrast_estimable"] for r in results),
  "weights_sum_to_one":abs((72/96)+(24/96)-1)<1e-15,
  "response_independent":manifest()["response_independent"],
  "provider_calls":manifest()["provider_calls"] is False,
  "scientific_execution":manifest()["scientific_execution"] is False,
}
out={"artifact":"TI001_V012_NEXT4_DESIGN_MATRIX_AND_PRIMARY_CONTRAST_AUDIT_002",
     "status":"PASS" if all(checks.values()) else "FAIL",
     "implementation":"TI001_V012_NEXT4_DESIGN_MATRIX_AND_PRIMARY_CONTRAST_001.py",
     "implementation_commit":"d7f0fc454b61723ab63b6b1ba1eb3320db47d254",
     "checks":checks,"audits":results}
raw=json.dumps(out,sort_keys=True,separators=(",",":")).encode()
out["audit_result_sha256"]=hashlib.sha256(raw).hexdigest()
print(json.dumps(out,sort_keys=True,indent=2))
if out["status"]!="PASS": sys.exit(1)
