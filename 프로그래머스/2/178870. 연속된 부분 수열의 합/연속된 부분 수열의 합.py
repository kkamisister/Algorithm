def solution(sequence, k):
    n = len(sequence)
    start, end = 0, 0
    total = sequence[0]
    
    answer = [0, n-1]
    min_len = n

    while start <= end and end < n:
        if total < k:
            end += 1
            if end < n:
                total += sequence[end]
        elif total > k:
            total -= sequence[start]
            start += 1
        else:
            if end - start < min_len:
                min_len = end - start
                answer = [start, end]
            total -= sequence[start]
            start += 1

    return answer
