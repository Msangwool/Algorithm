def solution(n):    
    GCD = 0
    if n > 6:
        GCD = getGcd(n, 6)
    else:
        GCD = getGcd(6, n)
        
    return (n*6//GCD)//6

def getGcd(a, b):
    if a % b == 0:
        return b
    return getGcd(b, a % b)