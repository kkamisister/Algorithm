N = int(input())
members = []

for _ in range(N):
    a, n = input().split()
    members.append((int(a), _, n))

members.sort()
for _ in range(N):
    print(members[_][0], members[_][-1])