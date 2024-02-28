import sys
sys.stdin = open('test_input.txt', encoding='utf-8')

T = int(input())
for tc in range(1, T+1):
    pattern = input()
    target = input()

    P = len(pattern)
    T = len(target)
    cnt = 0

    # p_idx = 0
    t_idx = 0

    while t_idx < T:
        # target 순회하며 탐색 (순회 방법 : 판별하며 t_idx += 1)
        for p_idx in range(P):
            test = 1
            if target[t_idx] == pattern[p_idx]:
                t_idx += 1
                test += 1
            else:
                t_idx += test
                break

        if test-1 == P:
            cnt += 1

    print(cnt)