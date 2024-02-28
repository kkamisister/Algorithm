import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    for _ in range(N):
        if '1' not in arr[_]:
            pass
        else:
            pws = arr[_]
    # first_idx = pws.index('1')-1
    # last_idx = first_idx + 55
    # pws = pws[first_idx: last_idx+1]

    for i in range(M-1, -1, -1):
        if pws[i] == '1':
            last_idx = i
            break

    first_idx = last_idx-55
    pws = pws[first_idx: last_idx+1]

    arr = []
    for i in range(0, 56, 7):
        arr.append(pws[i: i+7])

    # 냅다 숫자별 암호 지정하기
    for pw in range(8):
        if arr[pw] == '0001101':
            arr[pw] = 0
        elif arr[pw] == '0011001':
            arr[pw] = 1
        elif arr[pw] == '0010011':
            arr[pw] = 2
        elif arr[pw] == '0111101':
            arr[pw] = 3
        elif arr[pw] == '0100011':
            arr[pw] = 4
        elif arr[pw] == '0110001':
            arr[pw] = 5
        elif arr[pw] == '0101111':
            arr[pw] = 6
        elif arr[pw] == '0111011':
            arr[pw] = 7
        elif arr[pw] == '0110111':
            arr[pw] = 8
        else:
            arr[pw] = 9
    pw_sum = 0
    num_sum = 0
    for i in range(8):
        num_sum += arr[i]
        if i % 2 == 0:
            pw_sum += arr[i]*3
        else:
            pw_sum += arr[i]

    if pw_sum % 10 == 0:
        print(f'#{tc} {num_sum}')
    else:
        print(f'#{tc} 0')