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
    print(tc_num)
    print('ZRO ' * counts[0],end = '')
    print('ONE ' * counts[1],end = '')
    print('TWO ' * counts[2],end = '')
    print('THR ' * counts[3],end = '')
    print('FOR ' * counts[4],end = '')
    print('FIV ' * counts[5],end = '')
    print('SIX ' * counts[6],end = '')
    print('SVN ' * counts[7],end = '')
    print('EGT ' * counts[8],end = '')
    print('NIN ' * counts[9])