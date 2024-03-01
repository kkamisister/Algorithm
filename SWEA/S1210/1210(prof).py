import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    test_case = input()
    N = 100 # 크기
    arr = [list(map(int, input().split())) for _in range(N)] # N*N 사다리판

    # 1. 당첨되는 위치를 찾는다.
    # 2. 역으로 사다리를 올라간다.
        # 델타 이동으로 사다리 이동

    row = N-1
    col = N-1 # 이 값이 최종 리턴이 되어야 함
    # 시작 col 값을 찾자!
    for idx in range(N):
        # 당첨 위치는 맨 마지막 줄
        if arr[N-1][idx] == 2:
            col = idx
            break
            
    # 사다리를 올라가자
    # 델타 탐색으로 이동
    # 좌, 우를 먼저 탐색할 수 있도록 순서를 구성 (사다리 타기의 특징)
    
    dr = [0, 0, -1]
    dc = [-1, 1, 0]
    
    # 사다리 타기의 반복 횟수
    # 정확한 반복 횟수는 알 수 없다 -> while을 사용하자!
    # 언제까지 반복하면 되느냐????????? -> row가 0이면 도착
    while row > 0:
        # 델타 탐색
        for idx in range(3): # 3방향 탐색
            next_row = row + dr[idx] # 바로 이동하는 것이 아니라 이동할 곳이 갈 수 있는 곳인지 확인!!
            next_col = col + dc[idx]
            
            # 이동 가능한 곳인지 범위를 체크
            if 0 <= next_row < N and 0 <= next_col < N:
                # 갈 수 있는 위치인지 확인
                if arr[next_row][next_col] == 1:
                    # 이동하기 전에 다시 되돌아 가지 않도록 표시
                    arr [row][col] = 3
                    # 갈 수 있다면 현재 위치를 갱신
                    row = next_row
                    col = next_col
                    # 이동을 했다면 그 다음 방향을 잉어서 탐색하는 것이 아니라 새롭게 방향을 탐색
                    break # 불필요한 연산을 줄이기 위해
    
    # 도착했으면 col값을 출력                
    print(f'{tc} {col}')