def is_Prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

N = int(input())
arr = [*map(int, input().split())]

count = 0
for n in arr:
    if is_Prime(n):
        count += 1
print(count)