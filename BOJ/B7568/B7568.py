# BOJ 7568 덩치
import sys
sys.stdin = open('input.txt')

N = int(input())
info_dict = {}
for _ in range(N):
    x, y = map(int, input().split())
    info_dict[(x, y)] = 0
for i in info_dict.keys():
    for j in info_dict.keys():
        if i[0] < j[0] and i[1] < j[1]:
            info_dict[i] += 1
print(info_dict)

# 여기까지 풀고 막혔다가 김하연 아이디어 훔쳐왔습니다
# 눈물을 머금고 김하연에게 0.8박수 양도하겠습니다
rank = [0]*N
for i in info_dict.values():
    cnt = 0
    for j in info_dict.values():
        if i > j:
            cnt += 1