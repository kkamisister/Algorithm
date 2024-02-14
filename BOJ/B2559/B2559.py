import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, sys.stdin.readline().split()))

    # sum_list = []
    # for i in range(N-K+1):
    #     a = 0
    #     for j in range(K):
    #         a += arr[i+j]
    #     sum_list.append(a)
    max_sum = sum(arr[:K])
    idx = 0
    while idx <= N-K:
        if arr[idx] < arr[idx+K]:
            max_sum += arr[idx+K]-arr[idx]
            idx += 1
        elif arr[idx]+arr[idx+1] < arr[idx+K]+arr[idx+K+1]:
            max_sum += arr[idx+K]+arr[idx+K+1]-(arr[idx]+arr[idx+1])
            idx += 2
        elif max_sum < sum(arr[idx+K:idx+K+3]):
            max_sum += arr[idx+K]+arr[idx+K+1]-(arr[idx]+arr[idx+1])
            idx += 2
        elif:

