import sys
sys.stdin = open('input (1).txt')

T = 10
for tc in range(1, T+1):
    # 덤프 횟수 input
    D = int(input())
    # 각 상자의 높이가 나옴
    box_list = list(map(int, input().split()))

    # 할 일
    # 최고점 -1 / 최저점 +1 (덤프 횟수만큼 반복)
    # 항상 최고점과 최저점의 값이 바뀔 수 있으므로 작업 전 혹은 후에 체크 필수
    # 카운트 리스트를 사용하여 상자의 높이 별로 갯수를 등록
    # 등록된 카운트 리스트에서 최고점으로 쌓인 상자와, 최저점으로 쌓인 상자를 찾자

    count_list = [0] * 101 # 상자 높이의 범위가 1 ~ 100 # 인덱스를 맞추기 위해 100+1
    max_height = box_list[0]
    min_height = box_list[0]

    for height in box_list:
    # box_list의 height는 count_list의 index로 사용
    count_list[height] += 1

    #가장 높은 높이, 낮은 높이를 구하자
    if max_height < height:
        max_height = height

    if min_height > height:
        min_height = height
    # 가장 높은 값, 낮은 값, count list 준비완료~~~

    for _ in range(D):
        # 가장 높은 값에 -1
        count_list[max_height] -= 1
        count_list[max_height-1] += 1

        # 가장 낮은 값에 +1
        count_list[min_height] -= 1
        count_list[min_height+1] += 1

        # 최대, 최소 값이 계속 존재하는지 확인
        if count_list[max_height] == 0:
            max_height -= 1     # 최고 높이 갱신

        if count_list[min_height] == 0:
            min_height += 1     # 최저 높이 갱신

        if max_height -  min_height <= 1: # 평탄화를 더 이상 할 필요가 없는 상태
