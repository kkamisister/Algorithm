T = 10

for tc in range(1, T+1):
    N = int(input())
    buildings = list(map(int, input().split()))

    cnt = 0    # 조망권이 확보된 세대 수를 입력할 변수

    for building in range(2, N-2):  # 빌딩 리스트에서 양쪽 두 값씩 제외하고 순회
        temp = buildings[building-2:building+3] # 현재 building 기준 양쪽 두 값을 포함하여 슬라이싱, 변수에 저장

        # temp에서 최댓값 찾기
        temp_max = 0
        for height in temp:
            if temp_max < height:
                temp_max = height

        # 현재 building이 temp에서 최댓값인지 판별, 해당 값 제거
        if buildings[building] == temp_max:
            temp.remove(buildings[building])

        # 최댓값이 제거 된 상태에서 다시 최댓값을 구하고 (공동 최댓값이거나 or 두 번째로 큰 값이거나)
        temp_second = 0
        for height in temp:
            if temp_second < height:
                temp_second = height

        # 현재 building이 temp에서 유일한 최댓값이었는지 판별
        if buildings[building] > temp_second:
            cnt += buildings[building] - temp_second # 맞을 경우 두 번째로 큰 값과의 차를 cnt에 저장

    print(f'#{tc} {cnt}')