from collections import deque

def solution(begin, target, words):
    n = len(words)
    
    if target not in words:
        return 0
    
    visited = [0]*n
    
    queue = deque([(begin, 0)])
    
    while queue:
        current, depth = queue.popleft()
        if current == target:
            return depth
        
        for i in range(n):
            if visited[i]:
                continue
                
            word = words[i]

            cnt = 0
            for j in range(len(word)):
                if word[j] != current[j]:
                    cnt += 1
                    if cnt > 1:
                        break
                    
            if cnt == 1:
                visited[i] = 1
                queue.append((word, depth + 1))
    
    
    return 0