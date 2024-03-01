import sys
from collections import deque
sys.stdin = open('input.txt')

for T in range(1, 11):
    tc = int(input())
    queue = deque(map(int, input().split()))

    while queue[-1] != 0:
        for i in range(1, 6): # 한 사이클 진행
            if queue[0] - i > 0:
                queue[0] -= i
                queue.append(queue.popleft())
            else:
                queue[0] = 0
                queue.append(queue.popleft())
                break

    print(f'#{tc}', end=' ')
    print(*queue)