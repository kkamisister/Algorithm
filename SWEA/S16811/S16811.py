import sys
sys.stdin = open('sample_in.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    Ci = sorted(list(map(int, input().split())))

    result = 0

    min_gap = 1000 # 개수 차이의 최소값

    a_box = []  #  a : 대, b : 중, c : 소

    cnt_dict = {}
    for carrot in Ci:
        cnt_dict[carrot] = 0
    for carrot in Ci:
        cnt_dict[carrot] += 1
    for carrot in cnt_dict.values():
        if carrot > N//2:
            result = -1
            break

    if result == 0:


    print(f'#{tc} {result}')