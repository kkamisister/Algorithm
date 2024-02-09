N = int(input())

num_str = str(input())

num_list = [i for i in range(len(num_str))]

for i in range(len(num_str)):
    num_list[i] = int(num_str[i])

print(sum(num_list))