from collections import deque

def josephus_problem(n, k):
    queue = deque(range(1, n+1))  # 1번부터 N번까지 사람들 초기화
    result = []

    while queue:
        queue.rotate(-(k-1))  # 큐를 K-1번 왼쪽으로 회전
        result.append(queue.popleft())  # K번째 사람을 제거하고 결과에 추가

    return result

# 입력 받기
n, k = map(int, input().split())
result = josephus_problem(n, k)

# 요세푸스 순열 출력
print("<", ", ".join(map(str, result)), ">", sep='')
