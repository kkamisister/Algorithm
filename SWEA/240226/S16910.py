T = int(input())

def get_count(N):
    cnt = 0
    for y in range(-N, N+1):
        for x in range(-N, N+1):
            ans = x**2 + y**2
            if ans <= N**2:
                cnt += 1
    return cnt

for tc in range(1, T+1):
    N = int(input())
    result = get_count(N)

    print(f'#{tc} {result}')