import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    # N*N 빈 배열 만들기
    tri = [[0]*N for _ in range(N)]

    # 삼각형 만들기 시이작
    for r in range(N):
        for c in range(N):
            if c <= r:          # 0아닌 수 입력될 부분만 1로 채움
                tri[r][c] = 1

            if 0 < r and 0 < c: # 계산 필요한 범위에 한해 해당 값으로 계산
                tri[r][c] = tri[r-1][c-1] + tri[r-1][c]

    for r in range(N):
        for c in range(N):
            if tri[r][c] == 0:
                tri[r][c] = ''

    print(f'#{tc}')
    for triangle in tri:
        print(*triangle)