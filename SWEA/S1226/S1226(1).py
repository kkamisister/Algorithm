import sys
sys.stdin = open('input.txt')

# 시작점 찾기
def find_start():
    for r in range(16):
        for c in range(16):
            if maze[r][c] == '2':
                return r, c

def bfs(s_r, s_c, N):      # 시작정점 s, 노드개수 N
    q = []  # 큐
    global result
    while q:                # 큐가 비워질때까지 (남은 정점이 있으면)
        t = q.pop(0)

        for i in range(N):   # t에 인접인 정점 i
            if visited[i]==0:       # 방문하지 않은 정점이면
                q.append(i)
                visited[i] = 1 + visited[t]     # 방문표시

for T in range(1, 11):
    tc = int(input())   # 테케 받고
    maze = [list(input().strip()) for _ in range(16)]   # 미로 2차원 배열 받음

    s_r, s_c = find_start()  # 시작점 찾기

    result = 0
    bfs(s_r, s_c, 256)
    print(f'#{tc} {result}')