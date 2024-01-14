price = int(input())
N = int(input())
pricesum = 0
for i in range(1, N+1):
    a, b = input().split()
    a = int(a)
    b = int(b)
    pricesum += a*b
if pricesum == price:
    print('Yes')
else:
    print('No')