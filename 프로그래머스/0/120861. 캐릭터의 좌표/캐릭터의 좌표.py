def solution(keyinput, board):
    answer = [0, 0]
    key = {'up':[0, 1], 'down':[0, -1], 
           'left':[-1, 0], 'right':[1, 0]}
    maxX = [board[0]//2, -1*(board[0]//2)]
    maxY = [board[1]//2, -1*(board[1]//2)]
    
    for s in keyinput:
        answer[0] += key[s][0]
        answer[1] += key[s][1]
        
        if answer[0] > maxX[0] or answer[0] < maxX[1] or answer[1] > maxY[0] or answer[1] < maxY[1]:
            answer[0] -= key[s][0]
            answer[1] -= key[s][1]
            continue
    
    return answer