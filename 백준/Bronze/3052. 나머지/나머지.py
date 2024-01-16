num_list = []
remain_list = []
a = 0

for i in range(10):
    num_list.append('0')
    remain_list.append('0')
    
    num_list[i] = int(input())
    remain_list[i] = num_list[i] % 42
    
remain_list = set(remain_list)

print(len(remain_list))