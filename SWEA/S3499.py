T = int(input())
for tc in range(1, T+1):
    N = int(input())
    card_lst = list(input().split())

    a = 0
    b = N//2

    perfect = []
    while a < b and len(perfect) < N:
        perfect.append(card_lst[a])
        perfect.append(card_lst[b])
        a += 1
        b += 1

    print(perfect)