def solution(dots):
    x = 0
    y = 0
    if dots[0][0] == dots[1][0]:
        x = abs(dots[0][0] - dots[2][0])
    else:
        x = abs(dots[0][0] - dots[1][0])
    
    if dots[0][1] == dots[1][1]:
        y = abs(dots[0][1] - dots[2][1])
    else:
        y = abs(dots[0][1] - dots[1][1])
    
    return x * y