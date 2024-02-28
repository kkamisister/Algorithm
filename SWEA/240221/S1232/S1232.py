import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    result = []
    def inorder(rt):
        global result
        if rt:
            inorder(left[rt])
            result.append(node_dict[rt])
            inorder(right[rt])
        return result

    N = int(input())

    node_dict = {}
    left = [0]*(N+1)
    right = [0]*(N+1)
    par = [0]*(N+1)

    for _ in range(N):
        a = input().split()
        if len(a) == 2:
            node_dict[int(a[0])] = a[1]
        else:
            node_dict[int(a[0])] = a[1]
            left[int(a[0])] = int(a[2])
            right[int(a[0])] = int(a[3])
    rt = 1
    fx = inorder(rt)
    print(fx)
    cal = int(fx[0])
    for i in range(1, N-1):
        if fx[i] in '*/+-':
            if fx[i] == '*':
                cal *= int(fx[i+1])
                cal = int(cal)
            elif fx[i] == '/':
                cal /= int(fx[i+1])
                cal = int(cal)
            elif fx[i] == '+':
                cal += int(fx[i+1])
                cal = int(cal)
            else:
                cal -= int(fx[i+1])
                cal = int(cal)
    # print(cal)
    # break