import sys

S = set()
nums = [i for i in range(1, 21)]
N = int(input())

for _ in range(N):
    command = sys.stdin.readline().split()
    
    if len(command) == 1:
        if command[0] == "all":
            S.update(nums)
        elif command[0] == "empty":
            S = set()
        continue

    cmd, n = command[0], int(command[1])
    
    if cmd == "add":
        S.add(n)
    elif cmd == "remove":
        S.discard(n)
    elif cmd == "check":
        print(1 if n in S else 0)
    elif cmd == "toggle":
        if n in S:
            S.remove(n)
        else:
            S.add(n)
