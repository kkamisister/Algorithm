import sys
sys.stdin = open('input1.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    max_sum = 0
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    for r in range(N):
        for c in range(M):
            balloon_sum = arr[r][c]
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]

                if 0 <= nr <= N-1 and 0 <= nc <= M-1:
                    balloon_sum += arr[nr][nc]
            if max_sum < balloon_sum:
                max_sum = balloon_sum
    print(f'#{tc} {max_sum}')