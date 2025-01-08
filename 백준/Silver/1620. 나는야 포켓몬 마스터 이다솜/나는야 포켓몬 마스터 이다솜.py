import sys
input = sys.stdin.readline

# 입력 처리
N, M = map(int, input().split())

# 두 개의 딕셔너리 생성
name_to_num = {}
num_to_name = {}

# 포켓몬 데이터 저장
for i in range(1, N + 1):
    name = input().strip()
    name_to_num[name] = i
    num_to_name[i] = name

# 문제 처리
result = []
for _ in range(M):
    query = input().strip()
    if query.isdigit():  # 숫자인 경우
        result.append(num_to_name[int(query)])
    else:  # 문자열인 경우
        result.append(name_to_num[query])

# 출력
print("\n".join(map(str, result)))
