import sys
sys.stdin = open('5248_input.txt')

def dfs(v):+
    visited[v] = 1
    for nxt in grp[v]:
        if visited[nxt]:
            continue
        dfs(nxt)

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    grp = [[] for _ in range(N+1)]

    for i in range(M):
        v1 = arr[i*2]
        v2 = arr[i*2+1]
        grp[v1].append(v2)
        grp[v2].append(v1)

    visited = [0 for _ in range(N+1)]
    cnt = 0

    for i in range(1, N+1):
        if visited[i]:
            continue
        dfs(i)
        cnt += 1

    print(f'#{tc} {cnt}')