import sys
sys.stdin = open('in1.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # + 델타 인덱스 만들기
    dr1 = list(0 for _ in range(M-1)) \
          + list(i+1 for i in range(M-1)) \
          + list(0 for _ in range(M-1)) \
          + list(-(i+1) for i in range(M-1))
    # [0, 1, 0, -1]
    dc1 = list(i+1 for i in range(M-1)) \
          + list(0 for _ in range(M-1)) \
          + list(-(i+1) for i in range(M-1)) \
          + list(0 for _ in range(M-1))
    # [1, 0, -1, 0]

    # x 델타 인덱스 만들기
    dr2 = list(-(i+1) for i in range(M-1)) \
          + list(i+1 for i in range(M-1)) \
          + list(i+1 for i in range(M-1)) \
          + list(-(i+1) for i in range(M-1))
    # [-1, 1, 1, -1]
    dc2 = list(i+1 for i in range(M-1)) \
          + list(i+1 for i in range(M-1)) \
          + list(-(i+1) for i in range(M-1)) \
          + list(-(i+1) for i in range(M-1))
    # [1, 1, -1, -1]

    max_sum = 0
    for r in range(N):
        for c in range(N):

            # + 합 구하기
            fly_sum = arr[r][c]
            for d in range((M-1)*4):
                nr1 = r + dr1[d]
                nc1 = c + dc1[d]
                if 0 <= nr1 <= N-1 and 0 <= nc1 <= N-1:
                    fly_sum += arr[nr1][nc1]
            # 최대값 갱신
            if max_sum < fly_sum:
                max_sum = fly_sum

            # x 합 구하기
            fly_sum = arr[r][c]
            for d in range((M-1)*4):
                nr2 = r + dr2[d]
                nc2 = c + dc2[d]
                if 0 <= nr2 <= N-1 and 0 <= nc2 <= N-1:
                    fly_sum += arr[nr2][nc2]
            # 최대값 갱신
            if max_sum < fly_sum:
                max_sum = fly_sum

    print(f'#{tc} {max_sum}')