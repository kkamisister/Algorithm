import sys
sys.stdin = open('5102_input.txt')

def bfs(s, N, G):
    q = []                  # 큐 생성
    visited = [0]*(N+1)     # visited 생성
    q.append(s)             # 시작점 인큐
    visited[s] = 1          # 인큐 표시
    while q:                # 처리 안한 정점이 남아있으면
        t = q.pop(0)        # 처리할 정점 디큐
        if t==G:
            return visited[t]-1 # 최대 경로 간선 수
        for i in adjl[t]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = visited[t]+1
    return 0      # G까지 경로가 없는 경우

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adjl = [[] for _ in range(V+1)]
    for i in range(E):
        n1, n2 = map(int, input().split())
        adjl[n1].append(n2)
        adjl[n2].append(n1)
    S, G = map(int, input().split())

    print(f'#{tc} {bfs(S, V, G)}')