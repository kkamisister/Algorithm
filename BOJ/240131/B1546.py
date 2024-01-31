N = int(input())
score_list = list(map(int, input().split()))

# 최댓값 구하기
M = 0
for score in score_list:
    if M < score:
        M = score

for score_idx in range(N):
    score_list[score_idx] /= M
    score_list[score_idx] *= 100
    
score_sum = 0
for score in score_list:
    score_sum += score
    
print(score_sum / N)