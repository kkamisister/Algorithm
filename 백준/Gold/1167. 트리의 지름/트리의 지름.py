import sys
sys.setrecursionlimit(10**6)

# input = open('input.txt').readline
input = sys.stdin.readline

V = int(input()) # 노드 개수
graph = {}

for _ in range(V): # graph input 받기
    data = list(map(int, input().split()))
    node = data[0]

    if node not in graph: # 노드 없으면 빈 리스트 생성
        graph[node] = []

    index = 1
    while index < len(data) - 1:
        neighbor = data[index]
        weight = data[index + 1]

        if neighbor not in graph:
            graph[neighbor] = []

        graph[node].append((neighbor, weight))
        graph[neighbor].append((node, weight)) # 양방향 그래프

        index += 2

def dfs(node, distance):
    global max_distance, farthest_node
    if distance > max_distance:
        max_distance = distance
        farthest_node = node

    for neighbor, weight in graph[node]:
        if not visited[neighbor]:
            visited[neighbor] = True
            dfs(neighbor, distance + weight)

# 1. 시작 노드부터 가장 먼 노드까지의 거리
max_distance = 0
farthest_node = 0
visited = {key: False for key in graph}
visited[1] = True
dfs(1, 0)

# 2. 가장 먼 노드부터 가장 먼 노드까지ㅡ이 거리
max_distance = 0
visited = {key: False for key in graph}
visited[farthest_node] = True
dfs(farthest_node, 0)

print(max_distance)