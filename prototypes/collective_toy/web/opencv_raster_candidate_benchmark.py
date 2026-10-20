#!/usr/bin/env python3
"""Diagnostic OpenCV raster candidate benchmark; synthetic fixtures only.

This is a visual candidate generator, not an accepted detector. It detects circular
node candidates and tests straight-line pixel support between candidate centres.
Edge direction is deliberately left unresolved. Annotation data is used only for
scoring, never by the detector.
"""
from __future__ import annotations

import hashlib
import itertools
import json
import time
from pathlib import Path

import cv2
import numpy as np

ROOT = Path(__file__).resolve().parent
FIXTURE_ROOT = ROOT / "fixtures" / "ocr_graph_images"
MANIFEST_PATH = FIXTURE_ROOT / "synthetic_graph_image_annotations_v0.1.json"
REPORT_PATH = ROOT / "opencv-raster-candidate-report.json"
NODE_MATCH_TOLERANCE_PX = 12.0
EDGE_SUPPORT_THRESHOLD = 0.28
DARK_THRESHOLD = 185


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def detect_node_candidates(gray: np.ndarray) -> list[tuple[float, float, float]]:
    blurred = cv2.GaussianBlur(gray, (5, 5), 1.1)
    circles = cv2.HoughCircles(
        blurred,
        cv2.HOUGH_GRADIENT,
        dp=1.0,
        minDist=25,
        param1=100,
        param2=22,
        minRadius=10,
        maxRadius=20,
    )
    if circles is None:
        return []
    found = [(float(x), float(y), float(r)) for x, y, r in circles[0]]
    # Stable ordering for reproducible output; this does not use reference annotations.
    return sorted(found, key=lambda item: (round(item[1], 3), round(item[0], 3)))


def line_support(gray: np.ndarray, a: tuple[float, float], b: tuple[float, float]) -> float:
    x1, y1 = a
    x2, y2 = b
    length = float(np.hypot(x2 - x1, y2 - y1))
    if length < 42:
        return 0.0
    samples = max(12, int(length / 2.0))
    hits = 0
    total = 0
    height, width = gray.shape
    # Exclude node interiors/contours; inspect only the corridor between the nodes.
    for t in np.linspace(0.20, 0.80, samples):
        x = int(round(x1 + (x2 - x1) * t))
        y = int(round(y1 + (y2 - y1) * t))
        x0, x1p = max(0, x - 2), min(width, x + 3)
        y0, y1p = max(0, y - 2), min(height, y + 3)
        if x0 >= x1p or y0 >= y1p:
            continue
        total += 1
        if int(np.min(gray[y0:y1p, x0:x1p])) < DARK_THRESHOLD:
            hits += 1
    return hits / total if total else 0.0


def endpoint_arrowhead_score(gray: np.ndarray, endpoint, other) -> tuple[float, list[int]]:
    """Estimate whether a triangular arrowhead is present at one node boundary.

    Measure dark-pixel width across the edge corridor at increasing distances
    outward from the node. A triangular head should widen behind its tip and
    then return to the thin shaft. This is only a candidate signal; the result
    is never auto-accepted.
    """
    dx, dy = other[0] - endpoint[0], other[1] - endpoint[1]
    length = float(np.hypot(dx, dy))
    if length == 0:
        return 0.0, []
    ux, uy = dx / length, dy / length
    px, py = -uy, ux
    widths = []
    height, width = gray.shape
    for distance in (1, 3, 5, 7, 9, 11, 13):
        cx = endpoint[0] + ux * (endpoint[2] + distance)
        cy = endpoint[1] + uy * (endpoint[2] + distance)
        count = 0
        for offset in range(-8, 9):
            x = int(round(cx + px * offset))
            y = int(round(cy + py * offset))
            # A 3x3 neighbourhood tolerates rasterisation and sub-pixel line offsets.
            x0, x1 = max(0, x - 1), min(width, x + 2)
            y0, y1 = max(0, y - 1), min(height, y + 2)
            if x0 < x1 and y0 < y1 and int(np.min(gray[y0:y1, x0:x1])) < DARK_THRESHOLD:
                count += 1
        widths.append(count)
    base_width = max(widths[1:4])
    shaft_width = float(np.median(widths[4:]))
    return max(0.0, base_width - shaft_width), widths


def propose_edge_direction(gray: np.ndarray, left, right) -> dict:
    left_score, left_profile = endpoint_arrowhead_score(gray, left, right)
    right_score, right_profile = endpoint_arrowhead_score(gray, right, left)
    delta = right_score - left_score
    # A proposal is emitted only when the endpoint profiles separate clearly.
    if delta >= 1.5:
        direction = "left-to-right"
        status = "candidate-needs-human-review"
    elif delta <= -1.5:
        direction = "right-to-left"
        status = "candidate-needs-human-review"
    else:
        direction = "unknown"
        status = "needs-human-review"
    return {
        "direction": direction,
        "status": status,
        "arrowhead_score_at_left_endpoint": round(left_score, 3),
        "arrowhead_score_at_right_endpoint": round(right_score, 3),
        "score_delta_right_minus_left": round(delta, 3),
        "left_endpoint_width_profile": left_profile,
        "right_endpoint_width_profile": right_profile,
    }


