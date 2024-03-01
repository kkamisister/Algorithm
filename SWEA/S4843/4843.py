T = int(input())

for tc in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input().split()))

    sort_list = [0]*10

    for i in range(1, 6):

        max_num = num_list[0]
        for num in num_list:
            if max_num < num:
                max_num = num

        sort_list[2*i-2] = max_num
        num_list.remove(max_num)

        min_num = num_list[0]
        for num in num_list:
            if min_num > num:
                min_num = num

        sort_list[2*i-1] = min_num
        num_list.remove(min_num)

    print(f'#{tc} ', end='')
    print(*sort_list)