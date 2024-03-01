T = 10

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    for dump in range(N): # N번 덤프 시도
        max_height = 0 # 최고점을 넣을 변수
        max_idx = 0 # 최고점 인덱스를 넣을 변수
        min_idx = 0 # 최저점 인덱스를 넣을 변수

        for height in range(100):
            if max_height < arr[height]:
                max_height = arr[height]
                max_idx = height
            pass

        min_height = max_height # 최저점을 넣을 변수
        for height in range(100):
            if min_height > arr[height]:
                min_height = arr[height]
                min_idx = height
            pass

        arr[max_idx] -= 1
        arr[min_idx] += 1

    max_height = 0
    for height in range(100):
        if max_height < arr[height]:
            max_height = arr[height]
        pass

    min_height = max_height
    for height in range(100):
        if min_height > arr[height]:
            min_height = arr[height]

    result = max_height - min_height

    print(f'#{tc} {result}')
