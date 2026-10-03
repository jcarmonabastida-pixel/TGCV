#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"

SOURCE_REV="eb68158a3d74581f69ccb8bc4f47673b12abdf85"
TARGET_BLOB_SHA="7481dee30f1ae07d7dd9212d7891dc336f1e96ae"

echo "== Repository structure =="
test -f pom.xml
test -f target-definition/pom.xml
test -f target-definition/tgcv-viatra-v002-target.target
test -f cps-models/pom.xml
test -f observer/pom.xml
test -f observer/META-INF/MANIFEST.MF
test -f materialize-historical-cps-models.sh

echo "== Historical CPS materialization contract =="
grep -Fq "$SOURCE_REV" materialize-historical-cps-models.sh
for bundle in   org.eclipse.viatra.examples.cps.model   org.eclipse.viatra.examples.cps.deployment   org.eclipse.viatra.examples.cps.traceability
do
  b="cps-models/$bundle"
  test -f "$b/pom.xml"
  test -f "$b/META-INF/MANIFEST.MF"
  test -f "$b/build.properties"
  test -f "$b/plugin.xml"
  test -f "$b/plugin.properties"
  test -d "$b/model"
  test -d "$b/src"
  test -n "$(find "$b/model" -type f -print -quit)"
  test -n "$(find "$b/src" -type f -print -quit)"
done

echo "== Static XML/reactor closure audit =="

python3 - "$ROOT" <<'PY'
import hashlib
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

root = Path(sys.argv[1])

EXPECTED_ROOT = ("org.tgcv", "viatra-v002-observer-host", "0.1.0-SNAPSHOT")
EXPECTED_TARGET = ("org.tgcv", "tgcv-viatra-v002-target", "0.1.0-SNAPSHOT")
EXPECTED_CPS_AGG = ("org.tgcv", "tgcv-viatra-v002-cps-models", "0.1.0-SNAPSHOT")
EXPECTED_CPS = [
    ("org.tgcv", "org.eclipse.viatra.examples.cps.model", "2.1.0-SNAPSHOT"),
    ("org.tgcv", "org.eclipse.viatra.examples.cps.deployment", "2.1.0-SNAPSHOT"),
    ("org.tgcv", "org.eclipse.viatra.examples.cps.traceability", "2.1.0-SNAPSHOT"),
]
EXPECTED_OBSERVER = ("org.tgcv", "org.tgcv.viatra.v002.observer", "0.1.0-SNAPSHOT")

NS = {"m": "http://maven.apache.org/POM/4.0.0"}
POM_TAG = "{http://maven.apache.org/POM/4.0.0}"

def fail(msg):
    print(f"FAIL: {msg}")
    raise SystemExit(1)

def parse(path):
    try:
        return ET.parse(path).getroot()
    except Exception as exc:
        fail(f"invalid XML in {path}: {exc}")

def child(el, name):
    return el.find(f"m:{name}", NS)

def text(el, name):
    node = child(el, name)
    return None if node is None else (node.text or "").strip()

def direct_children(el, name):
    return el.findall(f"m:{name}", NS)

def gav(path):
    p = parse(path)
    group = text(p, "groupId")
    artifact = text(p, "artifactId")
    version = text(p, "version")
    if group is None or version is None:
        parent = child(p, "parent")
        if parent is None:
            fail(f"{path}: missing groupId/version and no parent")
        rel = text(parent, "relativePath") or "../pom.xml"
        parent_path = (path.parent / rel).resolve()
        if group is None:
            group = gav(parent_path)[0]
        if version is None:
            version = gav(parent_path)[2]
    if artifact is None:
        fail(f"{path}: missing artifactId")
    return (group, artifact, version)

def parent_gav(path):
    p = parse(path)
    parent = child(p, "parent")
    if parent is None:
        return None
    return (text(parent, "groupId"), text(parent, "artifactId"), text(parent, "version"))

def modules(path):
    p = parse(path)
    ms = child(p, "modules")
    return [] if ms is None else [(x.text or "").strip() for x in direct_children(ms, "module")]

def plugin_configs(path):
    p = parse(path)
    build = child(p, "build")
    if build is None:
        return []
    plugins = child(build, "plugins")
    if plugins is None:
        return []
    result = []
    for plugin in direct_children(plugins, "plugin"):
        result.append(plugin)
    return result

