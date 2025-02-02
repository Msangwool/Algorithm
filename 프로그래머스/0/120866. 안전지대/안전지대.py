def solution(board):
    N = len(board)
    xy = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                for x in range(max(i-1, 0), min(i+2, N)):
                    for y in range(max(j-1, 0), min(j+2, N)):
                        if board[x][y] == 1:
                            continue
                        board[x][y] = 2
                
    answer = 0
    for i in range(len(board)):
        answer += board[i].count(0)
        
    return answer