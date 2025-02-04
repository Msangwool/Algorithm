def solution(numer1, denom1, numer2, denom2):
    commonParent = denom1 * denom2

    child = (numer1 * commonParent//denom1) + (numer2 * commonParent//denom2)
    parent = commonParent
            
    for i in range(parent + 1, 1, -1):        
        if child % i == 0 and parent % i == 0:
            child //= i
            parent //= i
            
    return [child, parent]