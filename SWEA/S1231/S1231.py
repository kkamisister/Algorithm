import sys
sys.stdin = open('input.txt')

def yoonji_order(root):
    if root:
        yoonji_order(left[root])
        print(par_dict[root], end='')
        yoonji_order(right[root])

T = 10
for tc in range(1, T+1):
    N = int(input())
    left = [0]*(N+1)
    right = [0]*(N+1)
    par = [0]*(N+1)
    par_dict = {}

    for i in range(N):
        a = list(input().split())
        par_dict[int(a[0])] = a[1]

        if len(a) >= 3:
            left[int(a[0])] = int(a[2])
            par[int(a[2])] = int(a[0])
            if len(a) == 4:
                right[int(a[0])] = int(a[3])
                par[int(a[3])] = int(a[0])

    c = N
    while par[c] != 0:  # 부모가 있으면
        c = par[c]  # 부모를 새로운 자식으로 두고
    root = c  # 더이상 부모가 없으면 root
    print(par_dict)
    print(f'#{tc}', end=' ')
    yoonji_order(root)
    print()