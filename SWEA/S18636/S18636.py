import sys
sys.stdin = open('5202_input.txt')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    work_info = []
    for _ in range(N):
        work_info.append(tuple(map(int, input().split())))
    work_info.sort()

    # print(f'#{tc} {tc}')