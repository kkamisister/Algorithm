T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) + [0] for _ in range(N)]
    N += 1 # 0인 열과 행 추가
    # 가로, 세로로 연속한 1의 개수가 K인 경우의 수
    ans = 0
    for i in range(N):
        for j in range(N):
            cnt = 0 # j열에서 연속한 1의
            for j in range(N):
                if arr[i][j]:
                    cnt += 1
                else: # arr[i][j]==0
                    if cnt==K:
                        ans += 1
                    cnt = 0
    print(f'#{tc} {ans}')