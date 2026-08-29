"""Reference structural pipeline for EXT-1.1.

Input is already parsed historical VersionRecord objects. This module computes
candidate transformations without consulting outcome data.
"""
from collections import defaultdict
from .semver_reference import accessible_versions


def index_versions(records):
    by_package = defaultdict(list)
    for r in records:
        by_package[r.package].append(r.version)
    return {p: sorted(set(vs)) for p, vs in by_package.items()}


def accessible_dependency_targets(record, versions_by_package):
    targets = {}
    for name, req, optional, kind in record.dependencies:
        if optional:
            continue
        versions = versions_by_package.get(name, [])
        targets[name] = accessible_versions(versions, req)
    return targets


def t_acc_for_record(record, versions_by_package):
    """Return auditable dependency-target transformations for one version."""
    targets = accessible_dependency_targets(record, versions_by_package)
    return {
        (name, version)
        for name, versions in targets.items()
        for version in versions
    }


def delta_t_acc(old, new):
    return {"added": new - old, "removed": old - new}
