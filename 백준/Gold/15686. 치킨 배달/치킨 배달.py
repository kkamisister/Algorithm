n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]

houses = []
chickens = []

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            houses.append((i, j))
        elif city[i][j] == 2:
            chickens.append((i, j))

min_distance = float('inf')
selected = []

def get_city_chicken_distance():
    total_distance = 0
    for hx, hy in houses:
        distance = min(abs(hx - cx) + abs(hy - cy) for cx, cy in selected)
        total_distance += distance
    return total_distance

def dfs(start):
    global min_distance
    if len(selected) == m:
        min_distance = min(min_distance, get_city_chicken_distance())
        return
    for i in range(start, len(chickens)):
        selected.append(chickens[i])
        dfs(i + 1)
        selected.pop()

dfs(0)
print(min_distance)
