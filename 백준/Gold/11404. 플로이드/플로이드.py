import sys

# 무한을 의미하는 값 (최대 비용 100000 * 100 보다 큰 값)
INF = int(1e9)

# 입력 받기
n = int(sys.stdin.readline())  # 도시 개수 (노드 개수)
m = int(sys.stdin.readline())  # 버스 개수 (간선 개수)

# 그래프 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신으로 가는 비용은 0
for i in range(1, n + 1):
    graph[i][i] = 0

# 간선 정보 입력
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a][b] = min(graph[a][b], c)  # 같은 경로가 여러 개 있으면 최소 비용만 저장

# 플로이드-워셜 알고리즘 실행
for k in range(1, n + 1):  # 경유 노드
    for i in range(1, n + 1):  # 출발 노드
        for j in range(1, n + 1):  # 도착 노드
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 결과 출력
for i in range(1, n + 1):
    for j in range(1, n + 1):
        # 갈 수 없는 경우 0 출력
        if graph[i][j] == INF:
            print(0, end=" ")
        else:
            print(graph[i][j], end=" ")
    print()
