bingo = [list(map(int, input().split())) for _ in range(5)]
called_lst = []
for _ in range(5):
    called_lst += list(map(int, input().split()))

def bingo_count(bingo, called_lst):
    bingo_cnt = 0
    for call in range(25):
        for r in range(5):
            for c in range(5):
                if bingo[r][c] == called_lst[call]:
                    bingo[r][c] = 0

                # 가로 빙고 검사
                if sum(bingo[r]) == 0:
                    bingo_cnt += 1
                if bingo_cnt == 3:
                    return call+1

                # 세로 빙고 검사
                c_sum = 0
                for nr in range(5):
                    c_sum += bingo[nr][c]
                if c_sum == 0:
                    bingo_cnt += 1
                if bingo_cnt == 3:
                    return call+1

                # 우하향 대각선 빙고 검사
                cross_sum1 = 0
                if r == c:
                    for nc in range(5):
                        cross_sum1 += bingo[nc][nc]
                if cross_sum1 == 0:
                    bingo_cnt += 1
                if bingo_cnt == 3:
                    return call+1

                # 좌상향 대각선 빙고 검사
                cross_sum2 = 0
                if r == 5-c:
                    for nc in range(4, -1, -1):
                        cross_sum2 += bingo[nc][4-nc]
                if cross_sum2 == 0:
                    bingo_cnt += 1
                if bingo_cnt == 3:
                    return call+1

print(bingo_count(bingo, called_lst))