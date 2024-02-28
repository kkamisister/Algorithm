T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    # N*N 2차원 배열에서 인덱스 0부터 인덱스 N-M까지 순환하며

    sum_list = []

    for r in range(0, N-M+1):
        for c in range(0, N-M+1): # M*M 파리채의 가장 왼쪽 위 칸의 인덱스로 접근

            area_sum = 0

            for i in range(r, r+M):   # 해당 칸 기준으로
                for j in range(c, c+M):
                    area_sum += arr[i][j]

            sum_list.append(area_sum)

    max_sum = 0
    for a in sum_list:
        if max_sum < a:
            max_sum = a

    print(f'#{tc} {max_sum}')