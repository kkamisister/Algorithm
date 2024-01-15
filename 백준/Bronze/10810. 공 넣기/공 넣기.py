N, M = map(int, input().split())
bucket = []

for N in range(N):
    bucket.append(0)

for a in range(1, M+1):
    i, j, k = map(int, input().split())
    for b in range(i, j+1):
        bucket[b-1] = k
for N in range(N+1):
    print(bucket[N], end = ' ')