def match_nodes(candidates, reference_nodes):
    pairs = []
    for ci, candidate in enumerate(candidates):
        for ref in reference_nodes:
            distance = float(np.hypot(candidate[0] - ref["center"][0], candidate[1] - ref["center"][1]))
            if distance <= NODE_MATCH_TOLERANCE_PX:
                pairs.append((distance, ci, ref["id"]))
    pairs.sort()
    used_candidates, used_refs, mapping = set(), set(), {}
    for distance, ci, ref_id in pairs:
        if ci in used_candidates or ref_id in used_refs:
            continue
        used_candidates.add(ci)
        used_refs.add(ref_id)
        mapping[ci] = ref_id
    return mapping, used_candidates, used_refs


def score_edges(reference_edges, candidate_pairs):
    reference = {
        tuple(sorted((edge["source_node_id"], edge["target_node_id"])))
        for edge in reference_edges
    }
    candidate = set(candidate_pairs)
    tp = len(reference & candidate)
    fp = len(candidate - reference)
    fn = len(reference - candidate)
    precision = tp / (tp + fp) if tp + fp else (1.0 if fn == 0 else 0.0)
    recall = tp / (tp + fn) if tp + fn else (1.0 if fp == 0 else 0.0)
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
    return {"tp": tp, "fp": fp, "fn": fn, "precision": precision, "recall": recall, "f1": f1,
            "exact_undirected_topology_match": fp == 0 and fn == 0}


