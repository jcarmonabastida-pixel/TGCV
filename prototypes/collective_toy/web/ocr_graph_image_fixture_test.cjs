"use strict";
const assert = require("node:assert/strict");
const crypto = require("node:crypto");
const fs = require("node:fs");
const path = require("node:path");

const root = path.join(__dirname, "fixtures", "ocr_graph_images");
const manifest = JSON.parse(fs.readFileSync(path.join(root, "synthetic_graph_image_annotations_v0.1.json"), "utf8"));
assert.equal(manifest.dataset_id, "TGCV-OCR-SYNTHETIC-STRUCTURE-001");
assert.equal(manifest.status, "synthetic-development-fixtures-only");
assert.deepEqual(manifest.image_dimensions_px, [320, 180]);
assert.equal(manifest.images.length, 3);
const ids = new Set();

for (const image of manifest.images) {
  assert.equal(image.source_kind, "synthetic", image.image_id);
  assert.equal(image.split, "development", image.image_id);
  assert.equal(image.annotation_status.adjudicated, false, image.image_id);
  assert.ok(!ids.has(image.image_id), "duplicate image_id: " + image.image_id);
  ids.add(image.image_id);

  const imagePath = path.join(root, image.file);
  const bytes = fs.readFileSync(imagePath);
  const digest = crypto.createHash("sha256").update(bytes).digest("hex");
  assert.equal(digest, image.sha256, "SHA-256 mismatch: " + image.image_id);
  assert.equal(bytes.subarray(0, 8).toString("hex"), "89504e470d0a1a0a", "not a PNG: " + image.image_id);
  assert.equal(bytes.readUInt32BE(16), 320, "width mismatch: " + image.image_id);
  assert.equal(bytes.readUInt32BE(20), 180, "height mismatch: " + image.image_id);

  const nodeIds = new Set();
  for (const node of image.nodes) {
    assert.ok(node.id && !nodeIds.has(node.id), "missing/duplicate node id: " + image.image_id);
    nodeIds.add(node.id);
    assert.equal(node.center.length, 2);
    assert.equal(node.bbox.length, 4);
    const [x1, y1, x2, y2] = node.bbox;
    assert.ok(x1 >= 0 && y1 >= 0 && x2 <= 320 && y2 <= 180 && x1 < x2 && y1 < y2, "invalid bbox: " + image.image_id + "/" + node.id);
  }
  const edgeIds = new Set();
  for (const edge of image.edges) {
    assert.ok(edge.id && !edgeIds.has(edge.id), "missing/duplicate edge id: " + image.image_id);
    edgeIds.add(edge.id);
    assert.ok(nodeIds.has(edge.source_node_id), "unknown source node: " + image.image_id + "/" + edge.id);
    assert.ok(nodeIds.has(edge.target_node_id), "unknown target node: " + image.image_id + "/" + edge.id);
    assert.equal(edge.direction, "directed");
    assert.ok(Array.isArray(edge.polyline) && edge.polyline.length >= 2, "missing edge geometry: " + image.image_id + "/" + edge.id);
    for (const point of edge.polyline) {
      assert.equal(point.length, 2);
      assert.ok(point[0] >= 0 && point[0] <= 320 && point[1] >= 0 && point[1] <= 180, "edge point outside image: " + image.image_id + "/" + edge.id);
    }
  }
}
const crossing = manifest.images.find(x => x.image_id === "SYN-CROSSING-001");
assert.ok(crossing);
assert.equal(crossing.nodes.length, 4, "crossing must not create a phantom node");
assert.equal(crossing.edges.length, 2);
const branch = manifest.images.find(x => x.image_id === "SYN-BRANCH-001");
assert.equal(branch.nodes.length, 4);
assert.equal(branch.edges.length, 4);
process.stdout.write("PASS: " + manifest.images.length + " synthetic raster fixtures; PNG dimensions, SHA-256, geometry and graph-reference integrity verified. No OCR accuracy claim.\n");
