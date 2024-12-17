dp = [(1, 0), (0, 1)]
for num in range(2, 41):
    dp.append((dp[num-1][0]+dp[num-2][0], dp[num-1][1]+dp[num-2][1]))
# T = int(input())
# for tc in range(T):
N = int(input())
for tc_n in range(N):
    a = int(input())
    print(dp[a][0], dp[a][1])