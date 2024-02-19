import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*1001 for _ in range(1001)]
    x_lst = []
    y_lst = []
    for _ in range(N):
        x, y, w, h = map(int, input().split())
        x_lst.append(x)
        x_lst.append(x+w-1)
        y_lst.append(y)
        y_lst.append(y+h-1)
        for r in range(y, y+h):
            for c in range(x, x+w):
                arr[r][c] = _ + 1
    paper_cnt = []
    for i in range(N):
        cnt = 0
        for r in range(max(y_lst)+2):
            for c in range(max(x_lst)+2):
                if arr[r][c] == i+1:
                    cnt += 1
        paper_cnt.append(cnt)
    print(*paper_cnt, sep='\n')