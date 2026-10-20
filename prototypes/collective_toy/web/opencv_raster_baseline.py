#!/usr/bin/env python3
"""OpenCV-only structural baseline for TGCV synthetic raster fixtures.

This is a deliberately simple baseline, not a production parser. It scores node
regions and edge geometry separately; Hough segments do not establish direction.
"""
import argparse, json, math
from pathlib import Path
import cv2
import numpy as np

ROOT = Path(__file__).resolve().parent
FIXTURES = ROOT / "fixtures" / "ocr_graph_images"

def counts(tp, pred, ref):
    fp, fn = pred - tp, ref - tp
    p = tp / pred if pred else (1.0 if ref == 0 else 0.0)
    r = tp / ref if ref else (1.0 if pred == 0 else 0.0)
    return {"tp": tp, "fp": fp, "fn": fn, "precision": p, "recall": r,
            "f1": 2*p*r/(p+r) if p+r else 0.0}

def node_candidates(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    raw = []
    for c in contours:
        x, y, w, h = cv2.boundingRect(c)
        if 18 <= w <= 50 and 18 <= h <= 50 and cv2.contourArea(c) >= 100:
            raw.append({"center": [x+w/2, y+h/2], "bbox": [x,y,x+w-1,y+h-1],
                        "area": float(cv2.contourArea(c))})
    # Keep one representative per spatially overlapping contour family.
    raw.sort(key=lambda n: n["area"], reverse=True)
    kept = []
    for n in raw:
        x1,y1,x2,y2=n["bbox"]
        if any(math.dist(n["center"], k["center"]) < 8 for k in kept):
            continue
        kept.append(n)
    return kept

def merge_collinear_segments(segments, max_gap=18, max_angle_deg=12, max_offset=6):
    """Join nearby, nearly collinear Hough fragments; still geometry-only."""
    merged = [list(map(list, seg)) for seg in segments]
    angle_limit = math.radians(max_angle_deg)

    def angle(seg):
        (x1,y1),(x2,y2)=seg
        return math.atan2(y2-y1,x2-x1) % math.pi

    def angle_delta(a,b):
        d=abs(a-b) % math.pi
        return min(d, math.pi-d)

    def point_line_distance(p, seg):
        (x1,y1),(x2,y2)=seg
        den=math.hypot(x2-x1,y2-y1)
        return abs((y2-y1)*p[0]-(x2-x1)*p[1]+x2*y1-y2*x1)/den if den else math.dist(p,[x1,y1])

    changed=True
    while changed:
        changed=False
        for i in range(len(merged)):
            if changed: break
            for j in range(i+1,len(merged)):
                a,b=merged[i],merged[j]
                if angle_delta(angle(a),angle(b)) > angle_limit: continue
                endpoints=[(math.dist(a[0],b[0]),a[0],b[0]),
                           (math.dist(a[0],b[1]),a[0],b[1]),
                           (math.dist(a[1],b[0]),a[1],b[0]),
                           (math.dist(a[1],b[1]),a[1],b[1])]
                gap,pa,pb=min(endpoints,key=lambda item:item[0])
                if gap > max_gap: continue
                if point_line_distance(pb,a) > max_offset or point_line_distance(pa,b) > max_offset: continue
                points=a+b
                farthest=max(((math.dist(p,q),p,q) for p in points for q in points),key=lambda item:item[0])
                merged[i]=[list(farthest[1]),list(farthest[2])]
                del merged[j]
                changed=True
                break
    return merged

def edge_candidates(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 40, 120)
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=18,
                            minLineLength=28, maxLineGap=8)
    result=[]
    if lines is not None:
        for item in np.asarray(lines).reshape(-1, 4):
            x1,y1,x2,y2=map(int,item)
            if math.hypot(x2-x1,y2-y1) >= 28:
                result.append([[x1,y1],[x2,y2]])
    # Collapse near-identical Hough segments regardless of endpoint order.
    unique=[]
    for line in result:
        a,b=line
        if not any(min(math.dist(a,x)+math.dist(b,y),
                       math.dist(a,y)+math.dist(b,x)) < 14 for x,y in unique):
            unique.append(line)
    return merge_collinear_segments(unique)

def node_score(pred, refs, tolerance=12):
    pairs=[]
    for i,p in enumerate(pred):
        for j,r in enumerate(refs):
            d=math.dist(p["center"], r["center"])
            if d <= tolerance: pairs.append((d,i,j))
    usedp=set(); usedr=set(); tp=0
    for _,i,j in sorted(pairs):
        if i not in usedp and j not in usedr:
            usedp.add(i); usedr.add(j); tp+=1
    return counts(tp,len(pred),len(refs)), sorted(usedr)

def segment_distance_to_polyline(seg, poly):
    # Symmetric endpoint-to-polyline approximation, robust enough for this
    # initial straight-line fixture set; not a general curve-distance metric.
    def point_seg(p,a,b):
        vx,vy=b[0]-a[0],b[1]-a[1]
        den=vx*vx+vy*vy
        t=0 if den==0 else max(0,min(1,((p[0]-a[0])*vx+(p[1]-a[1])*vy)/den))
        return math.dist(p,[a[0]+t*vx,a[1]+t*vy])
    def dpoint(p,line):
        return min(point_seg(p,a,b) for a,b in zip(line,line[1:]))
    a,b=seg
    return (dpoint(a,poly)+dpoint(b,poly))/2

def edge_score(pred, refs, tolerance=14):
    pairs=[]
    for i,p in enumerate(pred):
        for j,r in enumerate(refs):
            d=segment_distance_to_polyline(p,r["polyline"])
            if d <= tolerance: pairs.append((d,i,j))
    usedp=set(); usedr=set(); tp=0
    for _,i,j in sorted(pairs):
        if i not in usedp and j not in usedr:
            usedp.add(i); usedr.add(j); tp+=1
    return counts(tp,len(pred),len(refs))

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--output", default="opencv-raster-baseline-report.json")
    args=ap.parse_args()
    manifest=json.loads((FIXTURES/"synthetic_graph_image_annotations_v0.1.json").read_text())
    report={"method":"OpenCV threshold+contours for node candidates; Canny+HoughLinesP for edge geometry",
            "dataset_id":manifest["dataset_id"],"dataset_version":manifest["dataset_version"],
            "dataset_status":manifest["status"],"direction_metrics":"NOT_MEASURED_BY_THIS_BASELINE",
            "images":[],"limitations":["Synthetic development fixtures only; annotations are single-annotator and not adjudicated.",
            "Hough line segments do not infer edge endpoints or arrow direction.",
            "Node/edge matching tolerances are provisional engineering settings, not validated thresholds."]}
    for item in manifest["images"]:
        path=FIXTURES/item["file"]
        img=cv2.imread(str(path))
        if img is None: raise RuntimeError("Unable to read fixture: "+str(path))
        nodes=node_candidates(img); lines=edge_candidates(img)
        ns,matched=node_score(nodes,item["nodes"])
        es=edge_score(lines,item["edges"])
        report["images"].append({"image_id":item["image_id"],"image_path":item["file"],
            "reference_nodes":len(item["nodes"]),"candidate_nodes":nodes,"node_metrics":ns,
            "reference_edges":len(item["edges"]),"candidate_edge_segments":lines,"edge_geometry_metrics":es,
            "direction_metrics":"NOT_MEASURED","annotation_adjudicated":item["annotation_status"]["adjudicated"]})
    out=Path(args.output)
    out.write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps({"status":"PASS","images":len(report["images"]),"output":str(out),
                      "scope":"OpenCV baseline only; no winner decision; direction not measured"}))
if __name__=="__main__": main()
