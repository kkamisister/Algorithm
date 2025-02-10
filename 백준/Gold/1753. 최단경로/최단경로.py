import sys
import heapq

input = sys.stdin.read
data = input().split()

V = int(data[0])
E = int(data[1])
K = int(data[2])

graph = [[] for _ in range(V + 1)]
dist = [float('inf')] * (V + 1)
dist[K] = 0
pq = [(0, K)]

index = 3
for _ in range(E):
    u, v, w = map(int, data[index:index + 3])
    graph[u].append((w, v))
    index += 3

while pq:
    d, node = heapq.heappop(pq)
    if d > dist[node]:
        continue
    for w, neighbor in graph[node]:
        new_dist = d + w
        if new_dist < dist[neighbor]:
            dist[neighbor] = new_dist
            heapq.heappush(pq, (new_dist, neighbor))

for d in dist[1:]:
    print(d if d != float('inf') else "INF")
