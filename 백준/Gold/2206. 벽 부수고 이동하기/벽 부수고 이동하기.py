from collections import deque
import sys
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    queue = deque()
    queue.append((0, 0, 0))
    visited[0][0][0] = 1

    while queue:
        x, y, wall_break = queue.popleft()
        if x == N - 1 and y == M - 1:
            return visited[x][y][wall_break]

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 0 and visited[nx][ny][wall_break] == 0:
                    visited[nx][ny][wall_break] = visited[x][y][wall_break] + 1
                    queue.append((nx, ny, wall_break))
                elif graph[nx][ny] == 1 and wall_break == 0:
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    queue.append((nx, ny, 1))
    return -1

N, M = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(N)]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]

print(bfs())
