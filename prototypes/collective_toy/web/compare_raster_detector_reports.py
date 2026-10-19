#!/usr/bin/env python3
"""Score Canvas edge candidates and OpenCV line segments against shared references."""
import json, math
from pathlib import Path
ROOT=Path(__file__).resolve().parent
FIX=ROOT/"fixtures"/"ocr_graph_images"/"synthetic_graph_image_annotations_v0.1.json"

def metrics(tp,pred,ref):
    fp,fn=pred-tp,ref-tp
    p=tp/pred if pred else (1.0 if ref==0 else 0.0)
    r=tp/ref if ref else (1.0 if pred==0 else 0.0)
    return {"tp":tp,"fp":fp,"fn":fn,"precision":p,"recall":r,"f1":2*p*r/(p+r) if p+r else 0.0}

def point_seg(p,a,b):
    vx,vy=b[0]-a[0],b[1]-a[1]; den=vx*vx+vy*vy
    t=0 if den==0 else max(0,min(1,((p[0]-a[0])*vx+(p[1]-a[1])*vy)/den))
    return math.dist(p,[a[0]+t*vx,a[1]+t*vy])

def point_line(p,line): return min(point_seg(p,a,b) for a,b in zip(line,line[1:]))
def line_distance(seg,poly):
    return (point_line(seg[0],poly)+point_line(seg[1],poly))/2

def match_segments(pred,refs,tol=14):
    pairs=[]
    for i,p in enumerate(pred):
        for j,r in enumerate(refs):
            d=line_distance(p,r["polyline"])
            if d<=tol: pairs.append((d,i,j))
    pi=set(); rj=set(); tp=0
    for _,i,j in sorted(pairs):
        if i not in pi and j not in rj: pi.add(i);rj.add(j);tp+=1
    return metrics(tp,len(pred),len(refs))

def match_nodes(pred,refs,tol=12):
    pairs=[]
    for i,p in enumerate(pred):
        for j,r in enumerate(refs):
            d=math.dist(p,r["center"])
            if d<=tol:pairs.append((d,i,j))
    pi=set();rj=set();tp=0
    for _,i,j in sorted(pairs):
        if i not in pi and j not in rj:pi.add(i);rj.add(j);tp+=1
    return metrics(tp,len(pred),len(refs))

def main():
    manifest=json.loads(FIX.read_text())
    opencv=json.loads((ROOT/"opencv-raster-baseline-report.json").read_text())
    canvas=json.loads((ROOT/"canvas-raster-candidate-report.json").read_text())
    cvmap={x["image_id"]:x for x in opencv["images"]}
    camap={x["image_id"]:x for x in canvas["images"]}
    report={"dataset_id":manifest["dataset_id"],"dataset_version":manifest["dataset_version"],
      "status":"PROVISIONAL_ENGINEERING_COMPARISON_NOT_A_WINNER_DECISION",
      "annotation_adjudicated":all(x["annotation_status"]["adjudicated"] for x in manifest["images"]),
      "matching":{"node_center_tolerance_px":12,"edge_mean_endpoint_to_polyline_tolerance_px":14,
        "note":"Provisional geometry matching only; edge segment scoring is not endpoint-pair/topology scoring."},
      "images":[],"direction":{"reference_edges_with_clear_direction":sum(1 for x in manifest["images"] for e in x["edges"] if e["arrow_status"]=="clear"),
        "canvas_proposed_directions":0,"canvas_unresolved_directions":sum(camap[x["image_id"]]["detector_result"]["direction_diagnostics"]["unresolved_directions"] for x in manifest["images"]),
        "opencv_direction_evaluated":False,"direction_accuracy":"NOT_COMPUTABLE_NO_DIRECTION_PROPOSALS_FROM_EITHER_METHOD"},
      "limitations":["Synthetic development fixtures only; one annotator, not adjudicated.",
        "Geometry-only edge scoring may count partial fragments as matches and does not verify source-target node pairs.",
        "OpenCV baseline has no arrow-direction inference; Canvas direction proposals are all unresolved in this run.",
        "No production integration or real-world accuracy claim."]}
    for item in manifest["images"]:
        ci=camap[item["image_id"]]["detector_result"]; oi=cvmap[item["image_id"]]
        canvas_nodes=[{"center":n["center"]} for n in ci["nodes"]]
        opencv_nodes=[{"center":n["center"]} for n in oi["candidate_nodes"]]
        canvas_edges=[{"polyline":[e["from"],e["to"]]} for e in ci["edge_candidates"]]
        opencv_edges=[{"polyline":seg} for seg in oi["candidate_edge_segments"]]
        report["images"].append({"image_id":item["image_id"],
          "canvas":{"nodes":match_nodes(canvas_nodes,item["nodes"]),"edge_geometry":match_segments(canvas_edges,item["edges"]),
            "edge_candidate_count":len(canvas_edges),"direction_proposed":ci["direction_diagnostics"]["proposed_directions"],
            "direction_unresolved":ci["direction_diagnostics"]["unresolved_directions"]},
          "opencv":{"nodes":match_nodes(opencv_nodes,item["nodes"]),"edge_geometry":match_segments(opencv_edges,item["edges"]),
            "edge_segment_count":len(opencv_edges),"direction_evaluated":False}})
    Path("raster-detector-comparison-report.json").write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps({"status":"PASS","images":len(report["images"]),"output":"raster-detector-comparison-report.json",
      "scope":report["status"],"direction_accuracy":report["direction"]["direction_accuracy"]}))
if __name__=="__main__":main()
