import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    exp_list = [2, 3, 5, 7, 11]
    exp_dict = {}

    for exp in exp_list:
        cnt = 0
        while N % exp == 0:
            N //= exp
            cnt += 1
        exp_dict[exp] = cnt

    print(f'#{tc}', *exp_dict.values())