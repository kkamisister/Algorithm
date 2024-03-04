hor, ver = map(int, input().split())
N = int(input())
hor_list = [0, ver]
ver_list = [0, hor]
for _ in range(N):
    a, b = map(int, input().split())
    if a == 0:
        hor_list.append(b)
    else:
        ver_list.append(b)
hor_list.sort()
ver_list.sort()
max_hor = 0
max_ver = 0
for i in range(1, len(hor_list)):
    temp_hor = hor_list[i] - hor_list[i-1]
    if max_hor < temp_hor:
        max_hor = temp_hor
for i in range(1, len(ver_list)):
    temp_ver = ver_list[i] - ver_list[i-1]
    if max_ver < temp_ver:
        max_ver = temp_ver
result = max_hor*max_ver
print(result)