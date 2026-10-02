from omega_u_constructor_v01 import build_u_t

VERSIONS = [
    {"id": 1, "package_id": 10, "version_str": "1.0.0", "created_at": "2022-08-01T00:00:00Z"},
    {"id": 2, "package_id": 20, "version_str": "1.0.0", "created_at": "2022-08-02T00:00:00Z"},
    {"id": 3, "package_id": 20, "version_str": "2.0.0", "created_at": "2022-08-03T00:00:00Z"},
    {"id": 4, "package_id": 30, "version_str": "1.0.0", "created_at": "2022-09-02T00:00:00Z"},
]
DEPS = [{"depending_version": 1, "depending_on_package": 20, "semver_str": "^1.0.0"},
        {"depending_version": 1, "depending_on_package": 20, "semver_str": "^1.0.0"}]

def run(deps=DEPS):
    return build_u_t(VERSIONS, deps, cutoff="2022-09-01T00:00:00Z")

def test_valid_adjacent_construction_and_duplicate_collapse():
    result=run(); assert result["u_count"]==1
    assert [r["tau"] for r in result["U_t"]]==[[1,20,2]]
    assert result["coverage_counts"]["OBSERVED_PRESENT"]==1

def test_out_of_scope_target_is_not_emitted():
    result=run([{"depending_version":1,"depending_on_package":30,"semver_str":"*"}])
    assert result["u_count"]==0
    assert result["coverage_counts"]["UNKNOWN_MISSING"]==1

def test_missing_origin_fails_closed():
    result=run([{"depending_version":999,"depending_on_package":20,"semver_str":"*"}])
    assert result["u_count"]==0
    assert result["coverage_counts"]["OUT_OF_SCOPE"]==1

def test_unknown_identity_input_is_unknown_missing():
    result=run([{"depending_version":None,"depending_on_package":20,"semver_str":"*"}])
    assert result["u_count"]==0
    assert result["unresolved_count"]==1
    assert result["coverage_counts"]["UNKNOWN_MISSING"]==1

def test_unknown_timestamp_fails_closed():
    bad=list(VERSIONS); bad[1]={**bad[1],"created_at":""}
    try: build_u_t(bad,DEPS,cutoff="2022-09-01T00:00:00Z")
    except ValueError: return
    raise AssertionError("missing timestamp was not rejected")

def test_future_target_never_enters_u():
    result=run([{"depending_version":1,"depending_on_package":30,"semver_str":"*"}])
    assert result["u_count"]==0

def test_firewall_fields_cannot_affect_u():
    d1=[{"depending_version":1,"depending_on_package":20,"semver_str":"*","T_acc":999,"Reach":999,"outcome":"bad","value":999}]
    d2=[{"depending_version":1,"depending_on_package":20,"semver_str":"*","T_acc":0,"Reach":0,"outcome":"good","value":0}]
    r1,r2=run(d1),run(d2)
    assert r1["U_t"]==r2["U_t"]; assert r1["output_sha256"]==r2["output_sha256"]

def test_deterministic_under_dependency_row_permutation():
    a,b=run(DEPS),run(list(reversed(DEPS)))
    assert a["U_t"]==b["U_t"]; assert a["output_sha256"]==b["output_sha256"]

def test_provenance_is_retained_for_origin_dependency_target():
    result=run(); p=result["U_t"][0]["provenance"]
    assert p[0]=="package_versions.csv:id:1"
    assert p[1].startswith("package_dependencies.csv:row:")
    assert p[2]=="package_versions.csv:id:2"

def test_schema_error_is_explicit():
    bad=[{"id":1,"package_id":10,"created_at":"2022-08-01T00:00:00Z"}]
    try: build_u_t(bad,DEPS,cutoff="2022-09-01T00:00:00Z")
    except ValueError: return
    raise AssertionError("schema error was not rejected")

def test_constructor_version_and_rule_are_emitted():
    result=run()
    assert result["construction_version"]=="RUST_OMEGA_U_CONSTRUCTOR_v0.4"
    assert result["temporal_rule"]=="DR-035-v0.1-ADJACENT-CREATED-AT"
    assert result["coverage_states"]==["OBSERVED_PRESENT","OBSERVED_ABSENT_COMPLETE","UNKNOWN_MISSING","OUT_OF_SCOPE"]


def test_complete_absence_requires_explicit_certificate():
    deps=[{"depending_version":1,"depending_on_package":30,"semver_str":"*"}]
    result=run(deps)
    assert result["coverage_counts"]["OBSERVED_ABSENT_COMPLETE"]==0
    assert result["coverage_counts"]["UNKNOWN_MISSING"]==1
    certified=build_u_t(VERSIONS, deps, cutoff="2022-09-01T00:00:00Z", complete_target_packages=[30])
    assert certified["coverage_counts"]["OBSERVED_ABSENT_COMPLETE"]==1
    assert certified["coverage_counts"]["UNKNOWN_MISSING"]==0
