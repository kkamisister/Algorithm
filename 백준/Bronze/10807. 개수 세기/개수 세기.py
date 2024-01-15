T = int(input())
numlist = list(map(int, input().split()))
a = int(input())
count = 0

for i in range(len(numlist)):
    if numlist[i] == a:
        count += 1
    else:
        pass
print(count)