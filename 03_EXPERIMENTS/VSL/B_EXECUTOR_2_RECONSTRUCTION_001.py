import hashlib
import json

N = 100
BASE = [
    ("o01", 0, 1, 6),
    ("o02", 0, 2, 8),
    ("o13", 1, 3, 5),
    ("o23", 2, 3, 2),
    ("o24", 2, 4, 5),
    ("o35", 3, 5, 7),
    ("o45", 4, 5, 2),
]
INTERVENTION = ("o14", 1, 4, 1)

def dataset_hash(rows):
    payload = json.dumps(rows, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()

def bfs(edges):
    adjacency = {node: [] for node in range(6)}
    for edge in sorted(edges, key=lambda x: x[0]):
        adjacency[edge[1]].append(edge)
    queue = [0]
    predecessor = {0: None}
    while queue:
        node = queue.pop(0)
        if node == 5:
            break
        for edge in adjacency[node]:
            nxt = edge[2]
            if nxt not in predecessor:
                predecessor[nxt] = (node, edge)
                queue.append(nxt)
    if 5 not in predecessor:
        raise RuntimeError("NO_TRAJECTORY")
    path = []
    node = 5
    while node != 0:
        previous, edge = predecessor[node]
        path.append(edge)
        node = previous
    return list(reversed(path))

def evaluate(edges):
    path = bfs(edges)
    cost = sum(edge[3] for edge in path)
    return {
        "t_acc_size": len(edges),
        "trajectory": [edge[0] for edge in path],
        "O": cost,
        "V_star": -cost,
    }

def main():
    rows = []
    for fixture in range(1, N + 1):
        control_edges = list(BASE)
        treatment_edges = list(BASE) + [INTERVENTION]
        control = evaluate(control_edges)
        treatment = evaluate(treatment_edges)
        rows.append({
            "fixture": fixture,
            "control": control,
            "treatment": treatment,
            "delta_t_acc": treatment["t_acc_size"] - control["t_acc_size"],
            "delta_V_star": treatment["V_star"] - control["V_star"],
        })
    result = {
        "N": N,
        "rows": rows,
        "dataset_sha256": dataset_hash(rows),
    }
    print(json.dumps(result, sort_keys=True, indent=2))

if __name__ == "__main__":
    main()
