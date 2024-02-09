T = int(input())

for T in range(T):
    R, S = map(str, input().split(' '))
    
    R = int(R)
    
    for s in S:
        print(s * R, end='')
    
    print()