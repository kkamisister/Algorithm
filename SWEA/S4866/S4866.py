import sys
sys.stdin = open('input (1).txt')

T = int(input())
for tc in range(1, T+1):
    target = input()

    size = len(target)
    stack = []
    top = -1

    for s in target:
        if s == '(':
            top += 1
            stack.append(s)
        elif s == ')':
            if stack.pop() == '(':
                top -= 1
            else:
                break