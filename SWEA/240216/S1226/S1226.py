import sys
sys.stdin = open('input.txt')

# 시작점 찾기
def find_start():
    for r in range(16):
        for c in range(16):
            if maze[r][c] == '2':
                return r, c

def find_path(row, col):
    global result
    if result:      # 이미 도착한 경우
        return

    # 델타 탐색
    for i in range(4):
        nr = row + dr[i]
        nc = col + dc[i]
        if 1 <= nr < 14 and 1 <= nc < 14 and maze[nr][nc] != '1':
            if maze[nr][nc] == '3':
                result = 1
                return
            elif maze[nr][nc] == '0':
                maze[nr][nc] = '1'
                find_path(nr, nc)

for T in range(1, 11):
    tc = int(input())   # 테케 받고
    maze = [list(input().strip()) for _ in range(16)]   # 미로 2차원 배열 받음

    # 델타 탐색을 위한 상,하,좌,우
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    s_r, s_c = find_start()     # 시작점

    result = 0
    find_path(s_r, s_c)
    print(f'#{tc} {result}')