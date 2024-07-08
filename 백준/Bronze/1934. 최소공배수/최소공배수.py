T = int(input())

def gcd(a, b):
    while b!=0:
        a, b = b, a%b
    return a

for tc in range(T):
    A, B = map(int, input().split())
    print(A*B // gcd(A, B))