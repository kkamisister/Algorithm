N = int(input())

for i in range(1, 2*N):
    if i <= N:
        # print(' ' * (i-1) + '*' * (2*N-1-2*(i-1)))
        print(' ' * (i-1) + '*' * (2*(N-i)+1))
    else:
        # print(' ' *  (N-(i-N+1))+ '*' * (2*(i-N+1)-1))
        print(' ' *  (2*N-i-1)+ '*' * (2*(i-N)+1))