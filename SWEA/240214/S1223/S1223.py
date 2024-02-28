import sys
sys.stdin = open('input.txt')

impt = {'+': 1, '*': 2}
T = 10
for tc in range(1, T+1):
    N = int(input())
    fx = input()
    stack = []
    postfix = []

    # 후위표기식 변경
    for n in range(N):  # N만큼 반복하여
        if fx[n].isdigit():  # 만약 숫자이면 바로 postfix에 추가
            postfix.append(fx[n])
        else:  # 그외에 경우 fx[n]이 stack[-1]의 우선순위와 같거나 보다 작으면 fx[n]의 우선순위가 더 커질때까지 pop
            while stack and impt[fx[n]] <= impt[stack[-1]]:
                postfix.append(stack.pop())  # pop한것들은 postfix에 추가 시켜줌
            stack.append(fx[n])  # 위의 조건이 완료 되면 stack에 추가

    while len(stack) != 0:  # stack에 남아있는 연산자들 postfix에 추가
        postfix.append(stack.pop())

    # 후위표기식 계산
    stack = []
    postfix = list(postfix)

    for tk in postfix:
        if tk not in '*+': # 피연산자가 나오면 push
            stack.append(int(tk))
        else:                   # 연산자가 나오면
            if tk == '*':  # 곱셈 연산 수행 후 push
                b = stack.pop()
                a = stack.pop()
                stack.append(a * b)
            else:          # 덧셈 연산 수행 후 push
                b = stack.pop()
                a = stack.pop()
                stack.append(a + b)
    print(f'#{tc} {stack.pop()}')