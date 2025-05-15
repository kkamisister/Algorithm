from collections import deque
import sys
input = sys.stdin.readline

# input : 지도 크기, 승객 수, 초기 연료
n, m, fuel = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
x, y = map(int, input().split())  # 택시 시작 위치
x -= 1
y -= 1

# 승객 정보 (출발좌표, 도착 좧표)
passengers = dict()
for _ in range(m):
    a, b, c, d = map(int, input().split())
    passengers[(a-1, b-1)] = (c-1, d-1)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS로 각 지점까지의 최단 거리 계산
def bfs(sx, sy):
    q = deque()
    q.append((sx, sy))
    visited = [[-1]*n for _ in range(n)]
    visited[sx][sy] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==-1 and board[nx][ny]==0:
                visited[nx][ny] = visited[x][y]+1
                q.append((nx, ny))
    return visited

# 가장 가까운 승객 찾기 (거리, 행, 열)
def find_nearest_passenger(tx, ty):
    dist_map = bfs(tx, ty)
    candidates = []
    for start in passengers.keys():
        sx, sy = start
        d = dist_map[sx][sy]
        if d != -1:
            candidates.append((d, sx, sy))
    if not candidates:
        return None
    candidates.sort()  # 거리, 행, 열
    return candidates[0]

# 목적지까지 이동 거리 반환
def move(dest_x, dest_y, tx, ty):
    dist_map = bfs(tx, ty)
    return dist_map[dest_x][dest_y]

# 승객 수만큼 반복
for _ in range(m):
    result = find_nearest_passenger(x, y)
    if not result:
        print(-1)
        exit()
    d, px, py = result  # 승객 위치까지 거리와 좌표
    if fuel < d:
        print(-1)
        exit()
    fuel -= d  # 승객 태우러 가면서 연료 소모
    x, y = px, py  # 택시 위치 갱신
    dest_x, dest_y = passengers[(px, py)]  # 승객 목적지
    del passengers[(px, py)]  # 승객 제거

    d2 = move(dest_x, dest_y, x, y)  # 목적지까지 거리 계산
    if d2 == -1 or fuel < d2:
        print(-1)
        exit()
    fuel -= d2  # 목적지까지 가면서 연료 소모
    fuel += d2 * 2  # 연료 충전
    x, y = dest_x, dest_y  # 택시 위치 갱신

print(fuel)  # 남은 연료
