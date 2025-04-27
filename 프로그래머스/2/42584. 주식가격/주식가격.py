def solution(prices):
    l = len(prices)
    
    # prices 길이만큼
    answer = [0]*l

    for i in range(l):
        for j in range(i+1, l):
            # 값이 현 시점 미만으로 떨어지면
            if prices[i] > prices[j]:
                # 해당 시점의 answer 값은 두 시점의 시간차
                answer[i] = j - i
                break
        # 끝까지 떨어지지 않으면 현 시점~ 끝까지의 시간차
        else:
            answer[i] = l - i - 1
        
    
    return answer