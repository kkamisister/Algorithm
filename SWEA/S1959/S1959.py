import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    Ai = list(map(int, input().split()))
    Bi = list(map(int, input().split()))

    sum_list = []
    if N >= M:  # Ai 길이가 Bi 길이보다 길 경우
        for i in range(0, N-M+1):
            num_sum = 0
            for j in range(M):
                num_sum += Ai[i+j]*Bi[j]
            sum_list.append(num_sum)
    else:
        for i in range(0, M-N+1):
            num_sum = 0
            for j in range(N):
                num_sum += Bi[i+j]*Ai[j]
            sum_list.append(num_sum)
    print(f'#{tc} {max(sum_list)}')