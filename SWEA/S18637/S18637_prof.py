import sys

sys.stdin = open('input.txt')


# 베이비진 확인
def is_babygin(target):
    # 이미 한 번 비교한 카드는 더 이상 비교하지 않기 위해 사용
    if tuple(target) in done:
        return False
    # global cnt
    # cnt += 1
    # triplet 확인
    if len(set(target)) == 1:
        return True

    # run 확인
    # run 확인을 쉽게 하기위해 sort
    # target.sort()   # 해당 sort 메서드는 원본을 변경하는 메서드!!
    # card 의 정보를 할당 복사하기 때문에 card 의 데이터도 똑같이 변경이 됨
    # 오동작할 가능성이 있음
    temp = sorted(target)  # 원본을 유지한 채로 정렬된 리스트를 반환
    if temp[0] + 1 == temp[1] and temp[1] + 1 == temp[2]:
        return True

    # triplet도 아니고 run도 아니면 다음에 같은 카드가 나오더라도 체크하지 않도록 넘기기 위해 세트에 저장
    # tuple로 형변환 하는 이유는 set 는 내부에 변경가능한 자료구조가 오면 안되기 때문
    done.add(tuple(target))
    return False


# 조합
# arr: p1, p2 리스트가 2개가 존재하기 때문에 인자로 후보 리스트를 받아오자
# i: 현재 뽑아야 하는 카드 index
# start: 후보카드의 시작점
# n: 뽑으려는 카드의 개수
def comb(arr, i, start, n, player):
    global result
    if result != 0:  # 베이비진이 나온경우 더이상 탐색을 하지 않도록 가지치기
        return

    if i == n:  # 다 뽑은 경우   # 3개를 뽑아야 하는데 3으로 하드코딩하는 버릇은 좋지 않음. n개를 뽑을 수 있도록 변수로 변경
        # if player == 2:   # 디버깅 용
        #     print(card, arr, player)    # 뽑힌 카드 출력
        if is_babygin(card):
            result = player
        return
    else:
        for j in range(start, len(arr)):
            card[i] = arr[j]
            comb(arr, i + 1, j + 1, n, player)  # 다음 카드선택 index와 다음 후보 시작점을 전달


T = int(input())
for tc in range(1, T + 1):
    card_list = list(map(int, input().split()))
    N = 12
    p1_list = []
    p2_list = []
    card = [0] * 3
    result = 0
    # 한번이라도 체크한 카드정보를 저장
    done = set()
    # cnt = 0     # 비교횟수 확용 정답과 무관
    for idx in range(N):
        if idx % 2 == 0:  # player 1
            p1_list.append(card_list[idx])
            if len(p1_list) >= 3:
                comb(p1_list, 0, 0, 3, 1)
        else:
            p2_list.append(card_list[idx])
            if len(p2_list) >= 3:
                comb(p2_list, 0, 0, 3, 2)

        if result != 0:
            break

    print(f'#{tc} {result}')

