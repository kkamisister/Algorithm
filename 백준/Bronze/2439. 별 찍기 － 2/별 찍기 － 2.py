T = int(input())
import sys
input = sys.stdin.readline

for i in range(1, T+1):
    print(' ' * (T-i) + '*' * i)