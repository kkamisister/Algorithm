def sieve_of_eratosthenes(m, n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0과 1은 소수가 아님
    
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    primes = [i for i in range(m, n + 1) if is_prime[i]]
    return primes

def main():
    import sys
    input = sys.stdin.read
    m, n = map(int, input().split())
    primes = sieve_of_eratosthenes(m, n)
    for prime in primes:
        print(prime)

if __name__ == "__main__":
    main()
