import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    for r in range(9):
        for c in range(9):

            if 0 <= r <= 2 and

    print(f'#{tc} {result}')