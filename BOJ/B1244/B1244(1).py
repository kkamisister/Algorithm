import sys
sys.stdin = open('input.txt')

N = int(input())    # 스위치 수
switch_arr = list(map(int, input().split())) # 스위치 상태
student = int(input())  # 학생 수
for _ in range(student):
    s, n = map(int, input().split())

    if s == 1:  # 남학생일 경우
        for i in range(N):
            if (i+1) % n == 0:
                switch_arr[i] ^= 1
    else:       # 여학생일 경우
        a = min(N-n, n-1)
        switch_arr[n-1] ^= 1
        if a > 0 :
            for i in range(1, a+1):
                if switch_arr[n-1+i] == switch_arr[n-1-i]:
                    switch_arr[n-1+i] ^= 1
                    switch_arr[n-1-i] ^= 1
                else:
                    break

for i in range(0, N, 20):
    print(*switch_arr[i:i+20])