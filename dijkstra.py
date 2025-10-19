import heapq

def dijkstra(vertices,edges,source):
    adj_list=[[] for _ in range(vertices)]
    for u,v,w in edges:
        adj_list[u].append((v,w))
        adj_list[v].append((u,w))
    distances=[float("inf")]*vertices
    distances[source]=0
    pq=[(0,source)]
    while pq:
        curr_dist,u =heapq.heappop(pq)
        if curr_dist>distances[u]:
            continue
        for v,w in adj_list[u]:
            distance=curr_dist+w
            if distance<distances[v]:
                distances[v]=distance
                heapq.heappush(pq,(distance,v))
    total=sum([dist for dist in distances if dist!=float("inf")])
    return distances,total


vertices = 5
edges = [
    (0, 1, 2),
    (0, 3, 6),
    (1, 2, 3),
    (1, 3, 8),
    (1, 4, 5),
    (2, 4, 7),
    (3, 4, 9)
]

# Find shortest paths from the source vertex (0)
source = 0
shortest_distances, total_cost = dijkstra(vertices, edges, source)

print("Shortest distances from source vertex:", shortest_distances)
print("Total cost of reaching all reachable vertices:", total_cost)
