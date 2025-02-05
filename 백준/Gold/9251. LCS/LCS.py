import sys

def lcs(A, B):
    len_a, len_b = len(A), len(B)
    dp = [[0] * (len_b + 1) for _ in range(len_a + 1)]
    
    for i in range(1, len_a + 1):
        for j in range(1, len_b + 1):
            if A[i - 1] == B[j - 1]:  # 문자가 같으면
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:  # 다르면
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[len_a][len_b]  # LCS 길이 반환

if __name__ == "__main__":
    A = sys.stdin.readline().strip()
    B = sys.stdin.readline().strip()
    print(lcs(A, B))
