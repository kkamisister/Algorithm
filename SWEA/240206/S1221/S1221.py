import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    # SOL1
    test_case, N = input().split()
    arr = input().split()
    number_list = ['ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SEV', 'EGT', 'NIN']
    
    for number in number_list:
        for i in range(int(N)):
            if number == arr[i]:
                print(number, end=' ')  
                
                
    # SOL2 수도코드
    # str_to_int = {'ZRO':0, ...}
    # int_to_str = {0:'ZRO', ...}
    # new = []
    # for i in range(int(N)):
    #     new.append(str_to_int.get(arr[i]))
    #     
    #     
    # new 소트
    # 
    # res = []
    # for i in range(int(N)):
    #     res.append(int_to_str.get(new[i]))
    #     
    # print(test_case)
    # print(*res)