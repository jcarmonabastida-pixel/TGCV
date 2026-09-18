#!/usr/bin/env python3
import hashlib,json

N=100
SEED=582031
BASE=[("e01",0,1,4),("e02",0,2,7),("e13",1,3,5),("e23",2,3,2),("e24",2,4,6),("e35",3,5,8),("e45",4,5,3)]
TREAT=("e14",1,4,1)

def sha(obj):
    return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(",",":")).encode()).hexdigest()

def trajectory(edges):
    adj={i:[] for i in range(6)}
    for e in sorted(edges,key=lambda x:x[0]): adj[e[1]].append(e)
    q=[0]; prev={0:None}
    while q:
        u=q.pop(0)
        if u==5: break
        for e in adj[u]:
            v=e[2]
            if v not in prev: prev[v]=(u,e); q.append(v)
    if 5 not in prev: raise RuntimeError("NO_TRAJECTORY")
    out=[]; cur=5
    while cur!=0:
        u,e=prev[cur]; out.append(e); cur=u
    return list(reversed(out))

def condition(edges):
    tr=trajectory(edges)
    o=sum(e[3] for e in tr)
    return {"t_acc_size":len(edges),"trajectory":[e[0] for e in tr],"O":o,"V_star":-o}

def main():
    rows=[]
    for fid in range(1,N+1):
        control=condition(list(BASE))
        treatment=condition(list(BASE)+[TREAT])
        rows.append({"fixture":fid,"control":control,"treatment":treatment,
                     "delta_t_acc":treatment["t_acc_size"]-control["t_acc_size"],
                     "delta_V_star":treatment["V_star"]-control["V_star"]})
    print(json.dumps({"N":N,"seed":SEED,"rows":rows,"dataset_sha256":sha(rows)},sort_keys=True,indent=2))
if __name__=="__main__": main()
