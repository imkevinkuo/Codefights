def graphDistances(g, s):
    dist = [31 for i in range(len(g))]
    Q = set(i for i in range(len(g)))
    dist[s] = 0
    while Q:
        u = min(Q, key=lambda p:dist[p])
        Q.remove(u)
        for v in Q:
            if g[u][v] > -1:
                alt = dist[u] + g[u][v]
                if alt < dist[v]:
                    dist[v] = alt
    return dist
