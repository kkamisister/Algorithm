def cal(a, b, c):
    if b==1:
        return a%c

    temp = cal(a, b//2, c)

    if b % 2 == 1:
        return (temp*temp)%c * a%c
    else:
        return (temp*temp)%c



A, B, C = map(int, input().split())
print(cal(A, B, C))