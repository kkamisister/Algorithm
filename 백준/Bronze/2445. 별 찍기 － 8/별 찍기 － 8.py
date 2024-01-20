N = int(input())

for i in range(1, 2*N):
    if i < N:
        # print('*' * (2*N-2*(N-i)) + ' ' * 2*(N-i) + '*' * (2*N-2*(N-i)))
        print('*' * i + ' ' * 2*(N-i) + '*' * i)
    else:
        print('*' * (N-(i-N)) + ' ' * (2*(i-N)) + '*' * (N-(i-N)))