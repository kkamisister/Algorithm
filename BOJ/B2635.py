N = int(input())
max_len = 0
temp_arr = []
for i in range(N, 0, -1):
    arr = [N]
    arr.append(i)
    idx1 = 0
    idx2 = 1
    while True:
        a = arr[idx1] - arr[idx2]
        if a < 0:
            break
        arr.append(a)
        idx1 += 1
        idx2 += 1
    temp = len(arr)
    if max_len < temp:
        temp_arr = arr
        max_len = temp
print(max_len)
print(*temp_arr)