import sys
sys.stdin = open('input2.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0

    dr = [0, 1, 1, 1, 0, -1, -1, -1]
    dc = [1, 1, 0, -1, -1, -1, 0, 1]

    for r in range(N):
        for c in range(M):
            lower_cnt = 0
            for d in range(8):
                nr = r + dr[d]
                nc = c + dc[d]
                if 0 <= nr <= N-1 and 0 <= nc <= M-1:
                    if arr[nr][nc] < arr[r][c]:
                        lower_cnt += 1
            if lower_cnt >= 4:
                cnt += 1
    print(f'#{tc} {cnt}')