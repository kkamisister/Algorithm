import sys
sys.stdin = open('input.txt')

N = int(input())
clap = [str(i) for i in range(1, N+1)]

for i in range(N):
    cnt = 0
    for j in range(len(clap[i])):
        if clap[i][j] in '369':
            cnt += 1
    if cnt == 1:
        clap[i] = '-'
    elif cnt == 2:
        clap[i] = '--'
    elif cnt == 3:
        clap[i] = '---'
    # clap[i] = clap[i].replace('3', '-')
    # clap[i] = clap[i].replace('6', '-')
    # clap[i] = clap[i].replace('9', '-')

for i in range(N):
    print(clap[i], end=' ')