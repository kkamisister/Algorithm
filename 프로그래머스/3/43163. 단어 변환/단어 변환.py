from collections import deque

def solution(begin, target, words):
    
    # 사전처리
    if target not in words:
        return 0

    
    visited = set()
    queue = deque([(begin, 0)])

    while queue:
        current, depth = queue.popleft()
        if current == target:
            return depth

        for word in words:
            if word in visited:
                continue

            diff = 0
            for i in range(len(current)):
                if current[i] != word[i]:
                    diff += 1
                    if diff > 1:
                        break

            if diff == 1:
                visited.add(word)
                queue.append((word, depth + 1))

