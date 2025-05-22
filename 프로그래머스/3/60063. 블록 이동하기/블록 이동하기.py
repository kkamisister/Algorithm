from collections import deque

def solution(board):
    n = len(board)
    # 보드에 외벽 추가
    new_board = [[1]*(n+2) for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            new_board[i+1][j+1] = board[i][j]

    def get_next_pos(pos):
        next_pos = []
        pos = list(pos)
        (x1, y1), (x2, y2) = pos[0], pos[1]
        
        # 이동
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        for i in range(4):
            nx1, ny1 = x1 + dx[i], y1 + dy[i]
            nx2, ny2 = x2 + dx[i], y2 + dy[i]
            if new_board[nx1][ny1] == 0 and new_board[nx2][ny2] == 0:
                next_pos.append({(nx1, ny1), (nx2, ny2)})
                
        # 회전
        if x1 == x2: # 가로
            for i in [-1, 1]:
                if new_board[x1+i][y1] == 0 and new_board[x2+i][y2] == 0:
                    next_pos.append({(x1, y1), (x1+i, y1)})
                    next_pos.append({(x2, y2), (x2+i, y2)})
        elif y1 == y2: # 세로
            for i in [-1, 1]:
                if new_board[x1][y1+i] == 0 and new_board[x2][y2+i] == 0:
                    next_pos.append({(x1, y1), (x1, y1+i)})
                    next_pos.append({(x2, y2), (x2, y2+i)})
        return next_pos

    q = deque()
    visited = []
    pos = {(1,1), (1,2)}
    q.append((pos, 0))
    visited.append(pos)
    while q:
        pos, cost = q.popleft()
        if (n, n) in pos:
            return cost
        for next_pos in get_next_pos(pos):
            if next_pos not in visited:
                q.append((next_pos, cost+1))
                visited.append(next_pos)
