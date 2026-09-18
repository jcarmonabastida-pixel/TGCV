#!/usr/bin/env python3
import hashlib, json, random

N=100
SEED=582031
BASE=[
("o01",0,1,6),("o02",0,2,8),("o13",1,3,5),
("o23",2,3,2),("o24",2,4,5),("o35",3,5,7),("o45",4,5,2)
]
TREAT=("o14",1,4,1)

def sha(obj):
    return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(",",":")).encode()).hexdigest()

def trajectory(edges):
    adj={i:[] for i in range(6)}
    for e in sorted(edges,key=lambda x:x[0]):
        adj[e[1]].append(e)
    q=[0]; prev={0:None}
    while q:
        u=q.pop(0)
        if u==5: break
        for e in adj[u]:
            v=e[2]
            if v not in prev:
                prev[v]=(u,e); q.append(v)
    if 5 not in prev: raise RuntimeError("NO_TRAJECTORY")
    out=[]; cur=5
    while cur!=0:
        u,e=prev[cur]; out.append(e); cur=u
    return list(reversed(out))

def run_fixture(fid,treated):
    edges=list(BASE)+([TREAT] if treated else [])
    tr=trajectory(edges); outcome=sum(e[3] for e in tr)
    return {"fixture":fid,"treated":treated,"t_acc_size":len(edges),
            "trajectory":[e[0] for e in tr],"O":outcome,"V_star":-outcome}

def main():
    rng=random.Random(SEED); rows=[]
    for fid in range(1,N+1):
        rows.append(run_fixture(fid,rng.random()<0.5))
    counts={"treated":sum(r["treated"] for r in rows),
            "control":sum(not r["treated"] for r in rows)}
    print(json.dumps({"N":N,"seed":SEED,"counts":counts,
      "rows":rows,"dataset_sha256":sha(rows)},sort_keys=True,indent=2))
if __name__=="__main__": main()
