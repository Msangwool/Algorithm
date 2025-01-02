import math

def solution(a, b, c, d):
    arr = [a, b, c, d]
    countMap = {}
    
    for num in arr:
        if num in countMap:
            countMap[num] += 1
            continue
        countMap[num] = 1
    
    if len(countMap) == 1:
        return 1111 * a

    if len(countMap) == 4:
        return min(arr)
    
    if len(countMap) == 3:
        return math.prod(key for key, value in countMap.items() if value != 2)
    
    p = 0
    q = 0
    val = 0
    for key, value in countMap.items():
        if value == 3:
            p = key
            continue
        if value == 1:
            q = key
            continue
        
        if val == 0:
            p = key
            val = 1
        else:
            q = key
            
    if val == 0:
        return (10*p + q)**2
    
    return (p+q) * abs(p-q)