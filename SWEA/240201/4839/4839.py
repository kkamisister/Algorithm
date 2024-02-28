# import sys
# sys.stdin = open('4839_input.txt')

T = int(input())
for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())

    a_turn = 0 # A의 시도 횟수
    b_turn = 0 # B의 시도 횟수

    now_Pa = 0 # 시도 후 A의 현재 페이지
    now_Pb = 0 # 시도 후 B의 현재 페이지

    while now_Pa != Pa:
        a_turn += 1
        if now_Pa < Pa:
            now_Pa = int((P+now_Pa)/2)
        else:
            now_Pa = int(now_Pa/2)

    while now_Pb != Pb:
        b_turn += 1

        if now_Pb < Pb:
            now_Pb = int((P+now_Pb) / 2)
        else:
            now_Pb = int(now_Pb / 2)

    # 결과 출력
    if a_turn < b_turn:
        print(f'#{tc} A')
    elif a_turn < b_turn:
        print(f'#{tc} B')
    print(f'#{tc} 0')
