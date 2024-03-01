import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    C_list = list(map(int, input().split()))
    cnt = 1

    for c in range(1, N):
        a = C_list[c-1]
        b = C_list[c]

        if b == a + 1:
          cnt += 1
        else:
            cnt = 0

    print(f'#{tc} {cnt}')