import sys
sys.stdin = open('5188_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dr = [0, 1]
    dc = [1, 0]