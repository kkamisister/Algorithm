from collections import Counter

N = int(input())
narr = list(map(int, input().split()))
M = int(input())
marr = list(map(int, input().split()))

counter = Counter(narr)
# 이렇게 하면 narr의 각 수의 갯수를 딕셔너리 형태로 counter에 저장함

result = [counter[m] for m in marr]

print(*result)