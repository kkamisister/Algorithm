C, R = map(int, input().split())
K = int(input())

arr = [[0]*C for _ in range(R)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
direction = 0

row = R-1
col = 0
num = 1
arr[row][col] = num

while num < K:
    nr = row + dr[direction]
    nc = col + dc[direction]

    if 0 <= nr <= R-1 and 0 <= nc <= C-1 and arr[nr][nc] == 0:
        num += 1
        row = nr
        col = nc
        arr[nr][nc] = num
    else:
        direction = (direction + 1) % 4

print(arr)
print(col+1, row+1)