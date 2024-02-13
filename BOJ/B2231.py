N = int(input())

for i in range(1, N):
    num_list = []
    a = i
    for j in range(6):
        num_list.append(a%10)
        a //= 10
    result_list = []
    if i + sum(num_list) == N:
        result_list.append(i)
if len(result_list) != 0:
    print(result_list[0])
else:
    print(0)