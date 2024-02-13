import sys
# sys.stdin = open('input.txt')
#
# T = int(input())
# for tc in range(1, T+1):
N = int(input())
arr = list(int(sys.stdin.readline()) for _ in range(N))

arr.sort()

# 최빈값 계산
cnt_dict = {}
for i in arr:
    cnt_dict[i] = 0
for i in arr:
    cnt_dict[i] += 1

mode = []
for k in cnt_dict:
    if cnt_dict[k] == max(cnt_dict.values()):
        mode.append(k)
mode.sort()

# 출력
print(round(sum(arr)/N))     # 산술평균 소수점 첫째 자리에서 반올림
print(arr[N//2])             # 중앙값

if len(mode) == 1:           # 최빈값
    print(mode[0])
else:
    print(mode[1])
print(max(arr)-min(arr))     # 범위
