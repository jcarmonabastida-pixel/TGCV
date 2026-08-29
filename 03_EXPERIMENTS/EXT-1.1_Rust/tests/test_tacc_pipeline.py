from src.index_adapter import parse_records
from src.tacc_pipeline import delta_t_acc, index_versions, t_acc_for_record


def rec(vers, deps=None, yanked=False):
    return {"vers": vers, "yanked": yanked, "deps": deps or []}


def dep(name, req, optional=False, kind="normal"):
    return {"name": name, "req": req, "optional": optional, "kind": kind}


def test_pipeline_expands_when_new_satisfying_version_appears():
    target_v1 = rec("1.0.0")
    target_v2 = rec("1.1.0")
    source = rec("1.0.0", [dep("target", "^1.0.0")])
    old = parse_records("target", [target_v1])
    source_record = parse_records("source", [source])[0]
    old_index = index_versions(old)
    new_index = index_versions(old + parse_records("target", [target_v2]))
    assert t_acc_for_record(source_record, old_index) == {("target", "1.0.0")}
    assert t_acc_for_record(source_record, new_index) == {("target", "1.0.0"), ("target", "1.1.0")}


def test_pipeline_preserves_empty_delta_for_irrelevant_state_change():
    source = rec("1.0.0", [dep("target", "1.0.0")])
    target = parse_records("target", [rec("1.0.0")])
    source_record = parse_records("source", [source])[0]
    assert delta_t_acc(
        t_acc_for_record(source_record, index_versions(target)),
        t_acc_for_record(source_record, index_versions(target)),
    ) == {"added": set(), "removed": set()}


def test_pipeline_detects_contraction():
    source = rec("1.0.0", [dep("target", "^1.0.0")])
    source_record = parse_records("source", [source])[0]
    old = parse_records("target", [rec("1.0.0"), rec("1.1.0")])
    new = parse_records("target", [rec("1.0.0")])
    assert delta_t_acc(
        t_acc_for_record(source_record, index_versions(old)),
        t_acc_for_record(source_record, index_versions(new)),
    )["removed"] == {("target", "1.1.0")}
