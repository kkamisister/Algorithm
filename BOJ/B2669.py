arr = [[0]*100 for _ in range(100)]
coord1 = []
coord2 = []
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    coord1.append((x1, y1))
    coord2.append((x2, y2))

for sqr in range(4):
    for r in range(coord1[sqr][0], coord2[sqr][0]):
        for c in range(coord1[sqr][1], coord2[sqr][1]):
            arr[r][c] = 1

sqr_sum = 0
for i in range(100):
    sqr_sum += sum(arr[i])
print(sqr_sum)