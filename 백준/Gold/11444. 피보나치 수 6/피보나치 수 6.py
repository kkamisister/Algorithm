import sys
input = sys.stdin.readline

MOD = 1000000007

def matrix_mul(a, b):
    return [
        [(a[0][0] * b[0][0] + a[0][1] * b[1][0]) % MOD, (a[0][0] * b[0][1] + a[0][1] * b[1][1]) % MOD],
        [(a[1][0] * b[0][0] + a[1][1] * b[1][0]) % MOD, (a[1][0] * b[0][1] + a[1][1] * b[1][1]) % MOD]
    ]

def matrix_pow(matrix, n):
    result = [[1, 0], [0, 1]]
    while n > 0:
        if n % 2 == 1:
            result = matrix_mul(result, matrix)
        matrix = matrix_mul(matrix, matrix)
        n //= 2
    return result

def fibonacci(n):
    if n == 0:
        return 0
    base = [[1, 1], [1, 0]]
    result = matrix_pow(base, n - 1)
    return result[0][0]

n = int(input())
print(fibonacci(n))
