# BOJ 4949 균형잡힌 세상
import sys
sys.stdin = open('input.txt')

while True:
    text = input()
    if text == '.':
        break

    stack = []
    for string in text:
        if string not in '()[]':
            pass
        else:
            if string in '([':
                stack.append(string)
            elif string == ')':
                if stack and stack.pop() == '(':
                    result = 'yes'
                else:
                    result = 'no'
                    break
            else:
                if stack and stack.pop() == '[':
                    result = 'yes'
                else:
                    result = 'no'
                    break
    else:
        if stack:
            result = 'no'
        else:
            result = 'yes'
    print(result)