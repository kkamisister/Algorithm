# BOJ 9012 괄호
import sys
sys.stdin = open('input.txt')

T = int(input())
for TC in range(1, T+1):
    N = int(input())
    for _ in range(N):
        PS = input()
        stack = []
        for ps in PS:
            if ps == '(':
                stack.append(ps)
            else:
                if stack and stack.pop() == '(':
                    result = 'YES'
                else:
                    result = 'NO'
                    break
        if stack:
            result = 'NO'

        print(result)
    print()