def target_artifacts(path):
    p = parse(path)
    parent = child(p, "parent")
    parent_version = text(parent, "version") if parent is not None else None
    out = []
    for plugin in plugin_configs(path):
        if text(plugin, "groupId") == "org.eclipse.tycho" and text(plugin, "artifactId") == "target-platform-configuration":
            cfg = child(plugin, "configuration")
            target = child(cfg, "target") if cfg is not None else None
            if target is None:
                fail(f"{path}: target-platform-configuration has no <target>")
            for artifact in direct_children(target, "artifact"):
                version = text(artifact, "version")
                if version == "${parent.version}":
                    if parent_version is None:
                        fail(f"{path}: ${parent.version} used but parent version is unavailable")
                    version = parent_version
                elif version == "${project.version}":
                    fail(f"{path}: ${project.version} is forbidden for target artifact version")
                out.append((text(artifact, "groupId"), text(artifact, "artifactId"), version))
    return out

def plugin_present(path, group, artifact):
    return any(
        text(p, "groupId") == group and text(p, "artifactId") == artifact
        for p in plugin_configs(path)
    )

def assert_eq(name, actual, expected):
    if actual != expected:
        fail(f"{name}: actual={actual!r} expected={expected!r}")

root_pom = root / "pom.xml"
target_pom = root / "target-definition" / "pom.xml"
cps_pom = root / "cps-models" / "pom.xml"
observer_pom = root / "observer" / "pom.xml"

print(f"ROOT_GAV={':'.join(gav(root_pom))}")
print(f"TARGET_GAV={':'.join(gav(target_pom))}")
print(f"CPS_AGG_GAV={':'.join(gav(cps_pom))}")
print(f"OBSERVER_GAV={':'.join(gav(observer_pom))}")

assert_eq("root GAV", gav(root_pom), EXPECTED_ROOT)
assert_eq("target GAV", gav(target_pom), EXPECTED_TARGET)
assert_eq("cps aggregator GAV", gav(cps_pom), EXPECTED_CPS_AGG)
assert_eq("observer GAV", gav(observer_pom), EXPECTED_OBSERVER)

assert_eq("root modules", modules(root_pom), ["target-definition", "cps-models", "observer"])
assert_eq(
    "cps modules",
    modules(cps_pom),
    [
        "org.eclipse.viatra.examples.cps.model",
        "org.eclipse.viatra.examples.cps.deployment",
        "org.eclipse.viatra.examples.cps.traceability",
    ],
)

assert_eq("target parent", parent_gav(target_pom), EXPECTED_ROOT)
assert_eq("cps parent", parent_gav(cps_pom), EXPECTED_ROOT)
assert_eq("observer parent", parent_gav(observer_pom), EXPECTED_ROOT)

def assert_default_or_explicit_parent_path(path, expected):
    p = parse(path)
    parent = child(p, "parent")
    actual = text(parent, "relativePath") if parent is not None else None
    if actual not in (None, expected):
        fail(f"{path}: parent relativePath actual={actual!r} expected absent(default) or {expected!r}")

assert_default_or_explicit_parent_path(target_pom, "../pom.xml")
assert_default_or_explicit_parent_path(cps_pom, "../pom.xml")
assert_default_or_explicit_parent_path(observer_pom, "../pom.xml")

if not plugin_present(root_pom, "org.eclipse.tycho", "tycho-maven-plugin"):
    fail("root Tycho extension is missing")
if not plugin_present(cps_pom, "org.eclipse.tycho", "target-platform-configuration"):
    fail("cps-models target-platform-configuration is missing")
if not plugin_present(observer_pom, "org.eclipse.tycho", "target-platform-configuration"):
    fail("observer target-platform-configuration is missing")
if plugin_present(target_pom, "org.eclipse.tycho", "target-platform-configuration"):
    fail("target-definition must not consume its own target-platform artifact")
if plugin_present(root_pom, "org.eclipse.tycho", "target-platform-configuration"):
    fail("root must not consume target-platform artifact")

