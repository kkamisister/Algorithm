import sys
sys.stdin = open('5203_input.txt')

T = int(input())
for tc in range(1, T+1):
    cards = list(map(int, input().split())) # 일단 카드 리스트 받고

    player1 = []
    player2 = []

    for i in range(6):
        player1.append(cards[i*2])          # 각자 카드 가져갑니다
        player2.append(cards[i*2+1])

    result = 0                              # default 무승부

    for i in range(2, 6):                   # 각자 가져간 카드 중 세 번째 부터 검사합니다

        # player1 triplet 검사
        if player1[:i+1].count(player1[i]) == 3: # 순회중인 인덱스 기준, 지금까지 받은 카드 중에 triplet이 있는지 확인
            result = 1                           # 있으면 1 이기고 바로 끝
            break

        # player1 run 검사
        p1_sliced = sorted(player1[:i+1])        # 순회중인 인덱스 기준, 지금까지 받은 카드만 슬라이싱하고 정렬
        for p1 in p1_sliced:                     # 슬라이싱 된 리스트를 순회할건데요
            if p1+1 in p1_sliced and p1+2 in p1_sliced: # 연속 3개 수가 있는지 확인하고
                result = 1                              # 있다면 1 이기고 바로 끝
                break

        if result == 1:
            break
        # player1 triplet, run 검사에서 결과가 안나왔다면 동일하게 player2 검사 진행합니다.

        # player1 triplet 검사
        if player2[:i + 1].count(player2[i]) == 3:
            result = 2
            break

        # player2 run 검사
        p2_sliced = sorted(player2[:i + 1])
        for p2 in p2_sliced:
            if p2+1 in p2_sliced and p2 + 2 in p2_sliced:
                result = 2
                break

    print(f'#{tc} {result}')