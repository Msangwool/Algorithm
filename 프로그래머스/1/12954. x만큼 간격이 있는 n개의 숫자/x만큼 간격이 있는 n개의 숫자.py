def solution(x, n):
    if x > 0:
        return [i for i in range(x, x*n+1, x)]
    
    arr = [x]
    while len(arr) < n:
        arr.append(arr[-1] + x)
    return arr