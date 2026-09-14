#!/usr/bin/env python3
"""TGCV C09 — KGFS/D178 local-only exact variable and reproducibility audit.

This runner deliberately performs NO network acquisition. GitHub is the
canonical governance/continuity source; the local D178 .dta files are the
execution/evidence inputs. It audits the 74 expected D178 files, including
reconciled/D178F70.dta, computes local SHA-256, inspects exact Stata variable
names/labels with pyreadstat, checks core identifiers, and records candidate
trajectory-variable names by transparent term matching. It does not infer
causal status, does not redefine T_acc from outcomes/take-up, and does not
upgrade C09/Core/RMA/STATUS.
"""
from __future__ import annotations
import hashlib, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
BASELINE = DATA / "baseline"
ENDLINE = DATA / "endline"
RECONCILED = ROOT / "reconciled"
OUTPUT = ROOT / "output"
OUTPUT.mkdir(parents=True, exist_ok=True)

EXPECTED = {f"D178F{i:02d}": ("baseline" if i <= 40 else "endline") for i in range(3, 77)}
CORE_IDS = ["hhid", "memid", "cont_s_id"]
TRAJECTORY_TERMS = [
    "occup", "occupation", "employ", "employment", "job", "income", "earn",
    "wage", "salary", "business", "enterprise", "sales", "profit", "loan",
    "borrow", "lender", "saving", "savings", "insurance", "insur", "asset",
    "wealth", "poverty", "wellbeing", "welfare"
]
EXCLUDED_FROM_TACC = [
    "loan", "borrow", "lender", "saving", "savings", "insurance", "insur",
    "investment", "invest", "employ", "employment", "job", "income", "earn",
    "wage", "salary", "business", "enterprise", "sales", "profit", "poverty",
    "wellbeing", "welfare"
]

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def locate(label: str):
    if label == "D178F70":
        p = RECONCILED / "D178F70.dta"
        return p if p.exists() else None
    category = EXPECTED[label]
    p = (BASELINE if category == "baseline" else ENDLINE) / f"{label}.dta"
    return p if p.exists() else None

def norm(s):
    return re.sub(r"[^a-z0-9_]+", "_", str(s).lower()).strip("_")

def main():
    try:
        import pyreadstat
    except Exception as e:
        raise SystemExit(f"pyreadstat is required for exact variable audit: {e}")

    files = []
    missing = []
    for label, wave in EXPECTED.items():
        p = locate(label)
        if p is None:
            missing.append(label)
            continue
        meta = pyreadstat.read_dta(str(p), metadataonly=True)[1]
        names = list(meta.column_names)
        labels = list(meta.column_labels) if meta.column_labels else [""] * len(names)
        label_map = dict(zip(names, labels))
        exact_ids = {k: (k in names) for k in CORE_IDS}
        lower_names = {n.lower(): n for n in names}
        matches = []
        for n in names:
            text = f"{n} {label_map.get(n, '')}".lower()
            hits = sorted({t for t in TRAJECTORY_TERMS if t in text})
            if hits:
                matches.append({"name": n, "label": label_map.get(n, ""), "matched_terms": hits})
        excluded_hits = []
        for n in names:
            text = f"{n} {label_map.get(n, '')}".lower()
            hits = sorted({t for t in EXCLUDED_FROM_TACC if t in text})
            if hits:
                excluded_hits.append({"name": n, "label": label_map.get(n, ""), "matched_terms": hits})
        files.append({
            "file_name": label,
            "wave": wave,
            "path": str(p),
            "size_bytes": p.stat().st_size,
            "sha256": sha256(p),
            "variable_count": len(names),
            "core_identifiers": exact_ids,
            "trajectory_term_matches": matches,
            "tacc_exclusion_matches": excluded_hits,
        })

    result = {
        "audit": "TGCV_C09_KGFS_D178_LOCAL_VARIABLE_AUDIT",
        "file_count_expected": 74,
        "file_count_audited": len(files),
        "missing_files": missing,
        "technical_status": "PASS" if len(files) == 74 and not missing else "OPEN",
        "scientific_claim_status": "NO_C09_UPGRADE",
        "scope": {
            "baseline": "D178F03-D178F40",
            "endline": "D178F41-D178F76",
            "reconciled_exception": "D178F70",
            "core_identifiers": CORE_IDS,
            "trajectory_matching_is_discovery_only": True,
            "tacc_outcome_exclusion_is_audit_guard": True,
        },
        "files": files,
    }
    (OUTPUT / "KGFS_TRAJECTORY_VARIABLE_AUDIT_EXACT.json").write_text(
        json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    md = [
        "# KGFS / D178 — Exact Local Variable Audit",
        "",
        f"- Files expected: **74**",
        f"- Files audited: **{len(files)}**",
        f"- Missing: **{len(missing)}**" + (f" ({', '.join(missing)})" if missing else ""),
        f"- Technical status: **{result['technical_status']}**",
        "- Scientific claim status: **NO C09 UPGRADE**",
        "",
        "## Core identifiers",
        "",
        "Exact presence is reported per file for `hhid`, `memid`, `cont_s_id`.",
        "",
        "## Trajectory-variable discovery",
        "",
        "Term matches are discovery/audit aids only. They do not constitute a TGCV trajectory definition.",
        "",
    ]
    for r in files:
        md.append(f"### {r['file_name']} ({r['wave']})")
        md.append(f"- size: {r['size_bytes']:,} bytes")
        md.append(f"- SHA-256: `{r['sha256']}`")
        md.append(f"- variables: {r['variable_count']}")
        md.append("- identifiers: " + ", ".join(f"`{k}`={'YES' if v else 'NO'}" for k,v in r['core_identifiers'].items()))
        md.append("- trajectory matches: " + (", ".join(f"`{x['name']}`" for x in r['trajectory_term_matches']) or "none"))
        md.append("- T_acc exclusion matches: " + (", ".join(f"`{x['name']}`" for x in r['tacc_exclusion_matches']) or "none"))
        md.append("")
    (OUTPUT / "KGFS_TRAJECTORY_VARIABLE_AUDIT_EXACT.md").write_text("\n".join(md), encoding="utf-8")
    print(json.dumps({"technical_status": result["technical_status"], "files_audited": len(files), "missing": missing, "scientific_claim_status": "NO_C09_UPGRADE"}, indent=2))
    return 0 if not missing else 2

if __name__ == "__main__":
    raise SystemExit(main())
