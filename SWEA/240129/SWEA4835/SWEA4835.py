import sys

sys.stdin = open('4835_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    sum_list = []

    for first in range(0, N-M+1):
        a = 0

        for num in range(first, first + M):
            a += arr[num]

        sum_list.append(sum)

    max_sum = sum_list[0]
    min_sum = sum_list[0]

    for b in sum_list:
        if max_sum < b:
            max_sum = b
        pass

    for b in sum_list:
        if min_sum > b:
            min_sum = b
        pass


    print(f'#{tc} {max_sum - min_sum}')
