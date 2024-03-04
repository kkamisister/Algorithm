# BOJ 10158 개미
import sys
# sys.stdin = open('input.txt')
#
# T = int(input())
#for tc in range(1, T+1):
w, h = map(int, sys.stdin.readline().split())
p, q = map(int, sys.stdin.readline().split())
t = int(input())

dr = 1
dc = 1

while t > 0:
    if p == 0 or p == w:
        dc *= -1
    if q == 0 or q == h:
        dr *= -1
    p += dc
    q += dr
    t -= 1
print(p, q)