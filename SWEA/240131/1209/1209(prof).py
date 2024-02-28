import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = 100
    arr = [list(map(int, input().split()))]
    # 행의 합
    for outer in range(N):
        total = 0
        for inner in range(N):
            total += number_list[outer][inner]


        if max_total < total:
            max_total = total

    # 열의 합
    for outer in range(N):


    # 대각선의 합 좌상 -> 우하
    total = 0
    for i in range(N):
        total += arr[i][i]

    if max_total < total:
        max_total = total

    total = 0
    for i in range(N)