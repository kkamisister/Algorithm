from collections import deque

N = int(input())
queue = deque(i for i in range(1, N+1))

while len(queue) >= 2:
    queue.popleft()
    queue.append(queue.popleft())

print(queue[0])