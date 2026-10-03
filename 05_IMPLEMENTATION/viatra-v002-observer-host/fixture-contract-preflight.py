#!/usr/bin/env python3
"""Deterministic VIATRA V002 fixture-level contract preflight.

This script is intentionally static: it does not invoke Maven, Tycho, Java,
VIATRA, or any transformation/runtime execution.
"""
from __future__ import annotations

import hashlib
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parent.parent.parent.parent
FIX = ROOT / "00_GOVERNANCE" / "architecture" / "fixtures"

FILES = {
    "cps": FIX / "TGCV_VIATRA_MINIMAL_FIXTURE_v002_CPS.xmi",
    "deployment_initial": FIX / "TGCV_VIATRA_MINIMAL_FIXTURE_v002_Deployment_INITIAL.xmi",
    "deployment_expected": FIX / "TGCV_VIATRA_MINIMAL_FIXTURE_v002_Deployment_EXPECTED.xmi",
    "trace_initial": FIX / "TGCV_VIATRA_MINIMAL_FIXTURE_v002_Traceability_INITIAL.xmi",
    "trace_expected": FIX / "TGCV_VIATRA_MINIMAL_FIXTURE_v002_Traceability_EXPECTED.xmi",
}
MANIFEST = FIX / "TGCV_VIATRA_V002_FIXTURE_BYTE_HASH_MANIFEST_001.md"

NS = {
    "xmi": "http://www.omg.org/XMI",
    "cps": "http://org.eclipse.viatra/model/cps",
    "dep": "http://org.eclipse.viatra/model/deployment",
    "tr": "http://org.eclipse.viatra/model/cps-traceability",
}

EXPECTED_ROOTS = {
    "cps": (NS["cps"], "CyberPhysicalSystem"),
    "deployment_initial": (NS["dep"], "Deployment"),
    "deployment_expected": (NS["dep"], "Deployment"),
    "trace_initial": (NS["tr"], "CPSToDeployment"),
    "trace_expected": (NS["tr"], "CPSToDeployment"),
}

TRANSFORMATION_ID = (
    "org.eclipse.viatra.examples.cps.xform.m2m.batch.viatra",
    "CPS2DeploymentTransformationViatra",
    "hostRule",
    "V002",
)

FORBIDDEN_TERMS = re.compile(
    r"(?i)\b(value|utility|reward|performance[_ -]?score|downstream[_ -]?outcome|"
    r"market|business[_ -]?variable|value[_ -]?construction)\b"
)


def fail(message: str) -> None:
    raise AssertionError(message)


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def ns_uri(tag: str) -> str:
    return tag[1:].split("}", 1)[0] if tag.startswith("{") else ""


def parse(path: Path) -> tuple[bytes, ET.Element]:
    raw = path.read_bytes()
    try:
        root = ET.fromstring(raw)
    except ET.ParseError as exc:
        fail(f"F2 XML parse failed: {path}: {exc}")
    return raw, root


def href_target(value: str) -> tuple[str, str]:
    value = unquote(value)
    if "#" not in value:
        fail(f"reference has no fragment: {value}")
    filename, fragment = value.split("#", 1)
    return Path(filename).name, fragment


def all_named(root: ET.Element, name: str) -> list[ET.Element]:
    return [e for e in root.iter() if local_name(e.tag) == name]


def assert_exactly(items, n: int, label: str) -> None:
    if len(items) != n:
        fail(f"{label}: expected {n}, found {len(items)}")


