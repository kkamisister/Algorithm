N = int(input())
dice_arr = [list(map(int, input().split())) for _ in range(N)]
for dice in range(N):
    A, B, C, D, E, F = dice_arr[dice]
