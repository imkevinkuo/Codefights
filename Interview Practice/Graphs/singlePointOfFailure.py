def singlePointOfFailure(connections):
    parents = {0:None}
    visited = set()
    cycEdges = []
    dfs(0, visited, parents, connections, cycEdges)
    cycles = []
    for edge in cycEdges:
        v = edge[0]
        cycle = [v]
        while v != edge[1]:
            v = parents[v]
            cycle.append(v)
        cycles.append(cycle)
    for cycle in cycles:
        for i in cycle:
            for j in cycle:
                connections[i][j] = 0
    return sum(sum(connections[i]) for i in range(len(connections)))/2

def dfs(v, visited, parents, connections, cycEdges):
    visited.add(v)
    for w in range(len(connections)):
        if connections[v][w] == 1:
            if w not in visited:
                parents[w] = v
                dfs(w, visited, parents, connections, cycEdges)
            elif parents[v] != w:
                if (v,w) not in cycEdges and (w,v) not in cycEdges:
                    cycEdges.append((v,w))
