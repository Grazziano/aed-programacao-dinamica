def shortest_path_dag(graph, start):
    order = topological_sort(graph)
    dist = {v: float('inf') for v in graph}
    dist[start] = 0
    
    for u in order:
        for v in graph[u]:
            if dist[v] > dist[u] + graph[u][v]:
                dist[v] = dist[u] + graph[u][v]
                
    return dist
