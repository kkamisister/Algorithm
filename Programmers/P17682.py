def solution(dartResult):
    score = ''
    bonus = []
    option = []
    score_sum = 0
    last_score = 0

    for string in dartResult:
        if string.isnumeric():
            if score:
                score += string

        elif string in 'SDT':
            if string == 'S':
                last_score = int(score)
                score_sum += last_score
                score = ''
            elif string == 'D':
                last_score = int(score)**2
                score_sum += last_score
                score = ''
            else:
                last_score = int(score)**3
                score_sum += last_score
                score = ''
        else:
            if string == '*'
                last_score *= 2
                score_sum += last_score
                last_score = int(score)*2

            elif
            option.append(string)

    answer = 0
    return answer