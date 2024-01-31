N, M = map(int, input().split())

# 보드를 2차원 배열로 받을 리스트 변수 생성
board = []

for i in range(N):
    board.append(list(input()))
    
    
# (0, 0)칸이 'w'인 8*8 체스판 (추후 비교에 사용)
chess_w = [
    ['w', 'b' ,'w', 'b', 'w', 'b' ,'w', 'b'],
    ['b' ,'w', 'b', 'w', 'b' ,'w', 'b', 'w'],
    ['w', 'b' ,'w', 'b', 'w', 'b' ,'w', 'b'],
    ['b' ,'w', 'b', 'w', 'b' ,'w', 'b', 'w'],
    ['w', 'b' ,'w', 'b', 'w', 'b' ,'w', 'b'],
    ['b' ,'w', 'b', 'w', 'b' ,'w', 'b', 'w'],
    ['w', 'b' ,'w', 'b', 'w', 'b' ,'w', 'b'],
    ['b' ,'w', 'b', 'w', 'b' ,'w', 'b', 'w'],
]


# (0, 0)칸이 'b'인 8*8 체스판 (추후 비교에 사용)
chess_b = [
    ['b' ,'w', 'b', 'w', 'b' ,'w', 'b', 'w'],
    ['w', 'b' ,'w', 'b', 'w', 'b' ,'w', 'b'],
    ['b' ,'w', 'b', 'w', 'b' ,'w', 'b', 'w'],
    ['w', 'b' ,'w', 'b', 'w', 'b' ,'w', 'b'],
    ['b' ,'w', 'b', 'w', 'b' ,'w', 'b', 'w'],
    ['w', 'b' ,'w', 'b', 'w', 'b' ,'w', 'b'],
    ['b' ,'w', 'b', 'w', 'b' ,'w', 'b', 'w'],
    ['w', 'b' ,'w', 'b', 'w', 'b' ,'w', 'b'],
]

coloring_sum_w = []
coloring_sum_b = []


for r in range(0, N-7):
    for c in range(0, M-7):
        
        # coloring = 0
        
        for i in range(r, r+8):
            for j in range(c, c+8):
                
                for chess_r in range(8):
                    for chess_c in range(8):
                        
                        coloring_w = 0
                        coloring_b = 0
                        
                        if board[i][j] != chess_w[chess_r][chess_c]:
                            coloring_w += 1
                            
                        if board[i][j] != chess_b[chess_r][chess_c]:
                            coloring_b += 1
                            
                        coloring_min = min(coloring_w, coloring_b)