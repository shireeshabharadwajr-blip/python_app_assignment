from collections import defaultdict

def findEulerPath(n, edges):
    graph = defaultdict(list)
    deg = [0] * n
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
        deg[u] += 1
        deg[v] += 1
        
    odd_nodes = [i for i in range(n) if deg[i] % 2 != 0]
    if len(odd_nodes) not in (0, 2):
        return False, deg, odd_nodes, None, []
        
    start = odd_nodes[0] if odd_nodes else 0
    stack = [start]
    path = []
    local_graph = {u: list(v) for u, v in graph.items()}
    
    while stack:
        u = stack[-1]
        if local_graph.get(u):
            v = local_graph[u].pop()
            local_graph[v].remove(u)
            stack.append(v)
        else:
            path.append(stack.pop())
            
    if len(path) != len(edges) + 1:
        return False, deg, odd_nodes, None, []
    return True, deg, odd_nodes, start, path[::-1]

if __name__ == "__main__":
    exists, deg, odd, start, path = findEulerPath(4, [[0,1],[1,2],[2,0],[1,3]])
    print("Exists:", exists, "| Degrees:", deg, "| Odd:", odd, "| Start:", start, "| Path:", path)
