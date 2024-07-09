N = int(input())
target = []
for _ in range(N):
    target.append(int(input()))
stack = []
result = []

idx = 0
for i in range(1, N+1):
    stack.append(i)
    result.append('+')
    while True:
        if stack and stack[-1] == target[idx]:
            stack.pop()
            result.append('-')
            idx += 1
        else:
            break
if result.count('-') == N:
    for _ in range(len(result)):
        print(result[_])
else:
    print('NO')