import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline

# 입력
N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

empties = [(i, j) for i in range(N) for j in range(M) if lab[i][j] == 0]
viruses = [(i, j) for i in range(N) for j in range(M) if lab[i][j] == 2]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def simulate(walls):
    g = [row[:] for row in lab]
    for x, y in walls:
        g[x][y] = 1

    q = deque(viruses)
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < N and 0 <= ny < M and g[nx][ny] == 0:
                g[nx][ny] = 2
                q.append((nx, ny))

    return sum(cell == 0 for row in g for cell in row)

answer = 0
for walls in combinations(empties, 3):
    safe = simulate(walls)
    if safe > answer:
        answer = safe

print(answer)
