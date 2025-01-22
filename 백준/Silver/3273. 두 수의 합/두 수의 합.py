# 입력 처리
n = int(input())
numbers = list(map(int, input().split()))
x = int(input())

# 정렬
numbers.sort()

# 투 포인터 초기화
left, right = 0, n - 1
count = 0

# 투 포인터 알고리즘
while left < right:
    current_sum = numbers[left] + numbers[right]
    if current_sum == x:
        count += 1
        left += 1
        right -= 1
    elif current_sum < x:
        left += 1
    else:
        right -= 1

# 결과 출력
print(count)
