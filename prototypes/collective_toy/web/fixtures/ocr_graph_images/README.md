# Synthetic visual graph fixtures 001

These PNGs and their independent geometric reference annotations form the first raster-level test scaffold for the TGCV collective-toy OCR import work.

- Dataset manifest: `synthetic_graph_image_annotations_v0.1.json`
- Scope: synthetic development fixtures only.
- Images: linear graph, branching/converging graph, and crossing edges with no node at the crossing.
- Annotation coordinates use the 320×180 image coordinate system.
- The PNG SHA-256 values are recorded in the manifest.
- Annotations are initial single-annotator labels and are **not adjudicated**.
- These fixtures do not establish performance on real-world diagrams and must not be pooled with future validation or locked-test images.

## Next gate

Implement deterministic fixture-integrity and annotation-contract checks first. Then add a visual candidate detector and compare its output with these references. Do not report image-to-graph accuracy until an extraction algorithm has actually run against the images.
