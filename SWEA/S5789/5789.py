import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split())

    arr = [0]*N

    for i in range(1, Q+1):
        Li, Ri = map(int, input().split())

        for box_idx in range(Li-1, Ri):
            arr[box_idx] = i

    print(f'#{tc} ', end='')
    print(*arr)