def solution(arr):
    x = len(arr[0])
    y = len(arr) 
    if y > x:
        for i in range(len(arr)):
            arr[i].extend([0] * (y - x))
    elif x > y:
        for _ in range(x - y):
            arr.append([0] * x)
    
    return arr