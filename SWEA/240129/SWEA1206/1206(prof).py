T = 10
for tc in range(1, T+1):
    N = int(input())
    building_list = list(map(int, input().split()))

    result = 0 # 조망권 갯수를 저장하는 변수

    for idx in range(N):
        # building_list[idx] : 현재 위치

        if building_list[idx] != 0:
            delta_idx = [-2, -1, 1, 2]
            # idx + delta_idx[n]     n 번 인덱스의 위치의 빌딩 높이를 확인할 수 있음
            # building_list[idx + delta_idx[0]] : 좌측 2번째 빌딩의 높이를 알 수 있다.
            # ...
            # building_list[idx + delta_idx[3]] : 우측 2번째 빌딩의 높이를 알 수 있다.
            # 가장 높은 건물을 확인
            max_height = 0
            for n in range(4):
                if max_height < building_list[idx + delta_idx[n]]:
                    max_height = building_list[idx + delta_idx[n]]

            # 현재 빌딩의 높이와 가장 큰 빌딩의 높이를 비교
            # 그리고 조망권을 확보할 수 있는지 계산

            if building_list[idx] > max_height:
                result += building_list[idx] - max_height # 조망권 누적

    print(f'#{tc} {result}')