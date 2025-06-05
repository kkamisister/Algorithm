from collections import deque


def bfs(N, K):
    # 최대 위치 범위
    max_position = 100000

    visited = [0] * (max_position + 1)

    # 큐 초기화
    # 시작위치 N, 시간 0 큐에 삽입
    queue = deque([(N, 0)])

    # 시작위치 방문표시
    visited[N] = 1

    while queue:
        # 큐 첫번째 값 pop
        position, time = queue.popleft()

        # 현재 위치가 동생의 위치(K)와 같다면, 현재까지의 시간을 반환
        if position == K:
            return time

        # 수빈이가 이동할 수 있는 세 가지 경우
        for next_position in (position - 1, position + 1, position * 2):
            # 다음 위치가 유효한 범위(0 ~ 100,000) 내에 있고 방문x여야함
            if 0 <= next_position <= max_position and not visited[next_position]:
                # 방문표시
                visited[next_position] = True
                # 다음 위치, 현재 시간 + 1을 큐에 추가
                queue.append((next_position, time + 1))

N, K = map(int, input().split())

result = bfs(N, K)
print(result)
