import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    fx = input()
    postfix = ''
    stack = [0]*len(fx)
    top = -1

    for tk in fx:
        if tk in '*/+-':
            top += 1
            stack[top] = tk
        else:
            postfix += tk
    for st in range(len(stack)-1, -1, -1):
        if stack[st] != 0:
            postfix += stack[st]
    print(f'#{tc} {postfix}')