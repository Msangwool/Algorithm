def solution(arr):
    X = 1
    while True:        
        if len(arr) <= X:
            break
        X *= 2
        
    arr.extend([0] * (X - len(arr)))
    return arr