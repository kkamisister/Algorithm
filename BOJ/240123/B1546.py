N = int(input())

score_list = [i for i in map(int, input().split())]

def new_score(score_list):
    
    max_score = int(max(score_list))

    for score in range(len(score_list)):
        score_list[score] /= max_score
        score_list[score] *= 100
    
    global N

    mean_score = sum(score_list) / N

    return mean_score

result = new_score(score_list)
print(result)