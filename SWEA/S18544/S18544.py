def pre_order(T):
    if T:
        print(T, end=' ')
        pre_order(left[T])
        pre_order(right[T])

N = int(input())        # 1번부터 N번까지인 정점
E = N-1
arr = list(map(int, input().split()))
left = [0]*(N+1)        # 부모를 인덱스로 왼쪽자식번호 저장
right = [0]*(N+1)       #
par = [0]*(N+1)         # 자식을 인덱스로 부모 저장

for i in range(E):
    p, c = arr[i*2], arr[i*2+1] # 한 쌍씩 입력 받기
# for i in range(0, E*2, 2):    # 한 쌍씩 입력 받기2
#     p, c = arr[i], arr[i+1]
    if left[p] == 0:    # 왼쪽 자식이 없으면
        left[p] = c
    else:
        right[p] = c
    par[c] = p

c = N
while par[c] != 0:      # 부모가 있으면
    c = par[c]          # 부모를 새로운 자식으로 두고
root = c                # 더이상 부모가 없으면 root
pre_order(root)