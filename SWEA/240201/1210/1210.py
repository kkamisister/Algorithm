T = 10

for tc in range(1, T+1):
    tc_num = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    goal_idx = arr[99].index(2)

    now_r = 99
    now_c = goal_idx

    now_r -= 1

    while now_r != 0:
        if 0 < now_c < 99: # 현재 c가 1~98 일 때 : 좌우 모두 탐색
            if arr[now_r][now_c-1] == 1: # 왼쪽이 1이면
                now_c -= 1  # 좌로 이동
                while arr[now_r-1][now_c] != 1: # 윗 인덱스가 1일 때 까지
                    now_c -= 1 # 좌로 이동
                now_r -= 1

            elif arr[now_r][now_c+1] == 1: # 오른쪽이 1이면
                now_c += 1  # 우로 이동
                while arr[now_r-1][now_c] != 1: # 윗 인덱스가 1일 때 까지
                    now_c += 1 # 우로 이동
                now_r -= 1

            else:
                now_r -= 1

        elif now_c == 0: # 현재 c가 0일 때 : 오른쪽만 탐색
            if arr[now_r][now_c+1] == 1: # 오른쪽이 1이면
                now_c += 1  # 우로 이동
                while arr[now_r-1][now_c] != 1: # 윗 인덱스가 1일 때 까지
                    now_c += 1 # 우로 이동
                now_r -= 1

            else:
                now_r -= 1

        else: # 현재 c가 99일 때 : 왼쪽만 탐색
            if arr[now_r][now_c-1] == 1: # 왼쪽이 1이면
                now_c -= 1  # 좌로 이동
                while arr[now_r-1][now_c] != 1: # 윗 인덱스가 1일 때 까지
                    now_c -= 1 # 좌로 이동
                now_r -= 1

            else:
                now_r -= 1

    print(f'#{tc} {now_c}')