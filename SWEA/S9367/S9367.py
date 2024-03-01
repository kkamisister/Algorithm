import sys
sys.stdin = open('carrot_sample_in.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    carrots = list(map(int, input().split()))
    result = 1
    max_result = 1
    for idx in range(1, N):
        if carrots[idx] > carrots[idx-1]:
            result += 1
        else:
            result = 1
        if max_result < result:
            max_result = result
    print(f'#{tc} {max_result}')