T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    idx = list(map(int, input()))
    cmt = 0

    for i in range(M):
        if i == 0:
            gap = idx[i]
        else:
            gap = idx[i] - idx[i-1]
        if gap >= K:
            cnt += 1