def solution(board):
    N = len(board)
    xy = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    
    boom = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                boom.append((i, j))
                
    for i in boom:
        for x, y in xy:
            iX = i[0] + x
            iY = i[1] + y
            if 0 <= iX < N and 0 <= iY < N:
                board[iX][iY] = 1
    
    answer = 0
    for i in range(len(board)):
        answer += board[i].count(0)
        
    return answer