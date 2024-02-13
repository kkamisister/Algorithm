import sys
sys.stdin = open('input.txt')

# 큐 아직 공부 안함
# 공부하고 다시 풀어보겠슴다
T = int(input())
for tc in range(1, T+1):
    N, M_idx = map(int, input().split())
    arr = list(map(int, input().split()))   # 데이터 받아오고 시이작~~~

    # A : M보다 큰 수 개수
    # B : M_idx까지의 M 개수
    # C : M_idx에 따라 달라짐

    M = arr[M_idx]
    A = B = C = 0

    for i in range(0, M_idx+1): # M_idx까지의 M 개수
        if arr[i] == M:
            B += 1

    if M != max(arr): # M이 최댓값이 아니라면
        for i in range(N):
            if arr[i] > M:
                A += 1      # M보다 큰 수 개수
                L_idx = i   # 마지막으로 M보다 큰 값의 idx 계산

        if M_idx < L_idx:
            for i in range(L_idx+1, N): # L_idx이후 값 중 M 개수 계산
                if arr[i] == M:
                    C += 1
            result = A + B + C
        else:
            for i in range(L_idx):  # 0 ~ L_idx 중 M 개수 계산
                if arr[i] == M:
                    C += 1
            result = A + B - C  # A과 L_idx~M_idx 사이의 M 개수

    else:  # M이 최댓값이면
        result = B # M_idx까지의 M 개수

    print(result)