import sys
sys.stdin = open('5251_input.txt')

def find_min_distance():
    dist = [10*E] * (N+1)
    visited = [0] * (N+1)

    dist[0] = 0     # 시작값

    for _ in range(N):
        min_idx = -1
        # 최소값 찾기
        for i in range(N+1):
            if not visited[i] and dist[i] < dist[min_idx]:
                min_idx = i

        visited[min_idx] = 1

        # 갱신 가능한 부분이 있다면 갱신
        for i in range(N+1):
            if not visited[i] and dist[i] > dist[min_idx] + adj_arr[min_idx][i]:
                dist[i] = dist[min_idx] + adj_arr[min_idx][i]

    return dist[N]


T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split()) # N : 도착지점, E : 간선 개수
    adj_arr = [[0]*(N+1) for _ in range(N+1)]

    for i in range(E):
        s, e, w = map(int, input().split())
        adj_arr[s][e] = w


    print(f'#{tc}', find_min_distance())