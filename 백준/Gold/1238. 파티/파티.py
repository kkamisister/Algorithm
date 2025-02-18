import heapq
import sys

INF = int(1e9)

def dijkstra(start, n, graph):
    dist = [INF] * (n + 1)
    dist[start] = 0
    pq = [(0, start)]
    
    while pq:
        d, node = heapq.heappop(pq)
        
        if dist[node] < d:
            continue
        
        for next_node, weight in graph[node]:
            cost = d + weight
            if cost < dist[next_node]:
                dist[next_node] = cost
                heapq.heappush(pq, (cost, next_node))
    
    return dist

n, m, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
rev_graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))
    rev_graph[b].append((a, t))

# X에서 다른 노드로 가는 최단 거리 구하기
dist_from_x = dijkstra(x, n, graph)

# 다른 노드에서 X로 가는 최단 거리 구하기
dist_to_x = dijkstra(x, n, rev_graph)

# 결과 계산: X에서 다른 노드까지 + 다른 노드에서 X까지
max_dist = 0
for i in range(1, n + 1):
    max_dist = max(max_dist, dist_from_x[i] + dist_to_x[i])

print(max_dist)
