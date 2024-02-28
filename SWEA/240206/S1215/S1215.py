import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(8)]

    count = 0

    # 가로 회문 탐색
    for r in range(8): # 총 8행 (0-> 7)
        for c in range(9-N): # 첫 글자 인덱스 범위
            test = 0
            for i in range(N // 2):
                if arr[r][c+i] == arr[r][c+N-1-i]:
                    test += 1
                else:
                    break
            if test == N//2:
                count += 1

    # 세로 회문 탐색
    for c in range(8):
        for r in range(9-N):
            test = 0
            for i in range(N // 2):
                if arr[r+i][c] == arr[r+N-1-i][c]:
                    test += 1
                else:
                    break
            if test == N//2:
                count += 1
    # print(count)
    print(f'#{tc} {count}')