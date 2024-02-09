N = int(input())

for i in range(1, 2*N):
    if i <= N:
        print(' ' * (N-i) + '*' * i)
    else:
        print(' ' * (i-N) + '*' * (2*N-i))