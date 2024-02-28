#############################
######안 돌아간 코드###########
#############################

import sys
sys.stdin = open('GNS_test_input.txt')

T = int(input()) # T 받아옴
for tc in range(1, T+1):    # T만큼 진행
    tc_num, N = input().split() # tc_num, N 받아옴
    num_list = input().split()  # num_list 받아옴
    N = int(N)

    # 1. 카운팅 정렬 시작
    counts = [0] * 10 # 카운팅 리스트 생성

    for i in num_list:
        if i == 'ZRO':
            counts[0] += 1
        elif i == 'ONE':
            counts[1] += 1
        elif i == 'TWO':
            counts[2] += 1
        elif i == 'THR':
            counts[3] += 1
        elif i == 'FOR':
            counts[4] += 1
        elif i == 'FIV':
            counts[5] += 1
        elif i == 'SIX':
            counts[6] += 1
        elif i == 'SVN':
            counts[7] += 1
        elif i == 'EGT':
            counts[8] += 1
        else:
            counts[9] += 1

    # 2. 누적 카운팅
    for i in range(1, 10):
        counts[i] += counts[i-1]

    # 3. 정렬
    sorted_num_list = [0] * N

    for i in range(N-1, -1, -1):
        if num_list[i] == 'ZRO':
            counts[0] -= 1
            sorted_num_list[counts[0]] = 'ZRO'
        elif num_list[i] == 'ONE':
            counts[1] -= 1
            sorted_num_list[counts[1]] = 'ONE'
        elif num_list[i] == 'TWO':
            counts[2] -= 1
            sorted_num_list[counts[3]] = 'TWO'
        elif num_list[i] == 'THR':
            counts[3] -= 1
            sorted_num_list[counts[3]] = 'THR'
        elif num_list[i] == 'FOR':
            counts[4] -= 1
            sorted_num_list[counts[4]] = 'FOR'
        elif num_list[i] == 'FIV':
            counts[5] -= 1
            sorted_num_list[counts[5]] = 'FIV'
        elif num_list[i] == 'SIX':
            counts[6] -= 1
            sorted_num_list[counts[6]] = 'SIX'
        elif num_list[i] == 'SVN':
            counts[7] -= 1
            sorted_num_list[counts[7]] = 'SVN'
        elif num_list[i] == 'EGT':
            counts[8] -= 1
            sorted_num_list[counts[8]] = 'EGT'
        else:
            counts[9] -= 1
            sorted_num_list[counts[9]] = 'NIN'

    # print(tc_num)
    # print(*sorted_num_list)
