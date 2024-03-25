import sys
sys.stdin = open('5204_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    case_num = 0


    print(f'#{tc}', case_num)