assert_eq("cps target artifact", target_artifacts(cps_pom), [EXPECTED_TARGET])
assert_eq("observer target artifact", target_artifacts(observer_pom), [EXPECTED_TARGET])
assert_eq("target artifact count", len(target_artifacts(target_pom)), 0)

target_file = root / "target-definition" / f"{EXPECTED_TARGET[1]}.target"
if not target_file.is_file():
    fail("target filename does not equal target artifactId")
target_files = list((root / "target-definition").glob("*.target"))
assert_eq("target file count", len(target_files), 1)

for gav_expected in EXPECTED_CPS:
    bundle = gav_expected[1]
    pom = root / "cps-models" / bundle / "pom.xml"
    manifest = root / "cps-models" / bundle / "META-INF" / "MANIFEST.MF"
    assert_eq(f"{bundle} GAV", gav(pom), gav_expected)
    assert_eq(f"{bundle} parent", parent_gav(pom), EXPECTED_CPS_AGG)
    if modules(cps_pom).count(bundle) != 1:
        fail(f"{bundle} must occur exactly once in CPS module list")
    if not manifest.is_file():
        fail(f"{bundle} manifest is missing")
    manifest_text = manifest.read_text(encoding="utf-8")
    required = [
        f"Bundle-SymbolicName: {bundle};singleton:=true",
        "Bundle-Version: 2.1.0.qualifier",
        "Bundle-RequiredExecutionEnvironment: JavaSE-1.8",
    ]
    for item in required:
        if item not in manifest_text:
            fail(f"{bundle} manifest missing: {item}")

# Observer packaging identity.
observer_manifest = (root / "observer" / "META-INF" / "MANIFEST.MF").read_text(encoding="utf-8")
required_observer = [
    "Bundle-SymbolicName: org.tgcv.viatra.v002.observer;singleton:=true",
    "Bundle-Version: 0.1.0.qualifier",
    "Bundle-RequiredExecutionEnvironment: JavaSE-1.8",
    "org.eclipse.emf.common",
    "org.eclipse.emf.ecore",
    "org.eclipse.emf.ecore.xmi",
    'org.eclipse.viatra.examples.cps.model;bundle-version="0.1.0"',
    'org.eclipse.viatra.examples.cps.deployment;bundle-version="0.1.0"',
    'org.eclipse.viatra.examples.cps.traceability;bundle-version="0.1.0"',
]
for item in required_observer:
    if item not in observer_manifest:
        fail(f"observer manifest missing: {item}")

trace_manifest = (root / "cps-models" / "org.eclipse.viatra.examples.cps.traceability" / "META-INF" / "MANIFEST.MF").read_text(encoding="utf-8")
for item in [
    'org.eclipse.viatra.examples.cps.model;bundle-version="0.1.0";visibility:=reexport',
    'org.eclipse.viatra.examples.cps.deployment;bundle-version="0.1.0";visibility:=reexport',
    "org.eclipse.emf.ecore;visibility:=reexport",
]:
    if item not in trace_manifest:
        fail(f"traceability manifest missing: {item}")

for bundle in ["org.eclipse.viatra.examples.cps.model", "org.eclipse.viatra.examples.cps.deployment"]:
    manifest = (root / "cps-models" / bundle / "META-INF" / "MANIFEST.MF").read_text(encoding="utf-8")
    for item in ["org.eclipse.core.runtime", "org.eclipse.emf.ecore;visibility:=reexport"]:
        if item not in manifest:
            fail(f"{bundle} manifest missing: {item}")

actual_sha = hashlib.sha1(
    b"blob " + str(target_file.stat().st_size).encode() + b"\0" + target_file.read_bytes()
).hexdigest()
assert_eq("target Git blob SHA", actual_sha, "7481dee30f1ae07d7dd9212d7891dc336f1e96ae")

print("STATIC_XML_REACTOR_AUDIT=PASS")
PY

echo "== Scientific/build firewall =="
if grep -R -nE 'mvn[[:space:]]|mvnw|java[[:space:]]|tycho' . --exclude='build-readiness-preflight.sh' --exclude='*.md' >/dev/null; then
  echo "INFO: build/runtime tokens exist in repository content; this is not itself a failure."
fi

echo "BUILD_READINESS_PREFLIGHT=PASS"
