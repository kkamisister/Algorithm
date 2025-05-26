from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    visited = [[0]*m for _ in range(n)]
    
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = 1
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while queue:
        x, y = queue.popleft()
        if x == n-1 and y == m-1:
            return maps[x][y]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0<= ny < m and maps[nx][ny] == 1 and visited[nx][ny] == 0:
                queue.append((nx, ny))
                visited[nx][ny] = 1
                maps[nx][ny] = maps[x][y] + 1
                
                
                
    
    return -1