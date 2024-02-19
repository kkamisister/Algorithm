import sys
sys.stdin = open('input.txt')

# input 받기
switch_num = int(input())                       # 스위치 수
onoff = list(map(int, input().split()))         # 각 스위치의 상태
student_num = int(input())                      # 학생수

# 드가자
for std in range(student_num):              # 학생수 만큼 반복
    s, n = map(int, input().split())        # s : 학생의 성별, n : 받은 수

    # 남학생
    if s == 1:
        for idx in range(n-1, switch_num):          # n번부터 배수 확인
            if (idx+1) % n == 0:                    # n의 배수번째가 맞으면
                onoff[idx] = int(not onoff[idx])    # 상태 전환

    # 여학생
    else:
        a = b = 0       # 대칭되는 수를 a, b에 넣고 추후 판단해줄겁니당
        check = 1       # 대칭 검사 한 칸씩 옮길때 사용
        onoff[n-1] = int(not onoff[n-1])    # 일단 n번째 스위치 바꿔주고
        while 0 <= n - check - 1 and n + check - 1 < switch_num: # 인덱스 범위 밖을 벗어나지 않는 동안
            a = onoff[n-check-1]                # n번의 좌
            b = onoff[n+check-1]                # n번의 우
            if a == b:                          # n번의 좌우가 같다면
                onoff[n-check-1] = onoff[n+check-1] = int(not onoff[n-check-1]) # 두 스위치의 상태 전환
                check += 1                      # 다음 대칭 확인
            else:                               # 좌우가 다르다면 종료
                break

# 20개씩 프린트를 해볼까요~
for i in range(0, switch_num, 20):
    print(*onoff[i:i+20])