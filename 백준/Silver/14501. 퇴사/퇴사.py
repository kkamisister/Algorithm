N = int(input())  # 전체 날짜 수
T = []  # 상담 기간
P = []  # 상담 수익
dp = [0] * (N + 1)  # dp 테이블 초기화

for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

# 뒤에서부터 계산
for i in range(N-1, -1, -1):
    if i + T[i] <= N:  # 상담이 퇴사일 전에 끝나는 경우
        dp[i] = max(dp[i+1], P[i] + dp[i + T[i]])
    else:  # 상담이 퇴사일 이후에 끝나는 경우
        dp[i] = dp[i+1]

print(dp[0])  # 최대 수익 출력
