import sys
sys.stdin = open('4865_input.txt')

T = int(input()) # T 받아옴
for tc in range(1, T+1):
    str1 = input() # str1 받아옴
    str2 = input() # str2 받아옴

    str1_dict = {} # str1 글자 딕셔너리 생성

    for str in str1: # str1의 각 글자별 값을 0으로 하는 키 생성
        str1_dict[str] = 0

    for str in str2: # str2 순회하며 글자별 카운팅
        if str in str1_dict.keys():
            str1_dict[str] += 1

    max_cnt = 0 # max 값
    for count in str1_dict.values():
        if max_cnt < count:
            max_cnt = count

    print(f'#{tc} {max_cnt}')