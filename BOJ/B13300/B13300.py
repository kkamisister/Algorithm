import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    room_info = {}

    for _ in range(N):
        S, Y = map(int, input().split())
        if (S, Y) in room_info:
            room_info[(S, Y)] += 1
        else:
            room_info[(S, Y)] = 1

    room_cnt = 0
    for k, v in room_info.items():
        if 0 < v <= K:
            room_cnt += 1
        elif K < v:
            if 0 < v % K:
                room_cnt += v // K + 1
            else:
                room_cnt += v // K
    print(room_cnt)