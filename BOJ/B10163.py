N = int(input())
arr = [[0]*1001 for _ in range(1001)]
for _ in range(N):
    x1, y1, w, h = map(int, input().split())
    for x in range(x1, x1+w):
        for y in range(y1, y1+h):
            arr[x][y] = _+1
for _ in range(N):
    count = 0
    for r in range(1001):
        for c in range(1001):
            if arr[r][c] == _+1:
                count += 1
    print(count)