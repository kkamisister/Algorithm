N = int(input())
buildings = []
max_height = 0
max_idx = []
for _ in range(N):
    x, y = map(int, input().split())
    if max_height < y:
        max_height = y
    buildings.append((x, y))
buildings.sort()

# max_idx 구하기
max_idx = []
for idx in range(N):
    if buildings[idx][1] == max_height:
        max_idx.append(idx)

# 첫 최대값 ~ 마지막 최대값 area 구하기:
area = 0
if len(max_idx) == 1:
    area += max_height
else:
    area += max_height * (buildings[max_idx[-1]][0]+1 - buildings[max_idx[0]][0])

# 첫 최대값 기준 왼쪽 훑기
building_idx = 0
last_max_locate = buildings[building_idx][0]
last_max_height = buildings[building_idx][1]
width = 0

while building_idx < max_idx[0]:  # 첫 최대값 전까지
    building_idx += 1
    if last_max_height >= buildings[building_idx][1]:
        continue
    else:
        width = buildings[building_idx][0]-last_max_locate
        area += width*last_max_height
        last_max_locate = buildings[building_idx][0]
        last_max_height = buildings[building_idx][1]

# 마지막 최대값 기준 오른쪽 훑기
building_idx = N-1
last_max_locate = buildings[building_idx][0]+1
last_max_height = buildings[building_idx][1]
width = 0

while building_idx > max_idx[-1]:  # 마지막 최대값 전까지
    building_idx -= 1
    if last_max_height >= buildings[building_idx][1]:
        continue
    else:
        width = last_max_locate - (buildings[building_idx][0]+1)
        area += width * last_max_height
        last_max_locate = buildings[building_idx][0]+1
        last_max_height = buildings[building_idx][1]
print(area)