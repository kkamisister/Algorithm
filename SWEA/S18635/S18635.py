import sys
sys.stdin = open('5201_input.txt')

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    weights = sorted(list(map(int, input().split()))) # 화물 무게 받아주자마자 정렬해버려
    trucks = sorted(list(map(int, input().split())))  # 트럭도 받아주자마자 정렬해버려

    weight_sum = 0 # 누적 무게 변수

    while weights and trucks:   # 무게 리스트와 트럭 리스트가 비어있지 않을 동안
       if weights[-1] <= trucks[-1]:    # 가장 큰 무게보다 최대 적재용량이 더 크다면
            weight_sum += weights[-1]   # 누적 무게에 더해주고
            weights.pop()               # 둘 다 없애버림
            trucks.pop()
        else:
            weights.pop()               # 아니라면 무게만 없애버림
    print(f'#{tc} {weight_sum}')
