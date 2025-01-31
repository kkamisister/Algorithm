import sys
# sys.stdin = open('input.txt')

n = int(input())
tri = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dp = [[0]*n for _ in range(n)]
dp[0][0] = tri[0][0]


for i in range(1, n): # i: 1 ~ (n-1)
    for j in range(i+1): # j: 0 ~ i
        if j == 0:
            dp[i][j] = dp[i-1][j] + tri[i][j]

        elif j == n-1:
            dp[i][j] = dp[i-1][j-1] + tri[i][j]

        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + tri[i][j]

print(max(dp[-1]))