from collections import deque

def bfs(start, visited, graph):
    queue = deque([start])
    visited[start] = 1
    count = 1
    
    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = 1
                queue.append(neighbor)
                count += 1
        
    return count

def solution(n, wires):
    min_diff = n
    for i in range(len(wires)):
        graph = [[] for _ in range(n+1)]
        for j in range(len(wires)):
            if i == j:
                continue
            a, b = wires[j]
            graph[a].append(b)
            graph[b].append(a)
            
        visited = [0]*(n+1)
        count = bfs(1, visited, graph)
        diff = abs(n-2*count)
        min_diff = min(diff, min_diff)
        
    return min_diff