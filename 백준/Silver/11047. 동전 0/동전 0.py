N, K = map(int, input().split())
A = []
for _ in range(N):
    Ai = int(input())
    A.append(Ai)

A.sort(reverse=True)

count = 0
for i in A:
    if K == 0:
        break
    else:
        count += K // i
    K %= i
print(count)