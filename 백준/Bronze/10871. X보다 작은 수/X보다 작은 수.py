N, X = map(int, input().split())
numlist = list(map(int, input().split()))

for i in range(len(numlist)):
    if numlist[i] < X:
        print(numlist[i], end = ' ')
    else:
        pass