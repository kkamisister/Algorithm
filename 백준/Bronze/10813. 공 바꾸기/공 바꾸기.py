N, M = map(int, input().split())
bucket = []

for N in range(N):
    bucket.append(N+1)

for a in range(M):
    i, j = map(int, input().split())
    bucket[i-1], bucket[j-1] = bucket[j-1], bucket[i-1]
for b in range(0, N+1):
    print(bucket[b], end = ' ')