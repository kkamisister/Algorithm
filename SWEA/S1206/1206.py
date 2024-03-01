for tc in range(1, 11):

    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0

    for i in range(2, N-2):
        temp = []
        for j in range(i-2, i+3):
            temp.append(arr[j])
            if temp[2] > temp[0 and 1 and 3 and 4]:
                temp.remove(arr[i])
                second = 0
                for i in temp:
                    if second < i:
                        second = i
                    pass
                cnt += (arr[i] - second)

            pass
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #     if arr[j] > arr[j-2 and i-1 and i+1 and i+2]:
        #     second =
        #
        #     if
        #
        #
        # max_temp = temp[0]
        # for num in temp:
        #     if num > max_temp:
        #         max_temp = num
        #     pass
        #
        # if arr[i] == max_temp:
        #     temp.remove(arr[i])
        #
        #     second_temp = temp[0]
        #     for num in temp:
        #         if num > second_temp:
        #             second_temp = num
        #         pass
        #
        # pass
        #
        #     # if max_temp = temp[0]
        #     #     for num in temp:
        #
        #
        # if max_temp == arr[i]:
        #
        #
        #
        #
        #
        #
        #
        #
        #     cnt += (arr[i] - second_temp)
        #
        # pass

    print(f'#{tc} {cnt}')