import sys
input = sys.stdin.readline

while True:
    A, B = map(int, input().split())
    if (A, B) != (0, 0):
        print(A + B)
    else:
        break