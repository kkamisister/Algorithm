import sys
N, K = map(int, sys.stdin.readline().split())
items = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[0] * (K + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    w, v = items[i - 1]
    for j in range(K + 1):
        if j < w:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)
print(dp[N][K])
