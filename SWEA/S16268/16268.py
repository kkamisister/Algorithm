T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    sum_list = []
    for r in range(1, N-1):
        for c in range(1, N-1):
            a_sum = 0
            a_sum += (arr[r-1][c] + arr[r][c-1] + arr[r][c] + arr[r][c+1] + arr[r+1][c])

            sum_list.append(a_sum)

    for r in range(N):
        for c in range(N):
            if r == 0 and c == 0:
                a_sum = 0
                a_sum += arr[r][c] + arr[r][c+1] + arr[r+1][c]
                sum_list.append(a_sum)

            elif r == 0 and c == N-1:
                a_sum = 0
                a_sum += arr[r][c] + arr[r][c - 1] + arr[r+1][c]
                sum_list.append(a_sum)

            elif r == 100 and c == 0:
                a_sum = 0
                a_sum += arr[r][c] + arr[r-1][c - 1] + arr[r+1][c]
                sum_list.append(a_sum)