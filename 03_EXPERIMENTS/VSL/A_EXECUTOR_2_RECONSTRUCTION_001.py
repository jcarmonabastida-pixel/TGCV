import hashlib,json,pathlib,collections
N=100
SEED=582031
BASE=[("e01",0,1,4),("e02",0,2,7),("e13",1,3,5),("e23",2,3,2),("e24",2,4,6),("e35",3,5,8),("e45",4,5,3)]
TREAT=("e14",1,4,1)
def adj(es): return {i:[e for e in sorted(es,key=lambda x:x[0]) if e[1]==i] for i in range(6)}
def trajectory(es):
 a=adj(es); q=collections.deque([0]); parent={0:None}
 while q:
  u=q.popleft()
  if u==5: break
  for e in a[u]:
   if e[2] not in parent: parent[e[2]]=(u,e); q.append(e[2])
 if 5 not in parent: raise RuntimeError("NO_TRAJECTORY")
 out=[]; c=5
 while c!=0:
  u,e=parent[c]; out.append(e); c=u
 return list(reversed(out))
def condition(es):
 t=trajectory(es); o=sum(e[3] for e in t)
 return {"t_acc_size":len(es),"trajectory":[e[0] for e in t],"O":o,"V_star":-o}
rows=[]
for fid in range(1,N+1):
 c=condition(list(BASE)); t=condition(list(BASE)+[TREAT])
 rows.append({"fixture":fid,"control":c,"treatment":t,"delta_t_acc":t["t_acc_size"]-c["t_acc_size"],"delta_V_star":t["V_star"]-c["V_star"]})
h=hashlib.sha256(json.dumps(rows,sort_keys=True,separators=(",",":")).encode()).hexdigest()
d={"executor":"EXECUTOR_2","bundle":"A","N":N,"seed":SEED,"rows":rows,"dataset_sha256":h}
p=pathlib.Path("03_EXPERIMENTS/VSL"); p.mkdir(parents=True,exist_ok=True)
(p/"A_EXECUTOR_2_RECONSTRUCTION_001.json").write_text(json.dumps(d,sort_keys=True,indent=2),encoding="utf-8")
print("EXECUTOR_2_A_RECONSTRUCTION_WRITTEN")
print("N="+str(N))
print("dataset_sha256="+h)
