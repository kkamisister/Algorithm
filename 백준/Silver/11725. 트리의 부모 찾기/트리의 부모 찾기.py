import sys
from collections import defaultdict, deque

sys.setrecursionlimit(10**6)
input = sys.stdin.read

def find_parents():
    # 입력 처리
    data = input().splitlines()
    n = int(data[0])
    graph = defaultdict(list)
    
    for i in range(1, n):
        a, b = map(int, data[i].split())
        graph[a].append(b)
        graph[b].append(a)
    
    # 부모 노드 저장
    parents = [0] * (n + 1)
    
    def dfs(node, parent):
        # 현재 노드의 부모를 기록
        parents[node] = parent
        # 자식 노드를 탐색
        for neighbor in graph[node]:
            if neighbor != parent:  # 부모 노드로는 돌아가지 않음
                dfs(neighbor, node)
    
    # 루트 노드는 1번
    dfs(1, 0)
    
    # 결과 출력 (2번 노드부터)
    sys.stdout.write("\n".join(map(str, parents[2:])))
    
find_parents()
