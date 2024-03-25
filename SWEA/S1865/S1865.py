import sys
sys.stdin = open('input.txt')

def ajdks(n, items, total):
    global ans

    if total <= ans:
        return
    if n == N:
        ans = max(ans, total)
        return

    for i in range(N):
        if i not in items:
            items.append(i)
            ajdks(n+1, items, total*(eff[n][i]/100))
            items.pop()

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    eff = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    ajdks(0, [], 1)
    print('#{} {:.6f}'.format(tc, round(ans*100,6)))