def check_manifest(raws: dict[str, bytes]) -> None:
    text = MANIFEST.read_text(encoding="utf-8")
    for key, path in FILES.items():
        if not path.exists():
            fail(f"F1 missing fixture: {path}")
        digest = hashlib.sha256(raws[key]).hexdigest()
        size = len(raws[key])
        labels = {
            "TGCV_VIATRA_MINIMAL_FIXTURE_v002_CPS.xmi": "CPS",
            "TGCV_VIATRA_MINIMAL_FIXTURE_v002_Deployment_INITIAL.xmi": "Deployment INITIAL",
            "TGCV_VIATRA_MINIMAL_FIXTURE_v002_Deployment_EXPECTED.xmi": "Deployment EXPECTED",
            "TGCV_VIATRA_MINIMAL_FIXTURE_v002_Traceability_INITIAL.xmi": "Traceability INITIAL",
            "TGCV_VIATRA_MINIMAL_FIXTURE_v002_Traceability_EXPECTED.xmi": "Traceability EXPECTED",
        }
        if digest not in text:
            fail(f"F1 SHA-256 for {path.name} is absent from canonical manifest: {digest}")
        label = labels[path.name]
        line = next((x for x in text.splitlines() if f"| {label} |" in x), "")
        if not line:
            fail(f"F1 manifest row missing for {path.name}")
        fields = [x.strip().strip("`") for x in line.strip().strip("|").split("|")]
        if len(fields) != 3 or fields[1] != digest:
            fail(f"F1 SHA-256 manifest mismatch for {path.name}: {digest}")
        try:
            recorded_size = int(fields[2])
        except ValueError:
            fail(f"F1 invalid byte count in manifest for {path.name}: {fields[2]!r}")
        if recorded_size != size:
            fail(f"F1 byte count mismatch for {path.name}: {size} != {recorded_size}")
        print(f"F1 PASS {path.name}: {size} bytes sha256={digest}")


def check_root(name: str, root: ET.Element) -> None:
    uri, local = EXPECTED_ROOTS[name]
    if ns_uri(root.tag) != uri or local_name(root.tag) != local:
        fail(f"F3 root mismatch for {name}: {{{ns_uri(root.tag)}}}{local_name(root.tag)}")
    if root.get(f"{{{NS['xmi']}}}version") != "2.0":
        fail(f"F3 xmi:version != 2.0 for {name}")
    print(f"F3 PASS {name}: {uri}/{local}")


def check_cps(root: ET.Element) -> None:
    hosts = all_named(root, "hostTypes")
    assert_exactly(hosts, 1, "F4 hostTypes")
    if hosts[0].get("identifier") != "Rawsberry.PI":
        fail("F4 hostType identifier mismatch")
    instances = all_named(hosts[0], "instances")
    assert_exactly(instances, 1, "F4 hostType instances")
    if instances[0].get("identifier") != "Aragorn":
        fail("F4 HostInstance identifier mismatch")
    if instances[0].get("nodeIp") != "152.66.102.6":
        fail("F4 HostInstance nodeIp mismatch")
    print("F4 PASS CPS semantic fixture")


def check_deployment_initial(root: ET.Element) -> None:
    assert_exactly(all_named(root, "hosts"), 0, "F5 initial hosts")
    print("F5 PASS initial Deployment has zero hosts")


def check_trace_initial(root: ET.Element) -> None:
    assert_exactly([root], 1, "F6 trace root")
    cps_refs = root.get("cps") or root.get("cpsSystem")
    dep_refs = root.get("deployment")
    if not cps_refs or not dep_refs:
        fail("F6 initial trace root references are incomplete")
    if all_named(root, "traces"):
        fail("F6 initial trace unexpectedly contains traces")
    cfile, cfrag = href_target(cps_refs)
    dfile, dfrag = href_target(dep_refs)
    if cfile != FILES["cps"].name or cfrag != "/":
        fail("F6 initial trace CPS reference mismatch")
    if dfile != FILES["deployment_initial"].name or dfrag != "/":
        fail("F6 initial trace Deployment reference mismatch")
    print("F6 PASS initial Traceability")


def check_deployment_expected(root: ET.Element) -> None:
    hosts = all_named(root, "hosts")
    assert_exactly(hosts, 1, "F7 expected hosts")
    if hosts[0].get("ip") != "152.66.102.6":
        fail("F7 expected host IP mismatch")
    print("F7 PASS expected Deployment")


