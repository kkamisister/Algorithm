a, b, c = input().split()
A = int(a)
B = int(b)
C = int(c)

numlist = [A, B, C]
numlist.sort()
if A != B:
    if A != C:
        if B != C: # A != B != C (3)
            reward = numlist[-1] * 100
        else: # A != B == C (2)
            reward = 1000 + B * 100
    else: # A == C != B (2) 
        reward = 1000 + A * 100
else:
    if A != C: # A == B != C (2)
        reward = 1000 + A * 100
    else: # A == B == C (1)
        reward = 10000 + A * 1000 
print(reward)