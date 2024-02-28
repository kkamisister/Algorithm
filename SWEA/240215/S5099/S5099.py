import sys
from collections import deque
sys.stdin = open('5099_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    Ci = deque(map(int, input().split()))

    # print(f'{tc} {result}')