def check_trace_expected(root: ET.Element) -> None:
    cps_refs = root.get("cps") or root.get("cpsSystem")
    dep_refs = root.get("deployment")
    if not cps_refs or not dep_refs:
        fail("F8 expected trace root references are incomplete")
    traces = all_named(root, "traces")
    assert_exactly(traces, 1, "F8 traces")
    trace = traces[0]
    source_refs = [e.get("href") or e.get("cpsElement") for e in all_named(trace, "cpsElements")]
    target_refs = [e.get("href") or e.get("deploymentElement") for e in all_named(trace, "deploymentElements")]
    source_refs = [x for x in source_refs if x]
    target_refs = [x for x in target_refs if x]
    assert_exactly(source_refs, 1, "F8 cpsElements")
    assert_exactly(target_refs, 1, "F8 deploymentElements")
    cfile, cfrag = href_target(cps_refs)
    dfile, dfrag = href_target(dep_refs)
    if cfile != FILES["cps"].name or cfrag != "/":
        fail("F8 expected trace CPS reference mismatch")
    if dfile != FILES["deployment_expected"].name or dfrag != "/":
        fail("F8 expected trace Deployment reference mismatch")
    sfile, sfrag = href_target(source_refs[0])
    tfile, tfrag = href_target(target_refs[0])
    if sfile != FILES["cps"].name or sfrag != "//@hostTypes.0/@instances.0":
        fail("F8 trace source reference mismatch")
    expected_hosts = all_named(DEP_EXP_ROOT, "hosts")
    assert_exactly(expected_hosts, 1, "F8 expected host")
    if tfile != FILES["deployment_expected"].name or tfrag != "//@hosts.0":
        fail("F8 trace target reference mismatch")
    print("F8 PASS expected Traceability")


def check_correspondence() -> None:
    initial_hosts = all_named(DEP_INIT_ROOT, "hosts")
    expected_hosts = all_named(DEP_EXP_ROOT, "hosts")
    initial_traces = all_named(TR_INIT_ROOT, "traces")
    expected_traces = all_named(TR_EXP_ROOT, "traces")
    assert_exactly(initial_hosts, 0, "F9 initial hosts")
    assert_exactly(expected_hosts, 1, "F9 expected hosts")
    if expected_hosts[0].get("ip") != all_named(CPS_ROOT, "instances")[0].get("nodeIp"):
        fail("F9 expected host IP does not equal CPS nodeIp")
    assert_exactly(initial_traces, 0, "F9 initial traces")
    assert_exactly(expected_traces, 1, "F9 expected traces")
    print("F9 PASS direct expected-state correspondence")


def check_identity() -> None:
    if TRANSFORMATION_ID != (
        "org.eclipse.viatra.examples.cps.xform.m2m.batch.viatra",
        "CPS2DeploymentTransformationViatra",
        "hostRule",
        "V002",
    ):
        fail("F10 transformation identity mismatch")
    print("F10 PASS canonical transformation identity")


def check_firewall() -> None:
    text = ""
    for path in FILES.values():
        text += path.read_text(encoding="utf-8")
    forbidden = FORBIDDEN_TERMS.findall(text)
    if forbidden:
        fail(f"F12 forbidden scientific fields/terms found: {forbidden}")
    print("F12 PASS scientific firewall")


raws = {}
roots = {}
for key, path in FILES.items():
    if not path.exists():
        fail(f"F1 missing fixture: {path}")
    raw, root = parse(path)
    raws[key] = raw
    roots[key] = root

CPS_ROOT = roots["cps"]
DEP_INIT_ROOT = roots["deployment_initial"]
DEP_EXP_ROOT = roots["deployment_expected"]
TR_INIT_ROOT = roots["trace_initial"]
TR_EXP_ROOT = roots["trace_expected"]

check_manifest(raws)
for name, root in roots.items():
    check_root(name, root)
check_cps(CPS_ROOT)
check_deployment_initial(DEP_INIT_ROOT)
check_trace_initial(TR_INIT_ROOT)
check_deployment_expected(DEP_EXP_ROOT)
check_trace_expected(TR_EXP_ROOT)
check_correspondence()
check_identity()
check_firewall()

print("F11 PASS static P1-P8 input surface; runtime-only properties remain gated")
print("VIATRA_V002_FIXTURE_PREFLIGHT=PASS")
