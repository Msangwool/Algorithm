def solution(n):
    d = [[0, 1], [1, 0], [0, -1], [-1, 0]]            
    answer = [[0] * n for _ in range(n)]
    x = 0
    y = 0
    dt = 0
    
    for i in range(n*n):
        answer[y][x] = i+1
        
        x_temp, y_temp = x + d[dt][1], y + d[dt][0]
        if 0 <= x_temp < n and 0 <= y_temp < n:
            if answer[y_temp][x_temp] == 0:
                x, y = x_temp, y_temp
                continue

        dt = (dt + 1) % 4
        x, y = x + d[dt][1], y + d[dt][0]
            
    return answer