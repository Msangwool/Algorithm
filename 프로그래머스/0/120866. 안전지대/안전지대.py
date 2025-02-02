def solution(board):
    N = len(board)
    xy = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                for x, y in xy:
                    targetX = i + x
                    targetY = j + y
                    if 0 <= targetX < N and 0 <= targetY < N:
                        if board[targetX][targetY] == 1:
                            continue
                        board[targetX][targetY] = 2
                
    answer = 0
    for i in range(len(board)):
        answer += board[i].count(0)
        
    return answer