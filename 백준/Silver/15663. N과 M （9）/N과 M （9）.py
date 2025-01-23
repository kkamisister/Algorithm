from itertools import permutations

# 입력 처리
n, m = map(int, input().split())
numbers = list(map(int, input().split()))

# 중복 제거를 위해 정렬
numbers.sort()

# 중복된 결과 방지를 위해 set을 활용
results = set(permutations(numbers, m))

# 결과 출력
for result in sorted(results):
    print(*result)
