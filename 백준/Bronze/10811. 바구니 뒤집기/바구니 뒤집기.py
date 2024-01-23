N, M = map(int, input().split())

bucket_list = [i for i in range(1, N+1)]

for M in range(1, M+1):

    i, j = map(int, input().split())

    temp = []

    temp = bucket_list[i-1:j]
    temp.reverse()

    bucket_list[i-1:j] = temp

for i in bucket_list:
    print(i, end = ' ')