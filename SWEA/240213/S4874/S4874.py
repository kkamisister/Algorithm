import sys
sys.stdin = open('4874_input.txt')

T = int(input())
for tc in range(1, T+1):
    fx = list(input().split())

    stack = []
    i = 0
    result = 0

    while fx[i] != '.':         # '.'이 나올때까지 fx 순회
        if fx[i] not in '*/+-': # 피연산자가 나오면 push
            stack.append(int(fx[i]))
            i += 1
        else:                   # 연산자가 나오면
            if len(stack) < 2:  # 연산 수행할 수 있는 숫자가 둘 이상인지 확인
                result = 'error'  # 불가하면 error 출력 후
                break
            elif fx[i] == '*':  # 곱셈 연산 수행 후 push
                b = stack.pop()
                a = stack.pop()
                stack.append(a * b)
            elif fx[i] == '/':  # 나눗셈 연산 수행 후 push
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a / b))
            elif fx[i] == '+':  # 덧셈 연산 수행 후 push
                b = stack.pop()
                a = stack.pop()
                stack.append(a + b)
            else:               # 뺄셈 연산 수행 후 push
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            i += 1

    if len(stack) != 1:
        result = 'error'

    if result != 'error':
        result = stack.pop()

    print(f'#{tc} {result}')