N = int(input())

coords = []

for _ in range(N):
    x, y = map(int, input().split())
    coords.append((x, y))

coords.sort()
for _ in range(N):
    print(*coords[_])