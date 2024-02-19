import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, sys.stdin.readline().split())) # 인풋 받고 시작~~~

    # max_sum : 결과로 도출할 최대합, # 인덱스 순회하며 갱신할 현재 합
    max_sum = a = sum(arr[:K]) # 초기값 설정
    for i in range(K, N):
        a += arr[i]-arr[i-K] # 현재합 갱신 : 현재 합이 계산된 K개의 값 중 첫 값과 새로운 값의 차를 더함

        if max_sum < a: # max_sum과 현재합 비교해서 갱신
            max_sum = a
    print(max_sum)