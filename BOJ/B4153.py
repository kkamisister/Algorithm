# BOJ 4153 직각삼각형
import sys

while True:
    num_lst = list(map(int, sys.stdin.readline().split()))
    if num_lst == [0, 0, 0]:
        break
    a = max(num_lst)
    num_lst.remove(a)
    b, c = [*num_lst]
    if a**2 == b**2 + c**2:
        print('right')
    else:
        print('wrong')