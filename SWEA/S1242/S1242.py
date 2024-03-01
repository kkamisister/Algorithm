import sys
sys.stdin = open('sample_input.txt')

# 테케를 받으세요
T = int(input())
for tc in range(1, T+1):
    # 인풋 받으세요
    N, M = map(int, input().split())
    arr = [sys.stdin.readline().strip() for _ in range(N)]

    # 암호 들어있는 행만 받기
    pw_row = []
    for i in range(N):
        if arr[i] == '0'*M:
            pass
        else:
            if arr[i] not in pw_row:
                pw_row.append(arr[i])