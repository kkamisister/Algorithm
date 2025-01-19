from itertools import permutations

n, m = map(int, input().split())
numbers = sorted(map(int, input().split()))
for perm in permutations(numbers, m):
    print(*perm)
