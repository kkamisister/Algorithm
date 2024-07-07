import sys
from collections import deque

input = sys.stdin.read

def main():
    data = input().strip().split('\n')
    N = int(data[0])
    
    q = deque()
    output = []
    
    for i in range(1, N + 1):
        command = data[i].split()
        if command[0] == "push":
            q.append(command[1])
        elif command[0] == "pop":
            if q:
                output.append(q.popleft())
            else:
                output.append(-1)
        elif command[0] == "size":
            output.append(len(q))
        elif command[0] == "empty":
            output.append(1 if not q else 0)
        elif command[0] == "front":
            if q:
                output.append(q[0])
            else:
                output.append(-1)
        elif command[0] == "back":
            if q:
                output.append(q[-1])
            else:
                output.append(-1)
    
    sys.stdout.write("\n".join(map(str, output)) + "\n")

if __name__ == "__main__":
    main()