def main():
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    cases = []
    started_all = time.perf_counter()

    for item in manifest["images"]:
        image_path = FIXTURE_ROOT / item["file"]
        image_hash = sha256_file(image_path)
        if image_hash != item["sha256"]:
            raise RuntimeError(f"Fixture hash mismatch for {item['image_id']}: {image_hash}")
        image = cv2.imread(str(image_path), cv2.IMREAD_GRAYSCALE)
        if image is None:
            raise RuntimeError(f"OpenCV could not read fixture: {image_path}")
        if [int(image.shape[1]), int(image.shape[0])] != manifest["image_dimensions_px"]:
            raise RuntimeError(f"Unexpected dimensions for {item['image_id']}")

        started = time.perf_counter()
        node_candidates = detect_node_candidates(image)
        mapping, matched_candidates, matched_refs = match_nodes(node_candidates, item["nodes"])
        candidate_edges = []
        blocked_by_intermediate_node = 0
        for left, right in itertools.combinations(range(len(node_candidates)), 2):
            a = node_candidates[left]
            b = node_candidates[right]
            # Do not collapse a multi-edge path through an intermediate detected node
            # into a spurious long edge (e.g. A—B—C must not also imply A—C).
            intermediate = False
            dx, dy = b[0] - a[0], b[1] - a[1]
            denom = dx * dx + dy * dy
            for other_index, other in enumerate(node_candidates):
                if other_index in (left, right) or denom == 0:
                    continue
                t = ((other[0] - a[0]) * dx + (other[1] - a[1]) * dy) / denom
                if 0.15 < t < 0.85:
                    px, py = a[0] + t * dx, a[1] + t * dy
                    distance = float(np.hypot(other[0] - px, other[1] - py))
                    if distance <= other[2] + 5.0:
                        intermediate = True
                        break
            if intermediate:
                blocked_by_intermediate_node += 1
                continue
            support = line_support(image, a[:2], b[:2])
            if support >= EDGE_SUPPORT_THRESHOLD:
                direction_proposal = propose_edge_direction(image, a, b)
                candidate_edges.append({
                    "source_candidate": left,
                    "target_candidate": right,
                    "support": round(support, 4),
                    "direction": direction_proposal["direction"],
                    "status": direction_proposal["status"],
                    "arrowhead_profile": direction_proposal,
                })
        mapped_pairs = [
            tuple(sorted((mapping[e["source_candidate"]], mapping[e["target_candidate"]])))
            for e in candidate_edges
            if e["source_candidate"] in mapping and e["target_candidate"] in mapping
        ]
        edge_score = score_edges(item["edges"], mapped_pairs)
        reference_directed_pairs = {
            (edge["source_node_id"], edge["target_node_id"])
            for edge in item["edges"] if edge["direction"] == "directed"
        }
        direction_correct = 0
        direction_wrong = 0
        direction_unresolved = 0
        for edge in candidate_edges:
            left, right = edge["source_candidate"], edge["target_candidate"]
            if left not in mapping or right not in mapping:
                direction_unresolved += 1
                continue
            if edge["direction"] == "unknown":
                direction_unresolved += 1
                continue
            if edge["direction"] == "left-to-right":
                proposed = (mapping[left], mapping[right])
            else:
                proposed = (mapping[right], mapping[left])
            if proposed in reference_directed_pairs:
                direction_correct += 1
            else:
                direction_wrong += 1
        node_tp = len(matched_candidates)
        node_fp = len(node_candidates) - node_tp
        node_fn = len(item["nodes"]) - len(matched_refs)
        node_precision = node_tp / (node_tp + node_fp) if node_tp + node_fp else (1.0 if node_fn == 0 else 0.0)
        node_recall = node_tp / (node_tp + node_fn) if node_tp + node_fn else (1.0 if node_fp == 0 else 0.0)
        node_f1 = 2 * node_precision * node_recall / (node_precision + node_recall) if node_precision + node_recall else 0.0
        cases.append({
            "image_id": item["image_id"],
            "source_kind": item["source_kind"],
            "annotation_status": item["annotation_status"],
            "image_sha256": image_hash,
            "image_dimensions_px": [int(image.shape[1]), int(image.shape[0])],
            "runtime_ms": round((time.perf_counter() - started) * 1000, 3),
            "node_detection": {
                "reference_count": len(item["nodes"]),
                "candidate_count": len(node_candidates),
                "matched": node_tp,
                "false_positive": node_fp,
                "false_negative": node_fn,
                "precision": round(node_precision, 4),
                "recall": round(node_recall, 4),
                "f1": round(node_f1, 4),
                "candidate_centres_px": [[round(x, 2), round(y, 2)] for x, y, _r in node_candidates],
            },
            "edge_topology_undirected": edge_score,
            "edge_candidates": candidate_edges,
            "candidate_pairs_blocked_by_intermediate_node": blocked_by_intermediate_node,
            "direction": {
                "reference_directed_edges": sum(1 for e in item["edges"] if e["direction"] == "directed"),
                "candidate_directions_proposed_correct": direction_correct,
                "candidate_directions_proposed_wrong": direction_wrong,
                "candidate_directions_unresolved": direction_unresolved,
                "directional_exact_match": direction_correct == len(item["edges"]) and direction_wrong == 0 and direction_unresolved == 0,
                "policy": "arrowhead-profile direction proposals remain unaccepted until human review",
            },
            "candidate_node_to_reference_mapping_for_scoring_only": {
                str(k): v for k, v in sorted(mapping.items())
            },
        })

    report = {
        "report_schema": "tgcv-opencv-raster-candidate-report/0.1",
        "status": "diagnostic-not-accepted",
        "dataset_id": manifest["dataset_id"],
        "dataset_version": manifest["dataset_version"],
        "dataset_scope": "synthetic-development-only; annotations are not adjudicated",
        "detector": {
            "library": "opencv-python-headless",
            "version": cv2.__version__,
            "node_method": "HoughCircles on blurred grayscale",
            "edge_method": "straight-corridor dark-pixel support between candidate node centres",
            "direction_method": "candidate arrowhead profile: cross-section width expands behind a triangular tip; all proposals require human review",
            "node_match_tolerance_px": NODE_MATCH_TOLERANCE_PX,
            "edge_support_threshold": EDGE_SUPPORT_THRESHOLD,
            "dark_threshold": DARK_THRESHOLD,
        },
        "aggregate": {
            "images": len(cases),
            "node_tp": sum(c["node_detection"]["matched"] for c in cases),
            "node_fp": sum(c["node_detection"]["false_positive"] for c in cases),
            "node_fn": sum(c["node_detection"]["false_negative"] for c in cases),
            "edge_tp": sum(c["edge_topology_undirected"]["tp"] for c in cases),
            "edge_fp": sum(c["edge_topology_undirected"]["fp"] for c in cases),
            "edge_fn": sum(c["edge_topology_undirected"]["fn"] for c in cases),
            "images_with_exact_undirected_topology": sum(c["edge_topology_undirected"]["exact_undirected_topology_match"] for c in cases),
            "undirected_topology_fixture_gate_pass": all(c["edge_topology_undirected"]["exact_undirected_topology_match"] for c in cases),
            "images_with_direction_fully_resolved": sum(c["direction"]["directional_exact_match"] for c in cases),
            "direction_proposals_correct": sum(c["direction"]["candidate_directions_proposed_correct"] for c in cases),
            "direction_proposals_wrong": sum(c["direction"]["candidate_directions_proposed_wrong"] for c in cases),
            "direction_proposals_unresolved": sum(c["direction"]["candidate_directions_unresolved"] for c in cases),
            "runtime_ms_total": round((time.perf_counter() - started_all) * 1000, 3),
        },
        "cases": cases,
        "interpretation": [
            "Synthetic development fixtures only; no real-image generalization claim.",
            "Undirected edge scoring isolates topology from arrow direction.",
            "Direction is intentionally unresolved; this report cannot pass the directed-structure acceptance gate.",
            "This candidate is not integrated into the application and must not replace the current import path.",
        ],
    }
    REPORT_PATH.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": report["status"], "report": str(REPORT_PATH), "aggregate": report["aggregate"]}, indent=2))
    if not report["aggregate"]["undirected_topology_fixture_gate_pass"]:
        raise SystemExit("FAIL: candidate did not recover exact undirected topology on every synthetic fixture; see the uploaded per-image report.")


if __name__ == "__main__":
    main()
