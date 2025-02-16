N = int(input())

ans = 0
board = [0] * N # board[i] = j : (i, j) 위치에 퀸을 놓겠다

def ssap_possible(x):
    for i in range(x): # 현재 행 x 이전까지의 행만 탐색
        # 같은 열 또는 대각선에 퀸이 있으면
        if board[i] == board[x] or abs(board[i] - board[x]) == abs(i-x):
            return False

    # 현재 행 x 이전까지의 행을 탐색했을 때 같은 열 또는 대각선에 퀸이 없으면
    return True


def n_queens(x):
    global ans
    if x == N: # 마지막 행까지 퀸을 모두 배치 했다면
        ans += 1
        return

    else:
        for j in range(N):
            board[x] = j # x번째 행의 j번째 열에 퀸 배치
            if ssap_possible(x):
                n_queens(x+1)

n_queens(0)
print(ans)