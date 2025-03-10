import sys
input = sys.stdin.readline

n = int(input())
max_dp = [0, 0, 0]
min_dp = [0, 0, 0]

first_row = list(map(int, input().split()))
max_dp = list(first_row)
min_dp = list(first_row)

for _ in range(n - 1):
    a, b, c = map(int, input().split())

    max_a = a + max(max_dp[0], max_dp[1])
    max_b = b + max(max_dp[0], max_dp[1], max_dp[2])
    max_c = c + max(max_dp[1], max_dp[2])

    min_a = a + min(min_dp[0], min_dp[1])
    min_b = b + min(min_dp[0], min_dp[1], min_dp[2])
    min_c = c + min(min_dp[1], min_dp[2])

    max_dp = [max_a, max_b, max_c]
    min_dp = [min_a, min_b, min_c]

print(max(max_dp), min(min_dp))
