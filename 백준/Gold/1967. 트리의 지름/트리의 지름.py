import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(node, weight):
    global max_distance, farthest_node
    if weight > max_distance:
        max_distance = weight
        farthest_node = node
    
    for next_node, next_weight in tree[node]:
        if not visited[next_node]:
            visited[next_node] = True
            dfs(next_node, weight + next_weight)
            visited[next_node] = False

# 1. 입력 받기
n = int(input())
tree = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    parent, child, weight = map(int, input().split())
    tree[parent].append((child, weight))
    tree[child].append((parent, weight))

# 2. 첫 번째 DFS: 임의의 노드(1번)에서 가장 먼 노드 A 찾기
max_distance = 0
farthest_node = 0
visited = [False] * (n + 1)
visited[1] = True
dfs(1, 0)

# 3. 두 번째 DFS: A에서 가장 먼 노드 B 찾기
max_distance = 0
visited = [False] * (n + 1)
visited[farthest_node] = True
dfs(farthest_node, 0)

# 4. 결과 출력 (트리의 지름)
print(max_distance)