# B14696 딱지놀이
N = int(input())
for _ in range(N):
    a, *a_lst = map(int, input().split())
    b, *b_lst = map(int, input().split())
    for i in range(a):
        if a_lst[i] == 4:
            a_lst[i] = 1000000000
        elif a_lst[i] == 3:
            a_lst[i] = 1000000
        elif a_lst[i] == 2:
            a_lst[i] = 1000

    for j in range(b):
        if b_lst[j] == 4:
            b_lst[j] = 1000000000
        elif b_lst[j] == 3:
            b_lst[j] = 1000000
        elif b_lst[j] == 2:
            b_lst[j] = 1000

    if sum(a_lst) > sum(b_lst):
        result = 'A'
    elif sum(a_lst) < sum(b_lst):
        result = 'B'
    else:
        result = 'D'

    print(result)