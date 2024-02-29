K = int(input())
length = [] # 길이 받아올 리스트

for _ in range(6):
    d, l = map(int, input().split())
    length.append(l)

length *= 2 # %로 인덱스 구하려다 머리 빠개져서 리스트 세 배 늘려줌
l_idx = length.index(max(length)) # 최대값의 두 번째 인덱스 구해줍니당

a, b, c, d, e, f = length[l_idx:l_idx+6] # 구한 최대값 인덱스 기준으로 6개 뽑아주고 (최대값이 a)

if a == c + e and b == d + f:       # a가 1번인 경우
    result = (a * b - d * e) * K
else:
    result = (a * f - c * d) * K    # a가 2번인 경우

print(result)