import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    pass

    # 달팽이를 그리기 위해 리스트를 미리 준비
    # snail = [[0] * N] * N # 얕은 복사
    snail = [[0] * N for _ in range(N)]

    # 이동 방향
    # 우 > 하 > 좌 > 상 > 우 > 하
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]


    col = 0
    num = 1
    snail[row][col] = num
    while num < N*N:    # 채워지는 숫자만큼 반복
        # 이동할 위치가 달팽이 범위 내에 있는지 확인
        # for _ in range(4): # 특정 조건에서 방향을 전환해야 하기 때문에 사용하지 않음
        nr = row + dr[direct]
        nc = col + dc[direct]

        if 0 <= nr < N and 0 <= nc < N:     # 이동하려는 방향이 범위 내인지 확인
            # 값이 비어있는지 확인
            if snail[nr][nc] == 0:
                num += 1
                row = nr
                col = nc
                snail[row][col] = num
                while