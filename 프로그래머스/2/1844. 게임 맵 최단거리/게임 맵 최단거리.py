from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])  # 행과 열의 크기
    visited = [[False]*m for _ in range(n)]  # 방문 여부를 저장하는 2차원 리스트
    queue = deque()
    queue.append((0, 0, 1))  # 시작 위치와 이동 횟수를 큐에 추가
    visited[0][0] = True  # 시작 위치 방문 처리

    # 상, 하, 좌, 우 이동을 위한 방향 벡터
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y, distance = queue.popleft()

        # 도착 지점에 도달한 경우
        if x == n - 1 and y == m - 1:
            return distance

        # 네 방향으로 이동
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 맵 범위 내에 있고, 이동할 수 있으며, 아직 방문하지 않은 경우
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True  # 방문 처리
                    queue.append((nx, ny, distance + 1))  # 큐에 다음 위치와 이동 횟수 추가

    # 도착 지점에 도달할 수 없는 경우
    return -1
