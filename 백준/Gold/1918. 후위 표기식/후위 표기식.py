import sys

stack = []
result = []
priority = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2}

for l in sys.stdin.readline().strip():
    if l.isalpha():
        result.append(l)
    elif l == '(':
        stack.append(l)
    elif l == ')':
        while stack and stack[-1] != '(':
            result.append(stack.pop())
        stack.pop()
    else:
        while stack and priority[l] <= priority[stack[-1]]:
            result.append(stack.pop())
        stack.append(l)

while stack:
    result.append(stack.pop())

print("".join(result))
