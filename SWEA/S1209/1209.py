T = 10

for tc in range(1, T+1):
    tc_num = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    sum_list = []

    # 각 행의 합
    for r in range(100):
        a_sum = 0
        for c in range(100):
            a_sum += arr[r][c]
        sum_list.append(a_sum)

    # 각 열의 합
    for c in range(100):
        a_sum = 0

        for r in range(100):
            a_sum += arr[r][c]
        sum_list.append(a_sum)

    # 우하향 대각선 합
    a_sum = 0
    for r in range(100):
        a_sum += arr[r][r]
    sum_list.append(a_sum)

    # 좌하향 대각선 합
    a_sum = 0
    for r in range(100):
        a_sum += arr[r][99-r]
    sum_list.append(a_sum)

    # 합의 최대값
    max_sum = 0
    for i in sum_list:
        if max_sum < i:
            max_sum = i

    print(f'#{tc} {max_sum}')