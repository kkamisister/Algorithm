# 큐 공부하고 왔습니다~~~~~~^^
from collections import deque
import sys
sys.stdin = open('input.txt')

T = int(input()) # T만큼
for tc in range(1, T+1):
    N, M_idx = map(int, input().split()) # 인풋 받고 시작
    impt = list(map(int, input().split()))

    M = impt[M_idx] # M_idx의 중요도 값 저장
    queue = deque() # 큐 활용 위해 덱 생성해둠
    check_list = []

    for i in range(N): # queue에 튜플로 저장
        if impt[i] >= M: # M보다 작은값은 버림
            queue.append((impt[i], i)) # 앞 : 중요도 값, 뒤 : 처음 인덱스
            check_list.append(impt[i])

    cnt = 0 # 카운팅 변수 생성
    last = (-1, -1)

    while last[1] != M_idx:
        if queue[0][0] == max(check_list):
            last = queue.popleft()
            check_list.pop(0)
            cnt += 1
        else:
            queue.append(queue.popleft())
            check_list.append(check_list.pop(0))
    print(cnt)