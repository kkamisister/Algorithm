def count(k, n):
    apt = [[0]*(n+1) for _ in range(k+1)]
    for i in range(1, n+1):
        apt[0][i] = i

    for floor in range(1, k+1):
        for room in range(1, n+1):
            apt[floor][room] = apt[floor-1][room] + apt[floor][room-1]

    return apt[k][n]
    
T = int(input())
for tc in range(T):
    k = int(input())
    n = int(input())
    print(count(k, n))