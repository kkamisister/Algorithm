import sys
sys.stdin = open('input (1).txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    fx = input()
    a = 0

    for tk in fx:
        if tk != '+':
         a += int(tk)

    print(f'#{tc} {a}')